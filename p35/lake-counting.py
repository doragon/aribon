"""p35 problem"""

# coding: utf-8
# ---------------------------------------------------------
# 池の数問題
# ---------------------------------------------------------


def get_lake_list_convert_to_index_list(lake_list):
    """ 池の範囲をindex化したリストで返す """
    return [i for i, x in enumerate(lake_list) if x == 'W']


def get_lake_counting(index_list, pre_list):
    """
        池のカウント数を返す。
        ただし、左上,上,右上,左に隣り合ったindexがない場合に限る。
    """
    # 1行目
    if len(pre_list) == 0:
        return len([i for i in index_list if i - 1 not in index_list])

    # 2行目以降
    count = 0
    for i in index_list:
        # 前の配列にて、左上,上,右上に池があるか確認
        if (i - 1 in pre_list) or i in pre_list or (i + 1 in pre_list):
            continue
        # 今の配列にて、左に池があるか確認
        if i - 1 in index_list:
            continue
        count = count + 1
    return count


if __name__ == '__main__':
    # n = 10
    # m = 12
    INPUT = []
    INPUT.append(['W', '', '', '', '', '', '', '', '', 'W', 'W', ''])
    INPUT.append(['', 'W', 'W', 'W', '', '', '', '', '', 'W', 'W', 'W'])
    INPUT.append(['', '', '', '', 'W', 'W', '', '', '', 'W', 'W', ''])
    INPUT.append(['', '', '', '', '', '', '', '', '', 'W', 'W', ''])
    INPUT.append(['', '', '', '', '', '', '', '', '', 'W', '', ''])
    INPUT.append(['', '', 'W', '', '', '', '', '', '', 'W', '', ''])
    INPUT.append(['', 'W', '', 'W', '', '', '', '', '', 'W', 'W', ''])
    INPUT.append(['W', '', 'W', '', 'W', '', '', '', '', '', 'W', ''])
    INPUT.append(['', 'W', '', 'W', '', '', '', '', '', '', 'W', ''])
    INPUT.append(['', '', 'W', '', '', '', '', '', '', '', 'W', ''])

    COUNT = 0
    PRE_LIST = []
    for lakes in INPUT:
        index_list = get_lake_list_convert_to_index_list(lakes)
        COUNT = COUNT + get_lake_counting(index_list, PRE_LIST)
        PRE_LIST = index_list
    print(COUNT)
