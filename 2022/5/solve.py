#!/usr/bin/env python
"""
--------------------- TITLE ------------------------
Advent of Code 2022 
---- Day 5: Supply Stacks ----
----------------------------------------------------

------- Author(s) --------
George Haddock - UID: 10278321 - george.haddock@student.manchester.ac.uk

---- File Description ----


----------------------------------------------------
Created:    28/09/23
Last Saved: 

"""
with open("2022\\5\\test_input.txt") as f:
    lines = f.read().splitlines()
""" psuedo code:
Reading in input:
crates --- labels --- instructions
format: crates lines contain [],
 labels after crates & only numbers (only need last label)
 instructions begin with 'move'

Store current set-up of crates as list-per-stack? Loop through line from botton up?
Flip crate stacks so entry 0 is ground entry, 1 is 1st stacked crate etc
Read through instructions line by line
move each crate from instructions one at a time (for loop?)
define move_crate function
move all crates as per instructions

"""
break_line_no = int(lines.index(''))
    
instructions = [line for n,line in enumerate(lines) if n > break_line_no]
crates_diagram = [line for n,line in enumerate(lines) if n < break_line_no-1]
labels = lines[break_line_no-1].split()
print(crates_diagram)
print(labels)
print(instructions)

#crates = [[crate for crate in crates_diagram[]] for n in range(len(labels))]



#print(answer)
