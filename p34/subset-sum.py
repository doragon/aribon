"""p34 problem"""

# coding: utf-8
# ---------------------------------------------------------
# 部分和問題
# ---------------------------------------------------------


def isExistenceSubsetSum(n, k):
    # 終了条件
    if n == 0:
        return True
    elif n < 0:
        return False
    # 上記に該当せず、リストが空の場合は該当和がなし
    if len(k) == 0:
        return False

    copy_k = list(k)
    value = copy_k.pop()

    isUnusedValue = isExistenceSubsetSum(n, copy_k)
    isUsedValue = isExistenceSubsetSum(n - value, copy_k)
    return isUnusedValue or isUsedValue


if __name__ == '__main__':
    n = 13
    k = [1, 7, 4, 2]

    print(str(isExistenceSubsetSum(n, k)))
