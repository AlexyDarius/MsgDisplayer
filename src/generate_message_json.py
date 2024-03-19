def generate_message_json(directory_path):
    json_code = f'''
'''

    with open(f"{directory_path}/msg-display/message.json", "w") as json_file:
        json_file.write(json_code)
        print("message.json generated !")
