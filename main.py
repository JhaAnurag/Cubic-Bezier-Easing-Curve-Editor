import pygame
import time

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Custom Easing Animation")

CIRCLE_RADIUS = 25
CIRCLE_Y = 200
END_POINT_X = SCREEN_WIDTH - CIRCLE_RADIUS * 2

TRACKER_HEIGHT = 10
TRACKER_WIDTH = SCREEN_WIDTH
FIXED_X_POSITION = SCREEN_WIDTH - TRACKER_WIDTH

TOTAL_TIME = 2
FRAME_RATE = 60

C1, V1 = 0, 0
C4, V4 = 1, 1
C2, V2 = 0.9, 0.1
C3, V3 = 0.1, 0.9

def bezier(t, p0, p1, p2, p3):
    return (1 - t) ** 3 * p0 + 3 * t * (1 - t) ** 2 * p1 + 3 * t ** 2 * (1 - t) * p2 + t ** 3 * p3

def draw_bezier_curve(screen):
    points = [(bezier(t / 100, C1, C2, C3, C4) * SCREEN_WIDTH, bezier(t / 100, V1, V2, V3, V4) * SCREEN_HEIGHT) for t in range(101)]
    pygame.draw.lines(screen, (0, 255, 0), False, points, 2)

def solve_t_for_x(x_target):
    left, right = 0.0, 1.0
    while right - left > 1e-5:
        mid = (left + right) / 2
        if bezier(mid, C1, C2, C3, C4) * SCREEN_WIDTH < x_target:
            left = mid
        else:
            right = mid
    return (left + right) / 2

running, animation_running, animation_start_time, selected_point = True, False, None, None
keys = {pygame.K_LEFT: False, pygame.K_RIGHT: False, pygame.K_UP: False, pygame.K_DOWN: False}

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                selected_point = 1
            elif event.key == pygame.K_2:
                selected_point = 2
            elif event.key in keys:
                keys[event.key] = True
            elif event.key == pygame.K_SPACE:
                animation_running = True
                animation_start_time = time.time()
        elif event.type == pygame.KEYUP:
            if event.key in keys:
                keys[event.key] = False

    if selected_point == 1:
        if keys[pygame.K_LEFT]:
            C2 -= 0.005
        if keys[pygame.K_RIGHT]:
            C2 += 0.005
        if keys[pygame.K_UP]:
            V2 -= 0.005
        if keys[pygame.K_DOWN]:
            V2 += 0.005
    elif selected_point == 2:
        if keys[pygame.K_LEFT]:
            C3 -= 0.005
        if keys[pygame.K_RIGHT]:
            C3 += 0.005
        if keys[pygame.K_UP]:
            V3 -= 0.005
        if keys[pygame.K_DOWN]:
            V3 += 0.005

    if animation_running:
        current_time = time.time() - animation_start_time
        if current_time >= TOTAL_TIME:
            animation_running = False
        
        normalized_time = current_time / TOTAL_TIME * END_POINT_X
        t_value = solve_t_for_x(normalized_time)
        circle_y_position = bezier(t_value, V1, V2, V3, V4) * SCREEN_HEIGHT
        circle_x_position = normalized_time
    else:
        circle_x_position = circle_y_position = CIRCLE_Y

    screen.fill((0, 0, 0))
    draw_bezier_curve(screen)
    pygame.draw.circle(screen, (255, 0, 0), (int(circle_x_position), int(circle_y_position)), CIRCLE_RADIUS)
    pygame.draw.rect(screen, (0, 255, 0), (FIXED_X_POSITION, circle_y_position - (TRACKER_HEIGHT / 2), TRACKER_WIDTH, TRACKER_HEIGHT))

    for cx, cy in [(C2, V2), (C3, V3)]:
        pygame.draw.circle(screen, (255, 255, 255), (int(cx * SCREEN_WIDTH), int(cy * SCREEN_HEIGHT)), 5)

    pygame.display.flip()
    pygame.time.Clock().tick(FRAME_RATE)

pygame.quit()
