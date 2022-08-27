leap = 0
flag = 0
counter = 0
temp = 6
print("Enter year: ")
year = int(input())
print("Enter month: ")
month = int(input())
print("Enter Day: ")
day = int(input())
while flag == 0:
    if year < 1399 or year > 1498:
        print("Try again Enter another year: ")
        year = int(input())
    else:
        flag = 1
if year == 1408 or year == 1441 or year == 1474:
    leap = 1
else:
    if year < 1408:
        if (year - 1399) % 4 == 0:
            if year != 1407:
                leap = 1
    else:
        if 1408 < year and year < 1441:
            if (year - 1408) % 4 == 0:
                if year != 1440:
                    leap = 1
        else:
            if 1441 < year and year < 1474:
                if (year - 1441) % 4 == 0:
                    if year != 1473:
                        leap = 1
            else:
                if year > 1474:
                    if (year - 1474) % 4 == 0:
                        leap = 1
diff = year - 1399
if leap == 1:
    diff = diff - 1
if year == 1399:
    pass
else:
    while year > 1399 and year <= 1498:
        if year >= 1474:
            while year >= 1474:
                if (year - 1474) % 4 == 0:
                    counter = counter + 1
                    year = year - 1
                else:
                    year = year - 1
        else:
            if year < 1474 and year >= 1441:
                while year < 1474 and year >= 1441:
                    if year != 1473:
                        if (year - 1441) % 4 == 0:
                            counter = counter + 1
                            year = year - 1
                        else:
                            year = year - 1
                    else:
                        year = year - 1
            else:
                if year < 1441 and year >= 1408:
                    while year < 1441 and year >= 1408:
                        if year != 1440:
                            if (year - 1408) % 4 == 0:
                                counter = counter + 1
                                year = year - 1
                            else:
                                year = year - 1
                        else:
                            year = year - 1
                else:
                    if year < 1408 and year >= 1399:
                        while year < 1408 and year >= 1399:
                            if year != 1407:
                                if (year - 1399) % 4 == 0:
                                    counter = counter + 1
                                    year = year - 1
                                else:
                                    year = year - 1
                            else:
                                year = year - 1
print("Leap: " + str(leap))
print("Diffrent: " + str(diff))
print("counter: " + str(counter))
diff = diff - counter
counter = counter * 2
pishravi = diff + counter
print(pishravi)
pishravi = pishravi % 7
print(pishravi)
while pishravi >= 0:
    if temp >= 0 and temp < 7:
        temp = temp + 1
        pishravi = pishravi - 1
    else:
        temp = temp - 7
temp = temp - 1
print("pishravi: " + str(temp))
if month == 1:
    pass
else:
    if month >= 2 and month <= 7:
        month = month - 1
        pdays = month * 31
    else:
        if month == 8:
            month = month - 2
            pdays = month * 31
            pdays = pdays + 30
        else:
            if month == 9:
                month = month - 3
                pdays = month * 31
                pdays = pdays + 60
            else:
                if month == 10:
                    month = month - 4
                    pdays = month * 31
                    pdays = pdays + 90
                else:
                    if month == 11:
                        month = month - 5
                        pdays = month * 31
                        pdays = pdays + 120
                    else:
                        if month == 12:
                            month = month - 6
                            pdays = month * 31
                            pdays = pdays + 150
print("Past Days: " + str(pdays))
day = day + pdays
day = day % 7
while day >= 0:
    if temp >= 0 and temp < 7:
        temp = temp + 1
        day = day - 1
    else:
        temp = temp - 7
temp = temp - 2
if temp == 0:
    print("shanbeh")
else:
    if temp == 1:
        print("1shanbeh")
    else:
        if temp == 2:
            print("2shanbeh")
        else:
            if temp == 3:
                print("3shanbeh")
            else:
                if temp == 4:
                    print("4shanbeh")
                else:
                    if temp == 5:
                        print("5shanbeh")
                    else:
                        if temp == 6:
                            print("adineh")
