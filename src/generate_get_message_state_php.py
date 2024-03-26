def generate_get_message_state_php(directory_path):
    php_code = f'''<?php
if(file_exists('../message.json')) {{
    $jsonContent = file_get_contents('../message.json');
    echo $jsonContent;
}} else {{
    echo json_encode(["message" => "", "display" => "off"]);
}}
?>

'''

    with open(f"{directory_path}/msg-display/requires/get_message_state.php", "w") as php_file:
        php_file.write(php_code)
        print("get_message_state.php generated !")
