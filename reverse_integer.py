def reverse(num):
    up_limit = 2 ** 31 - 1
    down_limit = - (2 ** 31)
    str_num = str(num)
    is_minus = ''
    if str_num[0] == '-':
        is_minus = '-'
        str_num = str_num[1:]

    reversed_num = int(is_minus + str_num[::-1])

    if reversed_num not in range(up_limit, down_limit):
        return 0

    return reversed_num


intiger = int(input())
print(reverse(intiger))