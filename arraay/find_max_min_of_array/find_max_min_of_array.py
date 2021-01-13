remaing_test_cases = int(input())
while remaing_test_cases > 0:
    size_of_array = int(input())
    given_array = list(map(int,input().split()))
    max_element = given_array[0]
    min_element = given_array[0]
    
    
    for element in range(size_of_array):
        if given_array[element] > max_element:
            max_element = given_array[element]
        if given_array[element] < min_element:
            min_element = given_array[element]
            
        
        
    print("max = "+str(max_element))
    print("min = "+str(min_element))   
    
    
    remaing_test_cases = remaing_test_cases - 1 