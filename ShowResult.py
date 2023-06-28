from PySide2.QtWidgets import QMainWindow, QApplication
from PySide2.QtCore import QThread, Signal
from PySide2.QtGui import QPixmap
from showResult_ui import Ui_MainWindow
import socket
from sklearnex import patch_sklearn
patch_sklearn()
# from utils import *
import binascii
from utils_crossDay import *
# from deep_forest_utils import *

envpath = r'D:\Anaconda\Lib\site-packages\PySide2\plugins\platforms'
os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = envpath
basedir = os.path.dirname(__file__)
# GRO = np.zeros((3, 100))
# ACC = np.zeros((3, 100))
# EMG = np.zeros((8, 100))
# trg = 'a'


class WorkThread(QThread):  # 接受数据的线程
    receive = Signal(dict)

    def __init__(self, coon, sk):
        super(WorkThread, self).__init__()
        self.coon = coon
        self.coon.settimeout(0.120)
        self.sk = sk
        self.sk.settimeout(0.5)
        # self.ser = ser

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
            for i in range(len(total_data) - 10):
                Head = total_data[i:i + 10].hex()
                if Head == sign_head:
                    data = total_data[i:i + bag_len]
                    remain_data = total_data[i + bag_len:]
                    trg_tmp = get_current_time()
                    break

            Type = data[10] + data[11] * 256
            len_a = hex(data[13])  # 16进制数转换成字符串‘0x...’，会带前缀'0x'
            len_b = hex(data[12])
            Length = int(len_a[2:] + len_b[2:], 16)  # 字符串拼接，先收到的数据为高位，后收到的位低位，转int类型

            print(Head)
            a = hex(binascii.crc32(data[10:14+Length]))[2:]   # crc32校验，输出字符串
            if len(a) < 8:
                for j in range(8 - len(a)):
                    a = '0' + a
            b = data[-4:].hex()  # 转换成字符串，不带前缀
            c = a[-2:] + a[-4:-2] + a[-6:-4] + a[-8:-6]  # 字符串拼接
            print('Type: ', Type)
            print('b',b)
            print('c',c)
            print('Length',Length)
            if b == c and Type == 2 and Length == 5626:
                print('read success!')
                pack = data[14:5614]
                packetIndex = data[5636] + data[5637] * 256 + data[5638] * 256 * 256 + data[5639] * 256 * 256 * 256
                if packetIndex - lastIdx != 1 and lastIdx != -1:
                    print("丢包", packetIndex - lastIdx - 1, '个')
                    print('上一包索引: ', lastIdx)
                    print('当前包索引: ', packetIndex, '\n')
                lastIdx = packetIndex
                idx_read = 0
                for n in range(0, 100): #读入100个采样点
                    for channel in range(0, 8):
                        EMG_data_tmp[channel, n] = get_data(pack[idx_read:idx_read + 4])  # 每个数据4字节，4*14通道=56
                        idx_read+=4
                        #EMG_data_tmp[channel, n] = get_data(pack[56*n+channel*4:56*n+channel*4+4])  #每个数据4字节，4*14通道=56
                    for axis in range(0, 3):
                        IMU_GroData_tmp[axis, n] = get_data(pack[idx_read:idx_read+4])
                        IMU_AccData_tmp[axis, n] = get_data(pack[idx_read+12:idx_read+16])
                        idx_read+=4
                        # IMU_GroData_tmp[axis, n] = get_data(pack[56*n+axis*4+32:56*n+axis*4+36])
                        # IMU_AccData_tmp[axis, n] = get_data(pack[56*n+axis*4+44:56*n+axis*4+48])
                    idx_read+=12
                self.receive.emit({"EMG": EMG_data_tmp, "ACC": IMU_AccData_tmp, "GRO": IMU_GroData_tmp, "trg": trg_tmp})




class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.forest_mdl_test = CascadeForestClassifier(max_layers=1, n_estimators=2, n_trees=30, random_state=1, n_jobs=-1,
                                                  backend="sklearn", use_predictor=True)
        # self.forest_mdl_test.load('D:\Huawei_V2_1122\DataSave\\liangen01sit\\liangen01sitforest')
        self.basedir = basedir
        # self.mdl1 = svm_load_model('liangen01sit' + 'mdl1')
        self.setupUi(self)
        self.setWindowTitle('测试结果')
        self.Start.pressed.connect(self.start)
        self.Stop.pressed.connect(self.stop)

        self.EMGdata_test = np.zeros((1000, 8))
        self.Accdata_test = np.zeros((1000, 3))
        self.Grodata_test = np.zeros((1000, 3))
        self.label2_now = 0
        self.cd_new = 0
        self.mode_value = 0


        self.comboBox_2.currentTextChanged.connect(self.mode_changed)
        self.comboBox_3.currentTextChanged.connect(self.crossDay_changed)
        self.crossDay = False



    def mode_changed(self, s):
        if s == 'high-accuracy':
            self.mode_value = 0
        if s == 'high-sensitivity':
            self.mode_value = 1
    def crossDay_changed(self,s):
        if "cross" in s:
            self.crossDay = True
        else:
            self.crossDay = False
        print(self.crossDay)

    def plot_image(self, image):
        pixmap = QPixmap(image).scaled(self.GestureResultFig.size())
        self.GestureResultFig.setPixmap(pixmap)
        self.GestureResultFig.show()

    def start(self):
        self.SubjectID.setReadOnly(True)
        self.Start.setEnabled(False)

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
        self.thread.receive.connect(self.show_result)
        self.label_temp = 0

    def stop(self):
        self.thread.terminate()
        self.coon.close()
        self.sk.close()

    def show_result(self, s):
        # global trg, EMG, GRO, ACC, currentFig
        global currentFig
        EMG = s["EMG"]
        # GRO = s["GRO"]
        # ACC = s["ACC"]
        # trg = s["trg"]

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



