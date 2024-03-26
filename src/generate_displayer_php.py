def generate_displayer_php(directory_path, main_domain):
    php_code = f'''<?php
if(file_exists('message.json')) {{
    $jsonContent = file_get_contents('message.json');
    $data = json_decode($jsonContent, true);
    
    if ($data['display'] == 'on') {{
        echo '<link rel="stylesheet" type="text/css" href="https://{main_domain}/modules/msg-display/css/style.css">';
        echo '<div class="container py-4 py-xl-5">';
            echo '<div class="row mb-5">';
                echo '<div class="col text-center" id="msg-display">';
                    echo $data['message'];
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
