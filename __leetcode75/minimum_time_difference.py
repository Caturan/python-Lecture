"""
Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.

Example 1:
Input: timePoints = ["23:59","00:00"]
Output: 1

Example 2:
Input: timePoints = ["00:00","23:59","00:00"]
Output: 0
"""

a = "23:59, 00:00"
b = "00:00,23:59,00:00"
x = "12:12,00:13"
li = []
i = 0 
while i < len(x):
    try:
        li.append(int(x[i]))
    
    except ValueError:
        pass
    i += 1

#print(li)

new_numbers = []

for i in range(0, len(li), 2):
    combined_number = int(f"{li[i]}{li[i+1]}")  # İki elemanı string olarak birleştirip integer'a çeviriyoruz
    new_numbers.append(combined_number)

#print(new_numbers)  

mini = []
i = 0

while i < len(new_numbers):
    if new_numbers[i] == 0:
        mini.append((new_numbers[i] + 24) * 60 + new_numbers[i+1])
    else:    
        mini.append(new_numbers[i] * 60 + new_numbers[i+1])
    
    i += 2

#print(mini)

mini.sort()  # Listeyi küçükten büyüğe sıralıyoruz

min_difference = float('inf')  # Başlangıçta min değeri çok büyük bir değerle başlatıyoruz

# Bitişik sayılar arasındaki farkları hesaplıyoruz
for i in range(len(mini) - 1):
    difference = mini[i+1] - mini[i]
    if difference < min_difference:
        min_difference = difference

if len(mini) > 1:
            wrap_around_difference = (24 * 60 + mini[0]) - mini[-1]
            if wrap_around_difference < min_difference:
                min_difference = wrap_around_difference

print(min_difference)



"""
 times = set()

        for timePoint in timePoints:
            time_val = 60 * int(timePoint[:2]) + int(timePoint[3:])
            if time_val in times:
                return 0
            times.add(time_val)
        
        times = list(times)
        times.sort()

        first = times[0]
        last = times[-1]

        min_diff = 1440 + first - last

        for i in range(len(times) - 1):
            curr_diff = times[i + 1] - times[i] 
            if min_diff > curr_diff:
                min_diff = curr_diff
"""
