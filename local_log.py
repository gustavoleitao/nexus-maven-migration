import os
from datetime import datetime

today = datetime.now()


def log(msg):
    if not os.path.exists("./logs"):
        os.makedirs("./logs")
    log_file_name = f"logs/log-upload-{today}.log"
    log_file = open(log_file_name, "a+")
    print(msg)
    log_file.writelines(f"{msg}\n")
    log_file.close()