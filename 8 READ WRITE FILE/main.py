def writeToFile(filename, text):
    with open(filename, 'w') as f:
        data = text
        f.write(data)
    

def appendToFile(fileName, text):
    with open(fileName, 'a') as f:
        data = text
        f.write(data)

def readFromFile(filename):
    with open(filename) as f:
        return f.read()
    
    
    


#print(readFromFile('greet.txt'))
writeToFile('greet.txt', 'Hello!\n')
appendToFile('greet.txt', 'Goodbye!\n')
assert readFromFile('greet.txt') == 'Hello!\nGoodbye!\n'