'''
Software Development Module FInal Project
File Description:
This is the Advance AI code and game window

Authour: Hani Khaled Kamal

Date : 11/5/2022

Notes: No external libraries required

'''

from tkinter import Entry, Menu, Button, Label, Tk, Frame, Checkbutton, IntVar, Toplevel,  StringVar
from tkinter import messagebox
import random
import main
import time


def create_about_menu():
    help_window = Toplevel(m)
    help_window.title('About')
    l = Label(help_window, text="""Minesweeper is a single-player logic-based computer game played on a rectangular board in which the goal is 
    to identify a specified number of randomly placed 'mines' in the lowest amount of time by clicking on 'flag' squares while avoiding mine-filled squares.""")
    l.grid()


def play_again():
    m.destroy()
    main.main()


def exit_game():
    msgbox = messagebox.askquestion(
        'Exit Application!', '''Are you sure you want to exit the application?''', icon='warning')
    if msgbox == 'yes':
        m.destroy()
    else:
        pass


class advance_AI():

    def ai_play_advance(user_row, user_col, user_mine):

        global m, count, first_click, buttons
        first_click = True
        count = 0
        rows = user_row
        cols = user_col
        mines = user_mine
        mine_grid = []
        buttons = []

        m = Tk()
        m.title('Minesweeper')

        # Creating menu bar top window
        menu_bar = Menu(m, tearoff=0)
        # Menu options
        filemenu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label='Menu', menu=filemenu)
        filemenu.add_command(label='New Game', command=play_again)
        filemenu.add_command(label='About', command=create_about_menu)
        filemenu.add_command(label='Exit', command=exit_game)

        # Display help menu
        m.config(menu=menu_bar)

        # Creating the board matrix
        for i in range(0, rows):
            mine_grid.append([])
            for j in range(0, cols):
                mine_grid[i].append(0)

        #Advance AI playing moves with cheacking the neighbour buttons
        def auto():
            selection = [item for elem in buttons for item in elem]
            mine_check = [item for elem in mine_grid for item in elem]
            selection[random.randint(0, (len(selection)-1))].invoke()
            m.update()
            time.sleep(2.5)
            m.update()
            mine_check = [item for elem in mine_grid for item in elem]
            clicked_buttons = []
            for p in range((rows*cols)**2):
                comp_i = random.randint(0, (len(selection)-1))
                n_comp_i = abs(comp_i-1)
                if comp_i not in clicked_buttons:
                    clicked_buttons.append(comp_i)
                    random_button = selection[comp_i]
                    random_mine = str(mine_check[comp_i])
                    neighbour_check = str(mine_check[n_comp_i])
                    neighbour_button = selection[n_comp_i]
                    neighbour_button_bg = neighbour_button['bg']
                    background = random_button['bg']
                    if random_mine != '1' and background == '#D3D3D3':
                        random_button.invoke()
                        m.update()
                        time.sleep(1)
                        m.update()
                    elif background != 'white':
                        random_button['fg'] = '#0000FF'
                        random_button['text'] = 'F'
                        random_button['state'] = 'disabled'

                    if neighbour_check == '1' and neighbour_button_bg != 'white':
                        neighbour_button['fg'] = '#0000FF'
                        neighbour_button['text'] = 'F'
                        neighbour_button['state'] = 'disabled'

        # click on button and event back from Left mouse button

        def Button1(x, y):
            global count, first_click, buttons
            buttons[x][y]['bg'] = 'white'
            buttons[x][y]['state'] = 'disabled'
            count += 1

            if (first_click == True):
                mine = mines
                while mine > 0:
                    r_x = random.randrange(0, rows)
                    r_y = random.randrange(0, cols)
                    if r_x != x and r_y != y and mine_grid[r_x][r_y] == 0:
                        mine_grid[r_x][r_y] = 1
                        mine -= 1
                first_click = False

            if mine_grid[x][y] == 1:
                for i in range(0, rows):
                    for j in range(0, cols):
                        if mine_grid[i][j] == 1:
                            buttons[i][j]['bg'] = 'red'
                            buttons[i][j]['text'] = "O'"
                msgbox = messagebox.askquestion(
                    'Exit Application!', '''You lose !!\nAre you sure you want to exit the application''', icon='warning')
                if msgbox == 'yes':
                    time.sleep(0)
                    m.update()
                    m.destroy()
                else:
                    messagebox.showinfo(
                        'Return', 'You will now return to the starting menu')
                    play_again()

            else:
                neighbour_mines = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if x+i >= 0 and x+i < rows and y+j >= 0 and y+j < cols:
                            if mine_grid[x+i][y+j] == 1:
                                neighbour_mines += 1
                if neighbour_mines > 0:
                    buttons[x][y]['text'] = str(neighbour_mines)
                else:
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            if x+i >= 0 and x+i < rows and y+j >= 0 and y+j < cols:
                                if buttons[x+i][y+j]['state'] != 'disabled':
                                    Button1(x+i, y+j)
                # Winning check after moves
                if count == rows * cols - mines:
                    msgbox = messagebox.askquestion(
                        'Exit Application', '''You Win !!\nAre you sure you want to exit the application''', icon='warning')
                    if msgbox == 'yes':
                        m.destroy()
                    else:
                        messagebox.showinfo(
                            'Return', 'You will now return to the application screen')
                        play_again()

        # Creating Right click on button for flagging
        def Button2(evt, x, y):
            global counter_for_flag, counter_for_mine
            if buttons[x][y]['relief'] != 'sunken' and buttons[x][y]['bg'] != 'white':
                if buttons[x][y]['text'] == '':
                    buttons[x][y]['fg'] = '#0000FF'
                    buttons[x][y]['text'] = 'F'
                    buttons[x][y]['state'] = 'disabled'
                else:
                    buttons[x][y]['text'] = ''
                    buttons[x][y]['state'] = 'normal'
        # Assigning and bind the squares function to the buttons functions
        for i in range(0, rows):
            buttons .append([])
            for j in range(0, cols):
                if user_row >= 15 and user_col >= 15:
                    button = Button(m, height=1, width=2, bg='#D3D3D3', command=lambda x=i, y=j: Button1(
                        x, y), activebackground='#D3D3D3')
                    button.bind('<Button-3>', lambda evt,
                                x=i, y=j: Button2(evt, x, y))
                    button.grid(row=i+1, column=j+1)
                    buttons[i].append(button)

                else:
                    button = Button(m, height=3, width=5, bg='#D3D3D3', command=lambda x=i, y=j: Button1(
                        x, y), activebackground='#D3D3D3')
                    button.bind('<Button-3>', lambda evt,
                                x=i, y=j: Button2(evt, x, y))
                    button.grid(row=i+1, column=j+1)
                    buttons[i].append(button)
        auto()
        m.mainloop()


if __name__ == "__main__":
    advance_AI.ai_play_advance()
