from PyQt6.QtCore import Qt, QTimer, QEventLoop
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton
import random
import sys


def blocking_delay(milliseconds):
    loop = QEventLoop()
    timer = QTimer()

    timer.timeout.connect(loop.quit)
    timer.start(milliseconds)

    loop.exec()


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

    def initUI(self):
        self.gridLayout = QGridLayout()
        self.cards = []

        # Initialize the cards with numbers
        for row in range(self.config.x):
            for col in range(self.config.y):
                card = QPushButton('', self)
                card.setFixedSize(100, 100)
                card.setIconSize(card.size())
                card.clicked.connect(self.cardClicked)
                self.gridLayout.addWidget(card, row, col)
                self.cards.append(card)
        
        self.shuffleAndHideCards()

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
                print("you win!")
                
        else:
            # Delay to let the player see the cards before hiding them
            blocking_delay(1000)
            self.hideSelectedCards()

    def hideSelectedCards(self):
        for card in self.selected_cards:
            card.setText('')
            card.isVisible = False
            card.setStyleSheet("")
        self.selected_cards = []

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    config = ConfigCardMatching(4,6,6)
    game = CardMatchingGame(config)
    game.show()
    sys.exit(app.exec())
