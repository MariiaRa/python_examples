import time
phrase = "CRON"
   
def follow(syslog_file):
    syslog_file.seek(0,1) # Go to the end of the file
    while True:
        line = syslog_file.readline()
        if not line:
            time.sleep(0.1) # Sleep briefly
            continue
        elif phrase in line:
            yield line


if __name__ == '__main__':
    logfile = open("/var/log/syslog", "r")
    loglines = follow(logfile)
    for line in loglines:
        print(line)


