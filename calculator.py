def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


n1, n2 = map(int, input("숫자를 입력하세요").split())
result = add(n1, n2)
print("더한값은 %d 입니다." % result)
result1 = subtract(n1, n2)
print("뺀값은 %d 입니다." % result1)
result2 = multiply(n1, n2)
print("곱셈한값은 %d 입니다." % result2)
result3 = divide(n1, n2)
print("나눈값은 %d 입니다." % result3)