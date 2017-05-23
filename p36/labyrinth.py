"""p36 problem"""

# coding: utf-8
# ---------------------------------------------------------
# 迷路の最短路問題
# ---------------------------------------------------------


def get_input_list_convert_to_num_list(inputList):
    """
        [#:-1, S:-2, G:-3, 空文字:0] の数値配列に置き換え、そのリストを返す
    """
    numList = []
    for row in inputList:
        rowList = []
        for col in row:
            if col == '#':
                rowList.append(-1)
            elif col == 'S':
                rowList.append(-2)
            elif col == 'G':
                rowList.append(-3)
            else:
                rowList.append(0)
        numList.append(rowList)
    return numList


def get_position(target_num, num_list):
    """
        target_num の位置を取得する
        該当箇所が存在しない場合は(-1,-1)を返す
    """
    for i, row in enumerate(num_list):
        for j, col in enumerate(row):
            if col == target_num:
                # 配列内の位置を取得
                return i, j
    return -1, -1


def is_unsearched(position):
    return position == 0


def is_goal(position):
    return position == -3


def get_index_in_all_directions(target_list, num_list, count, n, m):
    """
        対象位置から前後左右の有効なindex位置を返す
        また、有効なindex位置の歩数カウントを増やし、num_listを更新する
    """
    res = []
    for target in target_list:
        index_i = target[0]
        index_j = target[1]
        for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            index_i = target[0] + i
            index_j = target[1] + j
            if index_i < 0 or index_i >= n or index_j < 0 or index_j >= m:
                continue
            if is_unsearched(num_list[index_i][index_j]):
                num_list[index_i][index_j] = count + 1
                res.append([index_i, index_j])
            if is_goal(num_list[index_i][index_j]):
                res.append([index_i, index_j])
                return res
    return res


def is_next_step_goal(target_list, gi, gj):
    """
        次がゴール地点かどうか判定
    """
    for target in target_list:
        if target[0] == gi and target[1] == gj:
            return True
    return False


def get_step_count(num_list, n, m):
    """
        迷路の最短路を取得
    """
    # start, goalの場所を取得
    si, sj = get_position(-2, num_list)
    gi, gj = get_position(-3, num_list)

    step_count = 0
    index_list = [[si, sj]]
    while True:
        index_list = get_index_in_all_directions(index_list, num_list,
                                                 step_count, n, m)
        step_count = step_count + 1
        if len(index_list) == 0 or is_next_step_goal(index_list, gi, gj):
            break
    return step_count


def print_labyrinth(num_list):
    """
        経路確認用のメソッド
    """
    for nl in num_list:
        print(nl)


if __name__ == '__main__':
    # test case1
    N = 10
    M = 10
    INPUT = []
    INPUT.append(['#', 'S', '#', '#', '#', '#', '#', '#', '', '#'])
    INPUT.append(['', '', '', '', '', '', '#', '', '', '#'])
    INPUT.append(['', '#', '', '#', '#', '', '#', '#', '', '#'])
    INPUT.append(['', '#', '', '', '', '', '', '', '', ''])
    INPUT.append(['#', '#', '', '#', '#', '', '#', '#', '#', '#'])
    INPUT.append(['', '', '', '', '#', '', '', '', '', '#'])
    INPUT.append(['', '#', '#', '#', '#', '#', '#', '#', '', '#'])
    INPUT.append(['', '', '', '', '#', '', '', '', '', ''])
    INPUT.append(['', '#', '#', '#', '#', '', '#', '#', '#', ''])
    INPUT.append(['', '', '', '', '#', '', '', '', 'G', '#'])

    # test case2
    # N = 3
    # M = 3
    # INPUT = []
    # INPUT.append(['S', '', ''])
    # INPUT.append(['', '#', ''])
    # INPUT.append(['G', '#', '#'])

    num_list = get_input_list_convert_to_num_list(INPUT)
    print('=== Before ===')
    print_labyrinth(num_list)

    step_count = get_step_count(num_list, N, M)
    print('=== After ===')
    print_labyrinth(num_list)

    print('=== Answer ===')
    print(step_count)
