# Number Analysis System
numbers = []
# Input 10 integers
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
    
# Calculate sum
total = sum(numbers)

# Find maximum and minimum
maximum = max(numbers)
minimum = min(numbers)

# Count even numbers
even_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1

# Output results
print("\nNumbers:", numbers)
print("Sum:", total)
print("Maximum:", maximum)
print("Minimum:", minimum)
print("Even Count:", even_count)