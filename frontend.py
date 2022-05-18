import requests.exceptions
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import os
from backend import PornBlocker, TimedBlocker
from datetime import datetime as dt
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDateTime
import sys
from qt_material import apply_stylesheet
from date_time_functions import DateTimeFunctions


class Ui_MainWindow(object):
    porn_blocker_is_activated = None

    @staticmethod
    def createPopup(title, text, icon):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setIcon(icon)
        msg.exec_()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(644, 519)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 801, 701))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        # self.tabWidget.setStyleSheet("background-color:#1d212d; color: #ffffff")
        self.tabWidget.setObjectName("tabWidget")
        self.adult_content_blocker_tab = QtWidgets.QWidget()
        self.adult_content_blocker_tab.setObjectName("adult_content_blocker_tab")
        self.activate_btn = QtWidgets.QPushButton(self.adult_content_blocker_tab)
        self.activate_btn.setEnabled(True)
        self.activate_btn.setGeometry(QtCore.QRect(250, 370, 110, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.activate_btn.setFont(font)
        self.activate_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.activate_btn.setMouseTracking(False)
        self.activate_btn.setFocusPolicy(QtCore.Qt.StrongFocus)
        # self.activate_btn.setStyleSheet("background-color: #286779;")
        self.activate_btn.setCheckable(False)
        self.activate_btn.setObjectName("activate_btn")
        self.porn_datetimeedit = QtWidgets.QDateTimeEdit(self.adult_content_blocker_tab)
        self.porn_datetimeedit.setGeometry(QtCore.QRect(70, 290, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.porn_datetimeedit.setFont(font)
        # self.porn_datetimeedit.setStyleSheet("color:#af7bd5")
        self.porn_datetimeedit.setObjectName("porn_datetimeedit")
        self.deactivate_btn = QtWidgets.QPushButton(self.adult_content_blocker_tab)
        self.deactivate_btn.setGeometry(QtCore.QRect(250, 420, 110, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.deactivate_btn.setFont(font)
        self.deactivate_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # self.deactivate_btn.setStyleSheet("background-color:#ab6161;")
        self.deactivate_btn.setObjectName("deactivate_btn")
        self.porn_banned_until_label = QtWidgets.QLabel(self.adult_content_blocker_tab)
        self.porn_banned_until_label.setGeometry(QtCore.QRect(70, 250, 280, 41))
        font = QtGui.QFont()
        font.setFamily("HoloLens MDL2 Assets")
        font.setBold(True)
        font.setWeight(75)
        self.porn_banned_until_label.setFont(font)
        self.porn_banned_until_label.setStyleSheet("color:#6ca2ce")
        self.porn_banned_until_label.setObjectName("porn_banned_until_label")
        self.stop_image_label = QtWidgets.QLabel(self.adult_content_blocker_tab)
        self.stop_image_label.setGeometry(QtCore.QRect(20, 10, 251, 241))
        self.stop_image_label.setText("")
        self.stop_image_label.setPixmap(QtGui.QPixmap("res/icon.ico"))
        self.stop_image_label.setObjectName("stop_image_label")
        self.no_more_porn_label = QtWidgets.QLabel(self.adult_content_blocker_tab)
        self.no_more_porn_label.setGeometry(QtCore.QRect(280, 80, 311, 81))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.no_more_porn_label.setFont(font)
        self.no_more_porn_label.setStyleSheet("color:#6ca2ce")
        self.no_more_porn_label.setObjectName("no_more_porn_label")
        self.status_label = QtWidgets.QLabel(self.adult_content_blocker_tab)
        self.status_label.setGeometry(QtCore.QRect(390, 260, 81, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.status_label.setFont(font)
        self.status_label.setStyleSheet("color:#78aad6")
        self.status_label.setObjectName("status_label")
        self.activated_deactivated_label = QtWidgets.QLabel(self.adult_content_blocker_tab)
        self.activated_deactivated_label.setGeometry(QtCore.QRect(390, 300, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.activated_deactivated_label.setFont(font)
        self.activated_deactivated_label.setStyleSheet("color:#D41D21;")
        self.activated_deactivated_label.setObjectName("activated_deactivated_label")
        self.porn_mm__dd_yyyy = QtWidgets.QLabel(self.adult_content_blocker_tab)
        self.porn_mm__dd_yyyy.setGeometry(QtCore.QRect(70, 330, 111, 41))
        font = QtGui.QFont()
        font.setFamily("HoloLens MDL2 Assets")
        font.setBold(True)
        font.setWeight(75)
        self.porn_mm__dd_yyyy.setFont(font)
        self.porn_mm__dd_yyyy.setStyleSheet("color:#6ca2ce")
        self.porn_mm__dd_yyyy.setObjectName("porn_mm__dd_yyyy")
        self.porn_mm__dd_yyyy.raise_()
        self.activated_deactivated_label.raise_()
        self.stop_image_label.raise_()
        self.activate_btn.raise_()
        self.deactivate_btn.raise_()
        self.porn_banned_until_label.raise_()
        self.no_more_porn_label.raise_()
        self.status_label.raise_()
        self.porn_datetimeedit.raise_()
        self.tabWidget.addTab(self.adult_content_blocker_tab, "")
        self.website_blocker_tab = QtWidgets.QWidget()
        self.website_blocker_tab.setObjectName("website_blocker_tab")
        self.website_url_label = QtWidgets.QLabel(self.website_blocker_tab)
        self.website_url_label.setGeometry(QtCore.QRect(10, 40, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.website_url_label.setFont(font)
        self.website_url_label.setStyleSheet("color:#458bff")
        self.website_url_label.setObjectName("website_url_label")
        self.lineEdit = QtWidgets.QLineEdit(self.website_blocker_tab)
        self.lineEdit.setGeometry(QtCore.QRect(110, 40, 521, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        # self.lineEdit.setStyleSheet("color:#30d224")
        self.lineEdit.setObjectName("lineEdit")
        self.website_datetimeedit = QtWidgets.QDateTimeEdit(self.website_blocker_tab)
        self.website_datetimeedit.setGeometry(QtCore.QRect(190, 180, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.website_datetimeedit.setFont(font)
        # self.website_datetimeedit.setStyleSheet("color:#af7bd5")
        self.website_datetimeedit.setObjectName("website_datetimeedit")
        self.block_btn = QtWidgets.QPushButton(self.website_blocker_tab)
        self.block_btn.setEnabled(True)
        self.block_btn.setGeometry(QtCore.QRect(270, 340, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.block_btn.setFont(font)
        self.block_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.block_btn.setMouseTracking(False)
        self.block_btn.setFocusPolicy(QtCore.Qt.StrongFocus)
        # self.block_btn.setStyleSheet("background-color: #286779;")
        self.block_btn.setCheckable(False)
        self.block_btn.setObjectName("block_btn")
        self.unblock_btn = QtWidgets.QPushButton(self.website_blocker_tab)
        self.unblock_btn.setGeometry(QtCore.QRect(270, 390, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.unblock_btn.setFont(font)
        self.unblock_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # self.unblock_btn.setStyleSheet("background-color:#ab6161;")
        self.unblock_btn.setObjectName("unblock_btn")
        self.website_banned_until_label = QtWidgets.QLabel(self.website_blocker_tab)
        self.website_banned_until_label.setGeometry(QtCore.QRect(190, 140, 231, 41))
        font = QtGui.QFont()
        font.setFamily("HoloLens MDL2 Assets")
        font.setBold(True)
        font.setWeight(75)
        self.website_banned_until_label.setFont(font)
        self.website_banned_until_label.setStyleSheet("color:#458bff")
        self.website_banned_until_label.setObjectName("website_banned_until_label")
        self.blocked_unblocked_label = QtWidgets.QLabel(self.website_blocker_tab)
        self.blocked_unblocked_label.setGeometry(QtCore.QRect(190, 270, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.blocked_unblocked_label.setFont(font)
        # self.blocked_unblocked_label.setStyleSheet("color:#30d224;")
        self.blocked_unblocked_label.setObjectName("blocked_unblocked_label")
        self.website_mm__dd_yyyy = QtWidgets.QLabel(self.website_blocker_tab)
        self.website_mm__dd_yyyy.setGeometry(QtCore.QRect(190, 220, 111, 41))
        font = QtGui.QFont()
        font.setFamily("HoloLens MDL2 Assets")
        font.setBold(True)
        font.setWeight(75)
        self.website_mm__dd_yyyy.setFont(font)
        self.website_mm__dd_yyyy.setStyleSheet("color:#458bff")
        self.website_mm__dd_yyyy.setObjectName("website_mm__dd_yyyy")
        self.website_mm__dd_yyyy.raise_()
        self.website_banned_until_label.raise_()
        self.website_url_label.raise_()
        self.lineEdit.raise_()
        self.website_datetimeedit.raise_()
        self.block_btn.raise_()
        self.unblock_btn.raise_()
        self.blocked_unblocked_label.raise_()
        self.tabWidget.addTab(self.website_blocker_tab, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.listWidget = QtWidgets.QListWidget(self.tab)
        self.listWidget.setGeometry(QtCore.QRect(5, 5, 631, 481))
        # self.listWidget.setStyleSheet("color:#6ca2ce;font-size:14px;")
        self.listWidget.setObjectName("listWidget")
        self.tabWidget.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self.porn_blocker_is_activated = os.path.isfile(TimedBlocker.porn_ban_time_file)

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Weblocker"))
        self.activate_btn.setText(_translate("MainWindow", "Activate "))
        self.deactivate_btn.setText(_translate("MainWindow", "Deactivate"))
        self.porn_banned_until_label.setText(
            _translate("MainWindow", "Set the date and time\nto block adult sites till that date."))
        self.no_more_porn_label.setText(_translate("MainWindow", "Say NO to porn"))
        self.status_label.setText(_translate("MainWindow", "status"))

        if self.porn_blocker_is_activated:
            self.activated_deactivated_label.setText("Activated")
            self.activated_deactivated_label.setStyleSheet("color:#30d224;")
        else:
            self.activated_deactivated_label.setText(_translate("MainWindow", "Deactivated"))

        self.porn_mm__dd_yyyy.setText(_translate("MainWindow", "mm/dd/yyyy"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.adult_content_blocker_tab),
                                  _translate("MainWindow", "Adult content blocker"))
        self.website_url_label.setText(_translate("MainWindow", "Website url:"))
        self.block_btn.setText(_translate("MainWindow", "Block"))
        self.unblock_btn.setText(_translate("MainWindow", "Unblock"))
        self.website_banned_until_label.setText(_translate("MainWindow", "Set the date and time\nto block this website till that date."))
        self.blocked_unblocked_label.setText(_translate("MainWindow", ""))
        self.website_mm__dd_yyyy.setText(_translate("MainWindow", "mm/dd/yyyy          "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.website_blocker_tab),
                                  _translate("MainWindow", "Website blocker"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Blocked websites list"))

        self.activate_btn.clicked.connect(self.activate_porn_blocker)
        self.deactivate_btn.clicked.connect(self.deactivate_porn_blocker)
        self.block_btn.clicked.connect(self.block_the_site)
        self.unblock_btn.clicked.connect(self.unblock_the_site)

        now = dt.now()
        self.porn_datetimeedit.setDateTime(QDateTime(now.year, now.month, now.day, (now.hour + 8), now.minute))
        self.website_datetimeedit.setDateTime(QDateTime(now.year, now.month, now.day, (now.hour + 8), now.minute))

        if os.path.isfile(TimedBlocker.web_ban_time_file):
            site = TimedBlocker.read_json(TimedBlocker.web_ban_time_file)
            for x in site.keys():
                self.listWidget.addItem(x)

    def activate_porn_blocker(self):
        if not os.path.isfile(f"{PornBlocker.hostfile}_copy"):
            PornBlocker.make_copy_of_hostfile()

        if not self.porn_blocker_is_activated:
            # if porn blocker is not activated
            strdatetime = self.porn_datetimeedit.text()
            now = dt.now()
            porn_ban_datetime = DateTimeFunctions.strdatetime_to_datetime(strdatetime)
            present_datetime = dt(now.year, now.month, now.day, now.hour, now.minute)

            if porn_ban_datetime > present_datetime:
                # if the datetime sat in QdatetimeEdit is greater than present datetime
                TimedBlocker.block_porn_sites_until(strdatetime)
                self.activated_deactivated_label.setText("Activated")
                self.activated_deactivated_label.setStyleSheet("color:#30d224;")
                self.porn_blocker_is_activated = True
                return
            # print('Invalid DateTime')
            self.createPopup('Invalid date/time',
                             'Provided date/time is less than present date/time.\nPlease increase the date/time.',
                             QMessageBox.Critical)
            return
        # print('Porn blocker is already active.')
        self.createPopup('Already activated', 'Porn blocker is already activated.', QMessageBox.Information)

    def deactivate_porn_blocker(self):
        if self.porn_blocker_is_activated:
            strdatetime = TimedBlocker.read_json(TimedBlocker.porn_ban_time_file)['datetime']
            pornbandatetime = DateTimeFunctions.strdatetime_to_datetime(strdatetime)

            try:
                presentdatetime = DateTimeFunctions.fetch_datetime()

                if presentdatetime >= pornbandatetime:
                    # if present datetime is greater than pornban datetime
                    TimedBlocker.unblock_porn_sites()
                    self.activated_deactivated_label.setText("Deactivated")
                    self.activated_deactivated_label.setStyleSheet("color:#D41D21;")
                    self.porn_blocker_is_activated = False

                else:
                    # print(f'You need to wait "{pornbandatetime - presentdatetime} hrs" to unblock porn sites.')
                    remaining_time = str(pornbandatetime - presentdatetime)
                    remaining_days = ''
                    if len(remaining_time) > 8:
                        remaining_days, _time = remaining_time.split(',')
                        hrs, mins, secs = _time.split(':')
                    else:
                        hrs, mins, secs = remaining_time.split(':')
                    self.createPopup('cannot unblock now',
                                     f'''You blocked pornsites until "{strdatetime}".
                    So, you need to wait "{remaining_days}, {hrs} hrs, {mins} mins" to unblock porn sites.''',
                                     QMessageBox.Information)

            except requests.exceptions.ConnectionError:
                self.createPopup('No internet connection',
                                 'Your device is not connected to the internet.\nPlease connect to a internet connection first.',
                                 QMessageBox.Critical)
        else:
            # print('Porn blocker is not activated yet.')
            self.createPopup('Inactive', 'Porn blocker is not activated yet.', QMessageBox.Information)

    def block_the_site(self):
        strdatetime = self.website_datetimeedit.text()
        now = dt.now()
        web_ban_datetime = DateTimeFunctions.strdatetime_to_datetime(strdatetime)
        present_datetime = dt(now.year, now.month, now.day, now.hour, now.minute)

        if web_ban_datetime > present_datetime:
            weburl = self.lineEdit.text()
            if len(weburl) >= 3 and '.' in weburl:
                TimedBlocker.block_a_web_until(weburl, strdatetime)

                self.blocked_unblocked_label.setText('Block successful')
                self.blocked_unblocked_label.setStyleSheet("color:#30d224;")
                self.listWidget.addItem(weburl)
                self.lineEdit.setText('')
                return
            # print('Invalid URl.')
            self.createPopup('Invalid URL', 'Provided url is incorrect', QMessageBox.Critical)
            return
        # print('Invalid DateTime')
        self.createPopup('Invalid date/time',
                         'Provided date/time is less than present date/time.\nPlease increase the date/time.',
                         QMessageBox.Critical)

    def unblock_the_site(self):
        website = self.lineEdit.text()
        if os.path.isfile(TimedBlocker.web_ban_time_file):
            web_json_data = TimedBlocker.read_json(TimedBlocker.web_ban_time_file)

            if website in web_json_data:
                strdatetime = web_json_data.get(website)
                webbandatetime = DateTimeFunctions.strdatetime_to_datetime(strdatetime)

                try:
                    presentdatetime = DateTimeFunctions.fetch_datetime()

                    if presentdatetime > webbandatetime:
                        TimedBlocker.unblock_a_web(website)
                        self.blocked_unblocked_label.setText('Unblock successful')
                        self.blocked_unblocked_label.setStyleSheet("color:#D41D21;")
                        self.lineEdit.setText('')
                        self.listWidget.clear()
                        if os.path.isfile(TimedBlocker.web_ban_time_file):
                            site = TimedBlocker.read_json(TimedBlocker.web_ban_time_file)
                            for x in site.keys():
                                self.listWidget.addItem(x)
                    else:
                        # print(f'You need to wait "{webbandatetime - presentdatetime} hrs" to unblock this website.')

                        def get_remaining_time():
                            remaining_time = str(webbandatetime - presentdatetime)
                            _days = ''
                            if len(remaining_time) > 8:
                                _days, _time = remaining_time.split(',')
                                _hrs, _mins, _secs = _time.split(':')
                            else:
                                _hrs, _mins, _secs = remaining_time.split(':')

                            return (_days, _hrs, _mins)

                        remaining_days, hrs, mins = get_remaining_time()

                        self.createPopup('cannot unblock now', f'''You blocked this website until "{strdatetime}".
    So, you need to wait "{remaining_days}, {hrs} hrs, {mins} mins" to unblock it.''',
                                         QMessageBox.Information)
                except requests.exceptions.ConnectionError:
                    self.createPopup('No internet connection',
                                     'Your device is not connected to the internet.\nPlease connect to a internet connection first.',
                                     QMessageBox.Critical)
            else:
                # print('Website not present in block list.')
                self.createPopup('404 not found',
                                 '''Provided url is not present in the blocklist. 
Please see the blocked websites list in next tab and try again.''',
                                 QMessageBox.Critical)


def start_app():
    app = QtWidgets.QApplication(sys.argv)
    apply_stylesheet(app, 'dark_blue.xml')
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setWindowIcon(QIcon('res/icon.ico'))
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    pass
