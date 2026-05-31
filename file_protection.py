import base64

print("1. Protect File")
print("2. Restore File")

choice = input("Enter choice (1/2): ")

if choice == "1":
    text = input("Enter file content: ")

    encoded = base64.b64encode(text.encode()).decode()

    with open("protected_file.txt", "w") as file:
        file.write(encoded)

    print("File Protected Successfully!")
    print("Protected Data:", encoded)

elif choice == "2":
    with open("protected_file.txt", "r") as file:
        encoded = file.read()

    decoded = base64.b64decode(encoded).decode()

    print("Restored Content:")
    print(decoded)

else:
    print("Invalid Choice")
