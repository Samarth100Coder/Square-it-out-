l=int(input('Enter lower range: '))
u=int(input('Enter upper range: '))
for c in range(l,u+1):
    a=c*c
    if a%2==0:
        print(a,'is even')
    else:
        print(a,'is odd')