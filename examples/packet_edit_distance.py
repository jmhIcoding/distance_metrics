__author__ = 'dk'
#包长序列的编辑距离计算示例
from src.sequence_edition_distance import EDIT_distance
import numpy as np
src_packet_length = [160, -1448, -600, -816, -32, -916, 126, -242, 837, -1440, -1440, -1440, -1440, -1448, -32, -1440, -1440, -1440, -1440, -1448, -32, -1440, -1225, -1440, -1440, -1440, -1440, -1440, -1440, -1440, -1448, -56, -1440, -1440, -1440, -1440, -1448, -32, -1440, -1440, -1448, -16, -1448, -600, -193, 873, -1440, -1440, -1448, -600, -832, -1448, -32, -1448, -1448, -600, -832, -1440, -1440, -1448, -32, -1130, -1440, -1440, -1440, -1440, -32, -1440, -1440, -1440, -1440, -1448, -32, -1448, -1440, -1440, -1448, -600, -832, -1448, -32, -1448, -600, -832, -1448, -16, -1448, -1448, -1448, -1448, -1448, -1440, -1440, -1448, -193, 882, -1440, -1440, -1448, -333, 876, -1440, -1440, -1440, -1440, -1448, -32, -1440, -1440, -1448, -16, -1440, -1440, -1448, -16, -1138, -1440, -1440, -1440, -1440, -32, -1440, -1440, -1440, -1440, -1448, -32, -1440, -1440, -558]
dst_packet_length = [517, -137, 51, 1395, -1448, -216, 1255, -427, 1177, -866, 1255, -1448, -299, 1448, 1448, 1448, 1040, -610, 1448, 1448, 1448, 296, -610, 1448, 322, -610, 1448, 8, -1440, -8, -1448, -68, 1448, 275, -610, 1448, 287, -610, 1448, 320, -610, 1448, 1448, 809, -723, 1448, 521, -610, 1448, 750, -610, 1448, 479, -1040, 1448, 519, -1114, 1448, 526, -1114, 1356, -872, 1448, 129, -1440, 1377, -988]

def sample1():
    ##包长序列是带方向的
    def del_cost(i):
        return abs(src_packet_length[i-1])
    def ins_cost(j):
        return abs(dst_packet_length[j-1])
    def sub_cost(i,j):
        if src_packet_length[i-1] == dst_packet_length[j-1]:
            return 0
        else:
            return abs(src_packet_length[i-1]- dst_packet_length[j-1])
    dst = EDIT_distance(src=src_packet_length, dst=dst_packet_length,del_cost=del_cost, ins_cost=ins_cost, sub_cost= sub_cost)
    print(dst)

def sample2():
    #包长序列忽略方向
    def del_cost(i):
        return abs(src_packet_length[i-1])
    def ins_cost(j):
        return abs(dst_packet_length[j-1])
    def sub_cost(i,j):
        if np.abs(src_packet_length[i-1]) == np.abs(dst_packet_length[j-1]):
            return 0
        else:
            return abs(abs(src_packet_length[i-1])- abs(dst_packet_length[j-1]))
    dst = EDIT_distance(src=src_packet_length, dst=dst_packet_length,del_cost=del_cost, ins_cost=ins_cost, sub_cost= sub_cost)
    print(dst)

def sample3():
    #包方向序列
    def del_cost(i):
        return 1
    def ins_cost(j):
        return 1
    def sub_cost(i,j):
        if np.sign(src_packet_length[i-1]) == np.sign(dst_packet_length[j-1]):
            return 0
        else:
            return abs(np.sign(src_packet_length[i-1]) - np.sign(dst_packet_length[j-1]))
    dst = EDIT_distance(src=src_packet_length, dst=dst_packet_length,del_cost=del_cost, ins_cost=ins_cost, sub_cost= sub_cost)
    print(dst)

def sample4():
    ##标准的编辑距离
    dst = EDIT_distance(src=src_packet_length,dst = dst_packet_length)
    print(dst)
if __name__ == '__main__':
    sample1()
    sample2()
    sample3()
    sample4()