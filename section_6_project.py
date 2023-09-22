n=int(input("how many day's temperature : "))
total=0
l=[]
count=0
for i in range(n):
    nxtdy = int(input("Day"+str(i+1)+" 's high temperature is : "))
    l.append(nxtdy)
    total=total+l[i]
avgtemp=round(total/n,2) 
print("\nAverage = "+str(avgtemp))

for i in range(len(l)):
    if(l[i]>avgtemp):
        count=count+1
print("Number of days when temperature is higher than avg temerature is : ",count)
#