#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

# A line of hyphens as long as the belgium string

print("-" * len(Belgium))

# Comma separators replaced by colon

Commabelgium = Belgium.replace(",",":")
print(Commabelgium)

# population of belgium plus the capital population

print("Population of Belgium:", Belgium[8:16], "Capital city:", Belgium[17:25], "Capital population:", Belgium[26:32])
print("Population of Belgium plus the Capital:", (int(Belgium[8:16])+int(Belgium[26:32])))
