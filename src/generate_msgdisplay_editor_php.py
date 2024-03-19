def generate_msgdisplay_editor_php(directory_path, main_domain, full_body_tag):
    php_code = f'''<?php
require $_SERVER['DOCUMENT_ROOT']. '/modules/auth/checker.php';
include $_SERVER['DOCUMENT_ROOT']. '/includes/head.php'
?>

    <title>Votre interface de gestion d'affichage de message</title>
    <script src="https://cdn.ckeditor.com/4.16.0/standard/ckeditor.js"></script>
</head>

{full_body_tag}

<?php
include $_SERVER['DOCUMENT_ROOT']. '/includes/navbar.php'
?>

    <header>
        <h1 style="margin: 32px; font-weight: bold; text-align: center">Bienvenue sur votre espace gestionnaire d'affichage de message</h1>
    </header>

    <div class="container">
        <div class="row">
            <div class="col-md-12">
                <textarea id="editor" style="width: 80%; align-item: center"></textarea>
                <button id="saveButton" style="margin-top:32px; margin-bottom: 32px">Sauvegarder et envoyer le message</button>
            </div>
        </div>
    </div>
    </div>
        <p style="text-align: center; font-size: 24px"><a href="https://{main_domain}/">Revenir à l'accueil</a></p>
    </div>

    <script src="https://{main_domain}/modules/msgdisplay/js/msgSaver.js"></script>

<?php
include $_SERVER['DOCUMENT_ROOT']. '/includes/footer.php'
?>
'''

    with open(f"{directory_path}/msg-display/msgdisplay-editor.php", "w") as php_file:
        php_file.write(php_code)
        print("msgdisplay-editor.php generated !")