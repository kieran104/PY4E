try:
    userHours = float(input('Enter hours worked: '))
    userRate = float(input('Enter your rate: '))
except:
    print('Error, please enter a number')
    quit()
   
overtimeRate = userRate * 0.5
overtimeHours = 0
overtimePay = 0

if userHours > 40:
    overtimeHours = userHours - 40
    overtimePay = overtimeRate * overtimeHours


print('Pay: ', (userHours * userRate) + (overtimePay))