def main():
    # Open a file for writing and create it if it doesn't exist
    f = open("textfile.txt", "r")

    # Use this with open in Write mode when creating file for first time
    """for i in range(10):
        f.write("This is line" + str(i) + "\r\n")

    f.close()"""

    # Open the file back up and read the contents
    if f.mode == 'r':
        contents = f.read()
        print(contents)

if __name__ == "__main__":
    main()