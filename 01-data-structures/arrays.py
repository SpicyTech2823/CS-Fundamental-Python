numbers = [10, 20, 30, 40, 50]
print('Original array:', numbers)

# Accessing elements
print('First element:', numbers[0])
print('Third element:', numbers[2])

# update elements
numbers[1] = 25
print('Updated array:', numbers)
# Adding elements
numbers.append(60)
print('Array after appending 60:', numbers)
#removing elements
numbers.remove(30)
print('Array after removing 30:', numbers)
#looping through the array
for num in numbers:
    print('Element:', num)