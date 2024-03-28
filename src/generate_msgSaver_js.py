def generate_msgSaver_js(directory_path):
    js_code = f'''// Inside the script tag in the above HTML
CKEDITOR.replace('editor');

// Part of the script tag in the back-office page
fetch('requires/get_message_state.php')
.then(response => response.json())
.then(data => {{
    if (data.display === 'on') {{
        document.getElementById('displayOn').checked = true;
    }} else {{
        document.getElementById('displayOff').checked = true;
    }}
    CKEDITOR.instances.editor.setData(data.message);
}});

// Fetch and set the initial color values
fetch('requires/get_color.php')
.then(response => response.json())
.then(data => {{
    document.getElementById('bgColorPicker').value = data.bgColor;
    document.getElementById('fontColorPicker').value = data.fontColor;
}});

// Event listener for Save button
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
        alert("Contenu du message sauvegardé ! N'oubliez pas d'activer l'affichage du message");
        window.location.reload(); // Reload the page
    }});
}});

// Event listeners for radio buttons
document.querySelectorAll('input[name="display"]').forEach(radio => {{
    radio.addEventListener('change', function() {{
        const displayStatus = this.value;

        fetch('requires/save_display_status.php', {{
            method: 'POST',
            body: JSON.stringify({{ display: displayStatus }}),
            headers: {{
                'Content-Type': 'application/json'
            }}
        }})
        .then(response => response.text())
        .then(data => {{
            alert("L'affichage a été reglé sur " + displayStatus.toUpperCase() + " !");
            window.location.reload(); // Reload the page
        }});
    }});
}});

document.getElementById('saveColorsButton').addEventListener('click', function() {{
    const bgColor = document.getElementById('bgColorPicker').value;
    const fontColor = document.getElementById('fontColorPicker').value;

    fetch('requires/save_colors.php', {{
        method: 'POST',
        body: JSON.stringify({{ bgColor: bgColor, fontColor: fontColor }}),
        headers: {{
            'Content-Type': 'application/json'
        }}
    }}).then(response => response.text())
      .then(data => {{
        alert('Couleurs actualisées!');
        window.location.reload(); // Reload the page
      }});
}});
'''

    with open(f"{directory_path}/msg-display/js/msgSaver.js", "w") as js_file:
        js_file.write(js_code)
        print("msgSaver.js generated !")
