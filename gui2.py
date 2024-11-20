import pygame
from engine import Player
from engine import Game

# Global variables
SQ_SIZE = 40
H_MARGIN = SQ_SIZE * 4
V_MARGIN = SQ_SIZE
WIDTH = SQ_SIZE * 10 * 2 + H_MARGIN
HEIGHT = SQ_SIZE * 10 * 2 + V_MARGIN
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
GREY = (40, 50, 60)
WHITE = (255, 250, 250)
GREEN = (0, 128, 0)  # Dark green ships
RED = (255, 0, 0)
BLUE = (70, 130, 180)
ORANGE = (255, 140, 20)
INDENT = 10
COLOURS = {"U": GREY, "M": BLUE, "H": ORANGE, "S": RED}
HUMAN1 = True
HUMAN2 = False

pygame.init()
pygame.font.init()
pygame.display.set_caption("Battleship")
myfont = pygame.font.SysFont("fresansttf", 40)  

def draw_grid(player, left=0, top=0, search=False):
    for i in range(100):
        x = left + i % 10 * SQ_SIZE
        y = top + i // 10 * SQ_SIZE
        square = pygame.Rect(x, y, SQ_SIZE, SQ_SIZE)
        pygame.draw.rect(SCREEN, WHITE, square, width=3)
        if search:
            x += SQ_SIZE // 2
            y += SQ_SIZE // 2
            pygame.draw.circle(SCREEN, COLOURS[player.search[i]], (x, y), radius=SQ_SIZE // 4)


def draw_ships(player, left=0, top=0):
    for ship in player.ships:
        x = left + ship.col * SQ_SIZE + INDENT
        y = top + ship.row * SQ_SIZE + INDENT
        if ship.orientation == "h":
            width = ship.size * SQ_SIZE - 2 * INDENT
            height = SQ_SIZE - 2 * INDENT
        else:
            height = ship.size * SQ_SIZE - 2 * INDENT
            width = SQ_SIZE - 2 * INDENT
        rectangle = pygame.Rect(x, y, width, height)
        pygame.draw.rect(SCREEN, GREEN, rectangle, border_radius=15)


player1 = Player()
player2 = Player()
game = Game(HUMAN1, HUMAN2)
player1.search[0] = "S"
animating = True
pausing = False

while animating:
    # Track user actions
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            animating = False

        if event.type == pygame.MOUSEBUTTONDOWN and not game.over:
            x, y = pygame.mouse.get_pos()
            if game.player1_turn and x < SQ_SIZE * 10 and y < 10 * SQ_SIZE:
                row = y // SQ_SIZE
                col = x // SQ_SIZE
                index = row * 10 + col
                print(index)
                game.make_move(index)
            elif not game.player1_turn and x > WIDTH - SQ_SIZE * 10 and y > 10 * SQ_SIZE + V_MARGIN:
                row = (y - SQ_SIZE * 10 - V_MARGIN) // SQ_SIZE
                col = (x - SQ_SIZE * 10 - H_MARGIN) // SQ_SIZE
                index = row * 10 + col
                print(index)
                game.make_move(index)

        if event.type == pygame.KEYDOWN:
            # Escape key => close the animation
            if event.key == pygame.K_ESCAPE:
                animating = False
            # Space bar => pause and resume
            if event.key == pygame.K_SPACE:
                pausing = not pausing

            if event.key == pygame.K_RETURN:
                game = Game(HUMAN1, HUMAN2)

    if not pausing:
        SCREEN.fill(GREY)
        draw_grid(game.player1, search=True)
        draw_grid(game.player2, search=True, left=(WIDTH - H_MARGIN) // 2 + H_MARGIN,
                  top=(HEIGHT - V_MARGIN) // 2 + V_MARGIN)
        draw_grid(game.player2, left=(WIDTH - H_MARGIN) // 2 + H_MARGIN)
        draw_grid(game.player1, top=(HEIGHT - V_MARGIN) // 2 + V_MARGIN)
        draw_ships(game.player1, top=(HEIGHT - V_MARGIN) // 2 + V_MARGIN)
        # draw_ships(game.player2, left=(WIDTH - H_MARGIN) // 2 + H_MARGIN)  # Commented out to hide AI ships

        if not game.over and game.computer_turn:
            if game.player1_turn:
                game.basic_ai()
            else:
                game.basic_ai()

        if game.over:
            text = "Player " + str(game.result) + " wins!!!"
            textbox = myfont.render(text, False, GREY, WHITE)
            SCREEN.blit(textbox, (WIDTH // 2 - 240, HEIGHT // 2 - 50))
        pygame.time.wait(0)
        pygame.display.flip()


