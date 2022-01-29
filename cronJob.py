from crontab import CronTab

if __name__ == '__main__':
    cron = CronTab()
    job = cron.new(command='echo hello_world')

    job.minute.every(1)
    cron.write()
