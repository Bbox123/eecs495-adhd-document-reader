import json
import os
# We can create this object and give it to the Adhd reader in main, that can be referenced throughout the project that way
class Settings(object):
    def __init__(self) -> None:
        """set default settings here"""
        self.text = {
            "size" : 30,
            "style" : "Inter",
            "color" : "black"
        }

        self.pages = {
            "size" : 70
        }

        self.Milestones = {
            "frequency" : 5,
            "enabled" : {
                "Timed Break": True,
                "Card Matching Minigame": True, 
                "Pong Minigame": False,
                "Reading Comprehension Questions": True,
                "Reward Audio": False
            }
        }

        default_settings = {
            "text": self.text,
            "pages": self.pages,
            "milestones": self.Milestones
        }

        # path to settings file
        self.settings_filepath = 'settings.json'

        # load user settings if file exists, otherwise load default settings
        if os.path.isfile(self.settings_filepath):
            try:
                with open(self.settings_filepath, 'r') as settings_file:
                    self.settings = json.load(settings_file)
            except Exception as e:
                print(f'Error loading settings: {e}')
                self.settings = default_settings

        else:
            self.settings = default_settings
            # initialize settings
            self.initialize_settings(default_settings)

    def initialize_settings(self, default_settings):
        with open(self.settings_filepath, 'w') as settings_file:
                json.dump(default_settings, settings_file)

    def save_settings(self, new_settings):
        try:
            with open(self.settings_filepath, 'w') as settings_file:
                json.dump(new_settings, settings_file)
        except Exception as e:
            print(f'Error saving settings: {e}')

        
