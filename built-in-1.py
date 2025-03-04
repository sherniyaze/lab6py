import math 
numbers = input()
list_of_num = [int(x.strip()) for x in numbers.split(" ")]
product_of_all = math.prod(list_of_num)
print(f"the porduct of all numbers in list: {product_of_all}")
