# CS-175L-02
# Leslie Bustamante
# Average from input
def main():
    
    try:   
        file = open('numbers.txt', 'r')
        
        sum = 0
        count = 0
        
        for number in file:
            
            try:
                sum += int(number)
                count += 1
                num = int(number)
                print(f'I read in {count} number(s)  Current number is:    {num:.2f}        Total is :     {sum:.2f} ')       
            except ValueError:
                print(f'Bad data: {number}, skipping')
       
            average = sum / count
   
        print('The average is:', average)
        
    except IOError:
         print("SystemExit: File not found: numbers.txt - existing")
        
    
    file.close()
if __name__ == '__main__':
    main()

