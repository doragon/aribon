"""p43 problem"""

# coding: utf-8
# ---------------------------------------------------------
# 区間スケジューリングの問題
# ---------------------------------------------------------


def get_s_t_list(s, t, n):
    """
        s, tのリストをstart, endの辞書型のデータ構造にし、そのリストを返す
    """
    st_list = []
    for i in range(n):
        st_list.append({'start': s[i], 'end': t[i]})
    return st_list


def buble_sort(st_list):
    """
        引数リストにおいて終了時刻の昇順ソートを行う
    """
    k = len(st_list) - 1
    for i in range(k):
        for j in range(k, i, -1):
            if st_list[j - 1]['end'] > st_list[j]['end']:
                temp = st_list[j]
                st_list[j] = st_list[j - 1]
                st_list[j - 1] = temp


def get_work_count(st_list):
    """
        引数リストがこなせる最大仕事数を返す
    """
    count = 0
    pre_work_end_time = 0
    for i, x in enumerate(st_list):
        if i == 0 or x['start'] > pre_work_end_time:
            count += 1
            pre_work_end_time = x['end']
    return count


if __name__ == '__main__':
    n = 5
    # s = [1, 2, 4, 6, 8]
    # t = [3, 5, 7, 9, 10]
    s = [4, 2, 1, 6, 8]
    t = [7, 5, 3, 9, 10]

    st_list = get_s_t_list(s, t, n)
    buble_sort(st_list)
    print(get_work_count(st_list))
