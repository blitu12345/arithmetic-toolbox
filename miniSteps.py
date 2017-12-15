#use python 2
n=input()
s = [[0 for i in range(1)] for j in range(1000001)]
s[1][0]=0;s[2][0]=1;s[3][0]=1;i=4
s[1].append(1);s[2].extend([1,2]);s[3].extend([1,3])
while(i<=n):
	p=[]
	mini=99999999
	#print "entered"
	#print "i"
	#print i
	if(i%3==0):
	#print "if"
		p1=s[i/3][0]+1
		if(mini>p1):
			mini=p1
			p=[];p.extend(s[i/3][1:]);p.append(s[i/3][-1]*3)

	#	print "mini"
	#	print p1
	#	print mini
	elif(i%2==0):
		#print "elif"
		p2=s[i/2][0]+1
		if(mini>p2):
			mini=p2
			p=[];p.extend(s[i/2][1:]);p.append(s[i/2][-1]*2)
		#print "mini"
	#	print p2
		#print mini
	p3=s[i-1][0]+1
	#print "p3"
	#print p3
	if(mini>p3):
		mini=p3
		p=[];p.extend(s[i-1][1:]);p.append(s[i-1][-1]+1)
	s[i][0]=mini
	s[i].extend(p)
	#print "si"
	#print s[i][0]
	i+=1
print s[n][0]
print s[n][1:]