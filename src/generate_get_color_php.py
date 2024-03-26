def generate_get_color_php(directory_path):
    php_code = f'''<?php
header('Content-Type: application/json');

if(file_exists('../colors.json')) {{
    echo file_get_contents('../colors.json');
}} else {{
    // Default colors if the file doesn't exist
    echo json_encode(["bgColor" => "#6c757d", "fontColor" => "#0d6efd"]);
}}
?>
'''

    with open(f"{directory_path}/msg-display/requires/get_color.php", "w") as php_file:
        php_file.write(php_code)
        print("get_color.php generated !")
