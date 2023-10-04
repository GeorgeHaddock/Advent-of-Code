#!/usr/bin/env python

with open("1\input.txt") as f:
    elf_snacks = [[int(snack) for snack in elf.splitlines()] for elf in f.read().split('\n\n')]
    

elf_total = [sum(elf) for elf in elf_snacks]
elf_total.sort(reverse=True)
print(elf_total[0])

print(sum(elf_total[:3])) #'0' not needed in range
