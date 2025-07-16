def is_leap(year):
    if year % 4==0:
        if year % 100==0:
            if year % 400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
year_in = (int(input("enter a year ")))
print(is_leap(year_in))

    