# imports
import customtkinter  # Custom tkinter
from PIL import Image  # Pillow
import webbrowser  # Web browser

# Themes / Modes
customtkinter.set_appearance_mode("System")  # Modes: system, light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue, dark-blue, green


# Functions
def change_app_mode_event(new_app_mode: str):
    customtkinter.set_appearance_mode(new_app_mode)  #


def change_language_event(language: str):
    if language == "English":
        app.title("Converter")

    elif language == "Russian":
        app.title("Конвертер")


def convert_to_png():
    img = Image.open(path.get())
    img.save("Saves/output.png")


def convert_to_ico():
    img = Image.open(path.get())
    img.save("Saves/output.ico")


def convert_to_jpg():
    img = Image.open(path.get())
    img.save("Saves/output.jpg")


def open_github():
    webbrowser.open_new("https://github.com/Eragod/Converter")


# App create
app = customtkinter.CTk()
app.iconbitmap("Images/Converter.ico")
app.title("Converter")
app.geometry("500x350")
app.resizable(False, False)

# Tabview
Tabview = customtkinter.CTkTabview(app, width=480, height=345)
Tabview.add("Converter")
Tabview.add("Settings")
Tabview.add("About the creator")
Tabview.pack()

# Path entry
path = customtkinter.CTkEntry(Tabview.tab("Converter"), width=470)
path.pack(pady=10)

# Convert Buttons
btn_png = customtkinter.CTkButton(Tabview.tab("Converter"), text="Convert to .png", command=convert_to_png)
btn_png.pack(pady=10)
btn_ico = customtkinter.CTkButton(Tabview.tab("Converter"), text="Convert to .ico", command=convert_to_ico)
btn_ico.pack(pady=10)
btn_jpg = customtkinter.CTkButton(Tabview.tab("Converter"), text="Convert to .jpg", command=convert_to_jpg)
btn_jpg.pack(pady=10)

# Settings
change_app_mode_text = customtkinter.CTkLabel(Tabview.tab("Settings"), text="Change appearance mode:").pack(pady=10)
change_app_mode = customtkinter.CTkOptionMenu(Tabview.tab("Settings"), values=["System", "Dark", "Light"],
                                              command=change_app_mode_event).pack()
change_language_text = customtkinter.CTkLabel(Tabview.tab("Settings"), text="Change language:").pack(pady=10)
change_language = customtkinter.CTkOptionMenu(Tabview.tab("Settings"), values=["English", "Russian"],
                                              command=change_language_event).pack()

# About
about_text = customtkinter.CTkLabel(Tabview.tab("About the creator"),
                                    text="This application is created by Eragod1337 . . . \n"
                                         "Github - https://github.com/Eragod/Converter\n "
                                         "This application is open source").pack(pady=10)

open_repository = customtkinter.CTkButton(Tabview.tab("About the creator"), text="Open github repository!",
                                          command=open_github).pack(pady=10)

# Start!
app.mainloop()
