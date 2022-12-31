'''
Software Development Module FInal Project
File Description:
This is the single normal player code and window

Authour: Hani Khaled Kamal

Date : 11/5/2022

Notes: No external libraries required

'''


from tkinter import Entry, Menu, Button, Label, StringVar, Tk, Frame, Checkbutton, IntVar, Toplevel, filedialog
from tkinter import messagebox
from tkinter import *
import random
import main


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


class singleplayer():
    def singlegame(user_row, user_col, user_mine):
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

        # Creating Flag counter
        global counter_for_flag, flag_count
        new_frame = Frame(m)
        new_frame.grid(row=rows+1, columnspan=cols)
        counter_for_flag = 0
        flag_count = StringVar()
        flag_count.set(counter_for_flag)
        center_position = 0
        if (cols % 2) == 0:
            center_position = cols // 2
        else:
            center_position = (cols+1)//2
        flag_label = Label(new_frame, anchor='center', textvariable=flag_count)
        flag_label.grid(row=int(rows/2), column=center_position+4)
        flagname_label = Label(new_frame, anchor='center', text='Flags=')
        flagname_label.grid(row=int(rows/2), column=center_position+3)
        empty_label = Label(new_frame, anchor='center', text='-')
        empty_label.grid(row=int(rows/2), column=center_position)
        
        # Creating Mine counter
        global counter_for_mine, mine_count
        counter_for_mine = mines
        mine_count = StringVar()
        mine_count.set(counter_for_mine)
        center_position = 0
        if (cols % 2) == 0:
            center_position = cols // 2
        else:
            center_position = (cols+1)//2
        mine_label = Label(new_frame, anchor='center', textvariable=mine_count)
        minename_label = Label(new_frame, anchor='center', text='Mines=')

        mine_label.grid(row=int(rows/2), column=center_position-1)
        minename_label.grid(row=int(rows/2), column=center_position-2)

        # Creating the board matrix
        for i in range(0, rows):
            mine_grid.append([])
            for j in range(0, cols):
                mine_grid[i].append(0)

        # click on button and event back from Left mouse button
        def Button1(x, y):
            global first_click, buttons, number_buttons, counter_for_buttons, buttons_count
            buttons[x][y]['bg'] = 'white'
            buttons[x][y]['state'] = 'disabled'
            if (first_click == True):
                mine = mines
                while mine > 0:
                    r_x = random.randrange(0, rows) # Random selections 
                    r_y = random.randrange(0, cols) # Random selections 
                    if r_x != x and r_y != y and mine_grid[r_x][r_y] == 0:
                        mine_grid[r_x][r_y] = 1
                        mine -= 1
                first_click = False
        # Here what makes the mines and assign them to squares 
            if mine_grid[x][y] == 1:
                for i in range(0, rows):
                    for j in range(0, cols):
                        if mine_grid[i][j] == 1:
                            buttons[i][j]['bg'] = 'red'
                            buttons[i][j]['text'] = "O'"
                msgbox = messagebox.askquestion(
                    'Exit Application!', '''You lose !!\nAre you sure you want to exit the application''', icon='warning')
                if msgbox == 'yes':
                    m.destroy()
                else:
                    messagebox.showinfo(
                        'Return', 'You will now return to the starting menu')
                    play_again()
        # Creating the numbers buttons after assigning the mines
            else:
                neighbour_mines = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if x+i >= 0 and x+i < rows and y+j >= 0 and y+j < cols:
                            if mine_grid[x+i][y+j] == 1:
                                neighbour_mines += 1
                if neighbour_mines > 0:
                    buttons[x][y]['text'] = str(neighbour_mines)
        # THe Winning check after every move
                else:
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            if x+i >= 0 and x+i < rows and y+j >= 0 and y+j < cols:
                                if buttons[x+i][y+j]['state'] != 'disabled':
                                    Button1(x+i, y+j)
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
            global counter, counter_for_flag, counter_for_mine

            if buttons[x][y]['relief'] != 'sunken' and buttons[x][y]['bg'] != 'white':
                if buttons[x][y]['text'] == '':
                    buttons[x][y]['fg'] = '#D3D3D3'
                    buttons[x][y]['text'] = 'F'
                    buttons[x][y]['state'] = 'disabled'
                    counter_for_flag += 1
                    flag_count.set(counter_for_flag)
                    if counter_for_mine != 0:
                        counter_for_mine -= 1
                        mine_count.set(counter_for_mine)

                else:
                    buttons[x][y]['text'] = ''
                    buttons[x][y]['state'] = 'normal'
                    counter_for_flag -= 1
                    flag_count.set(counter_for_flag)
                    counter_for_mine += 1
                    mine_count.set(counter_for_mine)
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

        m.mainloop()


if __name__ == "__main__":
    singleplayer.singlegame()
