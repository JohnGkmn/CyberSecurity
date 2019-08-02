#!/usr/bin/env python

from pwn import *
import binascii


MMI = lambda A, n,s=1,t=0,N=0: (n < 2 and t%N or MMI(n, A%n, t, s-A//n*t, N or n),-1)[n<1]

r = remote('2018shell1.picoctf.com', 50652)

# Question 1
lines = r.recvuntil('IS THIS POSSIBLE and FEASIBLE? (Y/N):')
print lines

q = int([l for l in lines.split('\n') if 'q :' in l][0].split(':')[1].strip(), 10)
p = int([l for l in lines.split('\n') if 'p :' in l][0].split(':')[1].strip(), 10)

r.sendline('Y')
print r.recvuntil('n:')

ans = q * p
print 'Sending: {}'.format(ans)
r.sendline('{}'.format(ans))

# Question 2
lines = r.recvuntil('IS THIS POSSIBLE and FEASIBLE? (Y/N):')
print lines

p = int([l for l in lines.split('\n') if 'p :' in l][0].split(':')[1].strip(), 10)
n = int([l for l in lines.split('\n') if 'n :' in l][0].split(':')[1].strip(), 10)

r.sendline('Y')
print r.recvuntil('q:')

ans = n / p
print 'Sending: {}'.format(ans)
r.sendline('{}'.format(ans))

# Question 3
lines = r.recvuntil('IS THIS POSSIBLE and FEASIBLE? (Y/N):')
print lines

r.sendline('N')

# Question 4
lines = r.recvuntil('IS THIS POSSIBLE and FEASIBLE? (Y/N):')
print lines

q = int([l for l in lines.split('\n') if 'q :' in l][0].split(':')[1].strip(), 10)
p = int([l for l in lines.split('\n') if 'p :' in l][0].split(':')[1].strip(), 10)

r.sendline('Y')
print r.recvuntil('totient(n):')

ans = (q - 1) * (p - 1)
print 'Sending: {}'.format(ans)
r.sendline('{}'.format(ans))

# Question 5
lines = r.recvuntil('IS THIS POSSIBLE and FEASIBLE? (Y/N):')
print lines

plain = int([l for l in lines.split('\n') if 'plaintext :' in l][0].split(':')[1].strip(), 10)
e = int([l for l in lines.split('\n') if 'e :' in l][0].split(':')[1].strip(), 10)
n = int([l for l in lines.split('\n') if 'n :' in l][0].split(':')[1].strip(), 10)

r.sendline('Y')
print r.recvuntil('ciphertext:')

ans = pow(plain, e, n)
print 'Sending: {}'.format(ans)
r.sendline('{}'.format(ans))

# Question 6
lines = r.recvuntil('IS THIS POSSIBLE and FEASIBLE? (Y/N):')
print lines

r.sendline('N')

# Question 7
lines = r.recvuntil('IS THIS POSSIBLE and FEASIBLE? (Y/N):')
print lines

q = int([l for l in lines.split('\n') if 'q :' in l][0].split(':')[1].strip(), 10)
p = int([l for l in lines.split('\n') if 'p :' in l][0].split(':')[1].strip(), 10)
e = int([l for l in lines.split('\n') if 'e :' in l][0].split(':')[1].strip(), 10)

r.sendline('Y')
print r.recvuntil('d:')

ans = MMI(e, (q - 1) * (p - 1))
print 'Sending: {}'.format(ans)
r.sendline('{}'.format(ans))

# Question 8
lines = r.recvuntil('IS THIS POSSIBLE and FEASIBLE? (Y/N):')
print lines

p = int([l for l in lines.split('\n') if 'p :' in l][0].split(':')[1].strip(), 10)
cipher = int([l for l in lines.split('\n') if 'ciphertext :' in l][0].split(':')[1].strip(), 10)
e = int([l for l in lines.split('\n') if 'e :' in l][0].split(':')[1].strip(), 10)
n = int([l for l in lines.split('\n') if 'n :' in l][0].split(':')[1].strip(), 10)

r.sendline('Y')
print r.recvuntil('plaintext:')

q = n / p
d = MMI(e, (q - 1) * (p - 1))
ans = pow(cipher, d, n)
print 'Sending: {}'.format(ans)
r.sendline('{}'.format(ans))

lines = r.recvall()
print lines

print 'In hex: {}'.format(hex(ans))
print binascii.unhexlify(hex(ans)[2:]) # python 2
