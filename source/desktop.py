from source.helpers import *
from source.components import *
from tkinter import *
from tkinter.dnd import DndHandler

window = Tk()
window.title("S*C*R*A*M*B*L*E")
window.geometry('800x600')
window.config(bg='#F2B33D')
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

root = LabelFrame(window)
root.grid(column=0, row=1, sticky="nsew")
root.columnconfigure(0, weight=1)
root.rowconfigure(3, weight=1)
root.pack(expand=True)

dnd_manager = DndManager(root, 500, 500)

name = 'david'
username = 'azeroth'
password = 'qwerty'
user = User(name, username, password)
computer = User('commodore', 'mr_computer', '10101010')
game = Game([user, computer])

board = Frame(dnd_manager.canvas)
board.grid(column=0, row=0, sticky="nsew")
board.columnconfigure(0, weight=1)
board.rowconfigure(0, weight=1)

for i, row in enumerate(game.board.grid):
    for j, column in enumerate(row):
        tile = game.board.grid[i][j].tile
        L = Frame(board, width=36, height=36, border=1, relief='sunken', bg='beige')
        L.grid(row=i, column=j+1, sticky='nsew') #keep first column free for player labels

game.players[0].add_tiles(game.take_tiles(7))

for n, player in enumerate(game.players):
    rack = LabelFrame(board, text=f'{player.username}', width=250, height=25, bg='white')
    rack.grid(row=len(game.board.grid)+n, column=0, sticky="ws")
    for x, tile in enumerate(player.rack):
        T = Label(rack, width=4, height=2, border=1, relief='raised', text=tile.letter, bg='brown')
        T.grid(row=0, column=x, sticky='nsew')
        D = Draggable(T)
        D.attach(dnd_manager.canvas, rack.winfo_x(), rack.winfo_y())

window.mainloop()
