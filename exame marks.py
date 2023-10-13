
# Open the file in write mode with a context manager
with open("marks.txt", "w") as file:
    while True:
        I = int(input("Enter the index number (enter 1 to exit): "))
        if I == -1:
            break
        
        x = input("Enter the first marks: ")
        y = input("Enter the second marks: ")
        z = input("Enter the third marks: ")
        
        data = str(I) + " " + x + "," + y + "," + z + "\n"
        file.write(data)

print("Data has been written to marks.txt")

# Close the file automatically using the context manager
