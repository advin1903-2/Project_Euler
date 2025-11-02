import numpy as np

numbers = np.arange(2, 10000)
divisors_sum = np.zeros(len(numbers), dtype=int)
amicable_test = np.zeros(len(numbers), dtype=int)

for i in range(len(numbers)):
    number_test = numbers[i]
    for j in range(1, number_test // 2 + 1):
        if number_test % j == 0:
            divisors_sum[i] += j

for i in range(len(numbers)):
    if divisors_sum[i] >= 10000:
        continue

    idx = int(divisors_sum[i] - 2) 
    if divisors_sum[idx] == numbers[i] and numbers[i] != divisors_sum[i]:
        amicable_test[i] = 1

sum_amicable_numbers = 0
for i in range(len(numbers)):
    if amicable_test[i] == 1:
        sum_amicable_numbers += numbers[i]

print(sum_amicable_numbers)