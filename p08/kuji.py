"""p08 problem"""

# coding: utf-8
# ---------------------------------------------------------
# くじびき問題
# ---------------------------------------------------------


def isUpperLimitOver(m, sum):
    return m < sum


def isExistenceCombination(k, m):
    for num1 in k:
        if isUpperLimitOver(m, num1):
            continue
        for num2 in k:
            if isUpperLimitOver(m, num1 + num2):
                continue
            for num3 in k:
                if isUpperLimitOver(m, num1 + num2 + num3):
                    continue
                for num4 in k:
                    if m == num1 + num2 + num3 + num4:
                        print(
                            str(num1) + ' : ' + str(num2) + ' : ' + str(num3) +
                            ' : ' + str(num4))
                        return True
    return False


if __name__ == '__main__':
    m = 100
    k = [1, 50, 40, 6, 4, 1, 1, 1, 1, 1]

    # 重複項目を削除して、降順ソートをかける
    k = list(set(k))
    k.reverse()

    if isExistenceCombination(k, m):
        print('True')
