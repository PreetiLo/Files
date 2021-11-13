# my_file=open('file.txt','w')
# my_file.write('sajan')
# my_file.write('\natram')
# my_file.close()


# my_file = open("people1-exercise.txt","r")
# file_data = my_file.readlines()
# count=0
# i=0
# while i <len(file_data):
#     count+=1
#     i+=1
# print(i)    
# my_file.close()

# my_file=open("question3.txt","w")
# banks_list=["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
# my_file=banks_list
# i=0
# while i<len(my_file):
#     print(my_file[i])
#     i+=1
# i=0
# # sum=0
# while i<11:
#     print(i)
#     if i==6:
#         break
#     # else:
#     #     print    
#     i+=1   


# def longest_word(filename):
#     with open(filename, 'r') as infile:
#               words = infile.read().split()
#     max_len = len(max(words, key=len))
#     return [word for word in words if len(word) == max_len]
# print(longest_word('test.txt'))


# def file_read(fname):
#         with open(fname, "w") as myfile:
#                 myfile.write("Python Exercises\n")
#                 myfile.write("Java Exercises")
#         txt = open(fname)
#         print(txt.read())
# file_read('abc.txt')

# def file_lengthy(fname):
#         with open(fname) as f:
#                 for i, l in enumerate(f):
#                         pass
#         return i + 1
# print("Number of lines in the file: ",file_lengthy("test.txt"))

# def line_count():
#     file = open("story.txt","r")
#     count=0
#     for line in file:
#         if line[0] not in 'total lines':
#             count+= 1
#     file.close()
#     print("No of lines not starting with 'total lines'=",count)

# line_count()

# fh=open("delhi.txt","r")
# count=0
# lines=fh.readlines()
# for a in lines:
#     count=count+1
#     print(count,a)
# fh.close()

# fh=open("shimla.txt","r")
# count=0
# lines=fh.readlines()
# for a in lines:
#     if (a.tolower().count("to") > 0) :
#           print(a)
# fh.close()

# fname = "shimla.txt"
# num_words = 0
# f= open(fname, 'r')
# words = f.read().split()
# for a in words:
#     if (a.tolower() == "to" or a.tolower() == "the" ):
#            num_words = num_words + 1
#     print("Number of words:", num_words)
# f.close()