remaing_test_cases = int(input())
while remaing_test_cases > 0:
    size_of_array = int(input())
    given_array = list(map(int,input().split()))
    array_count_0 = 0 
    array_count_1 = 0 
    array_count_2 = 0
     
    for element in range(size_of_array):
        if given_array[element] == 0:
            array_count_0 += 1
        if given_array[element] == 1:
            array_count_1 += 1
        if given_array[element] == 2:
            array_count_2 += 1    
       
        
    for element in range(array_count_0):    
         print(0,end=" ")
    for element in range(array_count_1):    
         print(1,end=" ")
    for element in range(array_count_2):    
         print(2,end=" ")         
         
    
    print()
    remaing_test_cases = remaing_test_cases - 1 