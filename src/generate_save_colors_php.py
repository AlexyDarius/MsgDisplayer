def generate_save_colors_php(directory_path):
    php_code = f'''<?php
$content = file_get_contents("php://input");
$data = json_decode($content, true);

if(isset($data['bgColor']) && isset($data['fontColor'])) {{
    file_put_contents('../colors.json', json_encode($data));
    echo "Color data saved successfully.";
}} else {{
    echo "Failed to receive color data.";
}}
?>
'''

    with open(f"{directory_path}/msg-display/requires/save_colors.php", "w") as php_file:
        php_file.write(php_code)
        print("save_colors.php generated !")
