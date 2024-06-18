import pygame
import time

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bezier Curve Easing Animation")

# Define the box properties
box_y = 200  # y remains constant
box_width = 50
box_height = 50
end_point_x = screen_width - box_width  # end point on x axis

total_time = 2  # duration in seconds
frame_rate = 60  

# Control points for the Bezier curve
c1, v1 = 0, 0
c4, v4 = 1, 1
c2, v2 = 0.9, 0.1  # Control point 2
c3, v3 = 0.1, 0.9  # Control point 3

# Function to calculate the Bezier curve point
def bezier(t, p0, p1, p2, p3):
    return (1 - t)**3 * p0 + 3 * t * (1 - t)**2 * p1 + 3 * t**2 * (1 - t) * p2 + t**3 * p3

# Function to draw the Bezier curve
def draw_bezier_curve(screen):
    points = []
    for t in range(101):
        t /= 100
        x = bezier(t, c1, c2, c3, c4) * screen_width
        y = bezier(t, v1, v2, v3, v4) * screen_height
        points.append((x, y))
    pygame.draw.lines(screen, (0, 255, 0), False, points, 2)

# Function to solve for t given x using binary search
def solve_t_for_x(x_target):
    left, right = 0.0, 1.0
    while right - left > 1e-5:
        mid = (left + right) / 2
        x_mid = bezier(mid, c1, c2, c3, c4) * screen_width
        if x_mid < x_target:
            left = mid
        else:
            right = mid
    return (left + right) / 2

# Main loop
running = True
animation_running = False
animation_start_time = None
selected_point = None

# Key press states
keys = {pygame.K_LEFT: False, pygame.K_RIGHT: False, pygame.K_UP: False, pygame.K_DOWN: False}

while running:
    # Event handling
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

    # Adjust control points based on key press states
    if selected_point == 1:
        if keys[pygame.K_LEFT]:
            c2 -= 0.005
        if keys[pygame.K_RIGHT]:
            c2 += 0.005
        if keys[pygame.K_UP]:
            v2 -= 0.005
        if keys[pygame.K_DOWN]:
            v2 += 0.005
    elif selected_point == 2:
        if keys[pygame.K_LEFT]:
            c3 -= 0.005
        if keys[pygame.K_RIGHT]:
            c3 += 0.005
        if keys[pygame.K_UP]:
            v3 -= 0.005
        if keys[pygame.K_DOWN]:
            v3 += 0.005

    if animation_running:
        current_time = time.time() - animation_start_time
        
        if current_time >= total_time:
            animation_running = False
        
        # Normalize current_time to range [0, end_point_x]
        normalized_time = current_time / total_time * end_point_x
        
        # Solve for t using normalized_time as x_target in Bezier curve equation
        t_value = solve_t_for_x(normalized_time)
        
        # Calculate y position using solved t_value in Bezier curve equation for y-axis control points
        box_y_position = bezier(t_value, v1, v2, v3, v4) * screen_height
        
        box_x_position = normalized_time
        
    else:
        box_x_position = box_y_position = box_y

    # Draw everything
    screen.fill((0, 0, 0))
    draw_bezier_curve(screen)
    pygame.draw.rect(screen, (255, 0, 0), (box_x_position, box_y_position, box_width, box_height))  # Draw the box

    # Draw control points
    for cx, cy in [(c2, v2), (c3, v3)]:
        pygame.draw.circle(screen, (255, 255, 255), (int(cx * screen_width), int(cy * screen_height)), 5)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(frame_rate)

pygame.quit()
