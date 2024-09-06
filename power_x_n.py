# O log N
def power(x, n):
    if n == 0:
        return 1

    if n < 0:
        x **= -1
        n *= -1

    # if n < 0:
    #     x = 1 / x
    #     return power(x, n * -1)

    if n % 2 == 1:
        return x * power(x, n - 1)
    else:
        num = power(x, n // 2)
        return num * num


if __name__ == '__main__':
    print(f'{power(2.00000, 10):,.5f}')
    print(f'{power(2.10000, 3):,.5f}')
    print(f'{power(2.00000, -2):,.5f}')
