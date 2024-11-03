import pygame

# pygame.init()

# WIDTH = 800
# HEIGHT = 600

# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.update()

# class Circle():
#     def __init__(self, radius, pos, color):
#         self.radius = radius
#         self.pos = pos
#         self.color = color
#         self.circle_radius = radius
#         self.circle_surface = screen

#     def draw(self):
#         pygame.draw.circle(self.circle_surface, self.radius, self.pos, self.color, self.circle_radius)

#     def grow(self):
#         self.circle_radius = self.circle_radius + 20
#         pygame.draw.circle(self.circle_surface, self.radius, self.pos, self.color, self.circle_radius)

# #creating instances of the class

# circle = Circle(50, (WIDTH/2, HEIGHT/2), "red")

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             circle.draw()
#             pygame.display.update()
#         if event.type == pygame.MOUSEBUTTONUP:
#             circle.grow()
#             pygame.display.update()





pygame.init()
screen= pygame.display.set_mode((600,600))
screen.fill((255,255,255))
blue = (0,0,255)
pygame.display.update()

class Circle():
    def __init__(self,color,pos,radius,width):
        self.circle_color = color
        self.circle_pos = pos
        self.circle_radius = radius      
        self.circle_width = width
        self.circle_surface = screen
        
    def draw(self):
       pygame.draw.circle(self.circle_surface, self.circle_color, self.circle_pos, self.circle_radius, self.circle_width)
    def grow(self,r):
        self.circle_radius = self.circle_radius + r
        pygame.draw.circle(self.circle_surface, self.circle_color, self.circle_pos, self.circle_radius, self.circle_width)
# instance of the class / object
circle = Circle(blue,(300,300),25,0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill((255,255,255))
            circle.draw()
            pygame.display.update()
        if event.type == pygame.MOUSEBUTTONUP:
            screen.fill((255,255,255))
            circle.grow(20) # important
            pygame.display.update()