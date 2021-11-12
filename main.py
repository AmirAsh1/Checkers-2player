from const import BLACK, ROWS, COLS, RED, WHITE, SQUARE_SIZE, CROWN, WHITE_WIN, RED_WIN
import pygame
import board as b
import game as g


# initialize pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Checkers')
icon = pygame.image.load('Checkers.png')
pygame.display.set_icon(icon)
# white_tile = obj.Tile('white_tile.png', 0, 0)
# brown_tile = obj.Tile('brown_tile.png', 0, 0)

tile_list = []
tile_mtx = [[]]

def get_row_col_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main():
    running = True
    clock = pygame.time.Clock()
    game = g.Game(screen)

   # p1 = board.get_piece(0, 1)
   # board.move(p1, 4, 3)

    while running:
        clock.tick(60)

        if game.winner() is not None:
            if game.winner() == RED:
                screen.blit(RED_WIN, (0, 0))
            if game.winner() == WHITE:
                screen.blit(WHITE_WIN, (0, 0))

        # exit loop for pygame window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if game.winner() is None:
                if pygame.mouse.get_pressed()[0] == 1:
                    pos = pygame.mouse.get_pos()
                    row, col = get_row_col_mouse(pos)
                    game.select(row, col)






        if game.winner() is not None:
            if game.winner() == RED:
                screen.blit(RED_WIN, (0, 0))
            if game.winner() == WHITE:
                screen.blit(WHITE_WIN, (0, 0))
        else:
            game.update()
        pygame.display.update()



main()



