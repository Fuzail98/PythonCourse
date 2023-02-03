#ASSIGNMENT 1
"""
with open ('abc1.txt', 'r') as f:
    r = f.read().splitlines()
    print(f'r is \n{r}')
"""

#ASSIGNMENT 2
#Create a Python function called tail that reads the last n lines of a text file.
#The function has two arguments: the file name and n (the number of lines to read).
# This is similar to the Linux `tail` command.
#Example: tail('sample_file.txt', 5) will return the last 5 lines from sample_file.txt.
"""
def tail(f_name, n):
    with open(f_name, 'r') as f:
        read = f.read().splitlines()
        for sentences in read[-n:]:
            print(sentences)
tail('abc1.txt', 2)
"""

#ASSIGNMENT 4
#Write a Python program to count the number of lines, words and characters in a text file.
#This is similar to the Linux `wc` command. Create a function if possible.
"""
def n_line(f_name):
    with open (f_name, 'r') as f:
        read = f.read()
        print(f'No. of lines in the file {f_name} = {len(read.splitlines())}')
def n_word(f_name):
    with open (f_name, 'r') as f:
        read = f.read()
        y = 0
        for words in read.splitlines():
            y += len(words.split(':'))
        print(f'No. of words in the file {f_name} = {y}')

def n_char(f_name):
    with open(f_name, 'r') as f:
        read = f.read()
        z = 0
        for word in read.splitlines():
            for char in word.split():
                z += len(char)
        print(f'No. of characters in the file {f_name} = {z} (excluding white spaces)')
#n_line('abc1.txt')
#n_word('abc1.txt')
n_char('xyza.txt')
"""

#ASSIGNMENT 5
#Write a Python program that calculates the net amount of a bank account based on the transactions saved in a
# text file. The file format is as following:
#D:50
#W:100
#D means deposit while W means withdrawal.
"""
with open('Account.txt', 'r') as f:
    read = f.read()
    d, w = 0, 0
    for item in read.splitlines():
        tmp = item.split(':')
        if tmp[0] == 'D':
            d += int(tmp[1])
        elif tmp[0] == 'W':
            w += int(tmp[1])
        else:
            d, w = 0, 0
            break
    if d == 0 & w == 0:#Need to change this condition or edit the above for block of code.
        print('File format error')
    else:
        b = d - w
        print(f'Your balance is {b}.')
"""

#ASSIGNMENT 6
#Write a Python script that compares two text files line by line and display the lines that differ.
"""
with open('xyza.txt', 'r') as f:
    reada = f.read()

with open('xyzb.txt', 'r') as f:
    readb = f.read()

print(readb.splitlines())
print(reada.splitlines())
x = 0
for senta in reada.splitlines():
    for sentb in readb.splitlines():

        if senta[x] != sentb[x]:
            print(f'{senta} : {sentb} Not Same sentence')
            #print(f'{senta}\n{sentb}')
            #print(f'The following are different lines in the two files: {senta}\n')
        else:
            #pass
            print(f'{senta} : {sentb}  same')

'My name is Fuzail.' == 'My name is Masood.'
"""
#ASSIGNMENT 7
#Write a Python script that reads the file in a dictionary.
# The words in the file will be the dictionary keys and the length of each word the corresponding values.
"""
with open('xyza.txt') as f:
    words = f.read().split()
#print(words)
words_and_length = dict()
for w in words:
    words_and_length[w] = len(w)
print(words_and_length)
for k, v in words_and_length.items():
    print(f'{k} -> {v}')


#ASSIGNMENT 8
#Consider the dictionary file from the previous challenge.
#Write a Python script that finds the first 100 longest words in the file.

view = sorted(words_and_length.items(), key = lambda x: x[1], reverse = True)
#The above instruction will sort the dictionary based on keys.

print('The following are the 5 longest words in the file:')
print(view[:5])
"""

#ASSIGNMENT 9
#Write a Python script that finds the number of occurrences of each letter of the alphabet in all the
# words in the dictionary. You want to see how many times do ‘a’, ‘b’, ‘c’ and so on appear in all the
# words in the dictionary. Which is the most frequently used letter in English words?
"""
with open('xyza.txt') as f:
    words = f.read().split()
    letters_freq = {}
    for word in words:
        for letter in word:
            letter = letter.lower()
            if letter in letters_freq:
                letters_freq[letter] += 1
            else:
                letters_freq[letter] = 1
l = dict(sorted(letters_freq.items(), key = lambda x:x[1], reverse = True))
print(l)
print(list(l.items())[0])
#for most repeated letter


#ASSIGNMENT 10
#Continue the previous challenge and find the 3 most frequently used letters in all English Words.
print(list(l.items())[0:3])
"""

#ASSIGNMENT 11

#Consider the following Python list: Using the CSV module write each element of the list
# (which is another list) into a CSV file called people1.csv
import csv
people = [['Dan', 34, 'Bucharest'], ['Andrei',21, 'London'], ['Maria', 45, 'Paris']]

with open('people1.csv', 'w') as f:
    csv.register_dialect('colon', delimiter = ':')
    writer = csv.writer(f, dialect='colon')
    writer.writerow(['Name', 'Age', 'Place'])
    for list in people:
        print(list)
        writer.writerow(list)
        #for item in list:
            #print(list)
            #writer.writerow(list)
