num = [10, 20, 50, 40, 60]
sum = 0
for x in num:
    sum = sum+x
    print(x)
print(sum)

list = ['appale', 'mango', 'bal', 'cherry']
for x in list:
    print(x)
print(len(x))

# break statement we can stop the loop before it has loop through

list = [2, 6, 8, 90]
for x in list:
    print(x)
    if x == 8:
        break

# break comes before the print:

list = [56, 76, 86, 97]
for x in list:
    if x == 86:
        break
    print(x)

list = [20, 40, 60, 80, 65]
for x in list:
    if x == 80:
        print(x)
        continue
