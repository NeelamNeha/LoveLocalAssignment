'''This takes a string as an input'''
s=input("Enter a string:") 

'''The string is then split into words'''
m=s.split()  
if not m:
    print("0")
else:
    '''prints the length of the last word. m[-1] indicates the index of the last word '''
    print(len(m[-1])) 

