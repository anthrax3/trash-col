num1,num2=map(int,raw_input().split())
fact1=fact2=1
i=1
while i<=num1:
	fact1*=i
	i+=1
i=1
while i<=num2:
	fact2*=i
	i+=1
print fact1,fact2
