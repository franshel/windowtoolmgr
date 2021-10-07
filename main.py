import pyautogui as p
from tkinter import *
from tkinter import messagebox
import tkinter as t
from pygetwindow import Win32Window
from random import randint



root = Tk()
title = 'Window Manager Tool'
root.title(title)
root.geometry('512x512')


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
frame = LabelFrame(root, text='frem', padx=5, pady=5)
frame.pack(padx=10, pady=10)

windows = [window for window in p.getAllTitles() if window != '']
print(windows)

# selected window methods
clicked = StringVar(root)
clicked.set('')

dropdown = OptionMenu(frame, clicked, *windows)
dropdown.pack()

refresh = Button(frame, text='refresh', command=refresh).pack()
maximize = Button(frame, text='maximize', command=lambda: manager('maximize')).pack()
minimize = Button(frame, text='minimize', command=lambda: manager('minimize')).pack()
close = Button(frame, text='close', command=lambda: manager('close')).pack()
restore = Button(frame, text='restore', command=lambda: manager('restore')).pack()

# window detail frame
frame_detail = LabelFrame(root, text='Window Details', padx=5, pady=5)
frame_detail.pack()

# window properties define
centerx = Label(frame_detail)
centery = Label(frame_detail)
height = Label(frame_detail)
width = Label(frame_detail)
isMinimized = Label(frame_detail)
isMaximized = Label(frame_detail)

# packing or gridding
centerx.pack()
centery.pack()
height.pack()
width.pack()
isMinimized.pack()
isMaximized.pack()

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
	except:
		pass


	root.after(10, update_props)

update_props()



root.mainloop()
