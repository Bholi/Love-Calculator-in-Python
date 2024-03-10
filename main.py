print('Welcome to Love Calculator ! Are you ready to calculate your love')
name = input('Enter your name : ')
lover = input('Enter your lover or crush name : ')

nt = name.lower().count('t')
lt = lover.lower().count('t')
t = nt + lt

nr = name.lower().count('r')
lr = lover.lower().count('r')
r = nr + lr

nu = name.lower().count('u')
lu = lover.lower().count('u')
u = nu + lu
ne = name.lower().count('e')
le = lover.lower().count('e')
e = ne + le
T = t + r + u + e

nl = name.lower().count('l')
ll = lover.lower().count('l')
L = nl + ll

no = name.lower().count('o')
lo = lover.lower().count('o')
o = no + lo

nv = name.lower().count('v')
lv = lover.lower().count('v')
v = nv + lv

nE = name.lower().count('e')
lE = lover.lower().count('e')
E = nE + lE

Love = L + o + v + E

print(f'Your score is {T}{Love}')
