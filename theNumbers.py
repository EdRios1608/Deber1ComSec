from string import ascii_uppercase as uppercase 

numbers = [ 16, 9, 3, 15, 3, 20, 6, '{', 20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14, '}']
flag_answer = []

for n in numbers:
    if type(n) == str:
        flag_answer.append(n)
    else:
        flag_answer.append(uppercase[n-1])
print(''.join(flag_answer))