import string


################### FUNCTIONS ###################

def mainMenu():
    menu_question = input('START?  (y/n)  ')
    print('')
    if menu_question == ('y'):
        setupMenu()
    else:
        mainMenu()
    
def setupMenu():
    print('1. Centimeters to inches')
    print('2. Inches to centimeters')
    print('')
    print('3. Celsius to Fahrenheit')
    print('4. Fahrenheit to Celsius')
    print('')
    print('5. Feet to inches')
    print('6. Inches to feet')
    print('')
    print('7. Miles to Yards')
    print('8. Yards to Miles')
    print('')
    print('9. Pounds to Ounces')
    print('10. Ounces to Pounds')

    choose_trans = input('Please choose a mode:  ')

    if choose_trans == ('1'):
        cmToInches()
    if choose_trans == ('2'):
        inchesToCm()
    if choose_trans == ('3'):
        celsiusToFahrenheit()
    if choose_trans == ('4'):
        fahrenheitToCelsius()
    if choose_trans == ('5'):
        feetToInch()
    if choose_trans == ('6'):
        inchesToCm()
    if choose_trans == ('7'):
        mileToYard()
    if choose_trans == ('8'):
        yardToMile()
    if choose_trans == ('9'):
        poundToOunce()
    if choose_trans == ('10'):
        ounceToPound()


################### FUNCTIONS START ###################

#   --------------------------------------------------------
#   CONVERT CENTIMETERS TO INCHES
def cmToInches():
    print('')
    print('Centimeters to inches')
    cmInput = int(input('Convert centimeters to inches: '))
    print(cmInput / 2.54, ' inches. ')

    while input:
        True
        cmInput = int(input('Convert centimeters to inches: '))
        print(cmInput / 2.54, ' inches. ')
#   --------------------------------------------------------

#   --------------------------------------------------------
#   CONVERT INCHES TO CENTIMETERS
def inchesToCm():
    print('')
    print('Inches to centimeters')
    inchInput = int(input('Convert inches to centimeters: '))
    print(inchInput * 2.54, ' centimeters. ')

    while input:
        True
        inchInput = int(input('Convert inches to centimeters: '))
        print(inchInput * 2.54, ' centimeters. ')
#   --------------------------------------------------------

#   --------------------------------------------------------
#   CONVERT CELSIUS TO FAHRENHEIT
def celsiusToFahrenheit():
    print('')
    print('Celsius to Fahrenheit')
    celInput = int(input('Enter Celsius: '))
    print(celInput * 9/5 + 32, 'Fahrenheit degrees' )

    while input:
        True
        celInput = int(input('Enter Celsius: '))
        print(celInput * 9/5 + 32, 'Fahrenheit degrees' )
#   --------------------------------------------------------

#   --------------------------------------------------------
# CONVERT FAHRENHEIT TO CELSIUS
def fahrenheitToCelsius():
    print('')
    print('Fahrenheit to Celsius')
    fahInput = int(input('Enter Fahrenheit: '))
    print(fahInput - 32 * 9/5 , 'Celsius' )

    while input:
        True
        fahInput = int(input('Enter Fahrenheit: '))
        print(fahInput - 32 * 9/5 , 'Celsius' )
#   --------------------------------------------------------

#   --------------------------------------------------------
#   CONVERT FEET TO INCHES
def feetToInch():
    print('')
    print('Feet to Inches')
    feeInput = int(input('Enter feet: '))
    print(feeInput * 12 , 'Inches' )

    while input:
        True
        feeInput = int(input('Enter feet: '))
        print(feeInput * 12 , 'Inches' )
#   --------------------------------------------------------

#   --------------------------------------------------------
#   CONVERT INCHES TO FEET
def inchToFeet():
    print('')
    print('Inches to Feet')
    incInput = int(input('Enter Inches: '))
    print(incInput / 12 , 'Feet' )

    while input:
        True
        incInput = int(input('Enter Inches: '))
        print(incInput / 12 , 'Feet' )
#   --------------------------------------------------------
        
#   --------------------------------------------------------
#   CONVERT MILES TO YARDS
def mileToYard():
    print('')
    print('Miles to Yards')
    mileInput = int(input('Enter Miles: '))
    print(mileInput * 1760, 'Yards')

    while input:
        True
        mileInput = int(input('Enter Miles: '))
        print(mileInput * 1760, 'Yards')
#   --------------------------------------------------------

#   --------------------------------------------------------
#   CONVERT YARDS TO MILES
def yardToMile():
    print('')
    print('Yards to Miles')
    mileInput = int(input('Enter Yards: '))
    print(mileInput / 1760, 'Miles')

    while input:
        True
        mileInput = int(input('Enter Yards: '))
        print(mileInput / 1760, 'Miles')
#   --------------------------------------------------------

#   --------------------------------------------------------
# CONVERT POUNDS TO OUNCES
def poundToOunce():
    print('')
    print('Pounds to Ounces')
    poundInput = int(input('Enter Pounds: '))
    print(poundInput * 16 , 'Ounces')

    while input:
        True
        poundInput = int(input('Enter Pounds: '))
        print(poundInput * 16 , 'Ounces')
#   --------------------------------------------------------

#   --------------------------------------------------------
# CONVERT OUNCES TO POUNDS
def ounceToPound():
    print('')
    print('Ounces to Pounds')
    ounceInput = int(input('Enter Ounces: '))
    print(ounceInput / 16 , 'Pounds')

    while input:
        True
        ounceInput = int(input('Enter Ounces: '))
        print(ounceInput / 16 , 'Pounds')
#   --------------------------------------------------------
    

################### FUNCTIONS END ###################

print('')
print("     V I P's   C O N V E R T E R     ")
print('')
mainMenu()
