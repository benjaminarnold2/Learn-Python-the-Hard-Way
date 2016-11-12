import time
import os
from datetime import datetime
while True:
        current_time = datetime.now().time()
        time_now = current_time.isoformat()
        print time_now
        time.sleep (1)
        os.system('cls')
        
  
