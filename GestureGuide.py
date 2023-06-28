import shutil
import time
import datetime
import winsound
from PySide2.QtWidgets import QMainWindow, QApplication, QMessageBox
from PySide2.QtGui import QPixmap
from PySide2.QtCore import QRunnable, QThreadPool, Slot, QTimer, QEventLoop
from GestureGuide_ui2 import Ui_MainWindow
import sys
import os
import openpyxl as xl
import scipy.io as scio
from random import shuffle

envpath = r'D:\Anaconda\Lib\site-packages\PySide2\plugins\platforms'
os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = envpath
basedir = os.path.dirname(__file__)


class SoundWorker(QRunnable):
    def __init__(self):
        super().__init__()

    @Slot()
    def run(self):
        winsound.Beep(600, 1000)


def get_current_time():

    ct = time.time()
    local_time = time.localtime(ct)
    data_head = time.strftime("%H%M%S", local_time)
    data_secs = (ct - int(ct)) * 1000
    time_stamp = "%s%03d" % (data_head, data_secs)
    return time_stamp


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle('数据采集')
        self.pushButton.pressed.connect(self.start)
        self.MissionTimer.setReadOnly(True)
        self.CurrentGesture.setReadOnly(True)
        self.NextGesture.setReadOnly(True)
        self.GestureNum.setReadOnly(True)
        self.TrialNum.setReadOnly(True)

        self.threadpool = QThreadPool()

        self.today = datetime.date.today()
        self.flag = 0
        self.comboBox.currentTextChanged.connect(self.numTrain_changed)
        self.num_train = 2

    def numTrain_changed(self,s):
        self.num_train = int(s)

    def plot_image1(self, image):
        pixmap = QPixmap(image).scaled(self.CurrentFig.size())
        self.CurrentFig.setPixmap(pixmap)
        self.CurrentFig.show()

    def plot_image2(self, image):
        pixmap = QPixmap(image).scaled(self.CurrentFig.size())
        self.NextFig.setPixmap(pixmap)
        self.NextFig.show()

    def start(self):

        self.SubjectID.setReadOnly(True)
        self.pushButton.setEnabled(False)
        gesture = ['手腕左曲+手指放松', '手腕右曲+手指放松', '伸食指', '伸中指+无名指+小指', '拇指与中指双击']
        TotalGesture = 5
        TotalTrial = self.num_train
        TimeDuration = [2, 1]

        ID = self.SubjectID.text()
        path = basedir + '/DataSave/' + ID + '_label/'
        LogFileName = path + '/' + ID + '_trigger.xlsx'
        LogMat = path + '/' + ID + '_label.mat'
        isExists = os.path.exists(path)
        if not isExists:
            os.makedirs(path)
            print("目录已创建")
            self.flag = 1
        else:
            dlg = QMessageBox(self)
            dlg.setWindowTitle('Warning')
            dlg.setText('目录已存在，是否覆盖该ID所对应的目录？')
            dlg.setIcon(QMessageBox.Question)
            yes_btn = dlg.addButton("是", QMessageBox.YesRole)
            dlg.addButton("否", QMessageBox.NoRole)
            dlg.exec_()
            if dlg.clickedButton() == yes_btn:
                shutil.rmtree(path)
                print("已删除旧目录")
                os.makedirs(path)
                print("目录已创建")
                self.flag = 1
            else:
                self.flag = 0

        if self.flag == 1:

            randIndex = list(range(5))
            shuffle(randIndex)
            workbook = xl.Workbook()
            workbook.save(LogFileName)
            wb = xl.load_workbook(LogFileName)
            sheet = wb.active
            dlg = QMessageBox(self)
            dlg.setWindowTitle('hint')
            dlg.setText(
                '休息:\n保持身体坐姿和手臂姿态\n手臂尽量放松不要发力\n动作:\n跟随指引,尽量在1秒内做完整个动作\n实验开始前保持身体稳定')
            dlg.setIcon(QMessageBox.Information)
            dlg.exec_()
            EventTimingtemp = []
            EventTimingtemp.append(['数据采集开始', get_current_time()])
            for tt in range(TotalTrial):
                for tg in range(TotalGesture):
                    self.GestureNum.setText(str(tg+1))
                    self.TrialNum.setText(str(tt+1))
                    self.CurrentGesture.setText(gesture[randIndex[tg]])
                    self.plot_image1(basedir + '/Gesture_Fig/' + str(randIndex[tg]+1)+'.png')

                    if tt == TotalTrial - 1 and tg == TotalGesture - 1:
                        self.NextGesture.setText('无')
                        self.plot_image2(basedir + '/Gesture_Fig/0.png')
                    elif tg == TotalGesture - 1:
                        self.plot_image2(basedir + '/Gesture_Fig/' + str(randIndex[0] + 1) + '.png')
                        self.NextGesture.setText(gesture[randIndex[0]])
                    else:
                        self.plot_image2(basedir + '/Gesture_Fig/' + str(randIndex[tg + 1] + 1) + '.png')
                        self.NextGesture.setText(gesture[randIndex[tg + 1]])
                    # if tg < TotalGesture - 1:
                    #     self.plot_image2(basedir + '/Gesture_Fig/' + str(randIndex[tg+1]+1)+'.png')
                    #     self.NextGesture.setText(gesture[randIndex[tg+1]])
                    # else:
                    #     self.NextGesture.setText('无')
                    #     self.plot_image2(basedir + '/Gesture_Fig/0.png')

                    EventTimingtemp.append([gesture[randIndex[tg]]+'第'+str(tt+1)+'组开始', get_current_time()])

                    for td in range(len(TimeDuration)):
                        # if td == 1:
                        #     worker = SoundWorker()
                        #     self.threadpool.start(worker)

                        for i in range(TimeDuration[td]):
                            self.MissionTimer.setText(str(TimeDuration[td]-i))
                            if td != 1 :
                                loop = QEventLoop()
                                QTimer.singleShot(1000, loop.quit)
                                loop.exec_()

                            # 动图
                            if td == 1:
                                worker = SoundWorker()
                                self.threadpool.start(worker)
                                for tp in range(10):
                                    self.plot_image1(basedir + '/Gesture_Fig/' + str(randIndex[tg]+1) + '.' + str(tp+1)
                                                     + '.png')
                                    if tp < 9:
                                        loop = QEventLoop()
                                        QTimer.singleShot(100, loop.quit)
                                        loop.exec_()
                                loop = QEventLoop()
                                QTimer.singleShot(100, loop.quit)
                                loop.exec_()

                            if i == TimeDuration[td]-1:
                                self.MissionTimer.setText('0')

                                loop = QEventLoop()
                                QTimer.singleShot(1000, loop.quit)
                                loop.exec_()

                    EventTimingtemp.append([gesture[randIndex[tg]] + '第' + str(tt + 1) + '组结束', get_current_time()])
                scio.savemat(LogMat, {'randIndex': randIndex})
            EventTimingtemp.append(['数据采集结束', get_current_time()])
            for j in EventTimingtemp:
                sheet.append(j)
            wb.save(LogFileName)

        self.pushButton.setEnabled(True)
        self.SubjectID.setReadOnly(False)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()






