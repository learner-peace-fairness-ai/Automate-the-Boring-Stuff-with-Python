from datetime import datetime
import time

helloween2030 = datetime(2030, 10, 31, 0, 0, 0)
while datetime.now() < helloween2030:
    time.sleep(1)
