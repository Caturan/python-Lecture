"""
If we want to add a single element an existing set, we can use the .add() operation. 
It add the element to the set and return 'None' 

Task:
Apply your knowledge of the .add() operation to help your friend Rupal. 
Rupal has a huge collection of country stamps. She decided to count the total number of discint country stamps in her collection. 
She asked for your help. Ypu pick the stamps one by one from a stack of N country stamps. 
Find the total number of discint country stamps. 

Input Format: 
The first line contains an integer N, the total number of country stamps. 
The next N lines contains the name of the country where the stamp is from. 

Constraints:
0<N<1000
"""

#print(dir(set))
"""
country_set = {7, "UK", "China", "USA", "France", "New Zealand", "UK", "France"}
country_list = list(country_set)

#print(country_list)

#print(country_list.count(country_list))

c = country_list

i = 0
total = 0
for c[i] in c:
    total+=1

print(total-1)
"""


# Read the total number of country stamps (N)
N = int(input())

# Initialize an empty set to store distinct country stamps
distinct_stamps = set()

# Iterate through the N country stamps
for _ in range(N):
    stamp = input()
    distinct_stamps.add(stamp)  # Add each stamp to the set

# Calculate the total number of distinct country stamps
total_distinct_stamps = len(distinct_stamps)

# Print the result
print(total_distinct_stamps)
