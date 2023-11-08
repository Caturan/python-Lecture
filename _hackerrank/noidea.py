
"""
There is an array of n integers. There are also 2 disjoint sets, A and B each containing m integers. 
You like all the integers in set A and dislike all the integers in set B. Your initial happiness is 0. 
For each i integer in the array, if i in A you add 1 to our happines. If i in B you -1 to your happiness. 
Otherwise, your happiness does not change. Output your final happiness at the end.  
"""

def get_array_input():
    input_str = input("Enter elements separated by spaces: ")
    input_list = input_str.split()

    array = [int(element) for element in input_list]
    return array 

if __name__ == "__main__":
    user_array = get_array_input()
    print("User input array:", user_array)

    myset1 = {1,3,5,7,9}
    myset2 = {2,4,6,8}

    total = 0
    for element in user_array:
        if element in myset1:
            total+=1
        else:
            pass
        if element in myset2:
            total-=1
        else:
            pass

    print(total)


"""
    Another Solution

# Read input
n, m = map(int, input().split())  # n: number of elements in the array, m: number of elements in sets A and B
arr = list(map(int, input().split()))  # The array of integers
set_A = set(map(int, input().split()))  # Elements in set A
set_B = set(map(int, input().split()))  # Elements in set B

# Initialize happiness
happiness = 0

# Calculate happiness
for num in arr:
    if num in set_A:
        happiness += 1
    if num in set_B:
        happiness -= 1

# Output the total happiness
print(happiness)

"""