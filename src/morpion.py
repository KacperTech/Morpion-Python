from random import randrange

board = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]
    ]

def display_board(board):
    print("+-------+-------+-------+")
    for ligne in board:
        print("|       |       |       |")
        print(f"|   {ligne[0]}   |   {ligne[1]}   |   {ligne[2]}   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")


def enter_move(board):
    while True : 
        try:
            case = int(input("Choisissez votre case : "))
        except ValueError :
            print("C'est votre tour, veuillez choisir une case entre 1 et 9 qui n'est pas occupée")
            continue
        
        if case > 9 or case < 1 :
            print("Veuillez choisir un nombre entre 1 et 9")
            continue
        
        case = case -1
        axeH = case // 3
        axeV = case % 3 
        
        if board[axeH][axeV] in ("O", "X"):
            print("La case est occupée, veuillez choisir une autre case ")
        else :
            board[axeH][axeV] = "O"
            break


def make_list_of_free_fields(board):
    cases_libres = []
    for l in range(3):
        for c in range(3):
            tlc = (l,c)
            if board[l][c] not in ("O" , "X"):
                cases_libres.append(tlc) 
            else :
                pass
                
    return cases_libres


def victory_for(board, sign):
    for l in range(3):
        if board[l][0] == board[l][1] == board[l][2] and board[l][0] == sign:
            return True
    for c in range(3) :
        if board[0][c] == board[1][c] == board[2][c] and board[0][c] == sign:
            return True
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] == sign:
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] == sign:
        return True
    else :
        return False


def draw_move(board):
    cases_libres = make_list_of_free_fields(board)
    
    i_random = randrange(0, len(cases_libres))
    tirage = cases_libres[i_random]
    l = tirage[0]
    c = tirage[1]
    board[l][c] = "X"

while True : 
    display_board(board)
    if make_list_of_free_fields(board) == []:
        print("C'est un match nul :O")
        break
    print("Tour de l'ordinateur")
    draw_move(board)
    display_board(board)
    if victory_for(board, "X"):
        display_board(board)
        print("Tu as perdu :( ")
        break
    if make_list_of_free_fields(board) == []:
        print("C'est un match nul :O")
        break
    enter_move(board)
    if victory_for(board, "O"):
        display_board(board)
        print("Tu as gagné :D ")
        break

input("Appuyez sur Entrée pour quitter...")
