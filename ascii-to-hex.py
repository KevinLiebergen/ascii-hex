#!/usr/bin/python

#text = "<script>alert('1')</script>"
text = raw_input("Introduce codigo a ofuscar: ")

splitted = list(text)
hexed = ""
asciied = ""

for i in splitted:
    hexed += '%' + hex(ord(i))[2:]
    #hexed += '\ x' + hex(ord(i))[2:]
    asciied += '&#' + str(ord(i))

print "hexed: ", hexed
print "asciied: ", asciied
