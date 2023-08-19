# For questions: @author Sandro
# script to demonstrate python list access


# Initialize
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get single
element = numbers[3]
print("One element:", element)

# Get first 4 elements
first_elements = numbers[:4]
print("First 4 elements:", first_elements)

# Get last 4 elements
last_elements = numbers[-4:]
print("Last 4 elements:", last_elements)

# Modify an element
numbers[2] = 100
print("Modified list:", numbers)

# Append
numbers.append(11)
print("Appended list:", numbers)

# Insert at a specific position
numbers.insert(4, 99)
print("Inserted list:", numbers)

# Remove element
numbers.remove(8)
print("List after removal:", numbers)

# Check if an element exists in the list
if 7 in numbers:
    print("7 is in the list")
if numbers.count(6) > 0:
    print("6 is in the list")

# Find the index of an element
index = numbers.index(6)
print("Index of 6:", index)

# Sort
numbers.sort() # Ascending
numbers.sort(reverse=True) # Descending
print("Sorted list:", numbers)

# Sort strings by length
texts = ['1', '22', '333', '4444', '5555555']
texts.sort(key=len, reverse=True)
print("Sorted string list:", texts)

# Reverse the order
numbers.reverse()
print("Reversed list:", numbers)