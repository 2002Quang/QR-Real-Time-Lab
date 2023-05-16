import time
from scheduler import *
from task1 import *
from task2 import *
scheduler = Scheduler()
scheduler.SCH_Init()

task1 = Task1()
task2 = Task2()

task1.Task1_Run()
task2.Task2_Run()