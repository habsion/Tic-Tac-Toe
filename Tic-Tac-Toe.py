# tic-tac-toe
s=[[None,None,None],[None,None,None],[None,None,None]]
def who_win():
    for i in range(3):
        if s[i][0] is not None:
            t=s[i].count(s[i][0])
            if t==3:
                return s[i][0]
    for i in range(3):
        l=[s[j][i] for j in range(3)]
        if l[0] is not None:
            t=l.count(l[0])
            if t==3:
                return l[0]
    if s[0][0]==s[1][1]==s[2][2]:
        return s[0][0]
    if s[0][2]==s[1][1]==s[2][0]:
        return s[0][2]
    return 'Tie!!!!' if None not in s[0]+s[1]+s[2] else None
a=input('Enter player names\nPlayer 1: ')
b=input('Player 2: ')
d=[a,b]
while True:
    for i in range(2):
        while True:
            a,b=map(int,input(d[i]+' enter co-ord(x,y) sep with comma: ').split(','))
            a-=1;b-=1
            if s[a][b] is None:
                s[a][b]='X' if i%2==0 else 'O'
                break
            else:
                print("You can can't do it enter new co-ord again")
        print('-'*7)
        print('\n'.join(['|'+' '.join(t if t else '-' for t in i)+'|' for i in s]))
        print('-'*7)
        t=who_win()
        if t:
            if t=='Tie!!!!':
                print(t)
            else:
                print(d[0]+' wins!!!!!!' if t=='X' else d[1]+' wins!!!!!!')
            exit()