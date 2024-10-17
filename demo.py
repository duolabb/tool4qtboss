# coding:utf-8
import sys
from PySide6.QtCore import QEasingCurve, Qt
from PySide6.QtWidgets import QApplication, QWidget, QPushButton

from qfluentwidgets import VBoxLayout, FlowLayout, PushButton, PrimaryPushButton


class Demo(QWidget):

    def __init__(self):
        super().__init__()
        layout = VBoxLayout(self)

        layout.setContentsMargins(30, 30, 30, 30)

        child_layout = VBoxLayout(self)
    
        child_layout.addWidget(PushButton('按钮1'))  
        child_layout.addWidget(PushButton('按钮2'))  
        child_layout.addWidget(PushButton('按钮3'))

        container = QWidget()
        container.setLayout(child_layout)
        layout.addWidget(container)

        layout.addWidget(PushButton('aiko'))
        layout.addWidget(PushButton('刘静爱'))
        layout.addWidget(PushButton('柳井爱子'))
        layout.addWidget(PushButton('aiko 赛高'))
        layout.addWidget(PushButton('aiko 太爱啦😘'))

        layout.insertWidget(1, PrimaryPushButton('西宫硝子'))

        self.resize(250, 300)
        self.setStyleSheet('Demo{background: white} QPushButton{padding: 5px 10px; font:15px "Microsoft YaHei"}')


if __name__ == '__main__':
    # enable dpi scale
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

    app = QApplication(sys.argv)
    w = Demo()
    w.show()
    app.exec()
