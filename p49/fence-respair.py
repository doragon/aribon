"""p49 problem"""

# coding: utf-8
# ---------------------------------------------------------
# フェンス修理の問題
# ---------------------------------------------------------


def get_total_cost(split_list):
    """
        コストの合計値を取得する
    """
    cost = 0
    pre_cost = 0
    for i, x in enumerate(split_list):
        if i == 0:
            pre_cost = x
            continue
        cost = cost + pre_cost + x
        pre_cost = cost
    return cost


if __name__ == '__main__':
    N = 3
    L = [8, 5, 8]

    L.sort()
    print(get_total_cost(L))
