def higher_freq(nums):
    '''Unique elements into the set'''
    unique_nums=set(nums)    
    elements=[]
    for num in unique_nums:
       '''Tf the count of the number is greater than n/3 the number goes into the elements''' 
       if nums.count(num)>len(nums)//3:
            elements.append(num)
    '''Printing the number with the frequency greater than n/3'''
    print("The majority elements are:", elements)


higher_freq([3,2,3])  
higher_freq([1]) 
higher_freq([1,2])  
