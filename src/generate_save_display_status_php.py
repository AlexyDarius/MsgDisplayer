def generate_save_display_status_php(directory_path):
    php_code = f'''<?php
// saveDisplayStatus.php
$content = file_get_contents("php://input");
$data = json_decode($content, true);

if(isset($data['display'])) {{
    if(file_exists('../message.json')) {{
        // Load existing JSON data
        $jsonData = json_decode(file_get_contents('../message.json'), true);
    }} else {{
        // Default JSON structure if file doesn't exist
        $jsonData = ["message" => "", "display" => "off"];
    }}

    // Update only the display status
    $jsonData['display'] = $data['display'];

    // Save the entire JSON data back to the file
    file_put_contents('../message.json', json_encode($jsonData));
    echo "Display status saved successfully.";
}} else {{
    echo "No display status received.";
}}
?>
'''

    with open(f"{directory_path}/msg-display/requires/save_display_status.php", "w") as php_file:
        php_file.write(php_code)
        print("save_display_status.php generated !")
