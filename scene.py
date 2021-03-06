import tkinter as tk

'''
Scene is the top half of the window that shows the background and has slots to place chacters.
'''


class Scene(tk.Frame):
    def __init__(self, master = None, initBackground = None, scale=0.5):
        tk.Frame.__init__(self, master)
        self.scene = tk.Canvas(self, width=scale*1920, height=scale*1080)
        self.background = initBackground
        self.scene.pack(side='top')
        self.characters = []
    
    def changeBackground(self, newBackground):
        '''
        Takes a background image and replaces the current background
        '''
        self.background = newBackground
        self.characters = []
    
    def changeCharacter(self, newCharacter = None, location = 0):
        '''
        Takes a person and puts them in the scene at the specified location
        '''
        self.characters[location] = newCharacter
        self.draw()
    
    def draw(self):
        pass
        
        
        
if __name__ == "__main__":
    class Application(tk.Frame):
        def __init__(self, master=None):
            super().__init__(master)
            self.pack()
            self.create_widgets()
    
        def create_widgets(self):
            self.hi_there = Scene(self)
            self.hi_there.pack(side="top")
    
            self.quit = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
            self.quit.pack(side="bottom")
    
        def say_hi(self):
            print("hi there, everyone!")

    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

