def generate_colors_json(directory_path):
    json_code = f'''{{"bgColor":"#ffffff","fontColor":"#000000"}}
'''

    with open(f"{directory_path}/msg-display/colors.json", "w") as json_file:
        json_file.write(json_code)
        print("colors.json generated !")
