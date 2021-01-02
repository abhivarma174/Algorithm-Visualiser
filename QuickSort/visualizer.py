import pygame, random

WIDTH = 1280
HEIGHT = 720
GAP = 2

ARRSIZE = 80
RECTW = WIDTH / ARRSIZE - GAP
arr = [random.randrange(50, 500) for i in range(80)]

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Quick Sort')

# ---------------------------

def displayArr(pivot):

    '''
    Displays the array as bars of height equal to the value
    '''

    window.fill((0, 0, 0)) 

    for i in range(len(arr)):

        if i == pivot:
            color = (0, 255, 0) # green
        else:
            color = (255, 0, 0) # red

        # (x-cord, y-cord, width, height)
        pygame.draw.rect(window, color, (i * (RECTW + GAP), HEIGHT - arr[i], RECTW, arr[i]))

    pygame.display.update()
    pygame.time.wait(20)

def logArr():
    for val in arr:
        print(val, end = ' ')
    print()

# --------------------------------

def quickSort(arr, start , stop):

    '''
    Sorts the given arr from start to stop indexes
    using the randmized quickSort algorithm
    '''

    # if there is less than one element
    # no need to sort
    if(start >= stop): 
        return        

    pivotIndex = partitionRand(arr, start, stop)
    
    # The array is partitioned at pivotIndex and
    # pivotIndex element is at it's final index
    # sort the two subarrays 
    # before and after the pivot
    quickSort(arr , start , pivotIndex - 1)
    quickSort(arr, pivotIndex + 1, stop)
 
def partitionRand(arr, start, stop):

    '''
    Generates a random index between start and stop
    and partitions the array
    '''
 
    randPivot = random.randrange(start, stop)

    # swap arr[stop] and arr[randPivot]
    arr[stop], arr[randPivot] = arr[randPivot], arr[stop]

    return partition(arr, start, stop)

def partition(arr, start, stop):

    '''
    Partitions the array at the pivot(the last element) 
    All the elements less than the pivot are to brought to it's left
    All the elements greater than the pivot are brought to it's right
    '''

    pivot = stop 
    i = start - 1
     
    for j in range(start, stop):
        if arr[j] <= arr[pivot]:
            i = i + 1
            arr[i] , arr[j] = arr[j] , arr[i]
            displayArr(pivot)

    #swap arr[i] and arr[pivot]
    arr[pivot] , arr[i + 1] = arr[i + 1] , arr[pivot]

    pivot = i + 1
    return pivot

# --------------------------------


# Driver Code
if __name__ == "__main__":
    running = True
    firstTime = True
    while running:

        window.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if firstTime:
            quickSort(arr, 0, ARRSIZE - 1)
        
        firstTime = False
