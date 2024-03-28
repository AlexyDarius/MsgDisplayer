def generate_style_css(directory_path, bg_color, primary_color):
    css_code = f'''#msg-display{{
    background: {bg_color}; 
    color: {primary_color}; 
    border-radius: 12px;
    padding-top: 12px;
    padding-bottom: 12px;
}}
'''

    with open(f"{directory_path}/msg-display/css/style.css", "w") as css_file:
        css_file.write(css_code)
        print("style.css generated !")
