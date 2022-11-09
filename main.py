import pygame
import sys

def endgame(mas, x, sc,d_w, d_h):

    text_pos = (d_w // 2, d_h - 50)
    font = pygame.font.Font(None, 60)

    if (mas[0][0] == mas[0][1] == mas[0][2] == 1) or \
            (mas[1][0] == mas[1][1] == mas[1][2] == 1) or \
            (mas[2][0] == mas[2][1] == mas[2][2] == 1) or \
            (mas[0][0] == mas[1][0] == mas[2][0] == 1) or \
            (mas[0][1] == mas[1][1] == mas[2][1] == 1) or \
            (mas[0][2] == mas[1][2] == mas[2][2] == 1) or \
            (mas[0][0] == mas[1][1] == mas[2][2] == 1) or \
            (mas[0][2] == mas[1][1] == mas[2][0] == 1):
        sc_text = font.render(f'Победил игрок 1', False, (255, 255, 255), (0, 0, 0))
        pos = sc_text.get_rect(center=text_pos)
        sc.blit(sc_text, pos)
        pygame.display.update()
        pygame.time.delay(3000)
        sys.exit()

    elif (mas[0][0] == mas[0][1] == mas[0][2] == 2) or \
            (mas[1][0] == mas[1][1] == mas[1][2] == 2) or \
            (mas[2][0] == mas[2][1] == mas[2][2] == 2) or \
            (mas[0][0] == mas[1][0] == mas[2][0] == 2) or \
            (mas[0][1] == mas[1][1] == mas[2][1] == 2) or \
            (mas[0][2] == mas[1][2] == mas[2][2] == 2) or \
            (mas[0][0] == mas[1][1] == mas[2][2] == 2) or \
            (mas[0][2] == mas[1][1] == mas[2][0] == 2):
        sc_text = font.render(f'Победил игрок 2', False, (255, 255, 255), (0, 0, 0))
        pos = sc_text.get_rect(center=text_pos)
        sc.blit(sc_text, pos)
        pygame.display.update()
        pygame.time.delay(3000)
        sys.exit()

    elif x == 9:
        sc_text = font.render(f'            Ничья           ', False, (255, 255, 255), (0, 0, 0))
        pos = sc_text.get_rect(center=text_pos)
        sc.blit(sc_text, pos)
        pygame.display.update()
        pygame.time.delay(3000)
        sys.exit()

def run():

    pygame.init()
    display_width = 640
    display_height = 740
    screen = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption("Крестики-нолики")
    bg_color = (0, 0, 0)
    width = height = 200
    margin = 10
    white = (255, 255, 255)
    mas = [[0] * 3 for i in range(3)]
    mas_turns = [[0] * 3 for i in range(3)]

    turn = 0
    player_1 = ((255, 0, 0), 1)
    player_2 = ((0, 255, 255), 2)
    player_turn = player_1[1]

    text_pos = (display_width // 2, display_height - 50)
    font = pygame.font.Font(None, 60)


    while True:
        endgame(mas, turn, screen, display_width, display_height)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x_mouse, y_mouse = pygame.mouse.get_pos()
                column = x_mouse//(margin + width)
                row = y_mouse // (margin + height)
                if player_turn == player_1[1] and mas_turns[row][column] == 0:
                    mas[row][column] = 1
                    player_turn = player_2[1]
                    mas_turns[row][column] = 1
                    turn += 1
                elif player_turn == player_2[1] and mas_turns[row][column] == 0:
                    mas[row][column] = 2
                    mas_turns[row][column] = 1
                    player_turn = player_1[1]
                    turn += 1
        screen.fill(bg_color)
        for row in range(3):
            for col in range(3):
                if mas[row][col] == 1:
                    color = player_1[0]
                    mas_turns[row][col] = 1
                elif mas[row][col] == 2:
                    color = player_2[0]
                    mas_turns[row][col] = 1
                else:
                    color = white
                x = col * width + (col + 1) * margin
                y = row * height + (row + 1) * margin
                pygame.draw.rect(screen, color, (x, y, width, height))

        sc_text = font.render(f'Ходит игрок {player_turn}', False, (255, 255, 255), (0, 0, 0))
        pos = sc_text.get_rect(center=text_pos)
        screen.blit(sc_text, pos)
        pygame.display.update()

run()
