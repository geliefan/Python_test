def countLines(name):
    file = open(name)
    return len(file.readlines())

def countChars(name):
    file = open(name,"r").read()
    return len(file)
def test(name):
    return countLines(name), countChars(name)

name = 'text.txt'
print test(name)

