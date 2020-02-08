from io import BytesIO
import threading
import time
import os

class WriteFileThread(threading.Thread):
    def __init__(self, filename, buffer):
        threading.Thread.__init__(self)
        self.filename = filename
        self.buffer = buffer

    def run(self):
        self.buffer.seek(0)
        with open(self.filename, 'wb') as f:
            while True:
                data = self.buffer.read(1024)
                if not data:
                    break

                f.write(data)
                time.sleep(.1)

        self.buffer.close()

buffer = BytesIO()
buffer.write(os.urandom(1024 * 60))

t = WriteFileThread('data.bin', buffer)
t.start()
t.join()
