original = open('shedevrofilefor7.txt', 'r')
copy = open('shedevrofilefor7b.txt', 'w')
how_m = int(input("how many content : "))
list  = []
for i in range(how_m):
    cash = int(input(f"Enter line for copy {i + 1} : ")) - 1
    list.append(cash)
    del cash
all_lines = original.readlines()
for i in list:
    content = original.readline(list[i])
    copy.write(all_lines[i])
    del content
original.close()
copy.close()
copy = open('shedevrofilefor7b.txt', 'r')
print(copy.read())