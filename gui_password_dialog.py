from tkinter import *

global password
global tmp_pwd
global app


def center_window(width=150, height=50):
    # get screen width and height
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    app.geometry('%dx%d+%d+%d' % (width, height, x, y))




def show():
    p = password.get() #get password from entry
    print(p)
    global tmp_pwd
    tmp_pwd = p
    app.destroy()

def run():
    global app
    global password

    app = Tk()
    center_window()
    password = StringVar() #Password variable
    passEntry = Entry(app, textvariable=password, show='*').pack()
    submit = Button(app, text='Input your password',command=show).pack()


    app.mainloop()

    #print('ma i gae bibun i da :',tmp_pwd)
    return  tmp_pwd

if __name__ == '__main__':
    run()


