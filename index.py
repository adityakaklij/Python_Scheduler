
import schedule
import time
from datetime import datetime
import pytz
import pyotp


def write_file(file_path, lines):
    with open(file_path, 'w') as file:
        file.writelines(lines)

IST = pytz.timezone('Asia/Kolkata')
def job():
    print("We are heres.")
    print("Running scheduled job at", datetime.now(IST).strftime("%Y-%m-%d %H:%M:%S"))

def run_continuously(interval=1):
    print("Tasks scheduled from Monday to Friday ", datetime.now(IST).strftime("%Y-%m-%d %H:%M:%S"))
    while True:
        schedule.run_pending()
        time.sleep(interval)

# Schedule the job every Monday to Friday at 5 AM IST
schedule.every().monday.at("05:00").do(job)
schedule.every().tuesday.at("05:00").do(job)
schedule.every().wednesday.at("05:00").do(job)
schedule.every().thursday.at("05:00").do(job)
schedule.every().friday.at("05:00").do(job)

# Start the continuous run
run_continuously()





