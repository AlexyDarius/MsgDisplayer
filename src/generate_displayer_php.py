def generate_displayer_php(directory_path, main_domain):
    php_code = f'''<link rel="stylesheet" type="text/css" href="https://{main_domain}/modules/msg-display/css/style.css">
<div class="container py-4 py-xl-5">
    <div class="row mb-5">
        <div class="col text-center" id="msg-display">
<?php
if(file_exists('message.json')) {{
    $jsonContent = file_get_contents('message.json');
    $data = json_decode($jsonContent, true);
    echo $data['message'];
}} else {{
    echo "No message available.";
}}
?>
        </div>
    </div>
</div>
'''

    with open(f"{directory_path}/msg-display/requires/displayer.php", "w") as php_file:
        php_file.write(php_code)
        print("displayer.php generated !")
