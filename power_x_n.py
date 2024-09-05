def power(x, n):
    if n == 0:
        return 1

    n = power(x, n // 2)
    if n % 2 == 0:
        return n * n
    else:
        if n > 0:
            return x * n * n
        else:
            return (n * n) / x


if __name__ == '__main__':
    print(power(2,4))
