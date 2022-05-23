import random
import pygame
import numpy as np
import sys
import math
# import time
pygame.init()

WIDTH, HEIGHT = 700, 700

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

ROW_COUNT = 6
COLUMN_COUNT = 7

PLAYER = 0
AI = 1
PLAYER2 = -1
EMPTY = 0
PLAYER_PIECE = 1
AI_PIECE = 2

WINDOW_LENGTH = 4


def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid(board, col):
    return board[ROW_COUNT-1][col] == 0


def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r


def print_board(board):
    print(np.flip(board, 0))


def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            coun = 0
            for i in range(4):
                if board[r][c+i] == piece:
                    coun += 1
            if coun == 4:
                return True

    # Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            coun = 0
            for i in range(4):
                if board[r+i][c] == piece:
                    coun += 1
            if coun == 4:
                return True

    # Check positively sloped diaganols
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            coun = 0
            for i in range(4):
                if board[r+i][c+i] == piece:
                    coun += 1
            if coun == 4:
                return True

    # Check negatively sloped diaganols
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            coun = 0
            for i in range(4):
                if board[r-i][c+i] == piece:
                    coun += 1
            if coun == 4:
                return True


def evaluate_window(win, piece):
    score = 0
    opp_piece = PLAYER_PIECE
    if piece == PLAYER_PIECE:
        opp_piece = AI_PIECE

    if win.count(piece) == 4:
        score += 100
    elif win.count(piece) == 3 and win.count(EMPTY) == 1:
        score += 5
    elif win.count(piece) == 2 and win.count(EMPTY) == 2:
        score += 2

    if win.count(opp_piece) == 3 and win.count(EMPTY) == 1:
        score -= 4

    return score


def score_position(board, piece):
    score = 0
    # Score center column
    center_array = [int(i) for i in list(board[:, COLUMN_COUNT//2])]
    center_count = center_array.count(piece)
    score += center_count * 3

    # Score Horizontal
    for r in range(ROW_COUNT):
        row_array = [int(i) for i in list(board[r, :])]
        for c in range(COLUMN_COUNT-3):
            window = row_array[c:c+WINDOW_LENGTH]
            score += evaluate_window(window, piece)

    # Score Vertical
    for c in range(COLUMN_COUNT):
        col_array = [int(i) for i in list(board[:, c])]
        for r in range(ROW_COUNT-3):
            window = col_array[r:r+WINDOW_LENGTH]
            score += evaluate_window(window, piece)

    # Score posiive sloped diagonal
    for r in range(ROW_COUNT-3):
        for c in range(COLUMN_COUNT-3):
            window = [board[r+i][c+i] for i in range(WINDOW_LENGTH)]
            score += evaluate_window(window, piece)

    for r in range(ROW_COUNT-3):
        for c in range(COLUMN_COUNT-3):
            window = [board[r+3-i][c+i] for i in range(WINDOW_LENGTH)]
            score += evaluate_window(window, piece)

    return score


def is_terminal_node(board):
    a = winning_move(board, PLAYER_PIECE)
    b = winning_move(board, AI_PIECE)
    c = len(get_valid_locations(board)) == 0
    return a or b or c


def minimax(board, depth, alpha, beta, maximizingPlayer):
    valid_locations = get_valid_locations(board)
    is_terminal = is_terminal_node(board)
    if depth == 0 or is_terminal:
        if is_terminal:
            if winning_move(board, AI_PIECE):
                return (None, 100000000000000)
            elif winning_move(board, PLAYER_PIECE):
                return (None, -10000000000000)
            else:  # Game is over, no more valid moves
                return (None, 0)
        else:  # Depth is zero
            return (None, score_position(board, AI_PIECE))
    if maximizingPlayer:
        value = -math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = board.copy()
            drop_piece(b_copy, row, col, AI_PIECE)
            new_score = minimax(b_copy, depth-1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value

    else:  # Minimizing player
        value = math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = board.copy()
            drop_piece(b_copy, row, col, PLAYER_PIECE)
            new_score = minimax(b_copy, depth-1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value


def get_valid_locations(board):
    valid_locations = []
    for col in range(COLUMN_COUNT):
        if is_valid(board, col):
            valid_locations.append(col)
    return valid_locations


def pick_best_move(board, piece):
    valid_locations = get_valid_locations(board)
    best_score = -10000
    best_col = random.choice(valid_locations)
    for col in valid_locations:
        row = get_next_open_row(board, col)
        temp_board = board.copy()
        drop_piece(temp_board, row, col, piece)
        score = score_position(temp_board, piece)
        if score > best_score:
            best_score = score
            best_col = col
    return best_col


def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            k = r*square_size+square_size
            m = square_size
            s = int(r*m+3*m/2)
            pygame.draw.rect(screen, BLUE, (c*m, k, m, m))
            pygame.draw.circle(screen, BLACK, (int(c*m+m/2), s), RADIUS)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            k = int(c*square_size+square_size/2)
            m = int(r*square_size+square_size/2)
            if board[r][c] == PLAYER_PIECE:
                pygame.draw.circle(screen, RED, (k, HEIGHT-m), RADIUS)
            elif board[r][c] == AI_PIECE:
                pygame.draw.circle(screen, YELLOW, (k, HEIGHT-m), RADIUS)
    pygame.display.update()


def select_opp(win, font):
    pvp = font.render('Player vs Player', 1, WHITE)
    pve = font.render('Player vs AI', 1, WHITE)
    x = WIDTH//6
    y = 4*HEIGHT//9
    pygame.draw.rect(win, RED, (WIDTH//9, HEIGHT//3, HEIGHT//3, HEIGHT//3))
    pygame.draw.rect(win, RED, (5*WIDTH//9, HEIGHT//3, HEIGHT//3, HEIGHT//3))
    win.blit(pvp, (x, y))
    win.blit(pve, (4*x, y))
    pygame.display.update()


board = create_board()
myfont = pygame.font.SysFont("comicsans", 75)
selfont = pygame.font.SysFont("comicsans", 35)
game = False
turn = 0
square_size = WIDTH//COLUMN_COUNT

RADIUS = int(square_size/2 - 5)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

screen.fill(BLACK)
select_opp(screen, selfont)

P2 = 1
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()

    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = pygame.mouse.get_pos()
        k = WIDTH//9
        m = HEIGHT//3
        if k <= x <= 4*k and m <= y <= 2*m:
            P2 = PLAYER2
            break
        elif 5*k <= x <= 8*k and m <= y <= 2*m:
            P2 = AI
            break
        else:
            continue


# time.sleep(10)
draw_board(board)
pygame.display.update()
turn = random.randint(PLAYER, P2)

while not game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, square_size))
            posx = event.pos[0]
            if P2 == AI:
                if turn == PLAYER:
                    pygame.draw.circle(screen, RED,
                                       (posx, int(square_size/2)), RADIUS)
            else:
                if turn == PLAYER:
                    pygame.draw.circle(screen, RED,
                                       (posx, int(square_size/2)), RADIUS)
                else:
                    pygame.draw.circle(screen, YELLOW,
                                       (posx, int(square_size/2)), RADIUS)

        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, square_size))
            # Ask for Player 1 Input
            if turn == PLAYER:
                posx = event.pos[0]
                col = int(math.floor(posx/square_size))
                if is_valid(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, PLAYER_PIECE)

                    if winning_move(board, PLAYER_PIECE):
                        label = myfont.render("Player 1 wins!!", 1, RED)
                        screen.blit(label, (40, 10))
                        game = True

                    turn += 1
                    turn = turn % 2

                    # print_board(board)
                    draw_board(board)

    # Ask for Player 2 Input
    if turn == AI and not game:
        col, minimax_score = minimax(board, 5, -math.inf, math.inf, True)

        if is_valid(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, AI_PIECE)

            if winning_move(board, AI_PIECE):
                label = myfont.render("Player 2 wins!!", 1, YELLOW)
                screen.blit(label, (40, 10))
                game = True

            # print_board(board)
            draw_board(board)

            turn += 1
            turn = turn % 2

    if game:
        pygame.time.wait(3000)


# integrate the pvp properly
