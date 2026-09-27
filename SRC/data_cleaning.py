file_path = "Data/Raw/alice_in_wonderland.txt"

with open(file_path, "r", encoding="utf-8") as file:
     text = file.read()

print("File loaded successfully!")
print("Number of characters:", len(text))
print("\nFirst 500 characters:")
print(text[:500])

print("\nLast 500 characters:")
print(text[-500:])