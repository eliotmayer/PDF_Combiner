'''
PDF Combiner
Python program to combine all PDF files in a folder, in alphabetical order, into a single PDF file.

Eliot Mayer
2/14/2022

Version Notes:
1.01  Removed unnecessary imports to reduce size of pyinstaller distribution
1.02  Interim version
1.03  Add handling of bad files & listing of all good & bad files in the command window
'''
version = "1.03"


from tkinter import *
# from PIL import ImageTk, Image
from tkinter import filedialog
import os
# from time import sleep  # Uncomment if using sleep in run_combiner()

from  combine_files import combine_files

global fld, start_folder, output_folder

# start_folder = "C:/Users"
start_folder = "C:/Users/eliot_5qir2nb/OneDrive/Documents/Python"

root = Tk()
root.title("PDF File Combiner V" + version)
# root.iconbitmap("1mJ.ico")      # Converted from 1mJ.png with online tool https://hnet.com/png-to-ico/.  Comment out if compiling with pyinstaller.
root.geometry("850x250")

fname_label1 = Label(root)  # Creating label outside folder so that updates don't leave old text dangling
def get_folder_name():
    global fld, start_folder, fname_label1
    dialog_title = "Select Folder with PDF Files to Combine"
    fld = filedialog.askdirectory(initialdir=start_folder, title=dialog_title)
    fname_label1.config(text=fld)
    fname_label1.place( x=160, y=20)

bt_get_folder = Button( root, text="Select Folder", command=get_folder_name)
bt_get_folder.place( x=20, y=20, width=125 )


def run_combiner():
    global fld, output_folder
    # The following kluge is the only way I was able to clear old messages.
    clr_msg = " "*200 + "\n" + " "*200 + "\n" + " "*200+ "\n" + " "*200
    combiner_status(clr_msg)
    combiner_status("Combining files ...")
    root.update_idletasks()
    # sleep(2)

    result, output_folder = combine_files(fld)
    combiner_status(clr_msg)
    combiner_status(result)
    root.update_idletasks()

result_label = Label(root, justify=LEFT)
result_label.place( x=160, y=56 )

def combiner_status(new_msg):
    result_label.config(text=new_msg)
    root.update_idletasks()

bt_combine = Button( root, text="Combine Files", command=run_combiner)
bt_combine.place( x=20, y=60, width=125 )


def explore_output_folder():
    global output_folder
    cmd1 = "explorer.exe " + os.path.normpath(output_folder)
    os.system(cmd1 )

bt_open_output_folder = Button( root, text="Open Output Folder", command=explore_output_folder)
bt_open_output_folder.place( x=20, y=140, width=125)

root.mainloop()
