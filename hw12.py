s = int(input('Please, input time in seconds: '))
h = s//3600
m = (s//60)%60
s1 = s%60
print("Your time is {0:=02}:{1:=02}:{2:=02}".format(h, m, s1))
