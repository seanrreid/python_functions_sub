def make_formal_greeting(name, title):
    return f"This is {name}, the {title}!"

def separateRuns():
    print('*******************')
    print()

mustard = make_formal_greeting('Mustard', 'Colonel')
professor = make_formal_greeting('Plum', 'Professor')

# print(professor)
# separateRuns()
# print(mustard)


def addTwo(startingValue):
    endingValue = startingValue + 2
    print('The sum of', startingValue, 'and 2 is:', endingValue)


result = addTwo(5)
print(result)
