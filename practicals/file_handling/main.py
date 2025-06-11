# Example 2: Reading from a File

with open("output.txt", "r") as file:
    content = file.read()
    print(content)
    
# Example 3: Appending to a File

with open("output.txt", "a") as file:
    file.write("\nThis line was added later.")

# Example 4: Reading Line by Line

with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())

# Example 5: Error Handling in File Access

try:
    with open("nonexistent.txt", "r") as file:
        data = file.read()
except FileNotFoundError:
    print("File not found. Please check the filename.")
