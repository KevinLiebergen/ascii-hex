#!/usr/bin/python3

text = "<script>alert(1)</script>"

splitted = list(text)
hexed = ""

for i in splitted:
    hexed += '%' + hex(ord(i))[2:]

print(hexed)
