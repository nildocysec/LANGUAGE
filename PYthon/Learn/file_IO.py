# Module
import os


# Open defualt mode is read
f = open("file1.txt")
f.close()

#Open read mode
f = open("file1.txt","r")

#Read
data = f.read()
print(data)
f.close()

'''
r = read mode
w = write mode
a = append mode
x = create new and open for write mode
'''

# Read first 3 characters
f = open("file1.txt","r")
data = f.read(3)
print(data)
data = f.read(2)
print(data)
f.close()

# Read a line at a time
f = open("file1.txt","r")
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
f.close()


# Open in write mode
f= open("file1.txt","w")
f.write("Writing this new liner @ 11\nBye")
f.close()

# Open in append mode
f =open("file1.txt","a")
f.write("\nSecond line")
f.close()

# with syntax
with open("file1.txt","r") as f:
    data = f.read()
    print(data)

# Create new file
f= open("newfile.txt","w")
f.close()

# Delete file
os.remove("newfile.txt")


with open("newfile.txt","w") as f:
    
    f.write("Hi everyone\nwe are learning file IO\nusing java\nI hate coding in java")

with open("newfile.txt","r") as f:

    data = f.read()
    new_data = data.replace("java","python")
    print(new_data)

    if(data.find("python") != -1):
        print("FOUND")
    else:
        print("NOT FOUND")

with open("newfile.txt","w") as f:

    f.write(new_data)

def fun_check_line_word():
    
    word = "hate"
    data = True
    line_no = 1
    with open("newfile.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print("Found ")
                print(line_no)
            line_no +=1
    return -1

fun_check_line_word()

with open("newfile.txt","r") as f:
    data = f.read()
    print(data)

    num =""
    for i in range(len(data)):
        if(data[i] == ","):
            print(int(num))
            num=""
        else:
            num = data[i] + num







