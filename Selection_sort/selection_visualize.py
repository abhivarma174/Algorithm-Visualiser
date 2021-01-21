import pygame
import random


WIDTH = 1280
HEIGHT = 720
GAP = 2

ARRSIZE = 80
RECTW = WIDTH / ARRSIZE - GAP
state = []
arr = []
for i in range(80):
    height = random.randint(10, 450)
    arr.append(height)
    state.append(1)

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Selection Sort')

# --------------------------------------


def displayArr(state):
    '''
      displays the array values as bars
      bars of  heights are equal to the values in array
    '''
    window.fill((0, 0, 0))
    for i in range(len(arr)):
        if state[i] == 0:
            color = (255, 0, 0)  # red
        elif state[i] == 2:
            color = (0, 255, 0)  # green
        else:
            color = (0, 0, 255)  # blue

        # (x-cord, y-cord, width, height)
        pygame.draw.rect(window, color, (i * (RECTW + GAP),
                                         HEIGHT - arr[i], RECTW, arr[i]))
    # (x-cord, y-cord, width, height)
    pygame.display.update()
    pygame.time.wait(150)

# -------------------------------------------


def selectionSort(itemsList):
    ''' 
       sorts the array with selction-sort technique
    '''
    n = len(itemsList)
    for counter in range(n):
        minValueIndex = counter

        for j in range(counter + 1, n):
            if itemsList[j] < itemsList[minValueIndex]:
                # changing the state value - as indication of minvalue
                state[j] = 0
                minValueIndex = j
            else:
                state[j] = 1
                state[minValueIndex] = 1

        # swaps - minimum value and counter

        itemsList[counter], itemsList[minValueIndex] = itemsList[minValueIndex], itemsList[counter]

        if counter < n:
            state[counter] = 2

        displayArr(state)


# ---------------------------------------'


# Driver code
if __name__ == "__main__":
    running = True
    firstTime = True
    while running:

        window.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if firstTime:
            selectionSort(arr)

        firstTime = False
