__author__ = 'dk'
#序列的DTW距离


def DTW_distance(src, dst, item_distance=None, position_distance=None):
    '''
    :param src: 源序列
    :param dst: 目标序列
    :param item_distance: 序列里面每个元素的对比函数.
                            默认为两个元素的差值, 可自定义此函数
    :param position_distance: 序列中两个位置i,j 的元素的距离函数, 此函数只衡量位置距离。与两个元素的具体取值无关
    :return:
    '''

    def default_item_distance(item1, item2):
        return  abs(item1-item2)
    def default_position_distance(i,j):
        return abs(i-j)

    if item_distance == None:
        item_distance = default_item_distance
    if  position_distance == None:
        position_distance = default_position_distance
    assert isinstance(src,list)
    assert isinstance(dst,list)
    m = len(src)
    n = len(dst)

    # 构建二位dp矩阵,存储对应每个子问题的最小距离
    dp = [[0]*n for _ in range(m)]

    # 起始条件,计算单个字符与一个序列的距离
    for i in range(m):
        dp[i][0] = item_distance(src[i],dst[0])
    for j in range(n):
        dp[0][j] = item_distance(src[0],dst[j])

    # 利用递推公式,计算每个子问题的最小距离,矩阵最右下角的元素即位最终两个序列的最小值
    for i in range(1,m):
        for j in range(1,n):
            dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1]) + item_distance(src[i],dst[j]) + position_distance(i,j)

    return dp[-1][-1]
if __name__ == '__main__':
    src = [1,3,2,4,2]
    dst = [1,3,2,4]
    print('DTW distance:', DTW_distance(src, dst))