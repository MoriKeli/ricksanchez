leap_yr = int(input('Enter a Year: '))
if leap_yr % 4 == 0 and leap_yr % 400 == 0 or leap_yr % 100 != 0:
    print(leap_yr, 'is a leap year.')
else:
    print(leap_yr, 'is not a leap year.')
