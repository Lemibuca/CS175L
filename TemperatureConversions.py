#LESLIE BUSTAMANTE
#CS 175L - 02
#TEMPERATURE CONVERSIONS

def main():
    controlLoop()

def convertToKelvin(Fahrenheit):
    kelvin =(Fahrenheit - 32) * 5/9 + 273.15
    return kelvin
    

def convertToCentigrade(Fahrenheit):
    centigrade =(Fahrenheit - 32) * 5/9
    return centigrade
    

def doConversion(Fahrenheit):
    kelvin = convertToKelvin(Fahrenheit)
    centigrade = convertToCentigrade(Fahrenheit)
    print(f'Fahrenheit: {Fahrenheit:.2f} Kelvin: {kelvin:.2f} Centigrade: {centigrade:.2f}')
    
    
def repeat():
    how_many_times = int(input('How many conversions would you like to do this time? ')) 
    
    for x in range (how_many_times):
        Fahrenheit = getFahrenheit()
        doConversion (Fahrenheit)        
            

def controlLoop():
    while True:
        control = input('Do you want to do some conversions(Yes or No)? ')
        if control == 'yes' or control == 'Yes' or control == 'YES':
            repeat()
        else:
            break
    

def getFahrenheit():
    while True:
        Fahrenheit = float(input('Enter Fahrenheit temperature (must be -50 to 130): '))
        if -50 <= Fahrenheit <=130:
            return Fahrenheit
        else:
            print('Please re-enter: ')
            
        

# This code will call the 'main' function if the entire program was run.
if __name__ == '__main__':
    main()
