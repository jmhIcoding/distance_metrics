__author__ = 'dk'
##序列的编辑距离
import numpy as np
def EDIT_distance(src, dst, del_cost=None, ins_cost=None, sub_cost=None):

    def default_del_cost(i):
        return 1
    def default_ins_cost(i):
        return 1
    def default_sub_cost(i,j):
        if src[i-1] == dst[j-1]:
            return  0
        else:
            return 2
    assert isinstance(src,list)
    assert isinstance(dst,list)
    del_cost = default_del_cost if del_cost is None else del_cost
    ins_cost = default_ins_cost if ins_cost is None else ins_cost
    sub_cost = default_sub_cost if sub_cost is None else sub_cost
    ##初始化
    matrix = np.zeros((len(src)+1, len(dst)+1), dtype = np.int).tolist()
    for i in range(1,len(src)):
        matrix[i][0] = matrix[i-1][0] + del_cost(i)
    for j in range(1, len(dst)):
        matrix[0][j] = matrix[0][j-1] + ins_cost(j)

    for i in range(1, len(src) + 1):
        for j in range(1, len(dst) + 1):
            matrix[i][j] = min(matrix[i - 1][j] + del_cost(i),
                               matrix[i][j - 1] + ins_cost(j),
                               matrix[i - 1][j - 1] + sub_cost(i,j))
    return matrix[len(src)][len(dst)]

if __name__ == '__main__':
    src= 'intention'
    dst= 'execution'
    print(EDIT_distance(src,dst,))