import os
import sys
import datetime
import winsound
import socket
import binascii
import openpyxl as xl
import pyqtgraph as pg

from PySide2.QtWidgets import QMainWindow, QApplication
from PySide2.QtCore import QRunnable, QThreadPool, Slot, QTimer, QEventLoop, QThread, Signal
from PySide2.QtGui import QPixmap
from EMGBracelet_ui import Ui_MainWindow
from random import shuffle

from utils import *

envpath = r'D:\Anaconda\Lib\site-packages\PySide2\plugins\platforms'
os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = envpath
basedir = os.path.dirname(__file__)


class Worker(QRunnable):  # 存储数据的线程
    def __init__(self, emg_handle, acc_handle, gro_handle, trg_handle, emg, acc, gro, trg):
        super().__init__()
        self.emg_handle = emg_handle
        self.acc_handle = acc_handle
        self.gro_handle = gro_handle
        self.trg_handle = trg_handle
        self.emg = emg
        self.acc = acc
        self.gro = gro
        self.trg = trg

    def run(self):
        for count in range(10):
            EMG = self.emg[count]
            ACC = self.acc[count]
            GRO = self.gro[count]
            TRG = self.trg[count]
            for i in range(100):
                for j in range(8):
                    self.emg_handle.write(str(EMG[j, i]) + ' ')
                    if j == 7:
                        self.emg_handle.write('\n')
                for m in range(3):
                    self.acc_handle.write(str(ACC[m, i]) + ' ')
                    if m == 2:
                        self.acc_handle.write('\n')
                for k in range(3):
                    self.gro_handle.write(str(GRO[k, i]) + ' ')
                    if k == 2:
                        self.gro_handle.write('\n')
            self.trg_handle.write(TRG + '\n')


class WorkThread(QThread):  # 接受数据的线程
    receive = Signal(dict)

    def __init__(self, coon, sk):
        super(WorkThread, self).__init__()
        self.coon = coon
        self.coon.settimeout(0.120)
        self.sk = sk
        self.sk.settimeout(0.5)

    def run(self):
        # global trg, EMG, GRO, ACC
        remain_data = bytes()
        bag_len = 5644
        sign_head = 'aa998877665544332211'  # 标准信号头
        lastIdx = -1
        while 1:
            IMU_GroData_tmp = np.zeros((3, 100))
            IMU_AccData_tmp = np.zeros((3, 100))
            EMG_data_tmp = np.zeros((8, 100))
            total_data = remain_data
            while True:
                print('\n=================================')
                print('waiting for data')
                try:
                    temp = self.coon.recv(1440)
                except Exception as e:
                    print('----接收数据超时----')
                    print('Error Type: ', e)
                    temp = bytes()
                    try:
                        print('断开连接...')
                        self.coon.close()
                        print('尝试重连...')
                        self.coon, addr = self.sk.accept()
                        print('连接成功!!!')
                        self.coon.settimeout(0.120)
                    except Exception as e:
                        print('重连超时: 0.5s')
                        print('Error Type: ', e)
                print(get_current_time(), 'received data: ', len(temp))
                total_data += temp
                if len(total_data) > bag_len * 2:
                    break
            print('大于两倍包长')
            for i in range(len(total_data) - 10):
                Head = total_data[i:i + 10].hex()
                if Head == sign_head:
                    data = total_data[i:i + bag_len]
                    remain_data = total_data[i + bag_len:]
                    trg_tmp = get_current_time()
                    print(trg_tmp, '检测到数据头:  ', i)
                    break
                elif i == len(total_data) - 10-1:
                    print('找不到数据头')

            Type = data[10] + data[11] * 256
            len_a = hex(data[13])  # 16进制数转换成字符串‘0x...’，会带前缀'0x'
            len_b = hex(data[12])
            Length = int(len_a[2:] + len_b[2:], 16)  # 字符串拼接，先收到的数据为高位，后收到的位低位，转int类型

            # print(Head)
            a = hex(binascii.crc32(data[10:14+Length]))[2:]   # crc32校验，输出字符串
            if len(a) < 8:
                for j in range(8 - len(a)):
                    a = '0' + a
            b = data[-4:].hex()  # 转换成字符串，不带前缀
            c = a[-2:] + a[-4:-2] + a[-6:-4] + a[-8:-6]  # 字符串拼接
            # print('Type: ', Type)
            # print('b',b)
            # print('c',c)
            print('Length', Length)
            print('Type', Type)
            print(b == c)
            if b == c and Type == 2 and Length == 5626:
                print('decode success!')
                pack = data[14:5614]
                packetIndex = data[5636] + data[5637] * 256 + data[5638] * 256 * 256 + data[5639] * 256 * 256 * 256
                if packetIndex-lastIdx != 1 and lastIdx != -1:
                    print("丢包", packetIndex-lastIdx-1, '个')
                    print('上一包索引: ', lastIdx)
                    print('当前包索引: ', packetIndex, '\n')
                lastIdx = packetIndex
                idx_read = 0
                for n in range(0, 100):     # 读入100个采样点
                    for channel in range(0, 8):
                        EMG_data_tmp[channel, n] = get_data(pack[idx_read:idx_read + 4])  # 每个数据4字节，4*14通道=56
                        idx_read += 4
                        # EMG_data_tmp[channel, n] = get_data(pack[56*n+channel*4:56*n+channel*4+4])  #每个数据4字节，4*14通道=56
                    for axis in range(0, 3):
                        IMU_GroData_tmp[axis, n] = get_data(pack[idx_read:idx_read+4])
                        IMU_AccData_tmp[axis, n] = get_data(pack[idx_read+12:idx_read+16])
                        idx_read += 4
                        # IMU_GroData_tmp[axis, n] = get_data(pack[56*n+axis*4+32:56*n+axis*4+36])
                        # IMU_AccData_tmp[axis, n] = get_data(pack[56*n+axis*4+44:56*n+axis*4+48])
                    idx_read += 12
            else:
                print('解包失败,补零')
            print('send data')
            self.receive.emit({"EMG": EMG_data_tmp, "ACC": IMU_AccData_tmp, "GRO": IMU_GroData_tmp, "trg": trg_tmp})


class SoundWorker(QRunnable):
    def __init__(self):
        super().__init__()

    @Slot()
    def run(self):
        winsound.Beep(600, 1000)


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle('EMG Bracelet')
        self.pushButton.pressed.connect(self.gesture_guide_start)
        self.MissionTimer.setReadOnly(True)
        self.CurrentGesture.setReadOnly(True)
        self.NextGesture.setReadOnly(True)
        self.GestureNum.setReadOnly(True)
        self.TrialNum.setReadOnly(True)
        self.today = datetime.date.today()
        self.gesture_guide_flag = 0
        self.comboBox.currentTextChanged.connect(self.numTrain_changed)
        self.num_train = 2
        self.threadpool = QThreadPool()
        pen = pg.mkPen(color=(0, 0, 255))

        self.basedir = basedir
        self.EMG1.setBackground("w")
        self.EMG2.setBackground("w")
        self.EMG3.setBackground("w")
        self.EMG4.setBackground("w")
        self.EMG5.setBackground("w")
        self.EMG6.setBackground("w")
        self.EMG7.setBackground("w")
        self.EMG8.setBackground("w")
        self.ACC.setBackground("w")
        self.GRO.setBackground("w")
        self.high = 1000
        self.low = -1000
        self.EMG1.setYRange(self.low, self.high)
        self.EMG2.setYRange(self.low, self.high)
        self.EMG3.setYRange(self.low, self.high)
        self.EMG4.setYRange(self.low, self.high)
        self.EMG5.setYRange(self.low, self.high)
        self.EMG6.setYRange(self.low, self.high)
        self.EMG7.setYRange(self.low, self.high)
        self.EMG8.setYRange(self.low, self.high)
        self.t = np.zeros(10000)
        self.act_acc = np.zeros((3, 10000))
        self.act_gro = np.zeros((3, 10000))
        self.act = np.zeros((8, 10000))
        self.emg1 = self.EMG1.plot(self.t, self.act[0, :], pen=pen)
        self.emg2 = self.EMG2.plot(self.t, self.act[1, :], pen=pen)
        self.emg3 = self.EMG3.plot(self.t, self.act[2, :], pen=pen)
        self.emg4 = self.EMG4.plot(self.t, self.act[3, :], pen=pen)
        self.emg5 = self.EMG5.plot(self.t, self.act[4, :], pen=pen)
        self.emg6 = self.EMG6.plot(self.t, self.act[5, :], pen=pen)
        self.emg7 = self.EMG7.plot(self.t, self.act[6, :], pen=pen)
        self.emg8 = self.EMG8.plot(self.t, self.act[7, :], pen=pen)
        self.ACC.plot(self.t, self.act_acc[0, :], pen=pen)
        self.ACC.plot(self.t, self.act_acc[1, :], pen=pen)
        self.ACC.plot(self.t, self.act_acc[2, :], pen=pen)
        self.GRO.plot(self.t, self.act_gro[0, :], pen=pen)
        self.GRO.plot(self.t, self.act_gro[1, :], pen=pen)
        self.GRO.plot(self.t, self.act_gro[2, :], pen=pen)

        self.train_model_flag = 0
        self.window_len = '1s'
        self.Start.pressed.connect(self.train_model_start)
        self.Stop.pressed.connect(self.train_model_stop)
        self.TrainModel.pressed.connect(self.train)
        self.plus.pressed.connect(self.range_plus)
        self.minus.pressed.connect(self.range_minus)

        self.count = 0
        self.write_flag = True
        self.write_EMG = [None] * 10
        self.write_ACC = [None] * 10
        self.write_GRO = [None] * 10
        self.write_trg = [None] * 10

        # self.comboBox.currentTextChanged.connect(self.text_changed)
        self.WindowLen.currentTextChanged.connect(self.window_len_changed)
        self.crossDay = False

        self.forest_mdl_test = CascadeForestClassifier(max_layers=1, n_estimators=2, n_trees=30, random_state=1,
                                                       n_jobs=-1, backend="sklearn", use_predictor=True)
        self.StartTest.pressed.connect(self.test_model_start)
        self.StopTest.pressed.connect(self.test_model_stop)
        self.EMGdata_test = np.zeros((1000, 8))
        self.Accdata_test = np.zeros((1000, 3))
        self.Grodata_test = np.zeros((1000, 3))
        self.label2_now = 0
        self.cd_new = 0
        self.mode_value = 0

        self.comboBox_18.currentTextChanged.connect(self.mode_changed)
        self.comboBox_2.currentTextChanged.connect(self.crossDay_changed)
        self.crossDay = False

    def numTrain_changed(self, s):
        self.num_train = int(s)

    def plot_image1(self, image):
        pixmap = QPixmap(image).scaled(self.CurrentFig.size())
        self.CurrentFig.setPixmap(pixmap)
        self.CurrentFig.show()

    def plot_image2(self, image):
        pixmap = QPixmap(image).scaled(self.CurrentFig.size())
        self.NextFig.setPixmap(pixmap)
        self.NextFig.show()

    def gesture_guide_start(self):
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
            self.gesture_guide_flag = 1
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
                self.gesture_guide_flag = 1
            else:
                self.gesture_guide_flag = 0

        if self.gesture_guide_flag == 1:
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
                        for i in range(TimeDuration[td]):
                            self.MissionTimer.setText(str(TimeDuration[td]-i))
                            if td != 1:
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

    def range_plus(self):
        self.high = self.high / 10
        self.low = self.low / 10
        self.EMG1.setYRange(self.low, self.high)
        self.EMG2.setYRange(self.low, self.high)
        self.EMG3.setYRange(self.low, self.high)
        self.EMG4.setYRange(self.low, self.high)
        self.EMG5.setYRange(self.low, self.high)
        self.EMG6.setYRange(self.low, self.high)
        self.EMG7.setYRange(self.low, self.high)
        self.EMG8.setYRange(self.low, self.high)

    def range_minus(self):
        self.high = self.high * 10
        self.low = self.low * 10
        self.EMG1.setYRange(self.low, self.high)
        self.EMG2.setYRange(self.low, self.high)
        self.EMG3.setYRange(self.low, self.high)
        self.EMG4.setYRange(self.low, self.high)
        self.EMG5.setYRange(self.low, self.high)
        self.EMG6.setYRange(self.low, self.high)
        self.EMG7.setYRange(self.low, self.high)
        self.EMG8.setYRange(self.low, self.high)

    def text_changed(self, s):
        self.com_num = s

    def window_len_changed(self, s):
        self.window_len = s

    def mode_change(self, s):
        if "cross" in s:
            self.crossDay = True
        else:
            self.crossDay = False
        print(self.crossDay)

    def train_model_start(self):
        self.Start.setEnabled(False)

        ID = self.SubjectID.text()
        path = self.basedir + '/DataSave/' + ID
        fileIDEMG = path + '/' + ID + '_EMGData.txt'
        fileIDAcc = path + '/' + ID + '_AccData.txt'
        fileIDGro = path + '/' + ID + '_GroData.txt'
        filetrigger = path + '/' + ID + '_Trigger.txt'
        isExists = os.path.exists(path)

        if not isExists:
            os.makedirs(path)
            print("目录已创建")
            self.train_model_flag = 1
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
                print("新目录已创建")
                self.train_model_flag = 1
            else:
                self.SubjectID.setReadOnly(False)
                self.Start.setEnabled(True)
                self.train_model_flag = 0

        if self.train_model_flag == 1:
            self.sk = socket.socket(socket.AF_INET,
                                    socket.SOCK_STREAM)  # 创建socket对象，同时设置通信模式，AF_INET代表IPv4，SOCK_STREAM代表流式socket，使用的是tcp协议
            self.sk.bind(('192.168.16.100', 8080))  # 绑定到设置的ip和端口元组
            self.sk.listen(5)  # 开始监听，5位最大挂起的连接数
            self.sk.settimeout(10)
            print('开始等待连接')
            # accept()方法被动接受客户端连接，阻塞，等待连接.
            # coon是客户端的socket对象，可以实现消息的接收和发送，addr表示客户端的地址
            self.coon, addr = self.sk.accept()

            # 23/02/14更新： 连接失败时继续重连
            while len(self.coon.recv(1440)) == 0:
                print('连接断开，尝试重连...')
                self.coon.close()
                self.coon, addr = self.sk.accept()
            # self.sk.settimeout(150)
            # self.coon.setblocking(False)
            self.coon.settimeout(0.120)
            print('连接成功')
            self.fileIDEMG_handle = open(fileIDEMG, mode='w')
            self.fileIDAcc_handle = open(fileIDAcc, mode='w')
            self.fileIDGro_handle = open(fileIDGro, mode='w')
            self.filetrigger_handle = open(filetrigger, mode='w')
            self.thread = WorkThread(self.coon, self.sk)
            self.thread.start()
            self.thread.receive.connect(self.update_data)

    def train_model_stop(self):
        self.thread.terminate()
        self.fileIDEMG_handle.close()
        self.fileIDAcc_handle.close()
        self.fileIDGro_handle.close()
        self.filetrigger_handle.close()
        self.coon.close()
        self.sk.close()
        print(self.sk)
        print('全部内容已关闭')
        self.SubjectID.setReadOnly(False)
        self.Start.setEnabled(True)

    def update_data(self, s):
        # global trg, EMG, GRO, ACC
        EMG = s["EMG"]
        GRO = s["GRO"]
        ACC = s["ACC"]
        trg = s["trg"]

        self.ACC.clear()
        self.GRO.clear()

        tmp_t = np.linspace(self.t[-1] + 0.001, self.t[-1] + 10, 10000)
        self.t = tmp_t

        tmp_act = np.zeros((8, 10000))
        tmp_act[:, 0:100] = EMG
        tmp_act[:, 100:] = self.act[:, 0:9900]
        self.act = tmp_act

        tmp_act_acc = np.zeros((3, 10000))
        tmp_act_acc[:, 0:100] = ACC
        tmp_act_acc[:, 100:] = self.act_acc[:, 0:9900]
        self.act_acc = tmp_act_acc

        tmp_act_gro = np.zeros((3, 10000))
        tmp_act_gro[:, 0:100] = GRO
        tmp_act_gro[:, 100:] = self.act_gro[:, 0:9900]
        self.act_gro = tmp_act_gro

        if self.window_len == '0.1s':
            wl = 100
        elif self.window_len == '1s':
            wl = 1000
        else:
            wl = 10000

        self.emg1.setData(self.t[:wl], self.act[0, :wl])
        self.emg2.setData(self.t[:wl], self.act[1, :wl])
        self.emg3.setData(self.t[:wl], self.act[2, :wl])
        self.emg4.setData(self.t[:wl], self.act[3, :wl])
        self.emg5.setData(self.t[:wl], self.act[4, :wl])
        self.emg6.setData(self.t[:wl], self.act[5, :wl])
        self.emg7.setData(self.t[:wl], self.act[6, :wl])
        self.emg8.setData(self.t[:wl], self.act[7, :wl])
        self.ACC.plot(self.t[:wl], self.act_acc[0, :wl], pen=(255, 0, 0))
        self.ACC.plot(self.t[:wl], self.act_acc[1, :wl], pen=(0, 255, 0))
        self.ACC.plot(self.t[:wl], self.act_acc[2, :wl], pen=(0, 0, 255))
        self.GRO.plot(self.t[:wl], self.act_gro[0, :wl], pen=(255, 0, 0))
        self.GRO.plot(self.t[:wl], self.act_gro[1, :wl], pen=(0, 255, 0))
        self.GRO.plot(self.t[:wl], self.act_gro[2, :wl], pen=(0, 0, 255))

        if self.write_flag:
            self.write_EMG[self.count] = EMG
            self.write_ACC[self.count] = ACC
            self.write_GRO[self.count] = GRO
            self.write_trg[self.count] = trg
            self.count += 1
            if self.count == 10:
                self.count = 0
                write_worker = Worker(self.fileIDEMG_handle, self.fileIDAcc_handle, self.fileIDGro_handle,
                                      self.filetrigger_handle, self.write_EMG, self.write_ACC, self.write_GRO,
                                      self.write_trg)
                self.threadpool.start(write_worker)

            print("OVER")

    def train(self):
        ID = self.SubjectID.text()
        path = self.basedir + '/DataSave/'

        if self.crossDay:
            num_train = 1
            num_source_train = 2
            sourceID = self.source.text()
            label_preprocess(path, ID, num_train)
            # data_preprocess(path, ID, num_train)
            data_preprocess2(self, path, ID, num_train)
            snr_channel_mean, snr_mean = snr_train(self, path, ID, num_train)
            deep_forest_online_train(path, ID, sourceID, num_train, num_source_train, snr_channel_mean)
        else:
            num_train = 5
            label_preprocess(path, ID, num_train)
            # data_preprocess(path, ID, num_train)
            data_preprocess2(self, path, ID, num_train)
            snr_channel_mean, snr_mean = snr_train(self, path, ID, num_train)
            online_train(path, ID, num_train, snr_channel_mean)

        self.SNR1.setText(str(snr_channel_mean[0])[:6])
        self.SNR2.setText(str(snr_channel_mean[1])[:6])
        self.SNR3.setText(str(snr_channel_mean[2])[:6])
        self.SNR4.setText(str(snr_channel_mean[3])[:6])
        self.SNR5.setText(str(snr_channel_mean[4])[:6])
        self.SNR6.setText(str(snr_channel_mean[5])[:6])
        self.SNR7.setText(str(snr_channel_mean[6])[:6])
        self.SNR8.setText(str(snr_channel_mean[7])[:6])
        self.SNR.setText(str(snr_mean)[:6])

        dlg = QMessageBox(self)
        dlg.setWindowTitle("Info")
        dlg.setText("模型训练完毕")
        dlg.setIcon(QMessageBox.Information)
        dlg.exec_()

    def mode_changed(self, s):
        if s == 'high-accuracy':
            self.mode_value = 0
        if s == 'high-sensitivity':
            self.mode_value = 1

    def crossDay_changed(self, s):
        if "cross" in s:
            self.crossDay = True
        else:
            self.crossDay = False
        print(self.crossDay)

    def plot_image(self, image):
        pixmap = QPixmap(image).scaled(self.GestureResultFig.size())
        self.GestureResultFig.setPixmap(pixmap)
        self.GestureResultFig.show()

    def test_model_start(self):
        self.SubjectID.setReadOnly(True)
        self.StartTest.setEnabled(False)
        self.write_flag = False
        self.ID = self.SubjectID.text()
        self.path = self.basedir + '/DataSave/' + self.ID + '/' + self.ID + '_train_data.mat'

        if self.crossDay:
            self.forest_mdl_test.load(self.basedir + '/DataSave/' + self.ID + '/' + self.ID + 'forest')
            self.mdl1 = svm_load_model(self.ID + 'mdl')
        self.cd_time = get_current_time()
        self.cd_time = int(self.cd_time[-5:])

        self.sk = socket.socket(socket.AF_INET,
                                socket.SOCK_STREAM)  # 创建socket对象，同时设置通信模式，AF_INET代表IPv4，SOCK_STREAM代表流式socket，使用的是tcp协议
        self.sk.bind(('192.168.16.100', 8080))  # 绑定到设置的ip和端口元组
        self.sk.listen(5)  # 开始监听，5位最大挂起的连接数
        self.sk.settimeout(10)

        # accept()方法被动接受客户端连接，阻塞，等待连接.
        # coon是客户端的socket对象，可以实现消息的接收和发送，addr表示客户端的地址
        self.coon, addr = self.sk.accept()

        # 23/02/14更新： 连接失败时继续重连
        while len(self.coon.recv(1440)) == 0:
            print('连接断开，尝试重连...')
            self.coon.close()
            self.coon, addr = self.sk.accept()
        self.coon.settimeout(0.120)
        print('连接成功')

        self.thread = WorkThread(self.coon, self.sk)
        self.thread.start()
        self.thread.receive.connect(self.update_data)
        self.thread.receive.connect(self.show_result)
        self.label_temp = 0

    def test_model_stop(self):
        self.thread.terminate()

    def show_result(self, s):
        global currentFig
        EMG = s["EMG"]

        self.EMGdata_test[0:900, :] = self.EMGdata_test[100:1000, :]
        self.EMGdata_test[900:1000, :] = EMG.T
        # self.Grodata_test[0:900, :] = 0
        # self.Accdata_test[0:900, :] = 0
        # self.Grodata_test[0:900, :] = self.Grodata_test[100:1000, :]
        # self.Grodata_test[900:1000, :] = GRO.T
        # self.Accdata_test[0:900, :] = self.Accdata_test[100:1000, :]
        # self.Accdata_test[900:1000, :] = ACC.T
        label2_last = self.label2_now
        cd_last = self.cd_new
        time_now = get_current_time()
        time_now = int(time_now[-5:])

        if self.crossDay:
            label_now, self.label2_now, self.cd_new, self.cd_time = deep_forest_online_test(self.ID, self.path, self.EMGdata_test,
                                                                                self.Grodata_test, self.Accdata_test,
                                                                                label2_last, cd_last, self.cd_time,
                                                                                time_now, self.mode_value, self.forest_mdl_test, self.mdl1)
        else:
            label_now, self.label2_now, self.cd_new, self.cd_time = online_test(self.ID, self.path, self.EMGdata_test,
                                                                                self.Grodata_test, self.Accdata_test,
                                                                                label2_last, cd_last, self.cd_time,
                                                                                time_now, self.mode_value)

        if label_now == self.label_temp and int(label_now) != 0:
            if label_now == 1 or label_now == 2:
                print('00000000000000000000000000000000000000000000000')
                self.speed.setText('X2')
        elif int(label_now) != 0:
            print('11111111111111111111111111111111111111111111111')
            self.speed.setText('X1')

        if self.cd_new == 1:
            if cd_last == 0:
                currentFig = self.basedir + '/Gesture_Fig/' + str(int(label_now)) + '.png'
                if int(label2_last) != 0:
                    self.label_temp = label_now
        if self.cd_new == 0:
            currentFig = self.basedir + '/Gesture_Fig/0.png'
        self.plot_image(currentFig)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()
