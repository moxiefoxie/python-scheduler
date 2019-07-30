import time
from datetime import datetime, timedelta


print(datetime.strftime(datetime.now() - timedelta(7), '%m/%d/%Y'))
