from tkinter import *
import tkinter as tk

def router(thisPage, nextPage):
    nextPage.pack()
    thisPage.destroy()

def start_clicked():
    if (variable.get() == "Facil"):
        bounds = 10
        num_bombs = 5
    
    for i in range(bounds):
        grid.append([])
        for j in range(bounds):
            grid[i].append(Button(master=game_frame, 
                                  text="*",
                                  height=3,
                                  width=7))
            grid[i][j]
            grid[i][j].grid(row=i + 1, column=j +2)
    router(main_frame, game_frame)

#game init
def generar_minas(bounds, numMinas):
    for i in range(bounds):
        grid.append([])
        for j in range(bounds):
            grid[i].append(Button(master=game_frame, 
                                  text="*",
                                  height=3,
                                  width=7))
            grid[i][j]
            grid[i][j].grid(row=i + 1, column=j +2)

grid = []
root = Tk()
root.geometry("800x800")
main_frame = Frame(width=800, height=800)
game_frame = Frame(width=800, height=800)

#generar escenario
title = Label(master=main_frame, text="Buscaminas")
subtitle = Label(master=main_frame, text="Selecciona la dificultad")

options = ["Facil", "Medio", "Dificil"]
variable = StringVar(main_frame)
variable.set(options[0])
select = tk.OptionMenu(main_frame,variable,*options)
btnStart = Button(master=main_frame,text="INICIAR", command=start_clicked)
btnStart.grid(row=3, column=3)
title.grid(row=0, column=0)
subtitle.grid(row=2, column=0)
select.grid(row=3, column=0)
btnStart.grid(row=4, column=0)

#escena de juego
main_frame.pack()
root.mainloop()