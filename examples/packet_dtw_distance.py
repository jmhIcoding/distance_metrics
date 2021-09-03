__author__ = 'dk'
#包长序列的dtw距离计算示例
from src.sequence_dtw_distance import DTW_distance
import numpy as np
src_packet_length = [160, -1448, -600, -816, -32, -916, 126, -242, 837, -1440, -1440, -1440, -1440, -1448, -32, -1440, -1440, -1440, -1440, -1448, -32, -1440, -1225, -1440, -1440, -1440, -1440, -1440, -1440, -1440, -1448, -56, -1440, -1440, -1440, -1440, -1448, -32, -1440, -1440, -1448, -16, -1448, -600, -193, 873, -1440, -1440, -1448, -600, -832, -1448, -32, -1448, -1448, -600, -832, -1440, -1440, -1448, -32, -1130, -1440, -1440, -1440, -1440, -32, -1440, -1440, -1440, -1440, -1448, -32, -1448, -1440, -1440, -1448, -600, -832, -1448, -32, -1448, -600, -832, -1448, -16, -1448, -1448, -1448, -1448, -1448, -1440, -1440, -1448, -193, 882, -1440, -1440, -1448, -333, 876, -1440, -1440, -1440, -1440, -1448, -32, -1440, -1440, -1448, -16, -1440, -1440, -1448, -16, -1138, -1440, -1440, -1440, -1440, -32, -1440, -1440, -1440, -1440, -1448, -32, -1440, -1440, -558]
dst_packet_length = [517, -137, 51, 1395, -1448, -216, 1255, -427, 1177, -866, 1255, -1448, -299, 1448, 1448, 1448, 1040, -610, 1448, 1448, 1448, 296, -610, 1448, 322, -610, 1448, 8, -1440, -8, -1448, -68, 1448, 275, -610, 1448, 287, -610, 1448, 320, -610, 1448, 1448, 809, -723, 1448, 521, -610, 1448, 750, -610, 1448, 479, -1040, 1448, 519, -1114, 1448, 526, -1114, 1356, -872, 1448, 129, -1440, 1377, -988]

def sample1():
    ##包长序列是带方向的
    def item_dist(src, dst):
        #每个包长需要考虑方向的反转
        if np.sign(src) == np.sign(dst):
            return abs(src-dst)
        else:
            #遇到方向相反的, 加大距离惩罚
            return abs(src-dst)*5

    dst = DTW_distance(src=src_packet_length, dst=dst_packet_length, item_distance=item_dist)
    print(dst)

def sample2():
    #包长序列忽略方向
    def item_dist(src, dst):
        return abs(src-dst)

    dst = DTW_distance(src=src_packet_length, dst=dst_packet_length, item_distance=item_dist)
    print(dst)

def sample3():
    def item_dist(src, dst):
        #每个包长需要考虑方向的反转
        if np.sign(src) ==  np.sign(dst):
            return 0
        else:
            return 1

    dst = DTW_distance(src=src_packet_length, dst=dst_packet_length, item_distance=item_dist)
    print(dst)

if __name__ == '__main__':
    sample1()
    sample2()
    sample3()