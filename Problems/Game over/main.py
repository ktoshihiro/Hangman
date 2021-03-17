scores = input().split()
# put your python code here
score = 0
falt = 0

for i in scores:
    if i == 'C':
        score += 1
    elif i == 'I':
        falt += 1
        if falt == 3:
            print('Game over')
            print(score)
            break

if falt < 3:
    print('You won')
    print(score)
