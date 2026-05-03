size = 1001
grid = [[0 for _ in range(size)] for _ in range(size)]
centre = size//2


right = (0,1)
left = (0,-1)
up = (-1,0)
down = (1,0)

def turn(direction):
    if direction == right:
         return  down
    elif direction == down:
         return  left
    elif direction == left:
        return up
    elif direction == up:
        return right

def gen_grid(grid,size):
    direction = right
    posx = centre
    posy = centre
    num = 1 
    while num <= size**2:
        grid[posy][posx] = num
        if grid[posy+turn(direction)[0]][posx+turn(direction)[1]] == 0 and num != 1: 
            direction = turn(direction)

        posy += direction[0] ; posx += direction[1]
        num+=1
    return grid

def sumDiagonals(grid):
    total = 0
    posx,posy = 0,0
    while posx < size:
        total += grid[posy][posx]
        posx+=1;posy+=1
    posx = 0 
    posy = size-1
    while posx < size:
        total += grid[posy][posx]
        posx+=1;posy-=1
    total -= grid[centre][centre]
    return total

grid = gen_grid(grid,size)
print(sumDiagonals(grid))

#4 line solution
total = 1 
for n in range(3,size+1,2):
    total += 4*n**2 - 6*(n-1)
print(total)

