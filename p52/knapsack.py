"""p52 problem"""

# coding: utf-8
# ---------------------------------------------------------
# ナップサックの問題
# ---------------------------------------------------------


def get_bigger_value(weight, index):
    """
        対象indexの要素を採用または非採用した場合のより大きい価値を返す
    """
    used = get_max_value(weight - w[index], index + 1) + v[index]
    unused = get_max_value(weight, index + 1)
    if used < unused:
        return unused
    return used


def get_max_value(weight, index):
    """
        引数の重さを超えない最大価値を返す
    """
    if n == index:
        # 全ての要素を検査した場合
        return 0

    value = 0
    if weight < w[index]:
        # 対象要素が引数の重さを超えた場合
        value = get_max_value(weight, index + 1)
    else:
        # 対象要素を採用または非採用した場合
        value = get_bigger_value(weight, index)
    return value


def set_global_variable():
    """
        使用するグローバル変数を設定する
        対象は要素数n, 重さリストw, 価値リストv
    """
    global n
    global w
    global v
    n = 4
    wv = [[2, 3], [1, 2], [3, 4], [2, 2]]
    w = []
    v = []
    for i, x in enumerate(wv):
        w.append(x[0])
        v.append(x[1])


if __name__ == '__main__':
    W = 5
    set_global_variable()
    print(get_max_value(W, 0))
