"""p56 problem"""

# coding: utf-8
# ---------------------------------------------------------
# 最長共通部分列の問題
#
# 模範解答と同じ
# http://d.hatena.ne.jp/naoya/20090328/1238251033
# ---------------------------------------------------------


def print_lcs(s, t, lcs, i, j):
    if i == 0 or j == 0:
        return
    if s[i - 1] == t[j - 1]:
        print_lcs(s, t, lcs, i - 1, j - 1)
        print(s[i - 1], end='')
    else:
        if lcs[i - 1][j] >= lcs[i][j - 1]:
            print_lcs(s, t, lcs, i - 1, j)
        else:
            print_lcs(s, t, lcs, i, j - 1)


def get_lcs(s, t):
    lcs = [[0 for j in range(len(t) + 1)] for i in range(len(s) + 1)]
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            x = 0
            if s[i - 1] == t[j - 1]:
                x = 1
            lcs[i][j] = max(lcs[i - 1][j - 1] + x, lcs[i - 1][j],
                            lcs[i][j - 1])
    return lcs


if __name__ == '__main__':
    n = 4
    m = 4
    s = 'abcd'
    t = 'becd'
    # Answer: 3(bcd)

    lcs = get_lcs(s, t)
    print(lcs)

    # Answer
    print(lcs[n][m])
    # 最長共通部分列
    print_lcs(s, t, lcs, len(s), len(t))
