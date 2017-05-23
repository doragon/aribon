"""p47 problem"""

# coding: utf-8
# ---------------------------------------------------------
# saruman's armyの問題
# ---------------------------------------------------------


def get_new_index(basic_range, x_list, index):
    """
        次の基点となるindexを取得する
    """
    point_range = x_list[index] + basic_range
    while True:
        if index == len(x_list) - 1:
            break
        if x_list[index] > point_range:
            break
        index += 1
    return index


def get_number_of_reference_point(basic_range, x_list):
    """
        基点数を返す
    """
    if len(x_list) == 0:
        return 0

    count = 1
    index = 0
    for i, x in enumerate(x_list):
        # 基点となるindex未満は除外
        if i < index:
            continue
        # 基点からの範囲を超えた場合
        if x > x_list[index] + basic_range:
            index = get_new_index(basic_range, x_list, i)
            count += 1
    return count


if __name__ == '__main__':
    N = 6
    R = 10
    X = [1, 7, 15, 20, 30, 50]

    print(get_number_of_reference_point(R, sorted(X)))
