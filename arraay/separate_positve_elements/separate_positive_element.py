remaing_test_cases = int(input())
while remaing_test_cases > 0:
    size_of_array = int(input())
    array = list(map(int,input().split()))
    for element in range(size_of_array):
        if array[element] < 0:
            negative_element = array.pop(element)
            array.insert(0,negative_element)
    print(*array)        #array with separeted positive and negative number
    remaing_test_cases = remaing_test_cases - 1 