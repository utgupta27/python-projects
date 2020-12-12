def savetofile(inputval, filename):
    with open(filename, 'w') as textfile:
        textfile.write(inputval)
