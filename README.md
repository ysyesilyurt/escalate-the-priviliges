# escalate-the-privileges 😈
Is it possible to exploit a program running in the remote machine and escalate to root a shell?! 😈

Keywords: `privilege escalation`, `setuid`, `root access`, `stack-overflow` 

# How?
This is an example of famous privilege escalation attack using setuid exploit, `saldir.py` exploits a program running on a remote machine to gain a root access.

Program running on the remote machine is given as 'overwrite' and it is compiled with `gcc -m32 -o overwrite overwrite.c` which means it has all the default exploit protections such as stack canaries, non executable stack etc. Namely the attack we perform doesn’t try to change the return pointer. Instead this script exploits a "stack overflow" bug in 'overwrite' that eventually allows us to execute any command we wish (i.e. as root) since 'overwrite' program has its "setuid" bit set.

The source code of the program is also given as 'overwrite.c' but the exploit in the program can also be detected by the assembly code of 'overwrite' (i.e. using the output of "objdump -d overwrite" or with gdb)

#### To run and actually test in your local: ./saldir.py | overwrite
#### To hack and test in a remote machine that runs 'overwrite' (actual target): (./saldir.py; cat) | nc <IP_ADDR> <PORT>
