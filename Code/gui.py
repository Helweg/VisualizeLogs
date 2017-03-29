import tkinter
from tkinter import *
from tkinter import messagebox

class Gui:
	def __init__(self):
		#Main window
		self.main_window = tkinter.Tk()

		#Set Window Default Size
		self.main_window.geometry('400x150')

		#Set Window Title
		self.main_window.wm_title('Visualising Logs Program')

		#Creating the two frames
		self.middle_frame = tkinter.Frame(self.main_window)
		self.bottom_frame = tkinter.Frame(self.main_window)

		#Sets the label\button widgets
		self.change_label = tkinter.Label(self.middle_frame, text='To change configurations: ').grid(row=0,column=0, pady=10)
		self.change_button = tkinter.Button(self.middle_frame, text='Change', command=self.change_config).grid(row=0,column=1, pady=10)

		#Sets the label\button widgets
		self.show_label = tkinter.Label(self.middle_frame, text='To open the graph and filter: ').grid(row=1,column=0, pady=10)
		self.show_button = tkinter.Button(self.middle_frame, text='Show', command = self.show_graph).grid(row=1,column=1, pady=10)

		#Sets the label\button widgets
		self.help_button = tkinter.Button(self.bottom_frame, text='Help', command=self.show_graph).grid(row=0,column=1, pady=10)
		self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy).grid(row=0,column=2, pady=10)

		#Packing the frames
		self.middle_frame.pack()
		self.bottom_frame.pack()

		#Enter the tkinter main loop.
		tkinter.mainloop()


	def show_graph(self):
		#Create TopLevel Window
		self.graph_window = tkinter.Toplevel(self.main_window)

		#Force the input focus to the widget
		self.graph_window.focus_force()

		#Set Window Default Size
		self.graph_window.geometry('900x400')

		#Set Window Title
		self.graph_window.wm_title('Graph')

		#Creating the frames
		self.top_frame = tkinter.Frame(self.graph_window)
		self.middle_frame = tkinter.Frame(self.graph_window)
		self.graph_frame = tkinter.Frame(self.graph_window)
		self.bottom_frame = tkinter.Frame(self.graph_window)

		#Sets the button widgets
		self.log_filter = tkinter.StringVar()

		#Set the label\entry widgets
		self.filter_label = tkinter.Label(self.top_frame, text='Filter: ').grid(row=0,column=0)
		self.filter_entry = tkinter.Entry(self.top_frame, textvariable = self.log_filter, width= 100)
		self.filter_entry.grid(row=0, column=1)
		self.filter_entry.insert(0, 'id=="SRX-A"; date=="2017-02-02"; time:range=="12:13:04":"12:16:04"; message=="security";')

		#Sets the button widgets
		self.generate_button = tkinter.Button(self.middle_frame, text='Generate', command=self.graph_window.destroy).grid(row=0,column=0)
		self.help_button = tkinter.Button(self.middle_frame, text='Help', command=self.graph_window.destroy).grid(row=0,column=1)

		#text

		#Sets the button widgets
		self.save_label = tkinter.Label(self.bottom_frame, text='Raw Log file ').grid(row=0,column=0)
		self.save_button = tkinter.Button(self.bottom_frame, text='Save', command=self.graph_window.destroy).grid(row=0,column=1)
		self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.graph_window.destroy).grid(row=0,column=2)

		#Packing the frames
		self.top_frame.pack()
		self.middle_frame.pack()
		self.graph_frame.pack()
		self.bottom_frame.pack()


	def change_config(self):
		#Create TopLevel Window
		self.config_window = tkinter.Toplevel(self.main_window)

		#Force the input focus to the widget
		self.config_window.focus_force()

		#Set Window Default Size
		self.config_window.geometry('400x300')

		#Set Window Title
		self.config_window.wm_title('Changing Configuration')

		#Creating the frames
		self.top_frame = tkinter.Frame(self.config_window)
		self.middle_frame = tkinter.Frame(self.config_window)
		self.bottom_frame = tkinter.Frame(self.config_window)

		#
		self.time_label = tkinter.Label(self.top_frame, text='Pull Log File and delete it every ').grid(row=0,column=0)
		self.time_entry = tkinter.Entry(self.top_frame, width= 2)
		self.time_entry.grid(row=0, column=1)
		self.time_entry.insert(0, '60')
		self.min_label = tkinter.Label(self.top_frame, text='min').grid(row=0,column=2)

		#
		self.headline_label = tkinter.Label(self.middle_frame, text='Choose a network device from the folllowing list:').grid(row=0,column=0, pady=20)

		#
		self.router_1 = tkinter.StringVar()
		self.router_2 = tkinter.StringVar()
		self.router_3 = tkinter.StringVar()
		self.router_4 = tkinter.StringVar()

		#Checkbox
		self.checkbox_1 = Checkbutton(self.middle_frame, text='SRX-A1', variable=self.router_1).grid(row=1,column=0)
		self.checkbox_2 = Checkbutton(self.middle_frame, text='SRX-A2', variable=self.router_2).grid(row=2,column=0)
		self.checkbox_3 = Checkbutton(self.middle_frame, text='SRX-A3', variable=self.router_3).grid(row=3,column=0)
		self.checkbox_4 = Checkbutton(self.middle_frame, text='SRX-A4', variable=self.router_4).grid(row=4,column=0)

		#NOTE: http://www.java2s.com/Tutorial/Python/0360__Tkinker/Reacttothecheckstateofacheckbox.htm

		#Sets the button widgets
		self.update_button = tkinter.Button(self.bottom_frame, text='Update', command=self.config_window.destroy).grid(row=0,column=0)
		self.help_button = tkinter.Button(self.bottom_frame, text='Help', command=self.config_window.destroy).grid(row=0,column=1)
		self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.config_window.destroy).grid(row=0,column=2)

		#Packing the frames
		self.top_frame.pack()
		self.middle_frame.pack()
		self.bottom_frame.pack()

#Create object
myGui = Gui()
