def generate_save_message_php(directory_path):
    php_code = f'''<?php
// saveMessage.php
$content = file_get_contents("php://input");
$data = json_decode($content, true);

if(isset($data['message'])) {{
    file_put_contents('../message.json', json_encode($data));
    echo "Message saved successfully.";
}} else {{
    echo "No message received.";
}}
?>
'''

    with open(f"{directory_path}/msg-display/requires/save_message.php", "w") as php_file:
        php_file.write(php_code)
        print("save_message.php generated !")
