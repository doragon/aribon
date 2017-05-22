"""p45 problem"""

# coding: utf-8
# ---------------------------------------------------------
# 辞書順最小の問題
# ---------------------------------------------------------


def is_front_small_character_code(arg):
    """
        引数文字列の最初と最後の文字コードサイズを比較し、最初が小さいかどうかの結果を返す
    """
    if arg[0] < arg[-1]:
        return True
    return False


if __name__ == '__main__':
    N = 6
    S = 'ACDBCB'
    T = ''

    print(S)
    for i in range(N):
        if is_front_small_character_code(S):
            T = T + S[0]
            S = S[1:]
        else:
            T = T + S[len(S) - 1]
            S = S[0:len(S) - 1]
    print(T)
