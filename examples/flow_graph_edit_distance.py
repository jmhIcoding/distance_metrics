__author__ = 'dk'
import pickle
import networkx as nx
from src.graph_edition_distance import  GRAPH_EDIT_distance
from src.sequence_edition_distance import EDIT_distance
from src.sequence_dtw_distance import DTW_distance
import numpy as np
from src.graph_edition_distance import dgl_to_networkx
if __name__ == '__main__':

    with open('graphs.pkl','rb') as fp:
        graphs = pickle.load(fp)
    graph1  = dgl_to_networkx(graphs[0],'pkt_length')
    graph2  = dgl_to_networkx(graphs[1], 'pkt_length')

    def node_ins_cost(node1):
        return np.linalg.norm(node1['pkt_length'], ord=1)
    def node_del_cost(node1):
        return np.linalg.norm(node1['pkt_length'], ord=1)
    def node_sub_cost(node1, node2):
        return EDIT_distance(node1['pkt_length'].tolist(),dst=node2['pkt_length'].tolist())

    print(GRAPH_EDIT_distance(src=graph1,dst=graph2,node_sub_cost=node_sub_cost,node_del_cost=node_del_cost, node_ins_cost=node_ins_cost))