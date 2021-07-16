# tic-tac-toe
s=[[None,None,None],[None,None,None],[None,None,None]]                   # A 2d array to store the selection tiles of players (we initialize all tiles to None)


# a function which determines whether someone win or not after every move taken by players
def who_win():
    # checking the horizontal lines
    for i in range(3):
        if s[i][0] is not None:
            t=s[i].count(s[i][0])
            if t==3:
                return s[i][0]
            
    # checking the the vertical lines
    for i in range(3):
        l=[s[j][i] for j in range(3)]
        if l[0] is not None:
            t=l.count(l[0])
            if t==3:
                return l[0]
            
    # checking the diagonal lines
    if s[0][0]==s[1][1]==s[2][2]:
        return s[0][0]
    if s[0][2]==s[1][1]==s[2][0]:
        return s[0][2]
    
    # if no one wins then we decide whether it's a draw or returns None if there are still moves remain
    return 'Tie!!!!' if None not in s[0]+s[1]+s[2] else None


# driver code
a=input('Enter player names\nPlayer 1: ')
b=input('Player 2: ')
d=[a,b]                                                              # we put the players names in a list to loop through it so that each player gets a chance to make their move
while True:
    for i in range(2):
        while True:
            # we take inputs in 1-based index and substacts it with 1 to convert it to 0th based index
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
            exit()                                                   # In case of a player's win or draw we terminate the whole code using exit()
