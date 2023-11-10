# We can create this object and give it to the Adhd reader in main, that can be referenced throughout the project that way
class Settings(object):
    def __init__(self) -> None:
        """set default settings here"""
        self.text = {
            "size" : 30,
            "style" : "Inter"
        }

        self.pages = {
            "size" : 100
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

        
