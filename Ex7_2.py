B = '1101'
I = 0
while B:
    I = I * 2 + (ord(B[0]) - ord('0'))
    B = B[1:]

print(I)

S = 'spam'
S = S + 'SPAM!'
print(S)
S = S[:4] + 'Burger' + S[-1]
print(S)
S = 'splot'
S = S.replace('pl', 'pamal')
print(S)
