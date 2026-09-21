import cv2
import pygame
import time

# -----------------------------
# IMAGE
# -----------------------------

image_path = "spiderman.png"

img = cv2.imread(image_path)

if img is None:
    print("Image nahi mili!")
    print("Check karo: spiderman.png same folder mein hai.")
    exit()

# Image ko grayscale karo
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Pencil effect
gray = cv2.GaussianBlur(gray, (5, 5), 0)

# Edges detect
edges = cv2.Canny(gray, 50, 150)

# -----------------------------
# CONTOURS
# -----------------------------

contours, _ = cv2.findContours(
    edges,
    cv2.RETR_LIST,
    cv2.CHAIN_APPROX_NONE
)

# Sirf useful lines
contours = [
    c for c in contours
    if cv2.arcLength(c, False) > 20
]

# -----------------------------
# SIZE
# -----------------------------

WIDTH = 800
HEIGHT = 800

scale = min(
    (WIDTH - 100) / img.shape[1],
    (HEIGHT - 100) / img.shape[0]
)

new_width = int(img.shape[1] * scale)
new_height = int(img.shape[0] * scale)

# -----------------------------
# PYGAME
# -----------------------------

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pencil Drawing")

clock = pygame.time.Clock()

# White paper
screen.fill((255, 255, 255))

# -----------------------------
# DRAWING
# -----------------------------

running = True

for contour in contours:

    if not running:
        break

    # Previous point
    previous = None

    for point in contour:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

        if not running:
            break

        # OpenCV point
        px, py = point[0]

        # Scale
        x = int(px * scale)
        y = int(py * scale)

        # Center image
        x += (WIDTH - new_width) // 2
        y += (HEIGHT - new_height) // 2

        current = (x, y)

        # Pencil line
        if previous is not None:

            pygame.draw.line(
                screen,
                (70, 70, 70),
                previous,
                current,
                2
            )

        # Pencil/cursor tip
        pygame.draw.circle(
            screen,
            (30, 30, 30),
            current,
            4
        )

        pygame.display.update()

        previous = current

        # Drawing speed
        clock.tick(180)

# -----------------------------
# KEEP WINDOW OPEN
# -----------------------------

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()