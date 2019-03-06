import os
from file_handler import make_content_from_file
from ui import display

clear = lambda: os.system('clear')

content = (make_content_from_file("gameoflife/Game_Of_Life/random_like_init.txt"))
#content = (make_content_from_file("gameoflife/Game_Of_Life/glider.txt"))

#display(content)
#print(content)


rules = {}
'''
Any live cell with fewer than two live neighbours dies, as if by underpopulation.
Any live cell with two or three live neighbours lives on to the next generation.
Any live cell with more than three live neighbours dies, as if by overpopulation.
Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.'''

def step(content):    
    for i in range(1,len(content[:-1])):
        row_list = list(content[i])
        for j in range(1,len(row_list[:-1])):
            living_neighbours = 0
            #print(content[i])
            #print(content[i][j])
            try:
                if content[i - 1][j- 1] != '_':
                    living_neighbours += 1
                if content[i - 1][j] != '_':
                    living_neighbours += 1
                if content[i - 1][j+ 1] != '_':
                    living_neighbours += 1
                if content[i][j- 1] != '_':
                    living_neighbours += 1
                if content[i][j+ 1] != '_':
                    living_neighbours += 1
                if content[i + 1][j- 1] != '_':
                    living_neighbours += 1
                if content[i + 1][j] != '_':
                    living_neighbours += 1
                if content[i + 1][j+ 1] != '_':
                    living_neighbours += 1
                #print(living_neighbours)
            except:
            #    print('exception' + str(living_neighbours))
                pass
            if row_list[j] == '0' and living_neighbours < 2:
                row_list[j] = '_'
            elif row_list[j] == '0' and 2 <= living_neighbours <= 3:
                pass
            elif row_list[j] == '0' and living_neighbours > 3:
                row_list[j] = '_'
            elif row_list[j] == '_' and living_neighbours == 3:
                row_list[j] = '0'

        content[i] = ''.join(row_list)    





    return content


        
        
while True:
    display(content)        
    input('press enter')
    content = step(content)
    clear()
    




