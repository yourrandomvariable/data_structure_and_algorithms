# Data Structure Question's and Answer
# Geeks for Geeks

# Sum of Series
def sum_of_series(arr):
    return arr * (arr + 1) // 2
print(sum_of_series(5))

# Sum of Elements in Array
def sum_of_all_elements(arr):
    sum_var = 0
    for i in arr:
        sum_var = sum_var + i
    return sum_var
print(sum_of_all_elements([1,2,3,4,5]))

# Find the number whether it is even or ordd
def even_odd(arr):
    even = []
    odd = []
    for elements in arr:
        if elements % 2 == 0:
            even.append(elements)
        else:
            odd.append(elements)
    return even,odd

print(even_odd([1,2,3,4,5]))



