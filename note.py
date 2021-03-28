print('Load modules...')
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from threading import Thread
import urllib, sys, random, os, SQLEasy, time, json, datetime, requests, traceback, webbrowser
import authwindow, journal, createGroup, createObject, taskInfo, editTask, LangChoose  # Интерфейсы
import updater
print('Finished.')

Supported_DataBaseVersion = '1.1'
programVersion = '1.1'
DataBase = SQLEasy.database('database.db')
DBVersion_code = updater.checkVersion(DataBase, Supported_DataBaseVersion)

localeData = {
    'langVersion_from': Supported_DataBaseVersion,
    'systemLang': 'en_ES',
    'machineTranslation': 0,
    'EnglishName': 'English',
    'LocaleName': 'English',
    'allow_allSymbols': 0,
    'warnMesTitle': 'Warning!',
    'oldestVersionMessage': 'An outdated version of the database was detected. Requires the update to continue?',
    'futureVersionMessage': 'An unsupported version of the database was detected. An attempt will be made to import the data. Continue?',
    'copyLog': 'Copy in',
    'mkdirLog': 'Creating folder',
    'chLang_title': 'Choose lang',
    'chLang': 'Choose your language',
    'machineTranslationAlert': 'Machine translation is present',
    'continue': 'Continue',
    'progamName': 'Student manager',  # Студенческий планировщик
    'journalTitle': 'Journal of',  # Журнал
    # (!) Сделать потом
    'authTitle': 'Authorization',  # Авторизация
    'loginText': 'Login',  # Логин
    'progrUpdateTitle': 'Application update',  # Обновление программы
    'progrUpdateMessage': 'An app update came out, don\'t want to update?',  # Вышло обновление программы, не хотите обновиться?
    'dataUpd_message': 'Data was been updated.',  # Данные были обновлены.
    'middleNameText': 'Last name',  # Фамлия
    'apply': 'Apply',  # Применить
    'failedConnection': 'No network connection.\nNetwork services are not available',  # Отстутствует подключение к сети. Сетевые службы недоступны
    'nameText': 'Name',  # Имя
    'sectionGroup': 'Group',  # Группа
    'in_developing_txt': 'In developing',  # В разработке
    'info_abTask': 'Information about task',  # Информация о задании
    'logIn_Text': 'LogIn',  # Войти
    'auth_act': 'Log In',  # Авторизоваться
    'regText': 'Registration',  # Регистрация
    'passwordText': 'Password',  # Пароль
    'professor': 'Professor',  # Преподаватель
    'showPassword': 'Show password',  # Показать пароль
    'len_description_Alert': 'Enter more than four characters in the "task Content" column!!!',  # Введите больше четырёх символов в графу "Содержание задания"!!!
    'logoutConfirmation': 'Are you sure you want to log out of this account?',  # Вы точно хотите выйти с этого аккаунта?
    'updateTitleProgram': 'Database update manager',  # Менеджер обновления базы данных
    'subjectTranslate': 'Subject',  # Предмет
    'subjectAdd': 'Lesson was been added',  # Предмет добавлен!
    'noLessons_descrAlert': 'There are no created disciplines. Create a discipline.',  # Нет созданных дисциплин. Создайте дисциплину.
    'groupTitle_of_app': 'group of',  # Группа
    'authError': 'Authorization failed.',  # Авторизация неудалась.
    'unc_passwordError': 'Invalid password.',  # Неверный пароль.
    'unc_loginError': 'Invalid login.',  # Неверный логин.
    'passwordError': 'Enter password.',  # Введите пароль.
    'openDatabaseLog': 'Open database',
    'addGroup': 'Group was been added.',  # Группа - добавлена
    'copyData_inBuffer_Log': 'Copying table data to the buffer',  # Копирование в буфер данных таблиц
    'complLogin': 'You have successfully logged in as',  # Вы успешно вошли как
    'deadlineText': 'Deadline:',  # Срок сдачи: до
    'short_deadlineText': 'Deadline:',  # Срок: до
    'copyDataLog': 'Copying data',  # Копирование данных
    'addAccount_message': 'Account was been added',  # Аккаунт добавлен
    'successAlert': 'Successfully!',  # Успех!
    'okay': 'OK',  # OK
    'delTask': 'Delete task',  # Удалить задание
    'editText': 'edit',  # ред.
    'errorAlert': 'Error.',  # Ошибка.
    'login_inDB_Error': 'This username is already in the database.',  # Данный логин уже есть в базе данных.
    'taskAdd': 'Task was been added.',  # Задание добавлено.
    'exceptionAlert_msg': 'Program was been terminated this exception:',  # Программа завершила свою работу со следующей ошибкой:
    'fromLog': 'from',  # из
    'ageTxt': 'Age',  # Полных лет
    'activateDarkTheme': 'Dark theme on',  # Включить тёмную тему
    'addTask': 'Add task',  # Добавить задание
    'tasks_txt': 'Tasks',  # Задания
    'textGeneral': 'General',  # Основное
    'add_text': 'Add',  # Добавить
    'deadline': 'Deadline:',  # Сделать до
    'start_notifying': 'Start notifying',  # Начать упоминать
    'shortStart_notifying': 'Show in',  # Отображение
    'task_descr': 'Task content',  # Содержание задания
    'group_t': 'Group:',  # Группа:
    'newPassword': 'New passsword',  # Новый пароль
    'resetPassword': 'Reset your password',  # Сбросить пароль
    'settings': 'Settings',  # Настройки
    'direction': 'Profession',  # Направление
    'networkSettings_section': 'Network settings',  # Настройка сетевого подключения
    'data_editionAlert': 'Are you sure you want to change the data?',  # Вы уверены, что хотите изменить данные?
    'securitySection': 'Security',  # Безопасноть
    'unlock': 'Unlock',  # Разблокировать
    'createProfileButton': 'Create profile',  # Создать профиль
    'curatorName': 'Curator\'s name',  # Имя куратора
    'profName': 'Professor\'s name',  # Имя преподавателя
    'subjName': 'Subject',  # Название предмета
    'subjDescr': 'Subject description',  # Описание предмета
    'createGroup': 'Create group',  # Создать группу
    'createSubject': 'Create subject',  # Создать предмет
    'deletedTask_message': 'Task was been deleted.',  # Задание было успешно удалено.
    'deleteTask_message': 'Do you want to delete this task?',  # Вы действительно хотите удалить данное задание?
    'wantProtect': 'Protect my profile with a password',  # Я хочу защитить профиль паролем
    'passsword': 'Password',  # Пароль
    'show_passsword': 'Show password',  # Показать пароль
    'passwReseted': 'Your password was been reseted',  # Ваш пароль был сброшен!
    'passwEdited': 'Your password was been edited',  # Ваш пароль был изменён!
    'typeOf_training': 'Type of training',  # Обучение...
    'budget': 'Budget',  # Бюджет
    'сommerce': 'Commerce',  # Контракт
    'currentTasks': 'Current tasks',  # Текущие задания
    'completeTask': 'Completed',  # Выполнено
    'course': 'Course',  # Курс
    'groupName': 'Group name',  # Название группы
    'hereLearn': 'Full-time',  # Очно
    'distantLearn': 'In absentia',  # Заочно
    'saveText': 'Save',  # Сохранить
    'cancelText': 'Cancel',  # Отмена
    'createButton': 'Create',  # Создать
    'requestError': 'Request denied',  # Запрос отклонён.
    # 'rewriteFormsAlert': 'All form data after recording is not subject to rewriting. Continue?',  # Все данные формы после записи перезаписи - не подлежат. Продолжить?
    'rewriteFormsAlert': 'Do you really want to create a profile?',  # Вы действительно хотите создать профиль?
    'openTableLog': 'Opening table',  # Открытие таблицы
    'exit': 'Exit',  # Выйти
    'upDated_alert': 'Your data has been transferred to a new version of the Database, click "Finish", after which the program will close.'  # Ваши данные были перенесены на новую версию Базы Данных, нажмите "Завершить", после чего, программа закроется.
}


def getTimeObject(timeUNIX):
    Time = str(datetime.datetime.utcfromtimestamp(timeUNIX).strftime('%Y_%m_%d_%H_%M_%S'))
    Time = Time.split('_')
    years = int(Time[0])
    months = int(Time[1])
    days = int(Time[2])
    return QDate(years, months, days)


def getCorret_login(login):
    formatedLogin = ''
    for symbol in login:
        if symbol in '_-1234567890qwertyuiopasdfghjklzxcvbnm' + 'qwertyuiopasdfghjklzxcvbnm'.upper():
            formatedLogin += symbol
    if len(formatedLogin) > 32:
        formatedLogin = formatedLogin[:32]
    return formatedLogin


def getCorret_password(login):
    formatedLogin = ''
    for symbol in login:
        if symbol in '_1234567890qwertyuiopasdfghjklzxcvbnm' + 'qwertyuiopasdfghjklzxcvbnm'.upper():
            formatedLogin += symbol
    if len(formatedLogin) > 64:
        formatedLogin = formatedLogin[:64]
    return formatedLogin


class app_win(QMainWindow):
    def chooseLingua(self, *args):
        self.chooseLang = QMainWindow()
        super(app_win, self).__init__()
        self.chooseLang_ui = LangChoose.Ui_Form()
        self.chooseLang_ui.setupUi(self.chooseLang)
        self.chooseLang.setMouseTracking(True)
        self.chooseLang.show()
        # Иницилизация языков
        self.langs = DataBase.getBase('langs')
        for langObj in self.langs:
            self.chooseLang_ui.set_lang.addItem(f"{langObj['LocaleName']} ({langObj['EnglishName']})")
        self.langObj = self.langs[self.chooseLang_ui.set_lang.currentIndex()]
        # Запуск таймера
        self.qtimer = QTimer()
        self.qtimer.timeout.connect(self.langCorrect)
        self.qtimer.start(1)
        # Завершение выбора
        self.chooseLang_ui.cont.clicked.connect(lambda: self.endChoose(*args))
    
    def endChoose(self, *args):
        DataBase.setItem(DatabaseName='applicationData', key='ActiveLingua', newValue=self.langObj['ID'], indexKey='Num', value=1)
        self.localeData = getLocale_data(DataBase, self.localeData)
        args = list(args)
        args[1] = self.localeData
        self.qtimer.stop()
        self.__init__(*args)
        self.globalEdit_localeData()
    
    def globalEdit_localeData(self):
        global localeData
        localeData = self.localeData
    
    def langCorrect(self):
        self.langObj = self.langs[self.chooseLang_ui.set_lang.currentIndex()]
        self.chooseLang.setWindowTitle(self.langObj['chLang_title'])
        if self.langObj['machineTranslation']:
            self.chooseLang_ui.machineTranslation_warn.setText(self.langObj['machineTranslationAlert'])
        else:
            self.chooseLang_ui.machineTranslation_warn.setText('')
        self.chooseLang_ui.label.setText('<html><head/><body><p align="center"><span style=" font-size:12pt;">%s</span></p></body></html>' % self.langObj['chLang'])
        self.chooseLang_ui.cont.setText(self.langObj['continue'])
    
    def __init__(self, app, localeData, internet):
        self.qtimer = QTimer()
        self.timer = QTimer()
        
        self.localeData = localeData
        self.app = app
        self.internetConnection = internet
        # Окна
        self.mainmenu = QMainWindow()     # Главное меню приложения
        self.createGroup = QMainWindow()  # Меню создания группы
        self.chooseLang = QMainWindow()   # Меню выбора языка
        
        # Тёмная тема, реализация
        self.darkThemeOn = bool(DataBase.getBase(DatabaseName='applicationData')[0]['activeTheme'])
        '''
        self.defaultTheme = QPalette()
        
        self.darkTheme = QPalette()
        self.darkTheme.setColor(QPalette.Window, QColor(53, 53, 53))
        self.darkTheme.setColor(QPalette.WindowText, Qt.white)
        self.darkTheme.setColor(QPalette.Base, QColor(25, 25, 25))
        self.darkTheme.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        self.darkTheme.setColor(QPalette.ToolTipBase, Qt.black)
        self.darkTheme.setColor(QPalette.ToolTipText, Qt.white)
        self.darkTheme.setColor(QPalette.Text, Qt.white)
        self.darkTheme.setColor(QPalette.Button, QColor(53, 53, 53))
        self.darkTheme.setColor(QPalette.ButtonText, Qt.white)
        self.darkTheme.setColor(QPalette.BrightText, Qt.red)
        self.darkTheme.setColor(QPalette.Link, QColor(42, 130, 218))
        self.darkTheme.setColor(QPalette.Highlight, QColor(42, 130, 218))
        self.darkTheme.setColor(QPalette.HighlightedText, Qt.black)
        
        if self.darkThemeOn:
            self.app.setPalette(self.darkTheme)
        '''
        if self.darkThemeOn:
            self.app.setStyleSheet(DataBase.getBase('styles')[1]['Style'])
        # Иницилизация окна
        super(app_win, self).__init__()
        self.authwindow_ui = authwindow.Ui_Form(self.localeData)
        self.authwindow_ui.setupUi(self)
        self.setMouseTracking(True)
        if DataBase.getBase(DatabaseName='applicationData')[0]['ActiveLingua'] in (None, -1):
            self.chooseLingua(app, localeData, internet)
        elif DataBase.getBase(DatabaseName='applicationData')[0]['activeProfile'] is None:
            self.authCode = 0
            
            self.show()
            self.authwindow_ui.applyDarkTheme.setChecked(self.darkThemeOn)
            # Пропишем список студентов
            self.authwindow_ui.userList.clear()
            for student in DataBase.getBase(DatabaseName='profiles'):
                self.authwindow_ui.userList.addItem(f"{student['name']} '{student['Username']}' {student['middleName']}, {self.localeData['groupTitle_of_app']} {SQLEasy.compareKey(DataBase.getBase(DatabaseName='groups'), 'ID')[student['GroupClass']]['name']}")
                
            
            for group in DataBase.getBase(DatabaseName='groups'):
                self.authwindow_ui.set_group.addItem(f"{group['name']} ({group['curatorName']})")
            # Реализуем кнопки и клики
            self.authwindow_ui.applyDarkTheme.clicked.connect(self.editDTheme)
            self.authwindow_ui.createAccount.clicked.connect(self.register)
            self.authwindow_ui.auth.clicked.connect(self.auth)
            self.authwindow_ui.auth.clicked.connect(self.hideMain)
            self.authwindow_ui.addGroup.clicked.connect(self.create_group)
            self.authwindow_ui.userList.clicked.connect(self.autoset_field)
            # Запустим QTimer для правки текста
            self.timer = QtCore.QTimer(self)
            self.timer.timeout.connect(self.autoReplaceFields)
            self.timer.start(1)
            
        else:
            self.go_to_MainMenu()
    
    def hideMain(self):
        if self.authCode == 1:
            self.hide()
    
    def autoset_field(self):
        if self.authwindow_ui.userList.currentRow() != -1:
            self.authwindow_ui.usernameEnter.setText(DataBase.getBase('profiles')[self.authwindow_ui.userList.currentRow()]['Username'])
 
    def autoReplaceFields(self):
        self.authwindow_ui.usernameEnter.setText(getCorret_login(self.authwindow_ui.usernameEnter.text()))
        self.authwindow_ui.login.setText(getCorret_login(self.authwindow_ui.login.text()))
        
        self.authwindow_ui.passwordEnter.setText(getCorret_password(self.authwindow_ui.passwordEnter.text()))
        self.authwindow_ui.passwordEnter_2.setText(getCorret_password(self.authwindow_ui.passwordEnter_2.text()))
        
        self.authwindow_ui.passwordEnter_2.setEnabled(self.authwindow_ui.applyPassword.isChecked())
        
        if self.authwindow_ui.showPassword.isChecked():
            self.authwindow_ui.passwordEnter.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.authwindow_ui.passwordEnter.setEchoMode(QtWidgets.QLineEdit.Password)
        
        if self.authwindow_ui.showPassword_2.isChecked():
            self.authwindow_ui.passwordEnter_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.authwindow_ui.passwordEnter_2.setEchoMode(QtWidgets.QLineEdit.Password)
        
        if self.authwindow_ui.applyPassword.isChecked():
            self.authwindow_ui.createAccount.setEnabled(
                len(self.authwindow_ui.set_group) > 0 and 
                len(self.authwindow_ui.login.text()) > 3 and 
                len(self.authwindow_ui.passwordEnter_2.text()) >= 8 and
                len(self.authwindow_ui.name.text()) > 0 and
                len(self.authwindow_ui.middleName.text()) > 0
            )
        else:
            self.authwindow_ui.createAccount.setEnabled(
                len(self.authwindow_ui.set_group) > 0 and 
                len(self.authwindow_ui.login.text()) > 3 and 
                len(self.authwindow_ui.name.text()) > 0 and
                len(self.authwindow_ui.middleName.text()) > 0
            )
    
    def old_editDTheme(self):
        if self.darkThemeOn:
            self.darkThemeOn = False
            self.app.setPalette(self.defaultTheme)
            DataBase.setItem(DatabaseName='applicationData', key='DarkTheme', newValue=0, indexKey='Num', value=1)
        else:
            self.darkThemeOn = True
            self.app.setPalette(self.darkTheme)
            DataBase.setItem(DatabaseName='applicationData', key='DarkTheme', newValue=1, indexKey='Num', value=1)
    
    def editDTheme(self):
        if self.darkThemeOn:
            self.darkThemeOn = False
            self.app.setStyleSheet(DataBase.getBase('styles')[0]['Style'])
            DataBase.setItem(DatabaseName='applicationData', key='activeTheme', newValue=0, indexKey='Num', value=1)
        else:
            self.darkThemeOn = True
            self.app.setStyleSheet(DataBase.getBase('styles')[1]['Style'])
            DataBase.setItem(DatabaseName='applicationData', key='activeTheme', newValue=1, indexKey='Num', value=1)
    
    def register(self):
        # Возьмём данные формы
        login = self.authwindow_ui.login.text()
        passsword = self.authwindow_ui.passwordEnter_2.text()
        name = self.authwindow_ui.name.text()
        middleName = self.authwindow_ui.middleName.text()
        age = self.authwindow_ui.age.value()
        set_group = self.authwindow_ui.set_group.currentIndex()
        typeLearn = [
            'free_personally',
            'free_distant',
            'contract_personally',
            'contract_distant'
        ][self.authwindow_ui.typeLearn.currentIndex()]
        # Создадим профиль или отклоним запрос
        if login not in SQLEasy.compareKey(DataBase.getBase('profiles'), 'Username'):
            if QMessageBox.warning(self, self.localeData['warnMesTitle'], self.localeData["rewriteFormsAlert"], QMessageBox.Ok, QMessageBox.Cancel) != 4194304:
                DataBase.add({
                    'ID': len(DataBase.getBase('profiles')) + 1,
                    'Username': login,
                    'password': passsword,
                    'name': name,
                    'middleName': middleName,
                    'age': age,
                    'GroupClass': set_group,
                    'learnType': typeLearn
                }, 'profiles')
                DataBase.setItem(DatabaseName='applicationData', key='activeProfile', newValue=DataBase.getBase('profiles')[-1]['ID'], indexKey='Num', value=1)
                QMessageBox.information(self, self.localeData["successAlert"], self.localeData["addAccount_message"], QMessageBox.Ok)
                self.authwindow_ui.userList.clear()
                for student in DataBase.getBase(DatabaseName='profiles'):
                    self.authwindow_ui.userList.addItem(f"{student['name']} '{student['Username']}' {student['middleName']}, {self.localeData['groupTitle_of_app']} {SQLEasy.compareKey(DataBase.getBase(DatabaseName='groups'), 'ID')[student['GroupClass']]['name']}")
            else:
                QMessageBox.critical(self, self.localeData["errorAlert"], self.localeData["requestError"], QMessageBox.Ok)
        else:
            QMessageBox.critical(self, self.localeData["errorAlert"], self.localeData["login_inDB_Error"], QMessageBox.Ok)
    
    def create_group(self):
        self.createGroup = QMainWindow()
        super(app_win, self).__init__()
        self.createGroup_ui = createGroup.Ui_Form(self.localeData)
        self.createGroup_ui.setupUi(self.createGroup)
        self.createGroup.setMouseTracking(True)
        self.createGroup.show()
        # Подрубим QTimer
        self.qtimer = QTimer()
        self.qtimer.timeout.connect(self.CheckCorrectDates_in_CG)
        self.qtimer.start(1)
        # Реализация кнопок
        self.createGroup_ui.createGroup.clicked.connect(self.action_createGroup)
    
    def CheckCorrectDates_in_CG(self):
        self.createGroup_ui.createGroup.setEnabled(
            len(self.createGroup_ui.CuratorName.text()) >= 4 and
            len(self.createGroup_ui.direction.text()) > 0 and
            len(self.createGroup_ui.groupName.text()) >= 2
        )
    
    def createLesson(self):
        self.createObject = QMainWindow()
        super(app_win, self).__init__()
        self.createObject_ui = createObject.Ui_Form(self.localeData)
        self.createObject_ui.setupUi(self.createObject)
        self.createObject.setMouseTracking(True)
        self.createObject.show()
        # Подрубим QTimer
        self.checker = QTimer()
        self.checker.timeout.connect(self.CheckCorrectDates_in_CL)
        self.checker.start(1)
        # Реализация кнопок
        self.createObject_ui.createButton.clicked.connect(self.createLesson_action)
    
    def createLesson_action(self):
        DataBase.add({
            'ID': len(DataBase.getBase('objects')),
            'objectName': self.createObject_ui.lessonName.text(),
            'teacher': self.createObject_ui.teacherName.text(),
            'description': self.createObject_ui.description.toPlainText()
        }, 'objects')
        
        self.mainmenu_ui.set_lesson.clear()
        for lesson in DataBase.getBase('objects'):
            self.mainmenu_ui.set_lesson.addItem(f"{lesson['objectName']} ({lesson['teacher']})")
        self.createObject.hide()
        QMessageBox.information(self, self.localeData["successAlert"], self.localeData["subjectAdd"], QMessageBox.Ok)
    
    def CheckCorrectDates_in_CL(self):
        self.createObject_ui.createButton.setEnabled(len(self.createObject_ui.lessonName.text()) >= 2 and len(self.createObject_ui.teacherName.text()) >= 5)
    
    def action_createGroup(self):
        dates = {
            'ID': len(DataBase.getBase('groups')),
            'name': self.createGroup_ui.groupName.text(),
            'curatorName': self.createGroup_ui.CuratorName.text(),
            'direction': self.createGroup_ui.direction.text(),
            'course': self.createGroup_ui.course.value(),
        }
        DataBase.add(dates, 'groups')
        self.authwindow_ui.set_group.clear()
        for group in DataBase.getBase(DatabaseName='groups'):
            self.authwindow_ui.set_group.addItem(f"{group['name']} ({group['curatorName']})")
        self.createGroup.hide()
        QMessageBox.information(self, self.localeData["successAlert"], self.localeData["addGroup"], QMessageBox.Ok)
    
    def auth(self):
        self.authCode = 0
        login = self.authwindow_ui.usernameEnter.text()
        password = self.authwindow_ui.passwordEnter.text()
        
        if login in SQLEasy.compareKey(DataBase.getBase('profiles'), 'Username'):
            if SQLEasy.compareKey(DataBase.getBase('profiles'), 'Username')[login]['password'] is None or len(SQLEasy.compareKey(DataBase.getBase('profiles'), 'Username')[login]['password']) == 0:
                DataBase.setItem(DatabaseName='applicationData', key='activeProfile', newValue=str(SQLEasy.compareKey(DataBase.getBase('profiles'), 'Username')[login]['ID']), indexKey='Num', value=1)
                if DataBase.getBase('applicationData')[0]['activeProfile'] == SQLEasy.compareKey(DataBase.getBase('profiles'), 'Username')[login]['ID']:
                    QMessageBox.information(self, self.localeData["successAlert"], f"{self.localeData['complLogin']} {SQLEasy.compareKey(DataBase.getBase('profiles'), 'Username')[login]['name']} {SQLEasy.compareKey(DataBase.getBase('profiles'), 'Username')[login]['middleName']}!", QMessageBox.Ok)
                    self.hide()
                    self.go_to_MainMenu()
                else:
                    QMessageBox.critical(self, self.localeData["errorAlert"], self.localeData["authError"], QMessageBox.Ok)
                    return
            else:
                if len(password) == 0:
                    QMessageBox.critical(self, self.localeData["errorAlert"], self.localeData["passwordError"], QMessageBox.Ok)
                    return
                elif password != SQLEasy.compareKey(DataBase.getBase('profiles'), 'Username')[login]['password']:
                    QMessageBox.critical(self, self.localeData["errorAlert"], self.localeData["unc_passwordError"], QMessageBox.Ok)
                    return
                else:
                    DataBase.setItem(DatabaseName='applicationData', key='activeProfile', newValue=str(SQLEasy.compareKey(DataBase.getBase('profiles'), 'Username')[login]['ID']), indexKey='Num', value=1)
                    if DataBase.getBase('applicationData')[0]['activeProfile'] == SQLEasy.compareKey(DataBase.getBase('profiles'), 'Username')[login]['ID']:
                        QMessageBox.information(self, self.localeData["successAlert"], f"{self.localeData['complLogin']} {SQLEasy.compareKey(DataBase.getBase('profiles'), 'Username')[login]['name']} {SQLEasy.compareKey(DataBase.getBase('profiles'), 'Username')[login]['middleName']}!", QMessageBox.Ok)
                        self.authCode = 1
                        self.hide()
                        self.go_to_MainMenu()
                    else:
                        QMessageBox.critical(self, self.localeData["errorAlert"], self.localeData["authError"], QMessageBox.Ok)
        else:
            QMessageBox.critical(self, self.localeData["errorAlert"], self.localeData["unc_loginError"], QMessageBox.Ok)
    
    def updGroupData(self):
        grID = SQLEasy.compareKey(DataBase.getBase('profiles'), 'ID')[DataBase.getBase('applicationData')[0]['activeProfile']]['GroupClass']
        groupObj = SQLEasy.compareKey(DataBase.getBase('groups'), 'ID')[grID]
        self.mainmenu_ui.groupName.setText(groupObj['name'])
        self.mainmenu_ui.direction.setText(groupObj['direction'])
        self.mainmenu_ui.CuratorName.setText(groupObj['curatorName'])
        self.mainmenu_ui.course.setValue(groupObj['course'])
        
        groupID = SQLEasy.compareKey(DataBase.getBase('profiles'), 'ID')[DataBase.getBase('applicationData')[0]['activeProfile']]['GroupClass']
        self.mainmenu_ui.set_group.clear()
        self.groupsList = list()
        INDEX = 0
        for groupObj in DataBase.getBase('groups'):
            self.mainmenu_ui.set_group.addItem(f"{groupObj['name']} ({groupObj['curatorName']})")
            self.groupsList.append(groupObj)
            if groupObj['ID'] == groupID:
                self.mainmenu_ui.set_group.setCurrentIndex(INDEX)
            INDEX += 1
    
    def go_to_MainMenu(self):
        self.password_unlocked = False
        self.qtimer.stop()
        self.timer.stop()
        self.userObj = SQLEasy.compareKey(DataBase.getBase('profiles'), 'ID')[DataBase.getBase('applicationData')[0]['activeProfile']]
        
        self.hide()
        self.mainmenu = QMainWindow()
        super(app_win, self).__init__()
        self.mainmenu_ui = journal.Ui_Form(self.localeData)
        self.mainmenu_ui.setupUi(self.mainmenu)
        self.mainmenu.setMouseTracking(True)
        self.mainmenu.show()
        # Запишем имя
        Name = SQLEasy.compareKey(DataBase.getBase('profiles'), 'ID')[DataBase.getBase('applicationData')[0]['activeProfile']]['name']
        middleName = SQLEasy.compareKey(DataBase.getBase('profiles'), 'ID')[DataBase.getBase('applicationData')[0]['activeProfile']]['middleName']
        groupID = SQLEasy.compareKey(DataBase.getBase('profiles'), 'ID')[DataBase.getBase('applicationData')[0]['activeProfile']]['GroupClass']
        # GroupLogIN = SQLEasy.compareKey(DataBase.getBase('groups'), 'ID')[SQLEasy.compareKey(DataBase.getBase('profiles'), 'ID')[int(DataBase.getBase('applicationData')[0]['activeProfile']]['GroupClass'])]['name']
        GroupLogIN = SQLEasy.compareKey(DataBase.getBase('groups'), 'ID')[groupID]['name']
        self.mainmenu.setWindowTitle(f"{self.localeData['journalTitle']} {Name} {middleName} {GroupLogIN}")
        # Зададим актуальную дату
        self.mainmenu_ui.deadline.setDate(QDate(datetime.date.today()))
        self.mainmenu_ui.push_in.setDate(QDate(datetime.date.today()))
        # Обновим раздел "настройки"
        
        # Персональная информация
        login = SQLEasy.compareKey(DataBase.getBase('profiles'), 'ID')[DataBase.getBase('applicationData')[0]['activeProfile']]['Username']
        learnType = SQLEasy.compareKey(DataBase.getBase('profiles'), 'ID')[DataBase.getBase('applicationData')[0]['activeProfile']]['learnType']
        age = SQLEasy.compareKey(DataBase.getBase('profiles'), 'ID')[DataBase.getBase('applicationData')[0]['activeProfile']]['age']
        password = SQLEasy.compareKey(DataBase.getBase('profiles'), 'ID')[DataBase.getBase('applicationData')[0]['activeProfile']]['password']
        self.mainmenu_ui.age.setValue(int(age))
        self.mainmenu_ui.Login.setText(login)
        self.mainmenu_ui.Name.setText(Name)
        self.mainmenu_ui.Family.setText(middleName)
        types_of_training = {
            "free_personally": 0,
            "free_distant": 1,
            "contract_personally": 2,
            "contract_distant": 3
        }
        learnType = types_of_training[learnType]
        self.mainmenu_ui.typeLearn.setCurrentIndex(learnType)
        self.mainmenu_ui.set_group.clear()
        self.groupsList = list()
        INDEX = 0
        for groupObj in DataBase.getBase('groups'):
            self.mainmenu_ui.set_group.addItem(f"{groupObj['name']} ({groupObj['curatorName']})")
            self.groupsList.append(groupObj)
            if groupObj['ID'] == groupID:
                self.mainmenu_ui.set_group.setCurrentIndex(INDEX)
            INDEX += 1
        # Информация о группе
        self.updGroupData()
        
        # Запустим таймер
        self.autoEnabler = QtCore.QTimer(self)
        self.true_values={'persona': {
            "login": login,
            "learnType": learnType,
            "age": age,
            "Name": Name,
            "Family": middleName,
            "GroupID": groupID
        }, 'groups': {
            "CuratorName": self.mainmenu_ui.CuratorName.text(),
            "GroupName": self.mainmenu_ui.groupName.text(),
            "prof": self.mainmenu_ui.direction.text(),
            "course": self.mainmenu_ui.course.value()
        }}
        self.autoEnabler.timeout.connect(lambda: self.edTimer(czekam_value_func=self.check_values))
        self.autoEnabler.start(1)        
        # Иницилизация тёмной темы
        if self.darkThemeOn:
            self.app.setStyleSheet(DataBase.getBase('styles')[1]['Style'])
        self.mainmenu_ui.applyDarkTheme.setChecked(self.darkThemeOn)
        # Обновим информацию (ref)
        self.updateInfo()
        # Применим блокировку к элементам пароля, когда пароль на аккаунте - не стоит
        self.mainmenu_ui.passwordUnlock.setEnabled(not(password is None) or password == '')
        self.mainmenu_ui.showPassword.setEnabled(not(password is None) or password == '')
        # Реализуем кнопки и клики
        self.mainmenu_ui.addLesson.clicked.connect(self.createLesson)
        self.mainmenu_ui.addTask.clicked.connect(self.addTask)
        self.mainmenu_ui.applyDarkTheme.clicked.connect(self.editDTheme)
        self.mainmenu_ui.calendarWidget.clicked.connect(self.updateInfo)
        self.mainmenu_ui.complete.clicked.connect(self.completeTask)
        self.mainmenu_ui.notcomplete.clicked.connect(self.finalize)
        self.mainmenu_ui.unlockSecurity_settings.clicked.connect(self.unlockPassEdit)
        self.mainmenu_ui.tasks.doubleClicked.connect(self.viewInformation_aboutTask)
        self.mainmenu_ui.completeTasks.doubleClicked.connect(self.complete_viewInformation_aboutTask)
        self.mainmenu_ui.ApplySaves_def.clicked.connect(self.apply_personalSettings)
        self.mainmenu_ui.ApplySaves_group.clicked.connect(self.apply_groupSettings)
        self.mainmenu_ui.logout.clicked.connect(lambda: self.logout(self.autoEnabler))
        self.mainmenu_ui.giveNull_password.clicked.connect(lambda: self.setPassword(True))
        self.mainmenu_ui.ApplySaves_protection.clicked.connect(self.setPassword)
        self.mainmenu_ui.addGroup.clicked.connect(self.create_group_fromSettings)
    
    def create_group_fromSettings(self):
        self.createGroup = QMainWindow()
        super(app_win, self).__init__()
        self.createGroup_ui = createGroup.Ui_Form(self.localeData)
        self.createGroup_ui.setupUi(self.createGroup)
        self.createGroup.setMouseTracking(True)
        self.createGroup.show()
        # Подрубим QTimer
        self.qtimer = QTimer()
        self.qtimer.timeout.connect(self.CheckCorrectDates_in_CG)
        self.qtimer.start(1)
        # Реализация кнопок
        self.createGroup_ui.createGroup.clicked.connect(self.action_createGroupFrom_setting)
    
    def action_createGroupFrom_setting(self):
        dates = {
            'ID': len(DataBase.getBase('groups')),
            'name': self.createGroup_ui.groupName.text(),
            'curatorName': self.createGroup_ui.CuratorName.text(),
            'direction': self.createGroup_ui.direction.text(),
            'course': self.createGroup_ui.course.value(),
        }
        DataBase.add(dates, 'groups')
        self.mainmenu_ui.set_group.clear()
        for group in DataBase.getBase(DatabaseName='groups'):
            self.mainmenu_ui.set_group.addItem(f"{group['name']} ({group['curatorName']})")
        
        self.groupsList = list()
        grID = SQLEasy.compareKey(DataBase.getBase('profiles'), 'ID')[DataBase.getBase('applicationData')[0]['activeProfile']]['GroupClass']
        groupID = SQLEasy.compareKey(DataBase.getBase('profiles'), 'ID')[DataBase.getBase('applicationData')[0]['activeProfile']]['GroupClass']
        INDEX = 0
        groupObj = SQLEasy.compareKey(DataBase.getBase('groups'), 'ID')[grID]
        for groupObj in DataBase.getBase('groups'):
            self.groupsList.append(groupObj)
            if groupObj['ID'] == groupID:
                self.mainmenu_ui.set_group.setCurrentIndex(INDEX)
            INDEX += 1
        self.updGroupData()
        
        self.createGroup.hide()
        QMessageBox.information(self, self.localeData["successAlert"], self.localeData["addGroup"], QMessageBox.Ok)
    
    def unlockPassEdit(self):
        true_passsword = SQLEasy.compareKey(DataBase.getBase('profiles'), 'ID')[DataBase.getBase('applicationData')[0]['activeProfile']]['password']
        unlocked = False
        if true_passsword is None:
            unlocked = True
        else:
            unlocked = self.mainmenu_ui.passwordUnlock.text() == true_passsword
        
        if unlocked:
            self.mainmenu_ui.NewPassword.setEnabled(True)
            self.password_unlocked = True
            self.mainmenu_ui.showPassword_2.setEnabled(True)
        else:
            QMessageBox.critical(self, self.localeData["errorAlert"], self.localeData["unc_passwordError"], QMessageBox.Ok)
    
    def check_values(self):
        return {'persona': {
            "login": self.mainmenu_ui.Login.text(),
            "learnType": self.mainmenu_ui.typeLearn.currentIndex(),
            "age": self.mainmenu_ui.age.value(),
            "Name": self.mainmenu_ui.Name.text(),
            "Family": self.mainmenu_ui.Family.text(),
            "GroupID": self.groupsList[self.mainmenu_ui.set_group.currentIndex()]['ID']
        }, 'groups': {
            "CuratorName": self.mainmenu_ui.CuratorName.text(),
            "GroupName": self.mainmenu_ui.groupName.text(),
            "prof": self.mainmenu_ui.direction.text(),
            "course": self.mainmenu_ui.course.value()
        }}
    
    def edTimer(self, czekam_value_func):
        self.mainmenu_ui.ApplySaves_def.setEnabled(czekam_value_func()['persona'] != self.true_values['persona'])
        self.mainmenu_ui.ApplySaves_group.setEnabled(czekam_value_func()['groups'] != self.true_values['groups'])
        
        if self.mainmenu_ui.Login.text() != getCorret_login(self.mainmenu_ui.Login.text()):
            self.mainmenu_ui.Login.setText(getCorret_login(self.mainmenu_ui.Login.text()))
        
        if self.mainmenu_ui.passwordUnlock.text() != getCorret_password(self.mainmenu_ui.passwordUnlock.text()):
            self.mainmenu_ui.passwordUnlock.setText(getCorret_password(self.mainmenu_ui.passwordUnlock.text()))
        
        if self.mainmenu_ui.NewPassword.text() != getCorret_password(self.mainmenu_ui.NewPassword.text()):
            self.mainmenu_ui.NewPassword.setText(getCorret_password(self.mainmenu_ui.NewPassword.text()))
        
        if self.mainmenu_ui.showPassword.isChecked():
            self.mainmenu_ui.passwordUnlock.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.mainmenu_ui.passwordUnlock.setEchoMode(QtWidgets.QLineEdit.Password)
        
        if self.mainmenu_ui.showPassword_2.isChecked():
            self.mainmenu_ui.NewPassword.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.mainmenu_ui.NewPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        
        self.mainmenu_ui.ApplySaves_protection.setEnabled(
            self.password_unlocked and 
            self.mainmenu_ui.NewPassword.text() != self.userObj['password'] and 
            len(self.mainmenu_ui.NewPassword.text()) >= 8
        )
        self.mainmenu_ui.giveNull_password.setEnabled(self.password_unlocked and (not(self.userObj['password'] in (None, ''))))
    
    def resetForms_password(self):
        self.mainmenu_ui.passwordUnlock.setText('')
        self.mainmenu_ui.NewPassword.setText('')
        self.password_unlocked = False
        self.mainmenu_ui.NewPassword.setEnabled(False)
        self.mainmenu_ui.showPassword_2.setEnabled(False)
    
    def setPassword(self, reset=False):
        if reset:
            if QMessageBox.warning(self, self.localeData['warnMesTitle'], self.localeData["data_editionAlert"], QMessageBox.Ok, QMessageBox.Cancel) != 4194304:
                self.userObj['password'] = ''
                DataBase.setItem(
                    DatabaseName='profiles',
                    indexKey='ID',
                    value=DataBase.getBase('applicationData')[0]['activeProfile'],
                    key='password',
                    newValue=''
                )
                self.resetForms_password()
                QMessageBox.information(self, self.localeData["successAlert"], self.localeData["passwReseted"], QMessageBox.Ok)
        else:
            if QMessageBox.warning(self, self.localeData['warnMesTitle'], self.localeData["data_editionAlert"], QMessageBox.Ok, QMessageBox.Cancel) != 4194304:
                self.userObj['password'] = self.mainmenu_ui.NewPassword.text()
                DataBase.setItem(
                    DatabaseName='profiles',
                    indexKey='ID',
                    value=DataBase.getBase('applicationData')[0]['activeProfile'],
                    key='password',
                    newValue=self.mainmenu_ui.NewPassword.text()
                )
                self.resetForms_password()
                QMessageBox.information(self, self.localeData["successAlert"], self.localeData["passwEdited"], QMessageBox.Ok)
    
    def apply_groupSettings(self):
        if QMessageBox.warning(self, self.localeData['warnMesTitle'], self.localeData["data_editionAlert"], QMessageBox.Ok, QMessageBox.Cancel) != 4194304:
            tempData = self.check_values()['groups']
            grData = {
                "name": tempData["GroupName"],
                "curatorName": tempData["CuratorName"],
                "course": tempData["course"],
                "direction": tempData["prof"]
            }
            
            for grData_key in grData:
                DataBase.setItem(
                    DatabaseName='groups',
                    indexKey='ID',
                    value=SQLEasy.compareKey(DataBase.getBase('profiles'), 'ID')[DataBase.getBase('applicationData')[0]['activeProfile']]['GroupClass'],
                    key=grData_key,
                    newValue=grData[grData_key]
                )
            
            self.true_values['groups'] = tempData
            self.mainmenu.setWindowTitle(f"{self.localeData['journalTitle']} {self.true_values['persona']['Name']} {self.true_values['persona']['Family']} {tempData['GroupName']}")
            self.updGroupData()
            QMessageBox.information(self, self.localeData["successAlert"], self.localeData["dataUpd_message"], QMessageBox.Ok)
    
    def apply_personalSettings(self):
        if QMessageBox.warning(self, self.localeData['warnMesTitle'], self.localeData["data_editionAlert"], QMessageBox.Ok, QMessageBox.Cancel) != 4194304:
            tempData = self.check_values()['persona']
            learnTypes = [
                "free_personally",
                "free_distant",
                "contract_personally",
                "contract_distant"
            ]
            
            userData = {
                "Username": tempData['login'],
                "name": tempData['Name'],
                "middleName": tempData['Family'],
                "age": tempData['age'],
                "GroupClass": tempData['GroupID'],
                "learnType": learnTypes[tempData['learnType']]
            }
            if userData['Username'] in [item['Username'] for item in DataBase.getBase('profiles')] and userData['Username'] != self.true_values['persona']['login']:
                QMessageBox.critical(self, self.localeData["errorAlert"], self.localeData["login_inDB_Error"], QMessageBox.Ok)
                return
            
            for userData_key in userData:
                DataBase.setItem(
                    DatabaseName='profiles', 
                    indexKey='ID', 
                    value=DataBase.getBase('applicationData')[0]['activeProfile'],
                    key=userData_key, 
                    newValue=userData[userData_key]
                )
            self.true_values['persona'] = tempData
            self.mainmenu.setWindowTitle(f"{self.localeData['journalTitle']} {tempData['Name']} {tempData['Family']} {SQLEasy.compareKey(DataBase.getBase('groups'), 'ID')[tempData['GroupID']]['name']}")
            self.updGroupData()
            QMessageBox.information(self, self.localeData["successAlert"], self.localeData["dataUpd_message"], QMessageBox.Ok)
    
    def completeTask(self):
        if self.mainmenu_ui.tasks.currentRow() != -1:
            DataBase.setItem(DatabaseName='tasks', indexKey='ID', value=self.TaskList['active'][self.mainmenu_ui.tasks.currentRow()]['ID'], key='is_complete', newValue=1)
        self.updateInfo()
    
    def finalize(self):
        if self.mainmenu_ui.completeTasks.currentRow() != -1:
            DataBase.setItem(DatabaseName='tasks', indexKey='ID', value=self.TaskList['complete'][self.mainmenu_ui.tasks.currentRow()]['ID'], key='is_complete', newValue=0)
        self.updateInfo()
    
    def viewInformation_aboutTask(self):
        if self.mainmenu_ui.tasks.currentRow() != -1:
            self.taskInfo = QMainWindow()
            super(app_win, self).__init__()
            self.taskInfo_ui = taskInfo.Ui_Form(localeData)
            self.taskInfo_ui.setupUi(self.taskInfo)
            self.taskInfo.setMouseTracking(True)
            self.taskInfo.show()
            # Обновим инфу
            LessonID = self.TaskList['active'][self.mainmenu_ui.tasks.currentRow()]['object']
            self.taskInfo_ui.label.setText(
                f"{self.localeData['subjectTranslate']}: {SQLEasy.compareKey(DataBase.getBase('objects'), 'ID')[LessonID]['objectName']}" +
                f"\n{self.localeData['professor']}: {SQLEasy.compareKey(DataBase.getBase('objects'), 'ID')[LessonID]['teacher']}" +
                f"\n{self.localeData['deadlineText']} {datetime.datetime.fromtimestamp(int(self.TaskList['active'][self.mainmenu_ui.tasks.currentRow()]['deadline'])).strftime('%d.%m.%Y')}"
            )
            taskObj = self.TaskList['active'][self.mainmenu_ui.tasks.currentRow()]
            self.taskInfo_ui.taskDescription.insertPlainText(self.TaskList['active'][self.mainmenu_ui.tasks.currentRow()]['description'])
            # Закрытие
            self.taskInfo_ui.close.clicked.connect(self.taskInfo.hide)
            # Редактирование
            self.activeScene_taskInfo = self.viewInformation_aboutTask
            self.taskInfo_ui.edit.clicked.connect(self.editTask_app)
            # Удаление
            self.taskInfo_ui.delButton.clicked.connect(lambda: self.deleteTask(taskObj))
    
    def complete_viewInformation_aboutTask(self):
        if self.mainmenu_ui.completeTasks.currentRow() != -1:
            self.taskInfo = QMainWindow()
            super(app_win, self).__init__()
            self.taskInfo_ui = taskInfo.Ui_Form(localeData)
            self.taskInfo_ui.setupUi(self.taskInfo)
            self.taskInfo.setMouseTracking(True)
            self.taskInfo.show()
            # Обновим инфу
            LessonID = self.TaskList['complete'][self.mainmenu_ui.completeTasks.currentRow()]['object']
            self.taskInfo_ui.label.setText(
                f"{self.localeData['subjectTranslate']}: {SQLEasy.compareKey(DataBase.getBase('objects'), 'ID')[LessonID]['objectName']}" +
                f"\n{self.localeData['professor']}: {SQLEasy.compareKey(DataBase.getBase('objects'), 'ID')[LessonID]['teacher']}" +
                f"\n{self.localeData['deadlineText']} {datetime.datetime.fromtimestamp(int(self.TaskList['complete'][self.mainmenu_ui.completeTasks.currentRow()]['deadline'])).strftime('%d.%m.%Y')}"
            )
            taskObj = self.TaskList['complete'][self.mainmenu_ui.completeTasks.currentRow()]
            self.taskInfo_ui.taskDescription.insertPlainText(self.TaskList['complete'][self.mainmenu_ui.completeTasks.currentRow()]['description'])
            # Закрытие
            self.taskInfo_ui.close.clicked.connect(self.taskInfo.hide)
            # Редактирование
            self.activeScene_taskInfo = self.complete_viewInformation_aboutTask
            self.taskInfo_ui.edit.clicked.connect(self.editTask_app)
            # Удаление
            self.taskInfo_ui.delButton.clicked.connect(lambda: self.deleteTask(taskObj))
    
    def deleteTask(self, taskObj):
        taskObj['hidden'] = 1
        if QMessageBox.warning(self, self.localeData['warnMesTitle'], self.localeData["deleteTask_message"], QMessageBox.Ok, QMessageBox.Cancel) != 4194304:
            DataBase.setItem(
                DatabaseName='tasks', 
                indexKey='ID', 
                value=taskObj['ID'],
                key='hidden', 
                newValue=1
            )
            QMessageBox.information(self, self.localeData["successAlert"], self.localeData["dataUpd_message"], QMessageBox.Ok)
            self.taskInfo.hide()
            self.updateInfo()
    
    def editTask_app(self):
        self.taskInfo.hide()
        
        self.editTaskInfo = QMainWindow()
        super(app_win, self).__init__()
        self.editTaskInfo_ui = editTask.Ui_Form(localeData)
        self.editTaskInfo_ui.setupUi(self.editTaskInfo)
        self.editTaskInfo.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)
        self.editTaskInfo.setMouseTracking(True)
        self.editTaskInfo.show()
        # Обновим инфу
        if self.activeScene_taskInfo == self.complete_viewInformation_aboutTask:
            LessonID = self.TaskList['complete'][self.mainmenu_ui.completeTasks.currentRow()]['object']
            self.editTaskInfo_ui.taskDescription.insertPlainText(self.TaskList['complete'][self.mainmenu_ui.completeTasks.currentRow()]['description'])
            taskObj = self.TaskList['complete'][self.mainmenu_ui.completeTasks.currentRow()]
        else:
            LessonID = self.TaskList['active'][self.mainmenu_ui.tasks.currentRow()]['object']
            self.editTaskInfo_ui.taskDescription.insertPlainText(self.TaskList['active'][self.mainmenu_ui.tasks.currentRow()]['description'])
            taskObj = self.TaskList['active'][self.mainmenu_ui.tasks.currentRow()]
        
        lessons = DataBase.getBase('objects')
        INDEX = 0
        for lesson in lessons:
            self.editTaskInfo_ui.lessonSelect.addItem(f"{lesson['objectName']} ({lesson['teacher']})")
            if lesson['ID'] == LessonID:
                self.editTaskInfo_ui.lessonSelect.setCurrentIndex(INDEX)
            INDEX += 1
        
        self.editTaskInfo_ui.deadline.setDate(getTimeObject(taskObj['deadline'] + 3600 * 24))
        self.editTaskInfo_ui.push_in.setDate(getTimeObject(taskObj['view_in_journal'] + 3600 * 24))
        
        # Запустим QTimer
        self.editorControl = QTimer()
        def dataGet():
            return {
                "dl_time": int(datetime.datetime.strptime(self.editTaskInfo_ui.deadline.date().toString("dd.MM.yyyy"), '%d.%m.%Y').timestamp()),
                "et_time": int(datetime.datetime.strptime(self.editTaskInfo_ui.push_in.date().toString("dd.MM.yyyy"), '%d.%m.%Y').timestamp()),
                "text": self.editTaskInfo_ui.taskDescription.toPlainText(),
                "lessons": lessons,
                "lessonList_ID": self.editTaskInfo_ui.lessonSelect.currentIndex()
            }
        
        startData = {
            "dl_time": int(datetime.datetime.strptime(self.editTaskInfo_ui.deadline.date().toString("dd.MM.yyyy"), '%d.%m.%Y').timestamp()),
            "et_time": int(datetime.datetime.strptime(self.editTaskInfo_ui.push_in.date().toString("dd.MM.yyyy"), '%d.%m.%Y').timestamp()),
            "text": self.editTaskInfo_ui.taskDescription.toPlainText(),
            "lessons": lessons,
            "lessonList_ID": self.editTaskInfo_ui.lessonSelect.currentIndex()
        }
        self.editorControl.timeout.connect(lambda: self.editorControl_timerVoid(startData, dataGet))
        self.editorControl.start(1)
        # Закрытие
        self.editTaskInfo_ui.cancel.clicked.connect(self.editorControl.stop)
        self.editTaskInfo_ui.cancel.clicked.connect(self.editTaskInfo.hide)
        self.editTaskInfo_ui.cancel.clicked.connect(self.activeScene_taskInfo)
        # Сохранить
        self.editTaskInfo_ui.Save.clicked.connect(lambda: self.saveTask_updates(dataGet(), taskObj, lessons))
        
    def saveTask_updates(self, Data, taskObj, lessons):
        if QMessageBox.warning(self, self.localeData['warnMesTitle'], self.localeData["data_editionAlert"], QMessageBox.Ok, QMessageBox.Cancel) != 4194304:
            DBData = {
                "object": lessons[Data['lessonList_ID']]['ID'],
                "description": Data['text'],
                "deadline": Data['dl_time'],
                "view_in_journal": Data['et_time']
            }
            
            for key in DBData:
                DataBase.setItem(
                    DatabaseName='tasks', 
                    indexKey='ID', 
                    value=taskObj['ID'],
                    key=key, 
                    newValue=DBData[key]
                )
            QMessageBox.information(self, self.localeData["successAlert"], self.localeData["dataUpd_message"], QMessageBox.Ok)
            self.editorControl.stop()
            self.editTaskInfo.hide()
            self.updateInfo()
            self.activeScene_taskInfo()
    
    def editorControl_timerVoid(self, startData, dataGet):
        self.editTaskInfo_ui.Save.setEnabled(dataGet() != startData)
    
    def addTask(self):
        data = {
            'ID': len(DataBase.getBase('tasks')),
            'object': self.mainmenu_ui.set_lesson.currentIndex(),
            'description': self.mainmenu_ui.taskDescription.toPlainText(),
            'deadline': int(datetime.datetime.strptime(self.mainmenu_ui.deadline.date().toString("dd.MM.yyyy"), '%d.%m.%Y').timestamp()),
            'view_in_journal': int(datetime.datetime.strptime(self.mainmenu_ui.push_in.date().toString("dd.MM.yyyy"), '%d.%m.%Y').timestamp()),
            'owner': int(DataBase.getBase('applicationData')[0]['activeProfile']),
            'is_complete': 0
        }
        if self.mainmenu_ui.set_lesson.currentIndex() == -1:
            QMessageBox.critical(self, self.localeData["errorAlert"], self.localeData["noLessons_descrAlert"], QMessageBox.Ok)
            return
        if len(data['description']) <= 4:
            QMessageBox.critical(self, self.localeData["errorAlert"], self.localeData["len_description_Alert"], QMessageBox.Ok)
            return
        
        DataBase.add(data, 'tasks')
        # Обновим информацию (ref)
        self.updateInfo()
        QMessageBox.information(self, self.localeData["successAlert"], self.localeData["taskAdd"], QMessageBox.Ok)
    
    def updateInfo(self):
        self.mainmenu_ui.set_lesson.clear()
        for lesson in DataBase.getBase('objects'):
            self.mainmenu_ui.set_lesson.addItem(f"{lesson['objectName']} ({lesson['teacher']})")
        self.TaskList = {
            'active': list(),
            'complete': list()
        }
        self.mainmenu_ui.tasks.clear()
        self.mainmenu_ui.completeTasks.clear()
        for task in DataBase.getBase('tasks'):
            if int(task['view_in_journal']) <= int(datetime.datetime.strptime(self.mainmenu_ui.calendarWidget.selectedDate().toString("dd.MM.yyyy"), '%d.%m.%Y').timestamp()) and int(datetime.datetime.strptime(self.mainmenu_ui.calendarWidget.selectedDate().toString("dd.MM.yyyy"), '%d.%m.%Y').timestamp()) < int(task['deadline']) and int(task['owner']) == int(DataBase.getBase('applicationData')[0]['activeProfile']):
                if task['hidden'] == 1:
                    pass
                elif task['is_complete'] == 1:
                    self.TaskList['complete'].append(task)
                    lesson = SQLEasy.compareKey(DataBase.getBase('objects'), 'ID')[task['object']]['objectName']
                    task_content = task['description']
                    self.mainmenu_ui.completeTasks.addItem(f"{lesson}:\n{task_content}")
                else:
                    self.TaskList['active'].append(task)
                    lesson = SQLEasy.compareKey(DataBase.getBase('objects'), 'ID')[task['object']]['objectName']
                    task_content = task['description']
                    self.mainmenu_ui.tasks.addItem(f"{lesson}:\n{task_content}")
        
        if len(self.mainmenu_ui.completeTasks) == 0:
            self.mainmenu_ui.progressBar.setValue(0)
        else:
            unitedValueofTasks = len(self.TaskList['active']) + len(self.TaskList['complete'])
            complete_all_tasks = len(self.TaskList['complete']) / unitedValueofTasks
            self.mainmenu_ui.progressBar.setValue(int(complete_all_tasks * 100))
        
        self.mainmenu_ui.title_2.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">{self.localeData['completeTask']} ({len(self.TaskList['complete'])})</span></p></body></html>")
        task_count = len(self.TaskList['active'])
        
        indexToday = [item['ID'] for item in self.TaskList['active']]
        
        TaskList_lastDay = {
            'active': list()
        }
        
        TimeLast = int(datetime.datetime.strptime(self.mainmenu_ui.calendarWidget.selectedDate().toString("dd.MM.yyyy"), '%d.%m.%Y').timestamp()) - 3600 * 24
        for task in DataBase.getBase('tasks'):
            if int(task['view_in_journal']) <= TimeLast and TimeLast < int(task['deadline']) and int(task['owner']) == int(DataBase.getBase('applicationData')[0]['activeProfile']):
                if task['hidden'] == 1:
                    pass
                elif task['is_complete'] == 0:
                    TaskList_lastDay['active'].append(task)
        
        indexLast = [item['ID'] for item in TaskList_lastDay['active']]
        addTasks = 0
        removeTasks = 0
        
        for index in indexLast:  # Просроченные задания
            if index not in indexToday:
                removeTasks += 1
        
        for index in indexToday:  # Новые задания
            if index not in indexLast:
                addTasks += 1
        
        addTaskText = ''
        if addTasks > 0:
            addTaskText = f" <font color=#00aa00>+{addTasks}</font>"
        rmTaskText = ''
        if removeTasks > 0:
            rmTaskText = f" <font color=#aa0000>-{removeTasks}</font>"
        newmData = f"{task_count}{rmTaskText}{addTaskText}"
        self.mainmenu_ui.title.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">{self.localeData['currentTasks']} ({newmData})</span></p></body></html>")
        
    def logout(self, timerObj):
        if QMessageBox.warning(self, self.localeData['warnMesTitle'], self.localeData["logoutConfirmation"], QMessageBox.Ok, QMessageBox.Cancel) != 4194304:
            timerObj.stop()
            darkTheme_logic = DataBase.getBase('applicationData')[0]['activeTheme']
            langID = DataBase.getBase('applicationData')[0]['ActiveLingua']
            DataBase.pop(DatabaseName='applicationData', key='Num', value=1)
            DataBase.add({'cache': 'ok'}, DatabaseName='applicationData')
            DataBase.setItem(
                DatabaseName='applicationData', 
                indexKey='cache', 
                value='ok',
                key='activeTheme', 
                newValue=darkTheme_logic
            )
            DataBase.setItem(
                DatabaseName='applicationData', 
                indexKey='cache', 
                value='ok',
                key='ActiveLingua', 
                newValue=langID
            )
            self.mainmenu.hide()
            self = self.__init__(self.app, self.localeData, self.internetConnection)


app = QApplication([])


def getLocale_data(database, localeData):
    DataApp = database.getBase('applicationData')[0]
    if 'ActiveLingua' not in DataApp:
        QMessageBox.warning(QMainWindow(), 'Warning!', 'The database translation table is either corrupted or missing due to an earlier version. Update the database, or install a more up-to-date version of the database.', QMessageBox.Ok)
        return localeData
    else:
        formed_locale = localeData.copy()
        awaible_keys = set()
        LanguageID = DataApp['ActiveLingua']
        if LanguageID in (None, -1):
            return localeData
        try:
            current_locales = SQLEasy.compareKey(database.getBase('langs'), 'ID')[LanguageID]
            for c_localeKey in current_locales:
                formed_locale[c_localeKey] = current_locales[c_localeKey]
                awaible_keys.add(c_localeKey)
            
            if len(awaible_keys) != len(formed_locale):
                QMessageBox.warning(QMainWindow(), 'Warning!', 'The database translation table is either corrupted or missing due to an earlier version. Update the database, or install a more up-to-date version of the database.', QMessageBox.Ok)
                return localeData
            
            for awKey in awaible_keys:
                if awKey not in localeData:
                    QMessageBox.warning(QMainWindow(), 'Warning!', 'The database translation table is either corrupted or missing due to an earlier version. Update the database, or install a more up-to-date version of the database.', QMessageBox.Ok)
                    return localeData
            
            return formed_locale
        except:
            QMessageBox.warning(QMainWindow(), 'Warning!', 'The database translation table is either corrupted or missing due to an earlier version. Update the database, or install a more up-to-date version of the database.', QMessageBox.Ok)
            return localeData


localeData = getLocale_data(DataBase, localeData)

if DBVersion_code != 1:
    viewMes = localeData[{0: 'oldestVersionMessage', 2: 'futureVersionMessage'}[DBVersion_code]]
    if QMessageBox.warning(QMainWindow(), localeData['warnMesTitle'], viewMes, QMessageBox.Ok, QMessageBox.Cancel) != 4194304:
        updater.setup_actual_version(Supported_DataBaseVersion, localeData)
        DataBase = SQLEasy.database('database.db')
    else:
        exit()

# Проверка обновлений

internet = True
exit_act = False


class timer(Thread):
    def pulse(self, Time):
        self.liczba = Time
        self.start()
    
    def __bool__(self):
        return self.liczba <= 0
    
    def run(self):
        time.sleep(self.liczba)
        self.liczba = 0


class update_checker(Thread):
    def check(self):
        global timer
        self.runned = True
        
        self.Return = {
            "internet": False,
            "exit": False
        }
        
        self.end = False
        Timer = timer()
        Timer.pulse(15)
        self.start()
        while not(self.end):
            if Timer:
                break
        
        print(self.Return)
        
        self.runned = False
        self.join()
        return self.Return
    
    def run(self):
        if self.runned:
            global localeData
            internet = True
            exit_act = False
            
            try:
                print('connecting to server...')
                # while True:
                    # pass
                urllib.request.urlopen("http://google.com")
                set_versionData = requests.get('https://student-manager.github.io/info/actual_version.json').json()
                if updater.versionObject(set_versionData['last_version']) > updater.versionObject(programVersion):
                    if QMessageBox.information(QMainWindow(), localeData['progrUpdateTitle'], localeData['progrUpdateMessage'], QMessageBox.Ok, QMessageBox.Cancel) != 4194304:
                        exit_act = True
                        webbrowser.open(set_versionData['download_url'], new=2)
                        os.abort()
            except IOError:
                internet = False
                QMessageBox.warning(QMainWindow(), localeData['errorAlert'], localeData['failedConnection'], QMessageBox.Ok)
            except:
                print(traceback.format_exc())
                internet = False
            
            self.Return = {
                "internet": internet,
                "exit": exit_act
            }
            self.end = True


update_checker = update_checker()
IntData = update_checker.check()
exit_act = IntData['exit']
internet = IntData['internet']
del IntData, update_checker

if exit_act:
    os.abort()

application = app_win(app, localeData, internet)
app.exec()
os.abort()