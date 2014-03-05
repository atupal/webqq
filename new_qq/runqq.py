#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  file   : license.py
#  author : atupal
#
#  Copyright 2013 atupal [HUST university uniquestudio algorithm group] <me@atupal.org>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#  site: http://atupal.org

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from login_qq import webqq
import threading
import Queue
from random import randint

msg_queue = Queue.Queue()
test_flag = 5

def poll2_daemon(qq):
    while 1:
        qq.poll2()

class process_msg_daemon(threading.Thread):
    def __init__(self, msg_queue, qq):
        threading.Thread.__init__(self)
        self.msg_queue = msg_queue
        self.qq = qq
        self.locale_message = open('res/message.dat', 'aw')

    def run(self):
        while 1:
            msg = self.msg_queue.get()
            print msg[0], ':', msg[1]
            self.locale_message.write(str(msg[0]) + ':' + str(msg[1]) + '\n')
            if msg[3] == 1:self.qq.sendMsg(msg[2], '我寂寞装逼迷人', face = randint(1,80))
            elif self.qq.gid[msg[2]] == 'test_1' or self.qq.gid[msg[2]] == '啦啦啦*17-422*啦啦啦' or self.qq.gid[msg[2]] == 'zs10634':
                self.qq.sendQunMsg(msg[2], '我寂寞装逼迷人', face = randint(1,80))
            self.msg_queue.task_done()

class senf_msg_daemon(threading.Thread):
    def __init__(self, send_queue):
        threading.Thread.__init__()
        self.send_queue = send_queue

    def run(self):
        while 1:
            send = self.send_queue.get()
            print send
            self.send_queue.task_done()

class runqq(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.lock = threading.Condition()
    def run(self):
        #user = raw_input('QQ:')
        #pwd = getpass.getpass('password: ')

        #user = os.environ['QQ']
        #pwd = os.environ['QQ_PASSWD']
        try:
            with open('./user') as fi:
              user = fi.readline().strip()
              pwd = fi.readline().strip()
        except:
            import getpass
            user = raw_input('QQ:')
            pwd = getpass.getpass('password: ')

        self.user = user
        self.pwd = pwd

        self.qq = webqq(user, pwd, msg_queue)
        self.qq.getSafeCode()
        self.qq.loginGet()
        self.qq.loginPost()
        self.qq.getGroupList()
        self.qq.getFriend()

        self.qq.setDaemon(True)
        self.qq.start()


        #self.pro_msg = process_msg_daemon(msg_queue, self.qq)
        #self.pro_msg.setDaemon(True)
        #self.pro_msg.start()
        #while 1:
        #    msg_queue.join()

import time
if __name__ == "__main__":
    Q = runqq()
    Q.run()
    Q.pro_msg = process_msg_daemon(msg_queue, Q.qq)
    Q.pro_msg.setDaemon(True)
    Q.pro_msg.start()
    while  1:
        time.sleep(10)
        msg_queue.join()
