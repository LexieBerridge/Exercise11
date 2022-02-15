#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

# A line of hyphens as long as the belgium string

print("-" * len(Belgium))

# Comma separators replaced by colon

Commabelgium = Belgium.replace(",",":")
print(Commabelgium)

# population of belgium plus the capital population


belgiumlist = Belgium.split(",")  #Alternative way of splitting list by :
Commalist = ":".join(belgiumlist)
print(Commalist)
print("Population of Belgium:", belgiumlist[1], "Capital city:", belgiumlist[2], "Capital population:", belgiumlist[3])
print("Population of Belgium plus the Capital:", (int(belgiumlist[1])+int(belgiumlist[3])))
