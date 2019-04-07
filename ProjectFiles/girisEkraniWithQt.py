import sys
from PyQt5.QtWidgets import *
app = QApplication(sys.argv)
window = QWidget()
layout = QVBoxLayout()
layout.addWidget(QPushButton('Başla'),)
layout.addWidget(QPushButton('Bitir'))
layout.addWidget(QPushButton('Puan Tablosu'))
window.setLayout(layout)
window.show()
sys.exit(app.exec_())
