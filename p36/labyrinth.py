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


def get_index_in_all_directions(target_list, num_list, count, n, m):
    """
        対象位置から前後左右の有効なindex位置を返す
        また、有効なindex位置の歩数カウントを増やし、num_listを更新する
    """
    res = []
    for target in target_list:
        i = target[0]
        j = target[1]
        if i - 1 >= 0 and num_list[i - 1][j] == 0:
            num_list[i - 1][j] = count + 1
            res.append([i - 1, j])
        if j - 1 >= 0 and num_list[i][j - 1] == 0:
            num_list[i][j - 1] = count + 1
            res.append([i, j - 1])
        if i + 1 < n and num_list[i + 1][j] == 0:
            num_list[i + 1][j] = count + 1
            res.append([i + 1, j])
        if j + 1 < m and num_list[i][j + 1] == 0:
            num_list[i][j + 1] = count + 1
            res.append([i, j + 1])
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

    # start, goalが隣合う場合はカウント1で終了
    if si == gi or sj == gj:
        return 1

    step_count = 0
    index_list = []
    while True:
        if step_count == 0:
            index_list = get_index_in_all_directions([[si, sj]], num_list,
                                                     step_count, n, m)
        else:
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
    n = 10
    m = 10
    input = []
    input.append(['#', 'S', '#', '#', '#', '#', '#', '#', '', '#'])
    input.append(['', '', '', '', '', '', '#', '', '', '#'])
    input.append(['', '#', '', '#', '#', '', '#', '#', '', '#'])
    input.append(['', '#', '', '', '', '', '', '', '', ''])
    input.append(['#', '#', '', '#', '#', '', '#', '#', '#', '#'])
    input.append(['', '', '', '', '#', '', '', '', '', '#'])
    input.append(['', '#', '#', '#', '#', '#', '#', '#', '', '#'])
    input.append(['', '', '', '', '#', '', '', '', '', ''])
    input.append(['', '#', '#', '#', '#', '', '#', '#', '#', ''])
    input.append(['', '', '', '', '#', '', '', '', 'G', '#'])

    num_list = get_input_list_convert_to_num_list(input)
    print('=== Before ===')
    print_labyrinth(num_list)

    step_count = get_step_count(num_list, n, m)
    print('=== After ===')
    print_labyrinth(num_list)

    print('=== Answer ===')
    print(step_count)
