#codeing utf-8

import logging,sys,os
import config
from lib import Singleton


@Singleton
class Logger(object):
    def __init__(self):

        tag = 'ProcessDaemon'
        if config.conf.has_key('logging'):
            tag = config.Config.logging['tag']
        self.logger = logging.getLogger(tag)
        self.logger.setLevel(logging.DEBUG)
        self.logger.propagate = False

        if sys.platform == "darwin":
            syslog_address = "/var/run/syslog"
        else:
            syslog_address = "/dev/log"

        syslog = logging.handlers.SysLogHandler(syslog_address)
        syslog.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s %(name)s: %(message)s",
                                          "%b %e %H:%M:%S")
        syslog.setFormatter(formatter)
        self.logger.addHandler(syslog)

    def log(self,msg):
        self.logger.info(msg)
