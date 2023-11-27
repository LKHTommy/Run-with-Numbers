import pygame
import random

pygame.init()
size = (400, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("game")

class MySprite1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 550

my_group1 = pygame.sprite.Group()
my_sprite1 = MySprite1()
my_group1.add(my_sprite1)

class MySprite2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([1, 600])
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 0

my_group2 = pygame.sprite.Group()
my_sprite2 = MySprite2()
my_group2.add(my_sprite2)

clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 32)
sum=1
while True:
    for i in range(10):
        clock.tick(60)

        f = random.randint(1, 4)
        if f == 1:
            c = "+"
        elif f == 2:
            f = "-"
        elif f == 3:
            c = "*"
        else:
            c = "/"
        
        g = random.randint(1, 4)
        if g == 1:
            d = "+"
        elif g == 2:
            d = "-"
        elif g == 3:
            d = "*"
        else:
            d = "/"
        
        b = random.randint(1, 100)
        e = random.randint(1, 100)
        
        text1 = font.render(c, True, (255, 255, 255))
        text2 = font.render(str(b), True, (255, 255, 255))
        text3 = font.render(d, True, (255, 255, 255))
        text4 = font.render(str(e), True, (255, 255, 255))
        
        text1_rect = text1.get_rect()
        text1_rect.x = 100
        text1_rect.y = 20
        
        text2_rect = text2.get_rect()
        text2_rect.x = 120
        text2_rect.y = 20
        
        text3_rect = text3.get_rect()
        text3_rect.x = 300
        text3_rect.y = 20
        
        text4_rect = text4.get_rect()
        text4_rect.x = 320
        text4_rect.y = 20
        
        for j in range(600):
            clock.tick(60)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        my_sprite1.rect.x -= 200
                    elif event.key == pygame.K_RIGHT:
                        my_sprite1.rect.x += 200
            
            text1_rect.y += 1
            text2_rect.y += 1
            text3_rect.y += 1
            text4_rect.y += 1
            
            screen.fill((0, 0, 0))
            my_group1.draw(screen)
            my_group2.draw(screen)
            screen.blit(text1, text1_rect)
            screen.blit(text2, text2_rect)
            screen.blit(text3, text3_rect)
            screen.blit(text4, text4_rect)
            
            pygame.display.update()
            pygame.display.set_caption("game")
            
            if my_sprite1.rect.colliderect(text1_rect):
                if f==1:
                    sum=sum+b
                elif f==2:
                    sum=sum-b
                elif f==3:
                    sum=sum*b
                else:
                    sum=sum/b
                
                print(sum,i+1)
                break
            elif my_sprite1.rect.colliderect(text3_rect):
                if g==1:
                    sum=sum+e
                elif g==2:
                    sum=sum-e
                elif g==3:
                    sum=sum*e
                else:
                    sum=sum/e
                
                print(sum,i+1)
                break
    z=random.randint(1,10000)
    print(z)
    if sum<z:
        print("you lost")
    elif sum==z:
        print("draw")
    else:
        print("you win")
                


    pygame.quit()