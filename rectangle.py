def inputnum(element):
    while not str.isdigit(element):
        element = input('This is not a number,Please input again:')
    element = int(element)
    return element

def draw(column, raw, mark):
    for i in range(0,column):
        print(mark*column)

recColumn = inputnum(input('Please input the column number:'))
recraw = inputnum(input('Please input the raw number:'))
recmark = input('Please input the mark:')
draw(recColumn, recraw, recmark)


