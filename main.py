import customtkinter
from PIL import Image


converter = "Converter"


customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green


def change_app_mode_event(new_appearance_mode: str):
    customtkinter.set_appearance_mode(new_appearance_mode)


def change_language_event(language: str):
    if language == "English":
        app.title("Converter")

    elif language == "Russian":
        app.title("Конвертер")


def convert_to_png():
    img = Image.open(path.get())
    img.save("output.png")


def convert_to_ico():
    img = Image.open(path.get())
    img.save("Converter.ico")


app = customtkinter.CTk()
app.title("Converter")
app.geometry("500x350")
app.resizable(False, False)


Tabview = customtkinter.CTkTabview(app, width=480, height=340)
Tabview.add("Converter")
Tabview.add("Settings")
Tabview.pack()


path = customtkinter.CTkEntry(Tabview.tab("Converter"), width=475)
path.pack(pady=10)


btn_png = customtkinter.CTkButton(Tabview.tab("Converter"), text="Convert to .png", command=convert_to_png)
btn_png.pack(pady=10)
btn_ico = customtkinter.CTkButton(Tabview.tab("Converter"), text="Convert to .ico", command=convert_to_ico)
btn_ico.pack(pady=10)


change_app_mode = customtkinter.CTkOptionMenu(Tabview.tab("Settings"), values=["System", "Dark", "Light"],
                                              command=change_app_mode_event).pack(pady=10)
change_language = customtkinter.CTkOptionMenu(Tabview.tab("Settings"), values=["English", "Russian"],
                                              command=change_language_event).pack()

app.mainloop()
