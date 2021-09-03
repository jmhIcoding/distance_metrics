__author__ = 'dk'
#图的编辑距离
import networkx
import networkx as nx
def real_length(pkt_length):
    l =0
    r = len(pkt_length)
    while l<r:
        mid = (l+r)// 2
        if pkt_length[mid] == 0:
            r = mid
        else:
            l = mid+1
    return l
def dgl_to_networkx(graph, feature_name):
    nxG = graph.to_networkx()
    ndata = {}
    for i in range(graph.ndata[feature_name].size()[0]):
        ndata.setdefault(i,{feature_name: graph.ndata[feature_name][i].reshape(-1)})
        l = real_length(ndata[i][feature_name])
        ndata[i][feature_name]= ndata[i][feature_name][:l]
    nx.set_node_attributes(nxG,ndata)
    return nxG

def GRAPH_EDIT_distance(src, dst, node_sub_cost, node_del_cost, node_ins_cost):
    assert isinstance(src, nx.MultiDiGraph)
    assert isinstance(dst, nx.MultiDiGraph)

    cost = networkx.graph_edit_distance (
        G1=src,
        G2=dst,
        node_del_cost=node_del_cost,
        node_ins_cost=node_ins_cost,
        node_subst_cost= node_sub_cost,
        timeout=1
    )
    return cost

if __name__ == '__main__':
    pass