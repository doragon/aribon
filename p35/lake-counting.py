"""p35 problem"""

# coding: utf-8
# ---------------------------------------------------------
# 池の数問題
# ---------------------------------------------------------


def getLakeListConvertToIndexList(lakeList):
    """ 池の範囲をindex化したリストで返す """
    res = []
    for i in range(len(lakeList)):
        if lakeList[i] == 'W':
            if i not in res:
                res.append(i)
    res.sort()
    return res


def getLakeCounting(indexList, preList):
    """
        池のカウント数を返す。
        ただし、前左右で隣り合ったindexがない場合に限る。
    """
    count = 0
    # 1行目
    if len(preList) == 0:
        for i in indexList:
            if i - 1 in indexList:
                continue
            count = count + 1
        return count

    # 2行目以降
    for i in indexList:
        if (i - 1 in preList) or i in preList or (i + 1 in preList):
            continue
        if i - 1 in indexList:
            continue
        count = count + 1
    return count


if __name__ == '__main__':
    n = 10
    m = 12
    input = []
    input.append(['W', '', '', '', '', '', '', '', '', 'W', 'W', ''])
    input.append(['', 'W', 'W', 'W', '', '', '', '', '', 'W', 'W', 'W'])
    input.append(['', '', '', '', 'W', 'W', '', '', '', 'W', 'W', ''])
    input.append(['', '', '', '', '', '', '', '', '', 'W', 'W', ''])
    input.append(['', '', '', '', '', '', '', '', '', 'W', '', ''])
    input.append(['', '', 'W', '', '', '', '', '', '', 'W', '', ''])
    input.append(['', 'W', '', 'W', '', '', '', '', '', 'W', 'W', ''])
    input.append(['W', '', 'W', '', 'W', '', '', '', '', '', 'W', ''])
    input.append(['', 'W', '', 'W', '', '', '', '', '', '', 'W', ''])
    input.append(['', '', 'W', '', '', '', '', '', '', '', 'W', ''])

    count = 0
    preList = []
    for lakes in input:
        indexList = getLakeListConvertToIndexList(lakes)
        count = count + getLakeCounting(indexList, preList)
        preList = indexList
    print(count)
