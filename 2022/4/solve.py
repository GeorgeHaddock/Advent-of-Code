#!/usr/bin/env python
"""
--------------------- TITLE ------------------------
Advent of Code 2022 
---- Day 4: Camp Clean-up ----
----------------------------------------------------

------- Author(s) --------
George Haddock - UID: 10278321 - george.haddock@student.manchester.ac.uk

---- File Description ----


----------------------------------------------------
Created:    28/09/23
Last Saved: 

"""
with open("4\\input.txt") as f:
    pairs = f.read().splitlines()
    
""" psuedo code:
for each pair:
    read-in upper & lower limit of each elf
    if one elf's upper limit is higher & lower limit lower than the other
        overlap! overlap count+1

"""
overlaps = 0
for pair in pairs:
    elf_0, elf_1 = pair.split(',')
    elf_0_lower, elf_0_upper = elf_0.split('-')
    elf_1_lower, elf_1_upper = elf_1.split('-')
    elf_0_lower, elf_1_lower, elf_0_upper, elf_1_upper = int(elf_0_lower), int(elf_1_lower), int(elf_0_upper), int(elf_1_upper)
    if (((elf_0_lower <= elf_1_lower) and (elf_0_upper >= elf_1_upper)) or
        ((elf_1_lower <= elf_0_lower) and (elf_1_upper >= elf_0_upper)) or
        ((elf_0_upper >= elf_1_lower) and (elf_0_lower <= elf_1_upper)) or
        ((elf_1_upper >= elf_0_lower) and (elf_1_lower <= elf_0_upper))):
        overlaps += 1
        #print(elf_0_lower, elf_0_upper, elf_1_lower, elf_1_upper)

print(overlaps)
