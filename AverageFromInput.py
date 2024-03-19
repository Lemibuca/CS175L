# CS-175L-02
# Leslie Bustamante
# Average from input
def main():
      
    file = open('numbers.txt', 'r')
    
    sum = 0
    count = 0

    for number in file:
        sum += int(number)
        count += 1
        num = int(number)
        print(f'I read in {count} number(s)  Current number is:    {num:.2f}        Total is :     {sum:.2f} ')
   
    average = sum / count

    print('The average is:', average)

    file.close()
if __name__ == '__main__':
    main()

