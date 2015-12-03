import math

a = [0,3,3,5,5,5,5,7,7,10]
length = len(a)
average = sum(a)/length
s = 0

for i in range(0,length):
    for j in range(0,length):
        s += abs(a[i] - a[j])
print(s/(2*math.pow(length,2)*average))

now = [32,19,10,24,15]
past = [28,13,18,29,12]
p_now = list(map(lambda n:n/100, now))
p_past = list(map(lambda n:n/100, past))
H_now = 0
H_past = 0
for i in range(0,4):
    H_now += p_now[i]*math.log(p_now[i])
    H_past += p_past[i]*math.log(p_past[i])
print("今年のエントロピーは{0}".format(-H_now))
print("10年前のエントロピーは{0}".format(-H_past))

b = [0,1,2,3,5,5,7,8,9,10]
average = sum(b)/len(b)
for i in range(0,len(b)):
    s = math.pow(b[i] - average, 2)
standard_deviation = math.sqrt( s/len(b) )
z = list(map(lambda n:(n-average)/standard_deviation, b))
print("データbの標準化は\n{0}".format(z))
T = list(map(lambda n:10*n+50, z))
print("偏差値得点は\n{0}".format(T))
