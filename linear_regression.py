import pygame , sys
from utiles import *

pygame.init()
clock = pygame.time.Clock()
SURFACE = pygame.display.set_mode((WIDTH, HEIGHT))
Right_clickd = False
Left_clicked = False
scroll_screen = False
center_x = 300
center_y = 300
# points = [(i/40,-(i/40)**2) for i in range(-100,100)]
points = []
m,c = 0,0
learning_rate = 0.01
while True:
    pygame.display.update()
    SURFACE.fill(back_ground)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if pygame.mouse.get_pressed()[1] and not scroll_screen:
        x0,y0 = pygame.mouse.get_pos()
        x0 -=center_x
        y0 -=center_y
        scroll_screen = True
    if pygame.mouse.get_pressed()[2] and not Right_clickd and len(points)>0:
        points.pop(-1)
        Right_clickd = True

    if pygame.mouse.get_pressed()[0] == 1 and not Left_clicked:
        real_x,real_y = pygame.mouse.get_pos()
        x_point = real_x - center_x
        y_point = center_y - real_y
        if y_point/40>3:
            points.append((x_point/40,y_point/40)) # (x,y,label)
        else:
            points.append((x_point/40,y_point/40)) # (x,y,label)
        Left_clicked =1
    if scroll_screen:
        x,y = pygame.mouse.get_pos()
        center_x = -x0 + x
        center_y = -y0 + y
    if pygame.mouse.get_pressed()[0] == 0:
        Left_clicked = False
    if pygame.mouse.get_pressed()[1] == 0:
        scroll_screen = False
    if pygame.mouse.get_pressed()[2] == 0:
        Right_clickd = False
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        learning_rate+=0.001
    if pygame.key.get_pressed()[pygame.K_LEFT] and learning_rate>0.0001:
        learning_rate-=0.001
    if pygame.key.get_pressed()[pygame.K_r]:
        m,c = 0,0
    for point in points:
        X = 40 * point[0]
        X +=center_x
        Y = 40 * point[1]
        Y = center_y - Y
        pygame.draw.circle(SURFACE,(0,255,0),(X,Y),5)
        pygame.draw.circle(SURFACE,(0,0,0),(X,Y),5,2)
    pygame.draw.line(SURFACE,axis_color,(center_x,0),(center_x,HEIGHT),2)
    pygame.draw.line(SURFACE,axis_color,(0,center_y),(WIDTH,center_y),2)
    if len(points)>0:
        pygame.display.set_caption(f'learning_rate:{learning_rate:05f}')
        m,c,error = linear_regression(points,m,c,learning_rate)
        print(error)
        line_space_to_draw(f"{m} * X + {c}",SURFACE,center_x,center_y)
