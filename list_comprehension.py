limit = int(input("Enter a number: "))


odd_numbers = [n for n in range(limit) if n % 2 != 0]

print(f"Odd numbers under {limit}: {odd_numbers}")


fruits = ["apple", "banana", "orange", "mango"]


updated_fruits = [fruit.capitalize() for fruit in fruits]

print(f"Old list: {fruits}")
print(f"Updated list: {updated_fruits}")