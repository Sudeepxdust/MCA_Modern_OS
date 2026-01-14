import time
import os

print("Container started")
print("Container PID:", os.getpid())

end_time = time.time() + 30   # run for 30 seconds

while time.time() < end_time:
    pass

print("Container finished execution")
