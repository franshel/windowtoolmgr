import pyautogui as p
from tkinter import *
from tkinter import messagebox
import tkinter as t
from pygetwindow import Win32Window
from random import randint

root = Tk()
title = 'Window Manager Tool'
root.title(title)
root.geometry('451x237')


def manager(instruction: str):
	global windows, selected_window
	selected_window_title = clicked.get()
	selected_window = p.getWindowsWithTitle(selected_window_title)[0]
	try:
		match instruction:
			case 'maximize':
				selected_window.maximize()
			case 'minimize':
				selected_window.minimize()
			case 'restore':
				selected_window.restore()
			case 'close':
				selected_window.close()
	except Exception as err:
		messagebox.showerror(title='Exception', message=err)
	print(selected_window)


def refresh():
	global dropdown
	clicked.set('')
	dropdown['menu'].delete(0, 'end')
	windows = [window for window in p.getAllTitles() if window != '']
	for window in windows:
		dropdown['menu'].add_command(label=window, command=t._setit(clicked, window))


# window control frame
frame = LabelFrame(root, text='frem', padx=5, pady=5, )
frame.pack(fill="both", expand=True)
frame.grid(row=0, column=0)

windows = [window for window in p.getAllTitles() if window != '']
print(windows)

# selected window methods
clicked = StringVar(root)
clicked.set('')

dropdown = OptionMenu(frame, clicked, *windows)
dropdown.config(width=20)

refresh = Button(frame, text='refresh', command=refresh)
maximize = Button(frame, text='maximize', command=lambda: manager('maximize'))
minimize = Button(frame, text='minimize', command=lambda: manager('minimize'))
close = Button(frame, text='close', command=lambda: manager('close'))
restore = Button(frame, text='restore', command=lambda: manager('restore'))

# window detail frame
frame_detail = LabelFrame(root, text='Window Details', padx=5, pady=5)
frame_detail.grid(row=0, column=1)

# window properties define
centerx = Label(frame_detail)
centery = Label(frame_detail)
height = Label(frame_detail)
width = Label(frame_detail)
isMinimized = Label(frame_detail)
isMaximized = Label(frame_detail)

centerxl = Label(frame_detail, text="centerx: ")
centeryl = Label(frame_detail, text="centery: ")
heightl = Label(frame_detail, text="height: ")
widthl = Label(frame_detail, text="width: ")
isMinimizedl = Label(frame_detail, text="isMinimized:")
isMaximizedl = Label(frame_detail, text="isMaximized:")

# labels to properties

# packing or gridding
# centerxl.pack()
# centerx.pack()

centerxl.grid(row=0, column=0)
centerx.grid(row=0, column=1)

# centeryl.pack()
# centery.pack()

centeryl.grid(row=1, column=0)
centery.grid(row=1, column=1)

# heightl.pack()
# height.pack()

heightl.grid(row=2, column=0)
height.grid(row=2, column=1)

# widthl.pack()
# width.pack()

widthl.grid(row=3, column=0)
width.grid(row=3, column=1)
#
# isMinimizedl.pack()
# isMinimized.pack()

isMinimizedl.grid(row=4, column=0)
isMinimized.grid(row=4, column=1)

# isMaximizedl.pack()
# isMaximized.pack()

isMaximizedl.grid(row=5, column=0)
isMaximized.grid(row=5, column=1)

# GRID POSITION
# frame.grid_rowconfigure(0, weight=1)
# frame.grid_rowconfigure(0, weight=1)
# frame.grid_columnconfigure(0, weight=1)
# frame.grid_columnconfigure(0, weight=1)

dropdown.grid(row=0, column=0, columnspan=3)
refresh.grid(row=0, column=3)
maximize.grid(row=1, column=0)
minimize.grid(row=1, column=1)
close.grid(row=1, column=2)
restore.grid(row=1, column=3)


def update_props():
	global selected_window
	selected_window_title = clicked.get()
	try:
		selected_window = p.getWindowsWithTitle(selected_window_title)[0]
		centerx['text'] = selected_window.centerx
		centery['text'] = selected_window.centery
		height['text'] = selected_window.height
		width['text'] = selected_window.width
		isMinimized['text'] = 'True' if selected_window.isMinimized == 1 else 'False'
		isMaximized['text'] = 'True' if selected_window.isMaximized == 1 else 'False'
	except Exception as err:
		pass

	root.after(10, update_props)


update_props()

root.mainloop()
