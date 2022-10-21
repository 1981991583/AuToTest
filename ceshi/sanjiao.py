n=int(input('please input the number:'))
k=int(n//2)
for i in range(1,k+1):
    s1='&'*(k+1-i)+'*'*(i*2-1)
    print(s1)


