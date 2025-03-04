file = open('shedevrofilefor5.txt', 'w')
number  = int(input("Enter size : "))
list = []
for i in range(number):
    list.append(i)
file.write(str(list))
file.close()
file = open('shedevrofilefor5.txt', 'r')
print(file.read())
file.close