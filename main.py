import pygame
import sys
import os

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pygame Window')

# Load the background image
try:
    background_image = pygame.image.load('background.jpg')
    background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
except pygame.error as e:
    print(f"Error loading background image: {e}")
    pygame.quit()
    sys.exit()

# Load Player animation frames
frame_folder = 'frames'  # Directory containing frame images
frames = []

try:
    frame_files = sorted(file_name for file_name in os.listdir(frame_folder) if file_name.endswith('.png'))
    for file_name in frame_files:
        frame_path = os.path.join(frame_folder, file_name)
        frame = pygame.image.load(frame_path)
        frames.append(frame)
except (OSError, pygame.error) as e:
    print(f"Error loading animation frames: {e}")
    pygame.quit()
    sys.exit()

frame_count = len(frames)
if frame_count == 0:
    print("No animation frames found in the 'frames' directory.")
    pygame.quit()
    sys.exit()

# Initialize animation variables
current_frame = 0
frame_rate = 15  # Number of frames to show per second
frame_duration = 1000 // frame_rate  # Milliseconds per frame
last_update_time = pygame.time.get_ticks()

#Initialize the background position and scroll speed
bg_x = 0
bg_speed = 10 # scroll speed of the background 

# Initialize sprite position
sprite_x, sprite_y = -90, 180  # Starting position of the sprite

# Initialize the exit flag
running = True

# Main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Scroll the background to the left
    bg_x -= bg_speed

    # Wrap background around when it goes off-screen
    if bg_x <= -screen_width:
        bg_x = 0

    # Draw the background image onto the screen
    screen.blit(background_image, (bg_x, 0))
    if bg_x < 0:
        screen.blit(background_image, (bg_x + screen_width, 0))

    # Update animation frame
    current_time = pygame.time.get_ticks()
    if current_time - last_update_time >= frame_duration:
        current_frame = (current_frame + 1) % frame_count
        last_update_time = current_time

    # Draw the current frame of the sprite
    screen.blit(frames[current_frame], (sprite_x, sprite_y))

    # Update the display
    pygame.display.update()

    # Control the frame rate
    pygame.time.Clock().tick(60)  # 60 frames per second

# Quit Pygame and exit the program
pygame.quit()
sys.exit()

#acds