import sys
def createIndex():
    return dict()

def recordBook(index,isbn,book):
    index[isbn] = book

def findBook(index,isbn):
    return  index[isbn] if index.get(isbn) else ''

def listBooks(index):
    return [] if not bool(index) else [str(i+1)+') '+k+': '+v for i,(k,v) in enumerate(index.items())]

def formatMenu():
    return [ 'What would you like to do?', '[r] Record a Book', '[f] Find a Book', '[l] List all Books', '[q] Quit' ]

def formatMenuPrompt():
    return 'Enter an option: '

def getUserChoice(string):
    ip = input(string).strip()
    return ip if ip != '' else getUserChoice(string)

def getISBN():
    return getUserChoice('Enter an ISBN: ')

def getTitle():
    return getUserChoice('Enter a book title: ')

def recordBookAction(index):
    isbn = getISBN()
    title = getTitle()
    index[isbn]=title
    print('Book saved!')

def findBookAction(index):
    isbn = getISBN()
    op =  findBook(index,isbn)
    if op == '':
        print('Book not found')
    else:
        print('Book found: '+op)

def listBooksAction(index):
    op = listBooks(index)
    if op == '':
        print('No books')
    else:
        for i in op:
            print(i)

def quitAction(index):
    print('Bye! See you next time!')
    sys.exit(0)

def applyAction(index,action):
    if action == 'r':
        recordBookAction(index)
    elif action == 'f':
        findBookAction(index)
    elif action == 'l':
        listBooksAction(index)
    elif action == 'q':
        quitAction(index)
    else:
        print('Sorry, that option is invalid.')

def main():
    index = createIndex()
    while True:
        for i in formatMenu():
            print(i)
        applyAction(index,getUserChoice(formatMenuPrompt()))

if __name__ == '__main__':
    main()

