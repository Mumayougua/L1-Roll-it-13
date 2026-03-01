first = "apple"
second = "banana"
print(f"First: {first} | Second {second}")

first, second = second, first
print("I've switched things around...")
print(f"First:{first} | Second {second}")