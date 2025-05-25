import os
import shutil
from tkinter import *
from tkinter import filedialog
import customtkinter as ctk

class Main(ctk.CTk):
    
    # Sort files
    def start_sort(self):

        folder_path = self.folder_directory
        if not os.path.exists(folder_path):
            self.add_sort_info("The path does not exist.")
            return

        extensions_dictionary = {
            # extension: folder name
            'pdf': 'PDF',
            'docx': 'Word',
            'txt': 'Text',
            'py': 'Python_code',
            'java': 'Java_code',
            'png': 'Image',
            'jpg': 'Image',
            'html': 'HTML',
            'exe': 'EXE',
            'msi': 'EXE',
            'dbs': '3D_project',
            'mkv': 'Video',
            'mp4': 'Video',
            'mp3': 'Audio'
        }

        # Looping through files in a folder(Перебираем файлы в папке)
        files = os.listdir(folder_path)

        # Variable to check if any files were sorted
        files_sorted = False

        for file in files:
            # Getting the file extention
            extension = file.split('.')[-1]
            
            # Checking if the file extentension is in the dictionary
            if extension in extensions_dictionary:
                files_sorted = True
                # Getting the folder name from the dictionary
                new_folder_name = extensions_dictionary[extension]
                
                # Creating a path to the new folder
                new_folder_path = os.path.join(folder_path, new_folder_name)
                
                # Creating a folder if the folder does not exist
                if not os.path.exists(new_folder_path):
                    os.makedirs(new_folder_path)
                
                # Moving the file into new folder
                old_file_path = os.path.join(folder_path, file)
                new_file_path = os.path.join(new_folder_path, file)
                shutil.move(old_file_path, new_file_path)
                self.add_sort_info(f"File {file} is moved into the {new_folder_name}.")
        
        if not files_sorted:
            self.add_sort_info("No files to sort in the directory!")
            return


    # Set the position of the center_screen 
    def position_center_screen(self, width:int, height:int):

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width/2)-(width/2))
        y = int((screen_height/2)-(height/2))

        return f'{width}x{height}+{x}+{y}'


    def __init__(self):

        super().__init__()

        # System settings
        ctk.set_appearance_mode('dark')

        # App frame 
        self.title('Sort app')
        self.geometry(self.position_center_screen(321, 270))
        self.configure(bg_color='#242424')
        # self.iconbitmap(bitmap='')

        # Sorting of progress information
        self.sort_info_window = ctk.CTkTextbox(self, 
                                  text_color='#cdcfd1', 
                                  fg_color='#242424', 
                                  border_width=2,
                                  height=150,
                                  font=('Consolas', 12),
                                  state=ctk.DISABLED
        )
        self.sort_info_window.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='we')

        # Buttons
        self.add_button(1, 0, "Select folder", command=self.select_path)
        self.add_button(1, 1, "Sort files", command=self.start_sort)

    
    # Add button
    def add_button(self, row, column, text, command=None, columnspan=1, padx=10, pady=20, ipadx=10, ipady=2, width=90, height=45, text_color='#cdcfd1'):

        btn = ctk.CTkButton(self, 
                            text=text, 
                            command=command, 
                            text_color=text_color, 
                            fg_color='#202121', 
                            hover_color='#19191a',
                            border_color='#555b61',
                            border_width=2, 
                            width=width,
                            height=height,
                            corner_radius=8, 
                            border_spacing=7, 
                            font=('Consolas', 16)
        )
        btn.grid(row=row, column=column, columnspan=columnspan, padx=padx, pady=pady, ipadx=ipadx, ipady=ipady)
        return btn
    

    # File sort information
    def add_sort_info(self, text=None):
        
        self.sort_info_window.configure(state=ctk.NORMAL)
        self.sort_info_window.insert(ctk.END, text + '\n')
        self.sort_info_window.configure(state=ctk.DISABLED)
    

    # Select the path to sort
    def select_path(self):

        self.folder_directory = filedialog.askdirectory()


if __name__ == '__main__':
    main = Main()
    main.mainloop()
