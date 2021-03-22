import sys
def milesPerGallon(miles,gallons):
    if(gallons==0):
        return 0.0
    else:
        return miles/gallons
def createNotebook():
    return list()

def recordTrip(notebook,date,miles,gallons):
    notebook.append({'date': date, 'miles': miles, 'gallons': gallons})

def listTrips(notebook):
    ret=list()
    for i in notebook:
        ret.append('On '+str(i['date'])+': '+str(i['miles'])+' miles traveled using '+str(i['gallons'])+' gallons. Gas mileage: '+str(milesPerGallon(i['miles'],i['gallons']))+' MPG')
    return ret

def calculateMPG(notebook):
    sum_miles=0
    sum_gallons=0
    for i in notebook:
        sum_miles+=i['miles']
        sum_gallons+=i['gallons']
    if(sum_gallons==0):
        return 0.0
    else:
        return float(sum_miles/sum_gallons)

def formatMenu():
    return ['What would you like to do?', '[r] Record Gas Consumption', '[l] List Mileage History', '[c] Calculate Gas Mileage', '[q] Quit']

def formatMenuPrompt():
    return 'Enter an option: '

def getUserString(prompt):
    a=str(input(prompt)).strip()
    if(a==''):
        return getUserString(prompt)
    else:
        return a

def getUserFloat(prompt):
    a=0
    try:
        a=float(input(prompt))
        if(a<=0):
            print('Please enter a number greater than zero.')
            return getUserFloat(prompt)
        else:
            return a
    except:
        print("Please enter a number.")
        return getUserFloat(prompt)

def getDate():
    a=getUserString('What is the date? ')
    return a

def getMiles():
    a=getUserFloat('How many miles did you drive since last filling up? ')
    return float(a)

def getGallons():
    a=getUserFloat('How many gallons of gas did you add to your tank? ')
    return float(a)

def recordTripAction(notebook):
    date=getDate()
    miles=getMiles()
    gallons=getGallons()
    recordTrip(notebook,date,miles,gallons)
    print('Saved!\n')

def listTripsAction(notebook):
    if(len(notebook)==0):
        print('You first need to record your gas consumption!\n')
    else:
        trips=listTrips(notebook)
        for i in trips:
            print(i)
        print()

def calculateMPGAction(notebook):
    if(len(notebook)==0):
        print('You first need to record your gas consumption!\n')
    else:
        print('Average gas mileage: ',str(calculateMPG(notebook)),' MPG\n',sep='')

def quitAction(notebook):
    print('Bye! See you next time!')
    sys.exit(0)

def applyAction(notebook,a):
    if(a=='r'):
        recordTripAction(notebook)
    elif(a=='l'):
        listTripsAction(notebook)
    elif(a=='c'):
        calculateMPGAction(notebook)
    elif(a=='q'):
        quitAction(notebook)
    else:
        print('Sorry, that option is invalid.\n')

def main():
    note=createNotebook()
    menu = formatMenu()
    while(True):
        for i in menu:
            print(i)
        a=getUserString('Enter an option: ')
        applyAction(note,a)

if __name__ == '__main__':
    main()
    