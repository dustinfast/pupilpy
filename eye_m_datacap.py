""" eye_m_datacap.py - The data logging module for eye_m.
    Obtains eye coords from eye_m_face. Also sends data to eye_m_learn
    at regular intervals.
"""

__author__ = "Dustin Fast (dustin.fast@outlook.com)"

import time
import threading
from eye_m_lib import Queue
from eye_m_lib import get_sqlconn
from eye_m_track import get_xyz

class learn(object):
    """ TODO
    """

    def __init__(self, data_hz, ann_path=None):
        """ TODO
        """
        maxrows = int(data_hz * (600 * str(data_hz)[::-1].find('.')))        
        self.data_rows = Queue(maxsize=maxrows)
        self.learn_thread = threading.Thread(target=self._learn,)
        self.data_thread = threading.Thread(target=self._data)
        self.data_hz = data_hz
        self.curr_error = 100
        self.threads_on = None
        self.ann = None  # TODO
        

    # Threaded
    def _datcap(self):
        """ Aggregates predicted pupil x, y, z data into self.data_rows at 
        self.data_hz. At a temporal depth of 1 second, aggregated data is sent
        to eye_m_learn through self._learn().
        """
        while True:
            # # Get eye xyz
            # left_x, left_y = 0
            # right_x, right_y = 0
            # left z, right, z = 0
            # predictoin_accuracy = ...
            # # get_xyz()
            # print([x,y,z])
            # self.data_rows.shove([x, y, z])

            break

            # if not self.threads_on:
            #     break

            

            # If max rows
              # log data
              # _learn()

            time.sleep(self.data_hz)
        print('b')

    # Threaded
    def _learn(self):
        """ Sends data to eye_m_earn
        """
        # For testing, wait for space instead of mouse-click
        # for row in self.data_rows.get_list():
        #     print(row)
        
        # if not self.threads_on:
        #         break
        pass

    def _wait_for(self):
        """ Waits for a mouse click and, on-click, does self._datacap
        """
        # For testing, wait for space instead of mouse-click
        # for row in self.data_rows.get_list():
        #     print(row)

        # if not self.threads_on:
        #         break
        pass

    def start(self):
        """ Starts the learning threads.
        """
        print('eye_m is learning...')

        # Start data collection and learning threads
        self.threads_on = True
        self.data_thread.start()
        self.learn_thread.start()
        
    def stop(self):
        """ Stop learning threads
        """
        self.threads_on = None

    def status(self):
        """ Outputs status to console.
        """
        if self.data_thread.isAlive():
            print('Data Thread: On')
        else:
            print('Data Thread: Off')

        if self.learn_thread.isAlive():
            print('Learning Thread: On')
        else:
            print('Learning Thread: Off')
        