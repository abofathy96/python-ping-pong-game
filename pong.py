# عند البداية:
from game_logic import ai_move

# إعدادات مضرب AI:
# ai_y يعبر عن top-position للمضرب المقابل
# افترض أن متغيرات height و PADDLE_HEIGHT موجودة كما في المثال السابق
HEIGHT = 480
PADDLE_HEIGHT = 80
ai_y = 0 # قيمة ابتدائية للمضرب AI
ball_y = 120 # مثال ابتدائي لموقع الكرة (يمكن أن يتغير خلال اللعبة)
# داخل حلقة اللعبة، قبل حركة المضرب المقابل:
dy_ai = ai_move(ai_y, ball_y, HEIGHT, PADDLE_HEIGHT, ai_speed_limit=0)

# ثم حفظ حدود AI:
ai_y = max(1, min(HEIGHT - PADDLE_HEIGHT, ai_y))
import pygame
import sys

# إعدادات أساسية
WIDTH, HEIGHT = 1000, 800
BG_COLOR = (0, 100, 100)
WHITE = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

clock = pygame.time.Clock()

# مضربان
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
player_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
ai_y = (HEIGHT // 2- PADDLE_HEIGHT // 2)
paddle_x_offset = 50

# كرة
BALL_SIZE = 20
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_dx, ball_dy = 6,6

# النقاط
player_score = 0
ai_score = 0
font = pygame.font.Font(None, 100)

def draw():
    screen.fill(BG_COLOR)
    # مضارب
    pygame.draw.rect(screen, WHITE, (20, player_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (WIDTH - 20 - PADDLE_WIDTH, ai_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    # الكرة
    pygame.draw.ellipse(screen, WHITE, (ball_x, ball_y, BALL_SIZE, BALL_SIZE))

    # الاهداف
    left_text = font.render(str(player_score), True, WHITE)
    right_text = font.render(str(ai_score), True, WHITE)
    screen.blit(left_text, (WIDTH//4, 20))
    screen.blit(right_text, (WIDTH*3//4, 20))

    pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # تحكم اللاعب
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_y > 0:
        player_y -= 6
    if keys[pygame.K_s] and player_y < HEIGHT - PADDLE_HEIGHT:
        player_y += 6

    # حركة الكرة
    ball_x += ball_dx
    ball_y += ball_dy

    # الاصطدام بالجدران عمودياً
    if ball_y <= 0 or ball_y >= HEIGHT - BALL_SIZE:
        ball_dy = -ball_dy

    # الاصطدام بالمضرب
    # مضرب اللاعب
    if (ball_x <= 20 + PADDLE_WIDTH and
        player_y < ball_y + BALL_SIZE and
        player_y + PADDLE_HEIGHT > ball_y):
        ball_dx = -ball_dx

    # مضرب الخصم
    if (ball_x >= WIDTH - 20 - PADDLE_WIDTH and
        ai_y < ball_y + BALL_SIZE and
        ai_y + PADDLE_HEIGHT > ball_y):
        ball_dx = -ball_dx

    # تسجيل النقاط عند فقد الكرة
    if ball_x < 0:
        ai_score += 1
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2
        ball_dx = -ball_dx
    if ball_x > WIDTH:
        player_score += 1
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2
        ball_dx = -ball_dx

    # حركة الذكاء الاصطناعي للمضرب المقابل
    if ai_y + PADDLE_HEIGHT/2 < ball_y:
        ai_y += 4
    elif ai_y + PADDLE_HEIGHT/2 > ball_y:
        ai_y -= 4
    ai_y = max(0, min(HEIGHT - PADDLE_HEIGHT, ai_y))

    draw()
    clock.tick(60)

pygame.quit()
sys.exit()