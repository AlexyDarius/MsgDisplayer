import tkinter as tk
from tkinter import filedialog
from tkinter import colorchooser
from generate_arbo import generate_arbo
from generate_displayer_php import generate_displayer_php
from generate_message_json import generate_message_json
from generate_msgdisplay_editor_php import generate_msgdisplay_editor_php
from generate_msgSaver_js import generate_msgSaver_js
from generate_save_message_php import generate_save_message_php
from generate_style_css import generate_style_css


def generate_files():
    directory_path = directory_var.get()
    main_domain = main_domain_entry.get()
    full_body_tag = full_body_tag_entry.get("1.0", "end-1c")
    bg_color = color_entry1.get()
    primary_color = color_entry2.get()

    if (all([directory_path, main_domain, full_body_tag, bg_color, primary_color])):
        # Generate tree path
        generate_arbo(directory_path)
        generate_displayer_php(directory_path, main_domain)
        generate_message_json(directory_path)
        generate_msgdisplay_editor_php(directory_path, main_domain, full_body_tag)
        generate_msgSaver_js(directory_path)
        generate_save_message_php(directory_path)
        generate_style_css(directory_path, bg_color, primary_color)

        result_label.config(text="Message Display files have been generated.")

        print("Message Display files well generated, don't forget to minify !")
        print("Read readme.txt for implementation.\n")

        app.quit()
    else:
        result_label.config(text="Please provide all required fields.")

def select_directory():
    directory_path = filedialog.askdirectory()
    if directory_path:
        directory_var.set(directory_path)

def open_color_picker1():
    color = colorchooser.askcolor()[1]
    color_entry1.delete(0, tk.END)
    color_entry1.insert(0, color)

def open_color_picker2():
    color = colorchooser.askcolor()[1]
    color_entry2.delete(0, tk.END)
    color_entry2.insert(0, color)

app = tk.Tk()
app.title("DariusDev Message Display Generator")

directory_var = tk.StringVar()

directory_label = tk.Label(app, text="Select Directory:")
directory_label.pack()
directory_entry = tk.Entry(app, textvariable=directory_var, width = 50)
directory_entry.pack()

select_directory_button = tk.Button(app, text="Browse", command=select_directory)
select_directory_button.pack()

main_domain_label = tk.Label(app, text="Enter the main domain (e.g. dariusdev.fr, without www. !) :")
main_domain_label.pack()
main_domain_entry = tk.Entry(app)
main_domain_entry.pack()

full_body_tag_label = tk.Label(app, text="Full Body tag (e.g. <body style=...>) :")
full_body_tag_label.pack()
full_body_tag_entry = tk.Text(app, width=50, height=5)
full_body_tag_entry.pack()

# Create an Entry widget for entering color in hex format
color_entry_label = tk.Label(app, text="Enter bg color of the message (#hex format) :")
color_entry_label.pack()
color_entry1 = tk.Entry(app)
color_entry1.pack()

# Create a Button to open the color picker
color_picker_button = tk.Button(app, text="Or use color picker", command=open_color_picker1)
color_picker_button.pack()

# Create an Entry widget for entering color in hex format
color_entry_label = tk.Label(app, text="Enter text color of the message (#hex format) :")
color_entry_label.pack()
color_entry2 = tk.Entry(app)
color_entry2.pack()

# Create a Button to open the color picker
color_picker_button = tk.Button(app, text="Or use color picker", command=open_color_picker2)
color_picker_button.pack()

blank_label = tk.Label(app, text="")
blank_label.pack()

generate_button = tk.Button(app, text="Generate", command=generate_files)
generate_button.pack()

result_label = tk.Label(app, text="")
result_label.pack()

app.mainloop()
