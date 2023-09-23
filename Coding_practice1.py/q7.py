'''def Permutation(str1,str2):
    flag=False
    x=list(str1)
    y=list(str2)
    if(len(x)==len(y)):
        for i in x:
            if(i in y):
                flag=True
    if(flag==True):
        return "Permutation Exist"
    else:
        return "Permutation not Exist "
                
        
   
        
str1="Sim"
str2="Miss"
print(Permutation(str1,str2))'''
def Perm(x,y):
    if(len(x)!=len(y)):
        return False
    else:
        a=list(x)
        b=list(y)
        a.sort()
        b.sort()
        if(a==b):
            return True 
        else:
            return False
str1="sims"
str2="miss"
print(Perm(str1,str2))
#a little bit improvement is rquired 
#need to make each letter either in upper or lower case.
        