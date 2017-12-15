#use python 2
m=map(int,raw_input().split())
M=map(int,raw_input().split())
for i in M[1:]:
	print m[1:].index(i),