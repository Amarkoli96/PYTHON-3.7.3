board=['00','01','02','03','04','05','06','07','08']
game_start=''


def print_board():
    print("--------------")
    print(" {} | {} | {} ".format(board[0],board[1],board[2]))
    print("--------------")
    print(" {} | {} | {} ".format(board[3],board[4],board[5]))
    print("--------------")
    print(" {} | {} | {} ".format(board[6],board[7],board[8]))
    print("--------------")

def maping_to_keypad(pos):
    if pos=='7':
        pos='0'
    elif pos=='8':
        pos='1'
    elif pos=='9':
        pos='2'
    elif pos=='4':
        pos='3'
    elif pos==5:
        pos='4'
    elif pos=='6':
        pos='5'
    elif pos=='1':
        pos='6'
    elif pos=='2':
        pos='7'
    elif pos=='3':
        pos='8'
    

def insert_zero(pos):
    #pos=maping_to_keypad(pos)
    if board[pos]!='0' and board[pos]!='x':
        board[pos]='0'
                
def insert_x(pos):
    #pos=mapping_to_keypad(pos)
    if board[pos]!='0' and board[pos]!='x':
        board[pos]='x'
        
def check_winner():
    if board[0]==board[1]==board[2]=='0' or board[3]==board[4]==board[5]=='0' or board[6]==board[7]==board[8]=='0' or board[0]==board[3]==board[6]=='0' or board[1]==board[4]==board[7]=='0' or board[2]==board[3]==board[8]=='0' or board[0]==board[4]==board[8]=='0' or board[2]==board[4]==board[6]=='0':
        print('Player one wins')
        return 1
    elif board[0]==board[1]==board[2]=='x' or board[3]==board[4]==board[5]=='x' or board[6]==board[7]==board[8]=='x' or board[0]==board[3]==board[6]=='x' or board[1]==board[4]==board[7]=='x' or board[2]==board[3]==board[8]=='x' or board[0]==board[4]==board[8]=='x' or board[2]==board[4]==board[6]=='x':
        print('Player two wins')
        return 1
    elif (board[0]=='0' or board[0]=='x')and(board[1]=='0' or board[1]=='x')and(board[2]=='0' or board[2]=='x')and(board[3]=='0' or board[3]=='x')and(board[4]=='0' or board[4]=='x')and(board[5]=='0' or board[5]=='x')and(board[6]=='0' or board[6]=='x')and(board[7]=='0' or board[7]=='x')and(board[8]=='0' or board[8]=='x'):
        print('Match Draw')
        return 1
def main():
    print("Welcome to the game tic tac toe")
    print('')
    print("Tip:First move my Player One")
    print('')
    print("Player One as mark 0")
    print("Player Two as mark X")
    print_board()

    while(1):
        print("Player One enter the Position to Insert 0 ")
        pos=int(input())
        insert_zero(pos)
        print_board()
        if check_winner() == 1:
            print("Do you want to play again")
            print("Y/N")
            game_start=input()
            if game_start=='Y'or'y':
                global board
                board =['00','01','02','03','04','05','06','07','08']
                main()
            else:
                break
        print("Player Two enter the Position to Insert X ")
        pos=int(input())
        insert_x(pos)
        print_board()
        if check_winner() == 1:
            print("Do you want to play again")
            print("Y/N")
            game_start=input()
            if game_start=='Y'or'y':
                board=['0','01','02','03','04','05','06','07','08']
                main()
            else:
                break
    return 0

def replay():
    print("Do you want to play the game")
    print("Y/N")

print("Do you want to play the game")
print("Y/N")
game_start=input()
if game_start=='Y'or'y':
    main()

    
