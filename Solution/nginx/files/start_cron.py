#! /usr/bin/env python3

from crontab import CronTab

if __name__ == '__main__':
    cron = CronTab(user='root')
    cron.remove_all()
    job = cron.new(command='sed -i "s/is .*$/is $(($(ps -o etimes= -p $(cat /var/run/nginx.pid)) / 60)) minutes/" '
                           '/opt/service_state', comment='Nginx uptime update')
    job.minute.every(1)
    cron.write()
    print('Running cron')
