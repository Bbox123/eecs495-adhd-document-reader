from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton
import random

class CardMatchingGame(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.gridLayout = QGridLayout()
        self.cards = []

        # Initialize the cards with numbers
        for row in range(4):
            for col in range(4):
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
        
        symbols = ['1', '1', '2', '2', '3', '3', '4', '4','1', '1', '2', '2', '3', '3', '4', '4']
        random.shuffle(symbols)
        for card, symbol in zip(self.cards, symbols):
            card.setIcon(QIcon())  # Clear the card
            card.setText('')
            card.symbol = symbol
            card.isVisible = False

    def cardClicked(self):
        sender = self.sender()
        if not sender.isVisible and len(self.selected_cards) < 2:
            sender.setText(sender.symbol)
            sender.isVisible = True
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

            if self.matched_pairs == 8:
                # win msg
                
                pass
        else:
            # Delay to let the player see the cards before hiding them
            QTimer.singleShot(1000, self.hideSelectedCards)

    def hideSelectedCards(self):
        for card in self.selected_cards:
            card.setText('')
            card.isVisible = False
        self.selected_cards = []

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    game = CardMatchingGame()
    game.show()
    sys.exit(app.exec())
