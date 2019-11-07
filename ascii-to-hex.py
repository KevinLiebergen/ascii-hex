#!/usr/bin/python3

#text = "<script>alert('1')</script>"
text = raw_input("Introduce codigo a ofuscar: ")

print(text)


splitted = list(text)
hexed = ""

for i in splitted:
    hexed += '%' + hex(ord(i))[2:]

print(hexed)

