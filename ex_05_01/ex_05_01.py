numberCount = 0
numberTotal = 0

while True:
    userNumber = input('Enter a number:')
    if userNumber == 'done':
        break
    try:
        userNumberFloat = float(userNumber)
    except:
        print('Invalid input')
        continue
    
    numberTotal = userNumberFloat + numberTotal
    numberCount = numberCount + 1

print('Average:' , numberTotal / numberCount)
print('Sum of all numbers:', numberTotal)
print('Count of numbers:', numberCount)
    