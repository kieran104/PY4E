userHours = float(input('Enter hours worked: '))
userRate = float(input('Enter your rate: '))
overtimeRate = userRate * 0.5 # it's 0.5 and not 1.5 because the hours over 40 are still calculated in the normal hours*rate
overtimeHours = 0
overtimePay = 0

if userHours > 40:
    overtimeHours = userHours - 40
    overtimePay = overtimeRate * overtimeHours


print('Pay: ', (userHours * userRate) + (overtimePay))