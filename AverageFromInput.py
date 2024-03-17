# CS-175L-02
# Leslie Bustamante
# Average from input

file = open("numbers.txt", "r")
lines = file.readlines()
k = 0
numbers = []
for line in lines:
    line = line.split()
    for num in line:
        numbers.append(int(num))
        k += int(num)
average = k/len(numbers)

print(f'I read in 1 number(s)  Current number is:    {numbers[0]:.2f}        Total is :     {numbers[0]:.2f}')
print(f'I read in 2 number(s)  Current number is:    {numbers[1]:.2f}        Total is :     {numbers[1]+numbers[0]:.2f}')
print(f'I read in 3 number(s)  Current number is:    {numbers[2]:.2f}       Total is :    {numbers[2]+numbers[1]+numbers[0]:.2f}')
print('Average is:',average)

file.close()
