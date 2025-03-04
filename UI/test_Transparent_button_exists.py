import sys, os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction, QWidget, QLabel, 
                             QVBoxLayout, QHBoxLayout, QPushButton, QMenuBar,
                             QListWidget, QSizePolicy, QGridLayout)
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import Qt, QTimer, QRect
#계속해서 수정하고 저장하면서 끝낼 완성본
#크게 수정할 일이 있을 시
#파일 저장 + 깃허브 커밋
#파일 이름 : "추가한 기능(간략하게)//제거한 기능(없을시 *)(간략하게)"
##### VS코드 닫기 전!!!
##### 최종 저장 & 깃허브 푸쉬
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        screen_rect = QApplication.desktop().screenGeometry()
        self.setGeometry(screen_rect)
        self.setWindowTitle('Delta_System')
        self.setWindowIcon(QIcon('robot_icon.png'))
        self.showMaximized()
        
        # 메뉴바 설정
        self.menu_bar = QMenuBar(self)
        file_menu = self.menu_bar.addMenu('&File')
        exit_action = QAction(QIcon('exit.png'), '&Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        self.setMenuBar(self.menu_bar)
        
        # 메인 레이아웃 설정
        main_layout = QVBoxLayout()
        
        # 시스템 로고 설정
        self.logo_label = QLabel(self)
        self.logo_pixmap = QPixmap('system_logo.png')
        self.logo_label.setPixmap(self.logo_pixmap)
        self.logo_label.setAlignment(Qt.AlignCenter)
        self.logo_label.mousePressEvent = self.refresh_system
        main_layout.addWidget(self.logo_label)
        
        # 상단 레이아웃 설정 (구상도 사진 및 옵션 버튼)
        top_layout = QHBoxLayout()
        
        # 구상도 이미지 설정
        self.assembly_label = QLabel(self)
        pixmap = QPixmap('assembly_image.jpg')
        fixed_width = 946  # 변경된 크기
        scaled_pixmap = pixmap.scaledToWidth(fixed_width, Qt.SmoothTransformation)
        self.assembly_label.setPixmap(scaled_pixmap)
        self.assembly_label.setGeometry(11, 44, scaled_pixmap.width(), scaled_pixmap.height())
        top_layout.addWidget(self.assembly_label)
        
        ##
        # # 같은 크기의 QPixmap 레이블 두 개와 크기가 같은 투명 버튼을 모두 겹쳐 하나의 레이아웃에 포함
        # label1 = QLabel(self)
        # pixmap1 = QPixmap('transport_ON.png')
        # label1.setPixmap(pixmap1)
        # label1.setAlignment(Qt.AlignCenter)

        # label2 = QLabel(self)
        # pixmap2 = QPixmap('transport_OFF.png')
        # label2.setPixmap(pixmap2)
        # label2.setAlignment(Qt.AlignCenter)

        # transparent_button = TransparentButton(self)
        # transparent_button.resize(label1.size())  # 투명 버튼의 크기를 레이블과 동일하게 설정
        # transparent_button.clicked.connect(self.buttonClicked)
        

        # layout = QVBoxLayout()
        # layout.addWidget(label1)
        # layout.addWidget(label2)
        # layout.addWidget(transparent_button)

        # top_layout.addLayout(layout)
        ##
        ###########################################################################################################
        
        options_layout = QHBoxLayout()
        self.option_buttons = [
                OptionButton('transport_ON.png', 'transport_OFF.png', 'Opt1', self),
                OptionButton('fragile_ON.png', 'fragile_OFF.png', 'Opt2', self),
                OptionButton('courier_ON.png', 'courier_OFF.png', 'Opt3', self),
            ]
        # 옵션 버튼들을 만드는 코드 부분
        for option_button in self.option_buttons:
            container = QWidget()
            layout = QVBoxLayout(container)
            layout.addWidget(option_button)

            transparent_button = TransparentButton(container)
            print(option_button.size())
            transparent_button.resize(option_button.size())
            transparent_button.clicked.connect(lambda _, b=option_button: self.toggleButton(b))
            layout.addWidget(transparent_button, 0, Qt.AlignTop)  # 투명 버튼을 옵션 버튼 위에 정확히 위치시킵니다.
            options_layout.addWidget(container)

        top_layout.addLayout(options_layout)
        
        main_layout.addLayout(top_layout)
        
        ###########################################################################################################
        
        # 중앙 레이아웃 설정 (세부항목 목록 및 장애이력)
        middle_layout = QHBoxLayout()
        
        # 장애이력 레이블 설정
        history_layout = QVBoxLayout()
        
        self.history_label = QLabel('History', self)
        self.history_label.setStyleSheet("""
            background-color: white;
            border: 2px solid black;
            border-radius: 10px;
        """)
        self.history_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)  # 크기 고정
        self.history_label.setGeometry(11, 585, 1680, 240)  # 위치와 크기 설정 (x, y, width, height)
        history_layout.addWidget(self.history_label)
        
        # 장애이력 출력 위젯 설정
        self.history_list_widget = QListWidget(self)
        self.history_list_widget.setStyleSheet("""
            background-color: white;
            border: 2px solid black;
            border-radius: 10px;
        """)
        self.history_list_widget.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)  # 크기 고정
        self.history_list_widget.setGeometry(11, 829, 1680, 860)  # 위치와 크기 설정 (x, y, width, height)
        history_layout.addWidget(self.history_list_widget)  # 장애이력 레이아웃에 위젯 추가
        
        middle_layout.addLayout(history_layout)  # 중앙 레이아웃에 장애이력 레이아웃 추가
                      
        # 첫 번째 세부항목 레이블 및 위젯 설정
        first_details_layout = QVBoxLayout()
        self.first_details_label = QLabel('First Details', self)
        self.first_details_label.setStyleSheet("""
            background-color: white;
            border: 2px solid black;
            border-radius: 10px;
        """)
        self.first_details_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)  # 크기 고정
        self.first_details_label.setGeometry(1695, 585, 1680, 240)  # 위치와 크기 설정 (x, y, width, height)
        first_details_layout.addWidget(self.first_details_label)  # 장애이력 레이아웃에 위젯 추가
        
        self.first_details_list_widget = QListWidget(self)
        self.first_details_list_widget.setStyleSheet("""
            background-color: white;
            border: 2px solid black;
            border-radius: 10px;
        """)
        self.first_details_list_widget.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)  # 크기 고정
        self.first_details_list_widget.setGeometry(1695, 829, 1680, 860)  # 위치와 크기 설정
        first_details_layout.addWidget(self.first_details_list_widget)
        
        middle_layout.addLayout(first_details_layout)
                
        # 두 번째 세부항목 레이블 및 위젯 설정
        second_details_layout = QVBoxLayout()
        self.second_details_label = QLabel('Second Details', self)
        self.second_details_label.setStyleSheet("""
            background-color: white;
            border: 2px solid black;
            border-radius: 10px;
        """)
        self.second_details_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)  # 크기 고정
        self.second_details_label.setGeometry(3379, 585, 1680, 240)  # 위치와 크기 설정 (x, y, width, height)
        second_details_layout.addWidget(self.second_details_label)
        
        self.second_details_list_widget = QListWidget(self)
        self.second_details_list_widget.setStyleSheet("""
            background-color: white;
            border: 2px solid black;
            border-radius: 10px;
        """)
        self.second_details_list_widget.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)  # 크기 고정
        self.second_details_list_widget.setGeometry(3379, 829, 1680, 860)  # 위치와 크기 설정
        second_details_layout.addWidget(self.second_details_list_widget)
        
        middle_layout.addLayout(second_details_layout)

        # 메인 레이아웃 설정
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_widget.setLayout(main_layout)

        # 중앙 레이아웃에 위젯 추가
        middle_layout.addWidget(self.history_list_widget)
        
        

        main_layout.addLayout(middle_layout)
        
        #  # 위젯 위치와 크기를 1초마다 출력하는 타이머
        # self.timer = QTimer(self)
        # self.timer.timeout.connect(self.printWidgetSizes)
        # self.timer.start(1000)  # 1초마다 실행
        
    def buttonClicked(self):
            print("Button clicked!")
            # Add your code here to handle the button click event
    
    def printWidgetSizes(self):
        # print("장애이력 위치:", self.history_label.pos())
        # print("장애이력 사이즈:", self.history_label.size())
        print("장애이력 위치:", self.history_list_widget.pos())
        print("장애이력 사이즈:", self.history_list_widget.size())
        print("왼파 세부사항 위치:", self.first_details_list_widget.pos())
        print("왼파 세부사항 사이즈:", self.first_details_list_widget.size())
        print("오른파 세부사항 위치:", self.second_details_list_widget.pos())
        print("오른파 세부사항 사이즈:", self.second_details_list_widget.size())
        
    
    def toggleButton(self, button):
        for option_button in self.option_buttons:
            if option_button != button:
                option_button.is_on = False  # 다른 버튼을 'off' 상태로 전환합니다.
                option_button.setScaledPixmap()
        button.toggle()

    def refresh_system(self, event):
        print('새로고침')
    
    # 신호에 따라 세부항목 목록에 텍스트를 추가하는 함수
    def addDetailItem(self, text):
        self.details_list_widget.addItem(text)
    
    # 장애이력에 항목을 추가하는 메서드
    def addHistoryItem(self, text):
        self.history_list_widget.addItem(text)
    
class TransparentButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFlat(True)
        self.setStyleSheet("background:transparent;")

class OptionButton(QLabel):
    def __init__(self, on_image_path, off_image_path, opt_text, parent=None):
        super().__init__(parent)
        self.on_pixmap = QPixmap(on_image_path)
        self.off_pixmap = QPixmap(off_image_path)
        self.opt_text = opt_text
        self.is_on = False
        self.setScaledPixmap()  # 최초에 비율 조정된 이미지로 설정합니다.

    def setScaledPixmap(self):
        label_size = self.size()  # QLabel의 크기를 가져옵니다.
        scaled_on_pixmap = self.on_pixmap.scaled(label_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        scaled_off_pixmap = self.off_pixmap.scaled(label_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.setPixmap(scaled_off_pixmap if not self.is_on else scaled_on_pixmap)
        self.update()

    def resizeEvent(self, event):
        self.setScaledPixmap()

    def toggle(self):
        self.is_on = not self.is_on
        self.setScaledPixmap()
        if self.is_on:
            print(self.opt_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 폰트 설정
    font = QFont('NanumSquareOTF', 9)
    app.setFont(font)
    mainWin = MainWindow()
    mainWin.showMaximized()
    mainWin.show()
    sys.exit(app.exec_())