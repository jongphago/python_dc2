def calculate(num1, num2):
    result1 = num1 + num2
    result2 = num1 - num2
    return result1, result2


print(calculate(134, 55))
print(calculate(182.5, 133))
print(calculate(12.67, 214.3))

result = calculate(134, 55)
print("더한 값: {}, 뺀 값:{}".format(result[0], result[1]))
