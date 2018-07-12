import time, smtplib

phrase = 'ERROR'
password = input('Please, enter your password: ')

def follow(syslog_file):
    '''Using the smtplib module, send emails when there is an error in syslog.

            Keyword arguments:
            phrase -- search syslog for this phrase
            password -- password to email box

            Returns: lines from syslog with phrase and sends emails

            '''

    syslog_file.seek(0, 2)  # Go to the end of the file
    while True:
        line = syslog_file.readline()
        if not line:
            time.sleep(0.1)  # Sleep briefly
            continue
        elif phrase in line:
            yield line # Gather lines which contain the phrase


def send_email(password): # Send alert email
    smtpObj = smtplib.SMTP('smtp.i.ua', 465)
    smtpObj.starttls()
    smtpObj.login('my_email@i.ua', password)
    smtpObj.sendmail('my_email@i.ua', 'recipient@gmail.com.com ',
                 'Subject: Error in syslog\nPlease, check syslog, an error has occured.')
    smtpObj.quit()

if __name__ == '__main__':
    logfile = open('/var/log/syslog', 'r')
    loglines = follow(logfile)
    for line in loglines:
        print(line)
#        send_email(password)
