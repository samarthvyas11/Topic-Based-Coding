remaing_test_cases = int(input())
while remaing_test_cases > 0:
    size_of_array = int(input())
    given_array = list(map(int,input().split()))
    
    for element in range(size_of_array//2):
        
        temp = given_array[element]
        given_array[element] = given_array[size_of_array-1-element]
        given_array[size_of_array-1-element] = temp
        
        
    print(*given_array) #reversed given array     
    remaing_test_cases = remaing_test_cases - 1 