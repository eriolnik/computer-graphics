import math

x = float(input())
y = float(input())
alpha = float(input())

Xsum = x * math.cos(alpha) - y * math.sin(alpha)
Ysum = x * math.sin(alpha) + y * math.cos(alpha)

print('x = ', Xsum, '\ny = ', Ysum)