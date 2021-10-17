try:
    month = int(input("Please, input number of month in 1 fo 12: "))
except ValueError:
    print("Wrong! Only numbers between 1 and 12")
else:
    win = [12, 1, 2]
    spr = [3, 4, 5]
    summertime_sadness = [6, 7, 8]
    falls = [9, 10, 11]
    if month in win:
        print("Winter")
    elif month in spr:
        print("Spring")
    elif month in summertime_sadness:
        print("Summer")
    elif month in falls:
        print("Fall")
    else:
        print("Wrong number. Only between 1 and 12")

