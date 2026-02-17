
def add_setting(settings, setting):
    key = setting[0].lower()
    value = setting[1].lower()
    if key in settings.keys():
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings, setting):
    key = setting[0].lower()
    value = setting[1].lower()
    if not key in settings.keys():
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
    settings[key] = value
    return f"Setting '{key}' updated to '{value}' successfully!"
    
def delete_setting(settings: dict, key):
    key = key.lower()
    if not key in settings.keys():
        return("Setting not found!")
    settings.pop(key)
    return f"Setting '{key}' deleted successfully!"

def view_settings(settings):
    if len(settings) == 0:
        return "No settings available."
    settings_text = 'Current User Settings:\n'
    for key, value in settings.items():
        settings_text += f"{key.capitalize()}: {value}\n"
    return settings_text


test_settings = {
    'theme': 'dark',
    'language': 'english'
}


if __name__ == "__main__":
    print('---ADD---')
    print(add_setting(test_settings, ('Theme', 'Light')))
    print(add_setting(test_settings, ('Notifications', 'Enabled')))
    print('---UPDATE---')
    print(update_setting(test_settings, ('Theme', 'System')))
    print(update_setting(test_settings, ('role', 'admin')))
    print('---DELETE---')
    print(delete_setting(test_settings, 'LANGUAGE'))
    print(delete_setting(test_settings, 'rOle'))
    print(view_settings(test_settings))
        
