"""
Created on 30 Aug, 2022 at 11:24
    Title: browse_gui.py - Browsing GUI for selecting Folders and Files
    Description:
        -   ...
@author: Supantha Sen, sunnymac, IISc Bangalore
"""

# Importing Modules
from tkinter import filedialog

# Importing Custom Modules
...

...

def browse_folder(title_details):
    directory = filedialog.askdirectory(initialdir = '/home/nrsc/Desktop/Temp_Files/',
                                        title = title_details
                                       )
    return directory


def browse_file(title_details):
    filename = filedialog.askopenfilename(initialdir = '/home/nrsc/Desktop/Temp_Files/',
                                          title = title_details,
                                          filetypes = (('all files','*.*'), ('text files', '*.txt*'))
                                         )
    return filename