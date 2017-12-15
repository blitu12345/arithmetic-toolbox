# use python 2
n = input()

a = map(int , raw_input().split())
b = map(int, raw_input().split())
a = sorted(a)
b = sorted(b)
sum1 = 0
for i in range(n):
	sum1 += a[i]*b[n-1-i]
print sum1