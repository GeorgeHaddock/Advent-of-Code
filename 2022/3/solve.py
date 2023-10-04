#!/usr/bin/env python

import string

with open("3\\input.txt") as f:
    rucksacks = f.read().splitlines()
    
""" psuedo code:
for each rucksack:
    split rucksack into sections
    !new interpret sections as sets
    use comparing method to compare whats in sections
    extract the item the sections have in common - take the intersection of the sets
look up & sum common item weights from dict of item values

result: sum of priorities of common items

# Sets is a good variable type to use for this: Set are a list of unique items
"""
"""
def compartmentalise(rucksack):
    size = len(rucksack)
    comp_1 = rucksack[:size//2]
    comp_2 = rucksack[size//2:]
    return set(comp_1), set(comp_2)
"""
def elf_group(rucksacks):
    groups = ((set(rucksacks[i]),set(rucksacks[i+1]),set(rucksacks[i+2])) for i in range(0,len(rucksacks), 3)) #Generator uses '()'
    return groups

#This is a time when using a Generator would be good, as it only needs to work in a for loop

item_priorities = {letter:i+1 for i,letter in enumerate(string.ascii_lowercase+string.ascii_uppercase)} #Define using dict comprehension? yep!
priorities_sum = 0
for elf_group in elf_group(rucksacks):
    elf_1,elf_2,elf_3 = elf_group
    badge_item = (elf_1 & elf_2 & elf_3).pop() #& is shorthand for intersection
    priorities_sum += item_priorities[badge_item]
    #print(badge_item,item_priorities[badge_item])

print(priorities_sum)