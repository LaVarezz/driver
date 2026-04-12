import threading
import queue
from pickle import TUPLE

from project.engine.utills.logging.log import log_info


class ConsoleManager:
    ''' Модуль для обработки команд в консоли. '''
    def __init__(self, main):
        log_info('Console module connected')
        self._queue = queue.Queue()
        self._thread = threading.Thread(target=self.input_thread, args=(self._queue, ))
        self._thread.daemon = True # Для выхода из потока после завершения программы
        self._thread.start()
        self.main = main
        log_info('Console thread activated')


    def update(self):
        try:
            command = self._queue.get_nowait().lower()
            if "get" in command:
                path = command[4:]
                path = path.split('|')
                try:
                    print(self.main.get_parameter(path, direct=True))
                except Exception as e:
                    print(f'Wrong path: {e}')
            else:
                print('Unknown command')

        except queue.Empty:
            pass


    def input_thread(self, input_queue):
        while True:
            user_input = input()
            input_queue.put(user_input)

