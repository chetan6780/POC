import tkinter

sim_window = tkinter.Tk()
sim_window.title("Epidemic Outbreak")
sim_canvas = tkinter.Canvas(sim_window, width=600,height=600, bg='blue')
sim_canvas.pack(side=tkinter.LEFT)
sim_canvas.mainloop()