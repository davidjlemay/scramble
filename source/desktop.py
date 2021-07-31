from source.helpers import *
from source.components import Board, Game, Player
import tkinter as tk

window = tk.Tk()
window.title("S*C*R*A*M*B*L*E")
window.geometry('500x500')
window.config(bg='#F2B33D')
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

root = tk.LabelFrame(window)
root.grid(column=0, row=1, sticky="nsew")
root.columnconfigure(0, weight=1)
root.rowconfigure(3, weight=1)
root.pack(expand=True)

name = 'david'
username = 'azeroth'
password = 'qwerty'
user = User(name, username, password)
game = Game([user])

board = tk.Frame(root)
board.grid(column=0, row=0, sticky="nsew")
board.columnconfigure(0, weight=1)
board.rowconfigure(0, weight=1)

for i, row in enumerate(game.board.grid):
    for j, column in enumerate(row):
        tile = game.board.grid[i][j].tile
        L = tk.Frame(board, width=25, height=25, border=1, relief='sunken', bg='beige')
        L.grid(row=i, column=j, sticky="nsew")
        L.bind('<Button-1>', lambda e, i=i, j=j: on_button_release(i, j, e, x))


for n, player in enumerate(game.players):
    rack = tk.Label(root, text=f'{player.name}', bg='white')
    rack.grid(row=2+n, column=0, sticky="ws")
    for x, tile in enumerate(player.tiles):
        T = tk.Frame(rack, width=25, height=25, border=1, relief='raised', text=tile.letter, bg='brown')
        T.grid(row=2+n, column=0 + x)
        make_draggable(T)

root.mainloop()
