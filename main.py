import os
from tkinter import *
import shutil

#t

types = [".folders"]
completedfiles = []



class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.buildGUI()
        self.filesMoved = 0
    
    def buildGUI(self):
        Label(self, text="Welcome to DirectoryCleaner").grid()
        Label(self, text="Enter your desired dir. (defalts to downloads)").grid()

        self.entry = Entry(self)
        self.entry.grid()

        Button(self, text="Clean", command=self.clean).grid()

        self.Return = Text(self)
        self.Return.grid()



    def clean(self):
        if self.entry.get() == "":
            self.path = "C:\\Users\\{}\\Downloads".format(os.getenv("username"))
        else:
            self.path = self.entry.get()
            if "C:\\Users\\{}".format(os.getenv("username")) not in self.path:
                self.path = "C:\\Users\\{}\\".format(os.getenv("username")) + self.path




        if os.path.exists(self.path):

            for file in os.listdir(self.path):
                self.check(file)
            for file in os.listdir(self.path):
                for ttype in types:                
                    if file.endswith(ttype):
                        if file not in completedfiles:
                            self.filesMoved += 1
                            self.buildDir(ttype)
                            if os.path.isdir(self.path + "\\" + file) == False:
                                shutil.move(self.path + "\\" + file, self.path + "\\" + ttype.replace(".", "")+ "\\" + file)
                            else:
                                if file.replace(".", "") not in types:
                                    self.buildDir(".folders")
                                    shutil.move(self.path + "\\" + file, self.path + "\\" + "folders"+ "\\" + file)
                            completedfiles.append(file)

                    elif os.path.isdir(self.path + "\\" + file):
                        if "." + file not in types and len(file) > 5:
                                self.filesMoved += 1
                                self.buildDir(".folders")
                                shutil.move(self.path + "\\" + file, self.path + "\\" + "folders"+ "\\" + file)


            self.alert(f"Directory Clense Completed\nYour files have been sorted\nA total of {self.filesMoved} files were moved")    
            print(types)
        else:
            self.alert(self.path + " Doesn't exist. try a different path")


    def buildDir(self, ttype):
        if os.path.exists(self.path + "\\" + ttype.replace(".", "")) == False:
            os.mkdir(self.path + "\\" + ttype.replace(".", ""))


    def alert(self, text):
        self.Return.delete(0.0, END)
        self.Return.insert(0.0, text)

    def check(self, file):
        if os.path.splitext(file)[1] not in types and os.path.splitext(file)[1] != "":
            types.append(str(os.path.splitext(file)[1]))
            print(str(os.path.splitext(file)[1]))


root = Tk()
root.title("DirCleaner")
root.geometry("640x460")

main = Application(root)

root.mainloop()