seg,p=map(int,raw_input().split())
s=[[0 for i in range(2)] for j in range(seg*2) ]
i=0
while(i<seg*2):
	s[i][0],s[i+1][0]=map(int,raw_input().split())
	s[i][1]='l';s[i+1][1]='r'
	i+=2
s=sorted(s)
print s
i=0
point = map(int,raw_input().split())
print point
while(i<p):
	print "i"
	print i
	j=0
	count=0
	while(j<seg*2-1):
		print "j"
		print j
		if( s[j][0]<=point[i]<=s[j+1][0] ):
			print "if-1"
			if( s[j][1]=='l' and s[j+1][1]=='r' ):
				print "if-2"
				count+=1
			if( s[j][1]=='l' and s[j+1][1]=='l' ):
				print "if-3"
				count+=1
			if(s[j][1]=='r' and s[j+1][1]=='r'):
				print "if-4"
				count+=1
			if(s[j][1]=='r' and s[j+1][1]=='l'):
				print "if-5"
				count+=0
		j+=1
	print count
	i+=1
