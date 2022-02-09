from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
import SQLEasy, time, os, sys, threading, database_updater_data
import updUI


class versionObject:
    def __init__(self, text_value_of_version, v_type='release'):
        self.v_type = v_type
        self.version_values = text_value_of_version.split('.')
        self.version_values = [int(item) for item in self.version_values]
    
    def __str__(self):
        return "v.%s" % '.'.join([str(item) for item in self.version_values])
    
    def __len__(self):
        return len(self.version_values)
    
    def __eq__(self, other):
        if self.version_values == other.version_values:
            return True
        elif len(self.version_values) > len(other.version_values):
            if self.version_values[:len(other.version_values)] == other.version_values:
                for item in self.version_values[len(other.version_values):]:
                    if item != 0:
                        return False
                return True
            else:
                return False
        else:
            if other.version_values[:len(self.version_values)] == self.version_values:
                for item in other.version_values[len(self.version_values):]:
                    if item != 0:
                        return False
                return True
            else:
                return False
    
    def __gt__(self, other):
        if self == other:
            return False
        
        checking_variable = self
        opposition_variable = other
        if len(self) >= len(other):
            checking_variable = other
            opposition_variable = self
        
        for index in range(len(checking_variable)):
            if checking_variable.version_values[index] != opposition_variable.version_values[index]:
                return self.version_values[index] > other.version_values[index]
        
        for numV in opposition_variable.version_values[len(checking_variable):]:
            if numV > 0:
                return True
        
        return False
    
    def __lt__(self, other):
        return not(self > other or self == other)
    
    def __le__(self, other):
        if self == other:
            return True
        else:
            return self < other
    
    def __ge__(self, other):
        if self == other:
            return True
        else:
            return self > other
    
    def __hash__(self):
        reversed_v = self.version_values.copy()
        reversed_v.reverse()
        nums = 0
        for vers in reversed_v:
            if vers != 0:
                nums += 1
            else:
                break
        reversed_v.reverse()
        if nums != 0:
            reversed_v = reversed_v[::nums]
        
        return hash('.'.join([str(N) for N in reversed_v]))
    
    def getVersion(self):
        return self.version_values


database_updater_data.init(versionObject)


def checkVersion(database, needed_version):  # 0 - Старая версия, 1 - ok , 2 - Неподдерживаемая версия
    version = database.getBase('applicationData')[0]
    needed_version = versionObject(needed_version)
    if 'version' not in version:
        version = versionObject('1.0')
    else:
        version = versionObject(version['version'])
    
    if version == needed_version:
        return 1
    elif version < needed_version:
        return 0
    else:
        return 2


def setup_actual_version(version_setup, localeData):
    version_setup = versionObject(version_setup)
    nullbytes = database_updater_data.db_bytes
    
    def upDate(data, to_version, currentVersion, localeData, echo=print):
        # if currentVersion == versionObject('1.0') and currentVersion >= versionObject('1.1'):
        if currentVersion == versionObject('1.0'):
            # Добавим новые таблицы
            data['langs'] = list()
            data['styles'] = list()
            # Обновим таблицы (Сначала которые были в версии 1.0, а затем, добавим новые значения)
            for i in range(len(data['applicationData'])):
                data['applicationData'][i]['activeTheme'] = data['applicationData'][i]['DarkTheme']
                del data['applicationData'][i]['DarkTheme']
                data['applicationData'][i]['version'] = '1.1'
                # data['applicationData'][i]['ActiveLingua'] = -1
            currentVersion = versionObject('1.1')
            
            for i in range(len(data['profiles'])):
                del data['profiles'][i]['tasks']
            
            for i in range(len(data['tasks'])):
                data['tasks'][i]['hidden'] = 0
        if currentVersion == versionObject('1.1'):
            # Добавим новые таблицы
            data['subjects_grs'] = list()
            rowID = 0
            for subject in data['objects']:
                for groupObj in data['groups']:
                    data['subjects_grs'].append({
                        "rowID": rowID,
                        "subjectID": subject['ID'],
                        "group_id": groupObj['ID']
                    })
                    rowID += 1
            # Обновим таблицы (Сначала которые были в версии 1.1, а затем, добавим новые значения)
            for i in range(len(data['applicationData'])):
                data['applicationData'][i]['version'] = '1.1.1'
                data['applicationData'][i]['ActiveLingua'] = None
            currentVersion = versionObject('1.1.1')
            # Удалим ненужное
            for i in data['styles']:
                data['styles'].pop(data['styles'].index(i))
            for i in data['langs']:
                data['langs'].pop(data['langs'].index(i))
        
        return data
    
    def pointerInspector(data):
        point = 0
        for table in data:
            tableObj = data[table]
            for AdvValue in tableObj:
                point += 1
        return point
    
    def Ref_DB(data, Database, localeData, echo=print, addpointFunc=lambda: None):
        for table in data:
            tableObj = data[table]
            for AdvValue in tableObj:
                echo(f"{localeData['copyDataLog']}: {AdvValue} {localeData['fromLog']} {table}")
                addpointFunc()
                Database.add(AdvValue, table)
    
    class setupNewVersion(threading.Thread):
        def init(self):
            self.log = list()
            self.finished = False
            self.loadbar = 0
            
        def run(self):
            logwrite = self.log.append
            # Копирование в backups 
            if 'backups' not in os.listdir():
                logwrite('%s %s/backups' % (localeData['mkdirLog'], str(os.getcwd).replace('\\', '/')))
                os.mkdir('backups')
            
            logwrite('%s %s/backups' % (localeData['copyLog'], str(os.getcwd).replace('\\', '/')))
            copy = open('database.db', 'rb')
            copybytes = copy.read()
            copy.close()
            
            copy = open(f"backups/{time.time()}_database.db", 'wb')
            copy.write(copybytes)
            copy.close()
            
            del copybytes, copy
            # Открытие БД
            logwrite(localeData['openDatabaseLog'])
            DB = SQLEasy.database('database.db')
            if 'version' not in DB.getBase('applicationData')[0]:
                versionDB = versionObject('1.0')
            else:
                versionDB = versionObject(DB.getBase('applicationData')[0]['version'])
            # Копирование в буфер данных таблиц
            logwrite(localeData['copyData_inBuffer_Log'])
            tables = DB.getTables()
            data = dict()
            
            for table in tables:
                data[table] = DB.getBase(table)
            
            data = upDate(data, version_setup, versionDB, localeData, echo=logwrite)
            # Перезапишем базу данных
            del DB
            databaseFileMaster = open('database.db', 'wb')
            databaseFileMaster.write(nullbytes[version_setup])
            databaseFileMaster.close()
            del databaseFileMaster
            DB = SQLEasy.database('database.db')
            
            self.pointsMax = pointerInspector(data)
            
            class progress_point(int):
                def __init__(self):
                    self.p = 0
                
                def add(self):
                    self.p += 1
            
            self.progress_point = progress_point()
            
            # Обновим значения
            Ref_DB(data, DB, localeData, echo=logwrite, addpointFunc=self.updateData)
            
            self.finished = True
        
        def updateData(self):
            self.progress_point.add()
            if self.progress_point.p != 0:
                self.loadbar = int((self.progress_point.p / self.pointsMax) * 100)
    
    class app_win(QMainWindow):
        def __init__(self):
            super(app_win, self).__init__()
            self.update_ui = updUI.Ui_Form()
            self.update_ui.setupUi(self)
            self.setMouseTracking(True)
            self.setWindowTitle(localeData['updateTitleProgram'])
            self.localeData = localeData
            self.show()
            
            self.setup()
            self.finNoView = True
            
            self.update_ui.pushButton.clicked.connect(self.close)
        
        def setup(self):
            self.thr = setupNewVersion()
            self.thr.init()
            # Запуск таймера
            self.qtimer = QTimer()
            self.qtimer.timeout.connect(self.updLog)
            self.qtimer.start(3)
            
            self.cacheLog = self.thr.log.copy()
            self.thr.start()
            
        def updLog(self):
            if self.cacheLog != self.thr.log:
                self.update_ui.log.clear()
                for logInfo in self.thr.log:
                    self.update_ui.log.addItem(logInfo)
                self.cacheLog = self.thr.log.copy()
            if len(self.update_ui.log) > 0:
                self.update_ui.log.setCurrentRow(
                    len(self.update_ui.log) - 1
                )
            self.update_ui.progressBar.setValue(self.thr.loadbar)
            self.update_ui.pushButton.setEnabled(self.thr.finished)
            if self.thr.finished:
                self.alert()
        
        def alert(self):
            if self.finNoView:
                QMessageBox.warning(self, self.localeData['warnMesTitle'], self.localeData["upDated_alert"], QMessageBox.Ok)
                self.finNoView = False
    
    app = QApplication([])
    application = app_win()
    sys.exit(app.exec())