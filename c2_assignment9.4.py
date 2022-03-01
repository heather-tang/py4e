'''
9.4 Write a program to read through the mbox-short.txt and 
figure out who has sent the greatest number of mail messages. 
The program looks for 'From ' lines and 
takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address 
to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the dictionary 
using a maximum loop to find the most prolific committer.
'''

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()
lst = list()
for line in handle:
    line = line.split()
    if len(line) < 1 or line[0] != "From":
        continue
    lst.append(line[1])
for email in lst:
    counts[email] = counts.get(email, 0) + 1


bigemail = None
bigcount = None
for key,value in counts.items():
    if bigemail is None or value > bigcount:
        bigemail = key
        bigcount = value


print(bigemail, bigcount)
