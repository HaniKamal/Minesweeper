'''
Software Development Module FInal Project
File Description:
This is the Radnom computer player window and code

Authour: Hani Khaled Kamal

Date : 11/5/2022

Notes: No external libraries required

'''



from tkinter import Entry, Menu, Button, Label, Tk, Frame, Checkbutton, IntVar, Toplevel
from tkinter import messagebox
import random
import main
import time


def create_about_menu():
    help_window = Toplevel(m)
    help_window.title('About')
    l = Label(help_window, text="This is based on Original Minesweeper")
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


class random_AI():

    def ai_play_random(user_row, user_col, user_mine):

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
        menu_bar.add_cascade(label='File', menu=filemenu)
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

        # Random AI playing moves
        def auto():
            selection = [item for elem in buttons for item in elem]
            selection[random.randint(0, (len(selection)-1))].invoke()
            m.update()
            time.sleep(2.5)
            m.update()
            clicked_buttons = []
            for p in range((rows*cols)**2):
                comp_i = random.randint(0, (len(selection)-1))
                if comp_i not in clicked_buttons:
                    clicked_buttons.append(comp_i)
                    random_button = selection[comp_i]
                    background = random_button['bg']
                    if background == '#D3D3D3':
                        random_button.invoke()
                        m.update()
                        time.sleep(1)
                        m.update()

        # click on button and event back from Left mouse button
        def Button1(x, y):
            global count, first_click, buttons
            buttons[x][y]['bg'] = 'white'
            buttons[x][y]['state'] = 'disabled'
            count += 1

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
                else:
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            if x+i >= 0 and x+i < rows and y+j >= 0 and y+j < cols:
                                if buttons[x+i][y+j]['state'] != 'disabled':
                                    Button1(x+i, y+j)
            # The Winning check after every move
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
            if buttons[x][y]['relief'] != 'sunken' and buttons[x][y]['bg'] != 'white':
                if buttons[x][y]['text'] == '':
                    buttons[x][y]['fg'] = '#D3D3D3'
                    buttons[x][y]['text'] = 'F'
                    buttons[x][y]['state'] = 'disabled'

                else:
                    buttons[x][y]['text'] = ''
                    buttons[x][y]['state'] = 'normal'
        # Assigning and bind the squares function to the buttons functions
        for i in range(0, rows):
            buttons .append([])
            for j in range(0, cols):
                if user_row >= 20 and user_col >= 20:
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
    random_AI.ai_play_random()
