import copy
import os
import time
from file_handler import make_content_from_file
from file_handler import get_rules_from_file
from ui import display
from ui import menu
import getch


def clear(): return os.system('clear')



'''
Any live cell with fewer than two live neighbours dies, as if by underpopulation.
Any live cell with two or three live neighbours lives on to the next generation.
Any live cell with more than three live neighbours dies, as if by overpopulation.
Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.'''


def step(content,rules):
    newcontent = copy.deepcopy(content)
    for i in range(1, len(content[:-1])):
        row_list = list(content[i])
        new_rowlist = list(newcontent[i])
        for j in range(1, len(row_list[:-1])):
            living_neighbours = 0
            if content[i - 1][j - 1] != '_':
                living_neighbours += 1
            if content[i - 1][j] != '_':
                living_neighbours += 1
            if content[i - 1][j + 1] != '_':
                living_neighbours += 1
            if content[i][j - 1] != '_':
                living_neighbours += 1
            if content[i][j + 1] != '_':
                living_neighbours += 1
            if content[i + 1][j - 1] != '_':
                living_neighbours += 1
            if content[i + 1][j] != '_':
                living_neighbours += 1
            if content[i + 1][j + 1] != '_':
                living_neighbours += 1

            if row_list[j] == '0':
                if rules[living_neighbours][1] == 'd':
                    new_rowlist[j] = '_'
                else:
                    new_rowlist[j] = '0'
            if row_list[j] == '_':
                if rules[living_neighbours][2] == 'd':
                    new_rowlist[j] = '_'
                else:
                    new_rowlist[j] = '0'

        newcontent[i] = ''.join(new_rowlist)
    return newcontent


def main():
    rules = []
    rules = get_rules_from_file()
    user_is_smart = False
    print(rules)
    while user_is_smart == False:
        user_choose = menu()
        if user_choose == '1':
            content = make_content_from_file("random_like_init.txt")
        elif user_choose == '2':
            content = make_content_from_file("glider.txt")
        elif user_choose == '3':
            content = make_content_from_file("stable_configurations.txt")
        elif user_choose == '4':
            content = make_content_from_file("glider_gun.txt")
        elif user_choose == '5':
            filename = input("Insert path here:")
            content = make_content_from_file(filename)
        else:
            print('Think again!')
            continue
        user_is_smart = True

    display(content)
    input('Press enter to start!')
    run = True
    while run:
        display(content)
        time.sleep(.1)
        # if getch.getch():
        #	run = False
        #	print('paused')
        content = step(content,rules)
        clear()


if __name__ == "__main__":
    main()

    # if row_list[j] == '0' and living_neighbours < 2:
    #    new_rowlist[j] = '_'
    # elif row_list[j] == '0' and 2 <= living_neighbours <= 3:
    #    new_rowlist[j] = '0'
    # elif row_list[j] == '0' and living_neighbours > 3:
    #    new_rowlist[j] = '_'
    # elif row_list[j] == '_' and living_neighbours == 3:
    #    new_rowlist[j] = '0'
