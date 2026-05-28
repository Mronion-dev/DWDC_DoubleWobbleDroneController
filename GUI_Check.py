# Example file showing a basic pygame "game loop"
import pygame
import serial
import serial.tools.list_ports
import time

# pygame setup
pygame.init()
pygame.font.init()
Tecst = pygame.font.Font()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
running = True

def find_device():
    for port in serial.tools.list_ports.comports():
        screen.fill("Black")
        test_port = my_font.render(f"Testing port:", True, (255,255,255))
        port_render = my_font.render(port.device , True, (10,255,102))
        screen.blit(test_port, (500,500))
        screen.blit(port_render, (500 + test_port.get_width(), 500))
        pygame.display.flip()
        try:
            ser = serial.Serial(port.device, 115200, timeout=1)
            print(f"Testing {port.device}")
            for i in range(3):
                ser.write("REPLY".encode("utf-8"))
                readen = ser.readline().decode("utf-8")
                if readen.strip() != "":
                    print(f"Reply from {port.device}: {readen}")
                if readen.strip() == "YES":
                   print(f"{port.device} is the correct port!")
                   ser.close
                   return(port.device)
        except:
           print("Access denied or board not responding")

true_port = find_device()
print(true_port)


if true_port == None:          
    screen.fill("Black")
    com_not_found = my_font.render("No port available for use ¯\_('v')_/¯ ", True, (255,255,255))
    screen.blit(com_not_found, (1280/2-com_not_found.get_width()/2,720/2))
    pygame.display.flip()
    time.sleep(5)
    running = False
else:
    screen.fill("Black")
    screen.blit((my_font.render(f"Working port: {true_port}", True, (255,255,255))), (500, 100))
    time.sleep(1)
#Find joysticks:
try:
    pygame.joystick.Joystick(0).init()
    joystick = pygame.joystick.Joystick(0)
    tadext = f"Controller {joystick.get_name()} found"
except:
    tadext = "Controller not found, connect a controller and restart the script"
    tadext_render = my_font.render(tadext, True, (255,0,0))
    screen.blit(tadext_render, (640 - tadext_render.get_width()/2,385 ))
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    running = False

#initialize serial and font
try:
    text_surface = my_font.render(tadext, True, (255,255,255))
    ser = serial.Serial(true_port, 115200, timeout=0.016)
except:
    pass

ser.close()
ser.open()
if ser.readline().strip() == "404/rf":
    running = False
    screen.blit((my_font.render("RF is not working on controller board! It needs immediate attention!", True, (255,255,255))), (1280/2 - my_font.render("RF is not working on controller board! It needs immediate attention!", True, (255,255,255)).get_width()/2, 700))
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.event.pump()
    posx = round(joystick.get_axis(0),1)
    posz = round(joystick.get_axis(1),1)
    pos2rot = round(joystick.get_axis(3),1)
    pos2y = round(joystick.get_axis(2),1)
    joined = f"{posx}{posz}{pos2rot}{pos2y}"
    ser.write(joined.strip().encode('utf-8'))
    # fill the screen with a color to wipe away anything from last frame
    screen.fill((0,0,0))
    sent = my_font.render("Sent: ", True, (124, 180, 190))
    screen.blit(sent, (200, 300))
    screen.blit((my_font.render(joined, True, (255,255,255))), (200 + sent.get_width(), 300))
    joined = f"X: {posx} Z: {posz} R: {pos2rot} Y: {pos2y}"
    screen.blit(text_surface, (1280/2 - text_surface.get_width()/2,35))
    values = my_font.render("Values: ", True, (205,95,102))
    screen.blit(values , (200, 200))
    screen.blit((my_font.render(joined, True, (255,255,255))), (200 + values.get_width(), 200))
    if ser.readable():
        read = ser.readline().decode("utf-8").strip()
        if read == "404/rf":
            running = False
            screen.fill((120, 6, 6))
            screen.blit((my_font.render("RF is not working on controller board! It needs immediate attention!", True, (255,255,255))), (1280/2 - my_font.render("RF is not working on controller board! It needs immediate attention!", True, (255,255,255)).get_width()/2, 550))
            pygame.display.flip()
            time.sleep(2)
        elif read == "DI":
            ser.close
            running = False
        if read == "RE":
            screen.blit((my_font.render("RE", True, (100,100,100))), (200, 600))
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
