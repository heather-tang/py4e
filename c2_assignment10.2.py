'''
10.2 Write a program to read through the mbox-short.txt and 
figure out the distribution by hour of the day for each of the messages. 
You can pull the hour out from the 'From ' line by finding the time and 
then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008 
Once you have accumulated the counts for each hour, 
print out the counts, sorted by hour as shown below.
'''

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

temp = list()
d = dict()
h = None
for lin in handle:
    lin = lin.split()
    if len(lin) < 1 or lin[0] != "From":
        continue
    lin = lin[5]
    h = lin[:2]
    temp.append(h)

for hr in temp:
    d[hr] = d.get(hr, 0) + 1

# lst = list()
# for k, v in d.items():
#     newtup = (k, v)
#     lst.append(newtup)

lst = sorted([ (k,v) for k,v in d.items()])

# lst = sorted(lst)
for k,v in lst:
    print(k, v)
