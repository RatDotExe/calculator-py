import math

fn = raw_input("Whats the first number? ")
sn = raw_input("Whats the second number? ")
o = raw_input("Whats the operation? ")

fnum = int(fn)
snum = int(sn)

if o == "+":
	r = fnum + snum
if o == "-":
	r = fnum - snum
if o == "*":
	r = fnum * snum
if o == "/":
	r = fnum / snum
print r