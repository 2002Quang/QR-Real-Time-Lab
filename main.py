import time
import scheduler
from task1 import *
from task2 import *
from Task3 import *

scheduler = scheduler.Scheduler()
scheduler.SCH_Init()
#task1 = Task1(0)
# task2 = Task2()
task3 = Task3(0)
task3cam2 = Task3(1)

#scheduler.SCH_Add_Task(task1.Task1Run, 1000, 2000)
scheduler.SCH_Add_Task(task3.Task3Run, 2000, 4000)
scheduler.SCH_Add_Task(task3cam2.Task3Run, 2000, 4000)
while True:
    scheduler.SCH_Update()
    scheduler.SCH_Dispatch_Tasks()
    time.sleep(1)

task1b.camera.release()
task1a.camera.release()
cv2.destroyAllWindows()
