def generate_displayer_php(directory_path, main_domain):
    php_code = f'''<?php
if(file_exists('message.json') && file_exists('colors.json')) {{
    $messageContent = file_get_contents('message.json');
    $colorContent = file_get_contents('colors.json');
    $messageData = json_decode($messageContent, true);
    $colorData = json_decode($colorContent, true);
    
    if ($messageData['display'] == 'on') {{
        echo '<link rel="stylesheet" type="text/css" href="https://{main_domain}/modules/msg-display/css/style.css">';
        echo '<div class="container py-4 py-xl-5">';
            echo '<div class="row mb-5">';
                echo '<div class="container py-4 py-xl-5" style="background-color: ' . $colorData['bgColor'] . '; color: ' . $colorData['fontColor'] . ';" id="msg-display">';
                    echo $messageData['message'];
                    echo '</div>';
            echo '</div>';
        echo '</div>';
    }}
}}
?>
'''

    with open(f"{directory_path}/msg-display/requires/displayer.php", "w") as php_file:
        php_file.write(php_code)
        print("displayer.php generated !")
