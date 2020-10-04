from userInterface import *
        
def main():
    master = Tk()
    master.title("Rockets and Metors")
    master.geometry("850x600")
    img = PhotoImage( file = "Group1.png")
    x = Display(master,img)
    master.mainloop()

main()
