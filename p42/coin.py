"""p42 problem"""

# coding: utf-8
# ---------------------------------------------------------
# 硬貨の問題
# ---------------------------------------------------------


def get_used_coin_list(C, A, key_list):
    """
        使用したコインのリストを返す
    """
    used_coin_list = []
    for key in key_list:
        for i in range(C[str(key)]):
            if A - key == 0:
                used_coin_list.append(key)
                return used_coin_list
            elif A - key < 0:
                break
            else:
                used_coin_list.append(key)
                A = A - key
    return used_coin_list


if __name__ == '__main__':
    C = {'1': 3, '5': 2, '10': 1, '50': 3, '100': 0, '500': 2}
    A = 620
    key_list = [500, 100, 50, 10, 5, 1]

    used_coin_list = get_used_coin_list(C, A, key_list)
    print(used_coin_list)
    print(len(used_coin_list))
