import pygame
import random

# تهيئة pygame
pygame.init()

# إعدادات نافذة اللعبة
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('لعبة سيارات')

# الألوان
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# تعريف السيارة
car_width = 50
car_height = 60
car_x = screen_width // 2 - car_width // 2
car_y = screen_height - car_height - 10
car_speed = 5

# إعدادات العقبات
obstacle_width = 50
obstacle_height = 60
obstacle_speed = 7
obstacles = []

# إعدادات اللعبة
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# وظيفة لعرض النصوص على الشاشة
def display_text(text, x, y, color):
    label = font.render(text, True, color)
    screen.blit(label, (x, y))

# وظيفة لإضافة عقبة جديدة
def add_obstacle():
    obstacle_x = random.randint(0, screen_width - obstacle_width)
    obstacle_y = random.randint(-150, -100)
    obstacles.append([obstacle_x, obstacle_y])

# اللعبة الرئيسية
def game_loop():
    global car_x

    running = True
    score = 0
    while running:
        screen.fill(BLACK)

        # التعامل مع الأحداث (مثل الخروج من اللعبة)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # تحريك السيارة
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and car_x > 0:
            car_x -= car_speed
        if keys[pygame.K_RIGHT] and car_x < screen_width - car_width:
            car_x += car_speed

        # إضافة عقبات
        if random.randint(1, 60) == 1:  # فرصة عشوائية لظهور عقبة
            add_obstacle()

        # تحريك العقبات
        for obstacle in obstacles[:]:
            obstacle[1] += obstacle_speed
            if obstacle[1] > screen_height:
                obstacles.remove(obstacle)
                score += 1  # كلما تفاديت عقبة تحصل على نقطة

        # التحقق من التصادمات بين السيارة والعقبات
        for obstacle in obstacles:
            if car_x < obstacle[0] + obstacle_width and car_x + car_width > obstacle[0] and \
               car_y < obstacle[1] + obstacle_height and car_y + car_height > obstacle[1]:
                running = False  # إذا تصادمت مع عقبة تنتهي اللعبة

        # رسم السيارة
        pygame.draw.rect(screen, BLUE, (car_x, car_y, car_width, car_height))

        # رسم العقبات
        for obstacle in obstacles:
            pygame.draw.rect(screen, RED, (obstacle[0], obstacle[1], obstacle_width, obstacle_height))

        # عرض النقاط
        display_text(f"النقاط: {score}", 10, 10, WHITE)

        # تحديث الشاشة
        pygame.display.update()

        # تحديد سرعة اللعبة
        clock.tick(60)

    pygame.quit()

# تشغيل اللعبة
game_loop()
