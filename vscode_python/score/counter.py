ls=[5.8,6.21,5.7,6.34,6.44,5.96,6.75,7.08,7.1,7.12,7.2,7.06,7.16,6.08,6.11,7.02,6.85,5.95,6.89,6.536,7.22,6.928,5.95,6.376,6.38,6.822]
print(len(ls))
max=0
rate=0
for i in range(0,len(ls)):
    if(ls[i]>=max):
        max=ls[i]
print(max)
rate=10/max
print(rate)
for i in range(0,len(ls)):
    ls[i]=round(ls[i]*rate,1)
for i in range(0,len(ls)):
    print("data"+str(i+1)+" is: "+str(ls[i]))