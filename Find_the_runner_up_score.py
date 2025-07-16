n = int(input("Enter the number 2"))
arr = list(map(int, input().split()))  # Convert to list
    
    # Remove duplicates and sort
unique_arr = list(set(arr))
unique_arr.sort()
    
    # Get second largest (second from the end)
second_largest = unique_arr[-2]
print(second_largest)