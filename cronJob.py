from crontab import CronTab

if __name__ == '__main__':
    cron = CronTab()
    job = cron.new(command='main.py')

    job.minute.every(1)
    cron.run_pending()
