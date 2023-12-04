from PyQt6.QtCore import Qt, QTimer, QEventLoop
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel, QVBoxLayout
import random
import sys
import time

blocking_status = 0




class ConfigCardMatching:
    def __init__(self, x: int=4, y: int=4, num: int=4, picture_mapping=str):
        """initialize the card board
        
        Keyword arguments:
        x: height (axis=0)
        y: width (axis=1)
        num: how many different cards
        picture_mapping: mapping function from int digits (1, 2, etc. to things that actually shown. Default is str function)
        (num*2)|(x*y) is required, otherwise error occurs
        
        """
        assert x*y % (num*2) == 0
        self.x = x
        self.y = y
        self.num = num
        self.symbols = (list(map(picture_mapping, range(1,num+1)))) * int(x*y/num)
        self.pairs_for_win = int(x*y/2)
        

class CardMatchingGame(QWidget):
    def __init__(self, config: ConfigCardMatching=ConfigCardMatching()):
        super().__init__()
        self.config = config
        self.initUI()
        self.blocking_status = 0
        

    def blocking_delay(self, milliseconds):
        print("blocking!")
        self.blocking_status = 1
        loop = QEventLoop()
        timer = QTimer()

        timer.timeout.connect(loop.quit)
        timer.start(milliseconds)

        loop.exec()
        self.blocking_status = 0
        print("end!")

    def initUI(self):
        self.gridLayout = QGridLayout()
        self.gridLayout.setContentsMargins(0, 0, 0, 0) 
        self.gridLayout.setSpacing(0)

        # add title to first grid row
        self.instructions = QLabel(parent=self)
        self.instructions.setStyleSheet("color: #4E8696;\n"
            "font-family: Inter;\n"
            "font-size: 30px;\n"
            "font-style: normal;\n"
            "font-weight: 400;\n"
            "line-height: normal;\n"
            "border-color: rgb(255, 255, 255);")
        self.instructions.setObjectName("instructions")
        self.instructions.setText("Find all the matching pairs!")
        self.gridLayout.addWidget(self.instructions, 0, 0, 1, 4, Qt.AlignmentFlag.AlignHCenter)

        self.cards = []

        # Initialize the cards with numbers
        for row in range(self.config.x):
            for col in range(self.config.y):
                card = QPushButton('', self)
                card.setFixedSize(100, 100)
                card.setIconSize(card.size())
                card.setStyleSheet("background-color: #F8F8FF; border: 1px solid black;")
                card.clicked.connect(self.cardClicked)
                self.gridLayout.addWidget(card, row + 1, col, Qt.AlignmentFlag.AlignHCenter)
                self.cards.append(card)
        
        self.shuffleAndHideCards()
        self.gridLayout.setContentsMargins(0, 0, 0, 0) 
        self.gridLayout.setHorizontalSpacing(0)  
        self.gridLayout.setVerticalSpacing(0)

        self.setLayout(self.gridLayout)
        self.selected_cards = []
        self.matched_pairs = 0

    def shuffleAndHideCards(self):
        
        symbols = self.config.symbols
        random.shuffle(symbols)
        for card, symbol in zip(self.cards, symbols):
            card.setIcon(QIcon())  # Clear the card
            card.setText('')
            card.symbol = symbol
            card.isVisible = False

    def cardClicked(self):
        sender = self.sender()
        if not sender.isVisible and len(self.selected_cards) < 2:
            sender.setText(sender.symbol)  # maybe use a different method if sender.symbol is not str
            sender.isVisible = True
            sender.setStyleSheet("background-color: gray;")
            self.selected_cards.append(sender)

        if len(self.selected_cards) == 2:
            self.checkMatch()

    def checkMatch(self):
        card1, card2 = self.selected_cards
        if card1.symbol == card2.symbol:
            self.matched_pairs += 1
            self.selected_cards = []
            card1.setStyleSheet("background-color: green;")
            card2.setStyleSheet("background-color: green;")

            if self.matched_pairs == self.config.pairs_for_win:
                # win msg
                self.instructions.setText("Nice one!")
                print("you win!")
                
        else:
            # Delay to let the player see the cards before hiding them
            if not blocking_status:
                self.blocking_delay(40)
                time.sleep(0.96)
                self.hideSelectedCards()

    def hideSelectedCards(self):
        for card in self.selected_cards:
            card.setText('')
            card.isVisible = False
            card.setStyleSheet("background-color: #F8F8FF; border: 1px solid black;")
        self.selected_cards = []


class LevelSelectionWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Level Selection")
        self.resize(800, 600)
        self.layout = QVBoxLayout()
        button_size = 200
        self.button_level1 = QPushButton("Level 1")
        self.button_level2 = QPushButton("Level 2")
        self.button_level3 = QPushButton("Level 3")
        
        self.button_level1.setFixedSize(button_size, button_size)
        self.button_level2.setFixedSize(button_size, button_size)
        self.button_level3.setFixedSize(button_size, button_size)
        

        self.button_level1.clicked.connect(self.show_level1)
        self.button_level2.clicked.connect(self.show_level2)
        self.button_level3.clicked.connect(self.show_level3)

        self.layout.addWidget(self.button_level1)
        self.layout.addWidget(self.button_level2)
        self.layout.addWidget(self.button_level3)
        self.setLayout(self.layout)

        self.level1_game = CardMatchingGame(ConfigCardMatching(4,4,4))
        self.level1_game.resize(200,200)
        self.level2_game = CardMatchingGame(ConfigCardMatching(4,6,6))
        self.level2_game.resize(200,200)
        self.level3_game = CardMatchingGame(ConfigCardMatching(6,6,9))
        self.level3_game.resize(200,200)

    def show_level1(self):
        self.clearLayout()
        self.layout.addWidget(self.level1_game)
        self.level1_game.show()

    def show_level2(self):
        self.clearLayout()
        self.layout.addWidget(self.level2_game)
        self.level2_game.show()

    def show_level3(self):
        self.clearLayout()
        self.layout.addWidget(self.level3_game)
        self.level3_game.show()
    
    def clearLayout(self):
        while self.layout.count():
            item = self.layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.level_selection = LevelSelectionWindow()
        self.game_level1 = CardMatchingGame(ConfigCardMatching(4,4,4))
        self.game_level2 = CardMatchingGame(ConfigCardMatching(4,6,6))
        self.game_level3 = CardMatchingGame(ConfigCardMatching(6,6,9))

        self.current_widget = self.level_selection  # Set the initial widget

        # Add the initial widget to the layout
        self.layout.addWidget(self.current_widget)
        self.setLayout(self.layout)

    def switch_to_level1(self):
        self.switch_widget(self.game_level1)

    def switch_to_level2(self):
        self.switch_widget(self.game_level2)

    def switch_to_level3(self):
        self.switch_widget(self.game_level3)

    def switch_widget(self, new_widget):
        # Remove the current widget from the layout
        self.layout.removeWidget(self.current_widget)
        self.current_widget.hide()

        # Set the new widget as the current widget
        self.current_widget = new_widget

        # Add the new widget to the layout
        self.layout.addWidget(self.current_widget)
        self.current_widget.show()


if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    config = ConfigCardMatching(6,6,6)
    game = CardMatchingGame(config)
    game.show()
    
    sys.exit(app.exec())
