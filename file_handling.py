f = open("D:\\Practice\\file_handling\\rain_poem.txt", 'r')

#Read a .txt file
#print(f.read())

#Read a .txt line by line
for txt in f.readlines():
    print(txt,end='')

# Write a file
f_write = open("D:\\Practice\\file_handling\\new_hello1.txt", 'a')
f_write.write('Hello World, How are you?\n')

#Copy content of one file(f1) to another file(f2)
f1 = open("D:\\Practice\\file_handling\\rain_poem.txt", 'r')
f2 = open("D:\\Practice\\file_handling\\rain_poem_copy.txt",'a')

for txt in f1.readlines():
    f2.write(txt)


