import pygame
import random

pygame.init()

screen=pygame.display.set_mode((800, 600))
clock=pygame.time.Clock()


class Fruit:
    def __init__(self, image):
        self.x=random.randint(0, 760)
        self.y=0
        self.image =pygame.image.load(image)
        self.image=pygame.transform.scale(self.image, (40, 40))

    def move(self):
        self.y += 3

    def draw(self):
        screen.blit(self.image, (self.x, self.y))


class Basket:
    def __init__(self):
        self.x=350
        self.y=530

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= 5
        if keys[pygame.K_RIGHT]:
            self.x += 5

    def draw(self):
        pygame.draw.rect(screen,"brown",(self.x, self.y,100,40))


basket=Basket()
fruit=Fruit(random.choice(["apple.png","banana.png","mango.png"]))

running=True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys=pygame.key.get_pressed()

    basket.move(keys)
    fruit.move()

    if fruit.y>530 and basket.x < fruit.x < basket.x + 100:
        fruit=Fruit(random.choice(["apple.png", "banana.png", "mango.png"]))

    if fruit.y>600:
        fruit=Fruit(random.choice(["apple.png", "banana.png", "mango.png"]))

    screen.fill("white")

    fruit.draw()
    basket.draw()

    pygame.display.update()
    clock.tick(60)

pygame.quit()


