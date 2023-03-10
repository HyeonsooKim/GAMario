# 03. pyqt_paint_event.py
# PyQt paint Event
import sys
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(200, 300)

        self.setWindowTitle('GA Mario')

        self.show()

    # 창이 업데이트 될 때마다 실행되는 함수
    def paintEvent(self, event):
        # 그리기 도구
        painter = QPainter()
        # 그리기 시작
        painter.begin(self)

        # QPen은 테두리
        painter.setPen(QPen(Qt.red, 2.0, Qt.SolidLine))  # 선 색, 두께, 선 모양
        # 선 그리기
        painter.drawLine(25, 150, 85, 270)

        painter.setPen(QPen(Qt.blue, 2.0, Qt.SolidLine))
        painter.drawLine(85, 150, 85, 270)

        painter.setPen(QPen(Qt.red, 2.0, Qt.SolidLine))
        painter.drawLine(145, 150, 85, 270)

        # RGB색으로 펜 설정
        painter.setPen(QPen(QColor.fromRgb(0, 0, 255), 0.5, Qt.SolidLine))
        # QBrush는 색을 채우는 역할
        painter.setBrush(QBrush(Qt.blue))
        # 직사각형
        painter.drawRect(0, 0, 50, 50)

        painter.setPen(QPen(QColor.fromRgb(0, 0, 0), 1.0, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.red))
        painter.drawRect(50, 50, 50, 50)

        painter.setPen(QPen(QColor.fromRgb(0, 0, 0), 1.0, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.red))
        painter.drawRect(50, 50, 50, 50)

        painter.setPen(QPen(QColor.fromRgb(0, 0, 0), 1.0, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.white))
        painter.drawRect(50, 0, 50, 50)

        painter.setPen(QPen(QColor.fromRgb(0, 0, 0), 1.0, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.white))
        painter.drawRect(0, 50, 50, 50)

        painter.setPen(QPen(Qt.black, 1.0, Qt.SolidLine))
        # RGB 색상으로 브러쉬 설정
        painter.setBrush(QBrush(QColor.fromRgb(150, 150, 150)))
        # 타원 그리기
        painter.drawEllipse(60, 245, 50, 50)

        painter.setPen(QPen(Qt.black, 1.0, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.cyan))
        painter.drawEllipse(0, 125, 50, 50)

        painter.setPen(QPen(Qt.black, 1.0, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.white))
        painter.drawEllipse(60, 125, 50, 50)

        painter.setPen(QPen(Qt.black, 1.0, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.cyan))
        painter.drawEllipse(120, 125, 50, 50)

        # painter.setPen(QPen(Qt.cyan, 1.0, Qt.SolidLine))
        # painter.setBrush(Qt.NoBrush)  # 채우기 색상 x
        # painter.drawText(0, 250, 'abcd')

        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())