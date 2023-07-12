def computepay(hours, rate):
    if hours > 40:
        regularPay = rate * hours
        overtimePay = (hours - 40) * (rate * 0.5)
        totalPay = regularPay + overtimePay
    else:
        totalPay = hours * rate
    return totalPay

userHours = float(input('Enter hours worked: '))
userRate = float(input('Enter your rate: '))
XP = computepay(userHours, userRate)

print('Pay:', XP)