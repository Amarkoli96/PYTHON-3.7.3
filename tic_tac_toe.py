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

def insert_zero(pos):
    if board[pos]!='0' and board[pos]!='x':
        board[pos]='0'
                
def insert_x(pos):
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
    print("welcome to the game tic tac toe")
    print("select your mark 0 or X")
    print("Tip:Always select 0 as player one choice")
    print("Player One Choice")
    player_one_choice = input()
    print("Player Two Choice ")
    player_two_choice = input()

    while(1):
        print("Enter the position to place {} in the board".format(player_one_choice))
        print_board()
        pos=int(input())
        insert_zero(pos)
        if check_winner() == 1:
            print("Do you want to play again")
            print("Y/N")
            game_start=input()
            if game_start=='Y'or'y':
                global board
                board = ['00','01','02','03','04','05','06','07','08']
                main()
            else:
                break
        print("Enter the position to place {} in the board".format(player_two_choice))
        print_board()
        pos=int(input())
        insert_x(pos)
        print_board()
        if check_winner() == 1:
            print("Do you want to play again")
            print("Y/N")
            game_start=input()
            if game_start=='Y'or'y':
                board=['00','01','02','03','04','05','06','07','08']
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

    
