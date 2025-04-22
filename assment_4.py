# task_1
try:
    file1 = open('sample.txt','r')
    reading_files = file1.read()
    print(reading_files)
    file1.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found")
finally:
    print(" ")
# task_2
file1 = open('output.txt','r+')
writing_files = file1.write(input(""))
file1.close()
file1 = open('output.txt','a')
appending_files = file1.write("Enter the text to write to the file:")
file1.close()
file1 = open('output.txt','r+')
rading_files = file1.read()
print(appending_files)
file1.close()