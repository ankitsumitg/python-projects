import sys
from caloric_balance import CaloricBalance
def formatMenu():
    return ['What would you like to do?', '[f] Record Food Consumption', '[a] Record Physical Activity', '[q] Quit']
def formatMenuPrompt():
    return 'Enter an option: '
def formatActivityMenu():
    return ['Choose an activity to record', '[j] Jump rope', '[r] Running', '[s] Sitting', '[w] Walking']
def getUserString(string):
    ip = input(string).strip()
    return ip if ip != '' else getUserString(string)
def getUserFloat(string):
    try:
        fnumtest = getUserString(string)
        fnum = float(fnumtest)
        if fnum <=0:
            print('Please enter a number greater than zero.')
            return getUserFloat(string)
        else: return  fnum
    except:
        print("Please enter a number.")
        return getUserFloat(string)
def createCaloricBalance():
    c = CaloricBalance(getUserString('What is your gender (f or m)? '),getUserFloat('What is your age? '),getUserFloat('What is your height in inches?? '),getUserFloat('What is your weight in pounds? '))
    print('\nThanks! Now, throughout the day, tell me each time you eat or move.\nYour caloric balance is starting at -1417.9 (you need to eat something)')
    return c
def recordActivityAction(cb):
    for i in formatActivityMenu():
        print(i)
    a = getUserString(formatMenuPrompt())
    dict={'j':0.074,'r':0.087,'s':0.009,'w':0.036}
    if(a in list('jrsw')):
        min=getUserFloat('For how many minutes did you perform this activity? ')
        cb.recordActivity(dict[a],min)
        print('Awesome! Your caloric balance is now '+str(cb.getBalance())+'\n')
    else:
        print('Sorry, that option is invalid.\n')

def eatFoodAction(cb):
    cal=getUserFloat('Okay! How many calories did you just eat? ')
    cb.eatFood(cal)
    print('Sweet! Your caloric balance is now '+str(cb.getBalance())+'\n')
def quitAction(cb):
    print('Leaving? You should do this again tomorrow. Stay healthy!')
    sys.exit(0)
def applyAction(cb,a):
    if (a == 'f'):
        eatFoodAction(cb)
    elif (a == 'a'):
        recordActivityAction(cb)
    elif (a == 'q'):
        quitAction(cb)
    else:
        print('Sorry, that option is invalid.\n')
def main():
    print('Hi! This program will calculate your caloric balance for the day!\nBefore we can start, I need some information about you. Be honest! :)\n')
    cb = createCaloricBalance()
    while True:
        for i in formatMenu():
            print(i)
        a = getUserString('Enter an option: ')
        applyAction(cb, a)

if __name__ == '__main__':
    main()