from datetime import datetime
import pprint
from time import sleep

from lorettOrbital.orbital import *
from pprint import pprint
import os
import serial


def start_rotating():
    path = 'C:/Users/User/PycharmProjects/dpp/tracks'
    config = supportedStationTypes['r8s'].copy()
    config['horizon'] = 20
    config['minApogee'] = 60
    station = Scheduler("r8sTest", 54.526731, 36.168006, 0.151, timeZone=24, config=config)
    station.update()


    print(station.getSchedule(12, returnTable=True, saveSchedule=True))
    sat_list = station.nextPass()
    # print(sat_list)
    # print(sat_list[1])
    parametrs = []
    sat_name = sat_list[0]

    if sat_list != 'FENGYUN 3C':
        for i in sat_list[1]:
            parametrs.append([i[1], i[2]])

        start_az, start_el = parametrs[1]
        print(start_az, start_el)
        # com1 = serial.Serial('Миша напиши это плез я не понимаю', 9600)
        # com1.write(sat_name.encode())
        # data = (str(start_az) + ', ' + str(start_el)).encode()
        # com1.write(data)

        if float(parametrs[1][0]) - float(parametrs[2][0]) < 0:
            print('влево')
            # com1.write('-1'.encode())  # влево
        else:
            print('вправо')
            # com1.write('1'.encode())  # вправо

        time = sat_list[1][0][0]
        # print(time)
        time = datetime.strptime(time, "%H:%M:%S").time()
        now = datetime.utcnow().date()
        time = datetime.combine(now, time)
        sleepeng_time = (time - datetime.utcnow()).seconds
        '''
        if datetime.utcnow().timestamp() < time.timestamp():
            print('сплю', sleepeng_time, 'секунд')
            sleep(sleepeng_time)'''


        for i in range(1, len(parametrs), 5):
            # data = (str(i[0]) + ', ' + str(i[1])).encode()
            print(parametrs[i], parametrs.index(parametrs[i]))


if __name__ == '__main__':
    start_rotating()
