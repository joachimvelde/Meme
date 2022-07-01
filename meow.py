import pygame
import serial
import time

WIDTH = 500
HEIGHT = 500

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    running = True

    arduino = serial.Serial(port="COM5", baudrate=9600, timeout=0.05)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        mouse_pos = pygame.mouse.get_pos()
        mouse_x = mouse_pos[0] / (WIDTH / 180)
        mouse_y = mouse_pos[1] / (HEIGHT / 180)
        serial_data = f'X{int(mouse_x)}Y{int(mouse_y)}'
        print(serial_data)
        time.sleep(0.05)
        arduino.write(bytes(serial_data, "utf-8"))

if __name__ == "__main__":
    main()