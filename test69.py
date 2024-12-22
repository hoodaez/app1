
import pygame

import random

# تهيئة pygame
pygame.init()

# إعدادات نافذة اللعبة
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('لعبة حروب')

# الألوان
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# تعريف اللاعب
player_width = 50
player_height = 60
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 5

# إعدادات الرصاص
bullet_width = 5
bullet_height = 10
bullet_speed = 7
bullets = []

# العدو
enemy_width = 50
enemy_height = 60
enemy_speed = 3
enemies = []

# إعدادات اللعبة
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# وظيفة لعرض النصوص على الشاشة
def display_text(text, x, y, color):
    label = font.render(text, True, color)
    screen.blit(label, (x, y))

# وظيفة لإضافة عدو جديد
def add_enemy():
    enemy_x = random.randint(0, screen_width - enemy_width)
    enemy_y = random.randint(-150, -100)
    enemies.append([enemy_x, enemy_y])

# اللعبة الرئيسية
def game_loop():
    global player_x, player_y

    running = True
    while running:
        screen.fill(BLACK)

        # التعامل مع الأحداث (مثل الخروج من اللعبة)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # تحريك اللاعب
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
            player_x += player_speed

        # إطلاق الرصاص
        if keys[pygame.K_SPACE]:
            bullets.append([player_x + player_width // 2 - bullet_width // 2, player_y])

        # تحريك الرصاص
        for bullet in bullets[:]:
            bullet[1] -= bullet_speed
            if bullet[1] < 0:
                bullets.remove(bullet)

        # إضافة أعداء
        if random.randint(1, 60) == 1:  # فرصة عشوائية لظهور عدو
            add_enemy()

        # تحريك الأعداء
        for enemy in enemies[:]:
            enemy[1] += enemy_speed
            if enemy[1] > screen_height:
                enemies.remove(enemy)

        # التحقق من التصادمات بين الرصاص والأعداء
        for bullet in bullets[:]:
            for enemy in enemies[:]:
                if bullet[0] < enemy[0] + enemy_width and bullet[0] + bullet_width > enemy[0] and \
                   bullet[1] < enemy[1] + enemy_height and bullet[1] + bullet_height > enemy[1]:
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    break

        # رسم اللاعب
        pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))

        # رسم الرصاص
        for bullet in bullets:
            pygame.draw.rect(screen, WHITE, (bullet[0], bullet[1], bullet_width, bullet_height))

        # رسم الأعداء
        for enemy in enemies:
            pygame.draw.rect(screen, RED, (enemy[0], enemy[1], enemy_width, enemy_height))

        # تحديث الشاشة
        display_text("حروب - اضغط المسافة لإطلاق النار", 10, 10, WHITE)
        pygame.display.update()

        # تحديد سرعة اللعبة
        clock.tick(60)

    pygame.quit()

# تشغيل اللعبة
game_loop()
