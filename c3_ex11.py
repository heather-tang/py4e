import re

tot = 0

han = open('regex_sum_1392608.txt')
for lin in han:
    n = re.findall('[0-9]+', lin)
    for i in n:
        tot = tot + float(i)

print(int(tot))

# most compact code following lead in optional section
import re
print( sum( [ int(i) for i in re.findall('[0-9]+', open('regex_sum_1392608.txt').read()) ] ) )
