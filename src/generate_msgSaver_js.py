def generate_msgSaver_js(directory_path):
    js_code = f'''// Inside the script tag in the above HTML
CKEDITOR.replace('editor');

document.getElementById('saveButton').addEventListener('click', function() {{
const userContent = CKEDITOR.instances.editor.getData();

fetch('requires/save_message.php', {{
    method: 'POST',
    body: JSON.stringify({{ message: userContent }}),
    headers: {{
        'Content-Type': 'application/json'
    }}
}})
.then(response => response.text())
.then(data => {{
    alert('Message saved!');
}});
}});
'''

    with open(f"{directory_path}/msg-display/js/msgSaver.js", "w") as js_file:
        js_file.write(js_code)
        print("msgSaver.js generated !")
