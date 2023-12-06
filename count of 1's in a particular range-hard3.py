'''Give a number as input which is greater than 0'''
n=input("Enter a number greater than 0:") 

'''count is intialised to 0'''
c = 0 

'''Typecasting the string to int'''
m=int(n) 

for i in range(1, m+1): 
    '''Converting each iteration to string'''
    strtonum = str(i) 
    
    '''Counting the number of 1's from 1 to n'''
    c=c+strtonum.count('1') 
print(c)
