'''
Software Development Module FInal Project
File Description:
This is the main window for the minesweeper game that has all the inout and all the options available

Authour: Hani Khaled Kamal

Date : 11/5/2022

Notes: No external libraries required

'''


from tkinter import Entry, Menu, Button, Label, Tk, Frame, Checkbutton, IntVar, Toplevel
from tkinter import messagebox
import single
import randomai
import aiplayer


# Global Var
global wn, row, col, mine

width = 720
height = 540


def display_inputs(fname):
    # Creating row col mine configuration
    global row_input, col_input, mine_input
    row_input = Entry(fname,  width=10)
    row_input.config(font=("Courier", 16))
    col_input = Entry(fname, width=10)
    col_input.config(font=("Courier", 16))
    mine_input = Entry(fname, width=10)
    mine_input.config(font=("Courier", 16))

# Creating the start game button with all the limits 
def start_game():
    global wn, row, col, mine
    try:
        row = int(row_input.get())
        col = int(col_input.get())
        mine = int(mine_input.get())
        if row < 4 or col < 4:
            messagebox.showinfo(
                'ERROR!', '''Cant choose grid less than 4x4''', icon='warning')
            raise ValueError
        else:
            if type(row) == int and type(col) == int and type(mine) == int and row <= 25 and col <= 60 and mine != row*col and mine < row*col and mine != 0 and (ch2.get() == 1 or ch3.get() == 1):
                messagebox.showinfo(
                    'ERROR!', '''Cant choose a AI for single player''', icon='warning')
                raise ValueError
            elif type(row) == int and type(col) == int and type(mine) == int and row <= 25 and col <= 60 and mine != row*col and mine < row*col and mine != 0 and ch2.get() == 0 and ch3.get() == 0:
                wn.destroy()
                single.singleplayer.singlegame(row, col, mine)
            elif type(row) == int and type(col) == int and type(mine) == int and row <= 25 and col <= 60 and mine != row*col and mine < row*col and ch2.get() == 1 and ch3.get() == 0 and mine != 0:
                randomai.random_AI.ai_play_random(row, col, mine)

            elif type(row) == int and type(col) == int and type(mine) == int and row <= 25 and col <= 60 and mine != row*col and mine < row*col and ch2.get() == 0 and ch3.get() == 1 and mine != 0:
                aiplayer.advance_AI.ai_play_advance(row, col, mine)
            elif mine >= row*col:
                messagebox.showinfo(
                    'ERROR!', '''The mines are equal to the squares''', icon='warning')
                raise ValueError
            elif mine == 0:
                messagebox.showinfo(
                    'ERROR!', '''The mines count cant be zero''', icon='warning')
                raise ValueError

            else:
                messagebox.showinfo(
                    'ERROR!', '''Please make sure that(Rows <= 25) and (Cols <= 60)''', icon='warning')
                raise ValueError
    except ValueError:
        row_input.delete(0, 'end')
        col_input.delete(0, 'end')
        mine_input.delete(0, 'end')
        pass

# Creating the Advance Computer solver game button with all the limits 
def ai_play_2():
    global wn, row, col, mine
    try:
        row = int(row_input.get())
        col = int(col_input.get())
        mine = int(mine_input.get())
        if type(row) == int and type(col) == int and type(mine) == int and row <= 25 and col <= 60 and mine != row*col and mine < row*col and mine != 0:
            wn.destroy()
            aiplayer.advance_AI.ai_play_advance(row, col, mine)
        elif mine >= row*col:
            messagebox.showinfo(
                'ERROR!', '''The mines are equal to the squares''', icon='warning')
            raise ValueError
        elif mine == 0:
            messagebox.showinfo(
                'ERROR!', '''The mines count cant be zero''', icon='warning')
            raise ValueError
        else:
            messagebox.showinfo(
                'ERROR!', '''Please make sure that(Rows <= 25) and (Cols <= 60)''', icon='warning')
            raise ValueError
    except ValueError:
        row_input.delete(0, 'end')
        col_input.delete(0, 'end')
        mine_input.delete(0, 'end')
        pass

# Creating the Random Computer solver game button with all the limits 
def ai_play():
    global wn, row, col, mine
    try:
        row = int(row_input.get())
        col = int(col_input.get())
        mine = int(mine_input.get())
        if type(row) == int and type(col) == int and type(mine) == int and row <= 25 and col <= 60 and mine != row*col and mine < row*col and mine != 0:
            wn.destroy()
            randomai.random_AI.ai_play_random(row, col, mine)
        elif mine >= row*col:
            messagebox.showinfo(
                'ERROR!', '''The mines are equal to the squares''', icon='warning')
            raise ValueError
        elif mine == 0:
            messagebox.showinfo(
                'ERROR!', '''The mines count cant be zero''', icon='warning')
            raise ValueError
        else:
            messagebox.showinfo(
                'ERROR!', '''Please make sure that(Rows <= 25) and (Cols <= 60)''', icon='warning')
            raise ValueError
    except ValueError:
        row_input.delete(0, 'end')
        col_input.delete(0, 'end')
        mine_input.delete(0, 'end')
        pass

# Creating the main window colors and interface with entry fields
def mainframe_title(name):
    # Create name as a lable
    title_label = Label(
        name, text='SUPER MINESWEEPER', width=17, height=1, bg='#3e050b', fg='white')
    title_label.config(font=("Courier", 40))
    title_label.place(x=100, y=80)
    # Create label rows
    rows_title = Label(
        name, text='Enter Rows', width=17, height=1, bg='#3e050b', fg='white')
    rows_title.config(font=("Courier", 16))
    rows_title.place(x=250, y=150)
    # Create label columns
    cols_title = Label(
        name, text='Enter Columns', width=17, height=1, bg='#3e050b', fg='white')
    cols_title .config(font=("Courier", 16))
    cols_title .place(x=250, y=220)
    # Create label mines
    mines_title = Label(
        name, text='Enter Mines', width=17, height=1, bg='#3e050b', fg='white')
    mines_title.config(font=("Courier", 16))
    mines_title.place(x=250, y=290)

# Creating the about button 
def create_about_menu():
    help_window = Toplevel(wn)
    help_window.title('About')
    l = Label(help_window, text="""Minesweeper is a single-player logic-based computer game played on a rectangular board in which the goal is
    to identify a specified number of randomly placed 'mines' in the lowest amount of time by clicking on 'flag' squares while avoiding mine-filled squares.""")
    l.grid()

# Creating the restart function
def play_again():
    wn.destroy()
    main()

# Creating the quit function
def exit_game():
    msgbox = messagebox.askquestion(
        'Exit Application!', '''Are you sure you want to exit the application?''', icon='warning')
    if msgbox == 'yes':
        wn.destroy()
    else:
        pass


def main():
    # Create the window and lock the size
    global wn
    wn = Tk()
    wn.geometry(f'{width}x{height}')
    wn.resizable(width=False, height=False)
    wn.title('Super Minesweeper')
    icon = '_Implementation\pictures\icon.ico'
    wn.iconbitmap(icon)
    # layout all of the main containers
    wn.grid_rowconfigure(1, weight=0)
    wn.grid_columnconfigure(1, weight=0)

    # Creating menu bar wn window
    menu_bar = Menu(wn, tearoff=0)
    # Menu options
    filemenu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label='Menu', menu=filemenu)
    filemenu.add_command(label='New Game', command=play_again)
    filemenu.add_command(label='About', command=create_about_menu)
    filemenu.add_command(label='Exit', command=exit_game)

    # Display help menu
    wn.config(menu=menu_bar)

    # Creating main menu frame
    main_frame = Frame(wn, width=width, height=height)
    main_frame.grid(sticky='nsew')
    main_frame.grid_rowconfigure(1, weight=0)
    main_frame.grid_columnconfigure(1, weight=0)
    main_frame.pack_propagate(0)

    # Create bg as a lable
    background_label = Label(main_frame, bg='#3e050b')
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    display_inputs(main_frame)

    row_input.place(x=300, y=190)
    col_input.place(x=300, y=260)
    mine_input.place(x=300, y=330)

    # Start Button
    global ch2, ch3
    ch2 = IntVar()
    d2 = Checkbutton(wn, text="Simple", variable=ch2,
                     onvalue=1, offvalue=0, height=1,
                     width=8)
    ch3 = IntVar()
    d3 = Checkbutton(wn, text="Advance", variable=ch3,
                     onvalue=1, offvalue=0, height=1,
                     width=8)

    d2.place(x=270, y=420)
    d3.place(x=370, y=420)
# Creating the cheack for the limitation of the selection for the solver options
    def ai_check():
        try:

            if ch2.get() == 1 and ch3.get() == 0:
                ai_play()
            elif ch2.get() == 0 and ch3.get() == 1:
                ai_play_2()

            else:
                raise SyntaxError
        except SyntaxError:
            messagebox.showinfo(
                'ERROR!', '''Please select only one AI option''', icon='warning')

    # Placing the Display Buttons
    start_button = Button(main_frame, text=' Start Game', width=10,
                          height=1,
                          command=start_game)
    start_button.place(x=325, y=370)

    ai_button = Button(main_frame, text=' Ai Solver', width=10,
                       height=1,
                       command=ai_check)
    ai_button.place(x=325, y=460)
    mainframe_title(background_label)

    wn.mainloop()


if __name__ == "__main__":
    main()
