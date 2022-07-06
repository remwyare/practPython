import math
import random
import statistics
import keyword #позволяет проверить является ли строка ключевым словом в python
import imp_hello # свой файл
import imp_test
import imp_cubed

print(math.pow(2,3))
print(random.randint(0,100))

nums = [1, 5, 33, 12, 46, 33, 2]
#среднее
print(statistics.mean(nums))
#медиана
print(statistics.median(nums))
#мода
print(statistics.mode(nums))
print(statistics.median_low(nums))

print(keyword.iskeyword("for"))

print(imp_cubed.cube(5))

imp_hello.print_hello()
