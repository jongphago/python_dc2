def calculate(num1:float, num2:float) -> tuple[float, float]:
    result1 = num1 + num2
    result2 = num1 - num2
    return result1, result2

# res_sum, res_sub = calculate(134, 55)
# print(res_sum)
# print(res_sub)
# print(calculate(182.5, 133))
# print(calculate(12.67, 214.3))

result:tuple[float, float] = calculate(134, 55)
print(f"더한 값: {result[0]}, 뺀 값:{result[1]}")
