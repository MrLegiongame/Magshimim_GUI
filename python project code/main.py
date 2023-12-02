import tkinter
from tkinter import messagebox
#asdasdasdsa
#asdasdasdsa
#import customtkinter as ctk
import requests#
import customtkinter
import tkinterDnD #pip install python-tkdnd
import configparser


class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, text=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.txt = ''
        self.geometry("600x980")
        self.resizable(False, False)
        font = ("Arial", 12)
        self.label = customtkinter.CTkLabel(self, text="Final text")
        self.label.pack(padx=20, pady=20)
        self.text_6 = customtkinter.CTkTextbox(master=self, width=300, height=500)
        self.text_6.configure('rtl', font=font)
        self.text_6.pack(side=tkinter.TOP, pady=10, fill=tkinter.BOTH, padx=10)

    def add_txt(self, txt):
        self.txt = txt
        self.text_6.insert('0.0', self.txt)


class MyFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.txt = ''
        config = configparser.ConfigParser()
        config.read('Config.ini')

        # Replace these variables with your GitLab information
        gitlab_url = 'https://gitlab.com'
        private_token = config['Api GitLab']['Key']
        project_id = config['Api GitLab']['ID']
        self.toplevel_window = None
        # Set up the base URL for GitLab API requests
        self.api_url = f'{gitlab_url}/api/v4/projects/{project_id}/issues/'
        self.headers = {'PRIVATE-TOKEN': private_token}

        customtkinter.set_ctk_parent_class(tkinterDnD.Tk)
        font = ("Arial", 12)  # You can choose a different font

        customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
        customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

        label_1 = customtkinter.CTkLabel(master=self, justify=customtkinter.LEFT)
        label_1.pack(pady=10, padx=10)
        label_1.configure(text="Group number {}".format(config['Group number']['Team']))

        label_2 = customtkinter.CTkLabel(master=self, justify=customtkinter.LEFT)
        label_2.configure(text="מספר מפגש")
        entry_1 = customtkinter.CTkEntry(master=self, placeholder_text="מספר")
        entry_1.configure('rtl', font=font)
        label_2.pack(side=tkinter.TOP, pady=10, padx=10)
        entry_1.pack(side=tkinter.TOP, pady=10, padx=10)

        label_3 = customtkinter.CTkLabel(master=self, justify=customtkinter.LEFT)
        label_3.configure(text="?האם יש פערים? מה הם? למה הם קרו? מתי אנחנו משלימים אותם")
        label_3.configure('rtl', font=font)
        label_3.pack(side=tkinter.TOP, pady=20, padx=40, anchor=tkinter.NE)
        text_1 = customtkinter.CTkTextbox(master=self, width=500, height=70)
        text_1.configure('rtl', font=font)
        text_1.pack(side=tkinter.TOP, pady=10, fill=tkinter.BOTH, padx=10)

        def gitlab_callback():
            self.txt = ''
            text_5.delete('1.0', 'end')
            print(self.api_url)
            print(self.headers)
            response = requests.get(self.api_url, headers=self.headers)
            if response.status_code == 200:
                # Successful request, print the response JSON
                boards_data = response.json()
                for data in boards_data:
                    if data['state'] != 'closed' and len(data['labels']) > 0 :
                        if len(data['assignees']) > 0 and data['labels'][0] != 'Done' and data['labels'][0] != 'done':
                            print(data['title'] + ' ' + (str)(data['due_date']) + ' ' + (str)(
                                data['assignees'][0]['name']))#
                            self.txt += data['title'] + ' | ' + (str)(data['due_date']) + ' | ' + (str)(
                                data['assignees'][0]['name']) + '\n'
                        elif data['labels'][0] != 'Done' and data['labels'][0] != 'done':
                            print(data['title'] + ' ' + (str)(data['due_date']) + ' ' + 'ERROR: No assignee')
                            self.txt += data['title'] + ' | ' + (str)(
                                data['due_date']) + ' | ' + 'ERROR: No assignee' + '\n'
            else:
                # Print an error message if the request was not successful
                print(f"Failed to get boards. Status code: {response.status_code}")
                print(response.text)
            text_5.insert('0.0', self.txt)

        button_1 = customtkinter.CTkButton(master=self, command=gitlab_callback)
        button_1.configure(text="Import Gitlab")
        button_1.pack(pady=10, padx=10)

        text_5 = customtkinter.CTkTextbox(master=self, width=300, height=300)
        text_5.configure('rtl', font=font)
        text_5.pack(side=tkinter.TOP, pady=10, fill=tkinter.BOTH, padx=10)

        label_4 = customtkinter.CTkLabel(master=self, justify=customtkinter.LEFT)
        label_4.configure(text="?תוספת למשימות")
        label_4.configure('rtl', font=font)
        label_4.pack(side=tkinter.TOP, pady=20, padx=40, anchor=tkinter.NE)
        text_2 = customtkinter.CTkTextbox(master=self, width=500, height=70)
        text_2.configure('rtl', font=font)
        text_2.pack(side=tkinter.TOP, pady=10, fill=tkinter.BOTH, padx=10)

        label_4 = customtkinter.CTkLabel(master=self, justify=customtkinter.LEFT)
        label_4.configure(text="?סטטוס עם המנטור")
        label_4.configure('rtl', font=font)
        label_4.pack(side=tkinter.TOP, pady=20, padx=40, anchor=tkinter.NE)
        text_3 = customtkinter.CTkTextbox(master=self, width=500, height=70)
        text_3.configure('rtl', font=font)
        text_3.pack(side=tkinter.TOP, pady=10, fill=tkinter.BOTH, padx=10)

        label_5 = customtkinter.CTkLabel(master=self, justify=customtkinter.LEFT)
        label_5.configure(text="סיכום הדברים והפקת לקחים")
        label_5.configure('rtl', font=font)
        label_5.pack(side=tkinter.TOP, pady=20, padx=40, anchor=tkinter.NE)
        text_4 = customtkinter.CTkTextbox(master=self, width=500, height=70)
        text_4.configure('rtl', font=font)
        text_4.pack(side=tkinter.TOP, pady=10, fill=tkinter.BOTH, padx=10)

        def open_toplevel(self, text):
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.toplevel_window = ToplevelWindow(self)  # create window if its None or destroyed
                self.toplevel_window.add_txt(text)
            else:
                self.toplevel_window.focus()  # if window exists focus i

        def finish_callback():
            Error = ''
            if entry_1.get() == '':
                Error += ' למלא מספר מפגש( חייב להיות מספר)'+ "\n"
            if text_5.compare("end-1c", "==", "1.0") and text_2.compare("end-1c", "==", "1.0"):
                Error += ' למלא רשימת משימות' + "\n"
            if text_1.compare("end-1c", "==", "1.0"):
                Error += ' למלא פערים ' + "\n"
            if text_3.compare("end-1c", "==", "1.0"):
                Error += 'למלא סטטוס עם המנטור' + "\n"
            if text_4.compare("end-1c", "==", "1.0"):
                Error += 'למלא סיכום' + "\n"
            if Error != '':
                messagebox.showerror("שגיאה", Error)
                return
            final_text = "סיכום שיחת סטטוס מפגש {} – צוות {}".format(entry_1.get(), config['Group number']['Team'])
            final_text = final_text + "\n\n\n\n" + " ?האם יש פערים? מה הם? למה הם קרו? מתי אנחנו משלימים אותם" + "\n"
            final_text = final_text + text_1.get("1.0", "end")
            final_text = final_text + "\n\n\n\n" + "רשימת משימות לשבוע הקרוב כולל אחראי ודד-ליין." + "\n\n"
            final_text = final_text + text_5.get("1.0", "end") + "\n" + text_2.get("1.0", "end") + "\n"
            final_text = final_text + "\n\n\n\n" + "?סטטוס עם המנטור" + "\n"
            final_text = final_text + text_3.get("1.0", "end")
            final_text = final_text + "\n\n\n\n" + "?סיכום הדברים והפקת לקחים" + "\n"
            final_text = final_text + text_4.get("1.0", "end")
            open_toplevel(self, final_text)

        button_2 = customtkinter.CTkButton(master=self, command=finish_callback)
        button_2.configure(text="Finish")
        button_2.pack(pady=10, padx=10)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        customtkinter.set_ctk_parent_class(tkinterDnD.Tk)
        font = ("Arial", 12)  # You can choose a different font

        customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
        customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
        self.title("Magshimim GUI by leonid")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.my_frame = MyFrame(master=self, width=600, height=980, corner_radius=0, fg_color="transparent")
        self.my_frame.grid(row=0, column=0, sticky="nsew")


if __name__ == "__main__":
    app = App()
    app.after(201, lambda: app.iconbitmap('11560173.ico'))
    app.mainloop()
