"""
@author: angelia
"""
import os
import logging
from config.config import LOG_FILE, LOG_LEVEL, LOG_FILEMODE


class Log:
    _single = None
    _fileHdlr = None
    _logger = None
    _levelDict = {"debug": logging.DEBUG,
                  "info": logging.INFO,
                  "warn": logging.WARNING,
                  "error": logging.ERROR,
                  "critical": logging.CRITICAL
                  }

    # singleton
    # private, can not invoke
    def __init__(self):
        if Log._single:
            raise Log._single
        Log._single = self

    @staticmethod
    def getinstance():
        try:
            _single = Log()
        except Log, s:
            _single = s
        return _single

    @staticmethod
    def getlog():
        try:
            if Log._logger is None:
                Log._logger = logging.getLogger('simple')
                if Log._fileHdlr is None:
                    path = os.getcwd().split("testcase")[0]
                    logfile = path + LOG_FILE
                    if os.path.exists(logfile):
                        filename = logfile
                    else:
                        filename = 'logs/log.log'
                    Log._fileHdlr = logging.FileHandler(filename, LOG_FILEMODE)
                    formatter = logging.Formatter(
                         '%(asctime)s %(levelname)s %(message)s')
                    Log._fileHdlr.setFormatter(formatter)
                    Log._logger.addHandler(Log._fileHdlr)
                    Log._logger.setLevel(Log._levelDict.get(LOG_LEVEL, logging.NOTSET))
        except BaseException:
            pass
        return Log._logger

    @staticmethod
    def info(msg):
        try:
            Log.getlog().info(msg)
        except AttributeError:
            pass

    @staticmethod
    def debug(msg):
        try:
            Log.getlog().debug(msg)
        except AttributeError:
            pass

    @staticmethod
    def exception(msg):
        try:
            Log.getlog().exception(msg)
        except AttributeError:
            pass

    @staticmethod
    def error(msg):
        try:
            Log.getlog().error(msg)
        except AttributeError:
            pass

    @staticmethod
    def close():
        try:
            if Log._fileHdlr is not None:
                Log._logger.removeHandler(Log._fileHdlr)
                Log._logger._fileHdlr.close()
            del Log._logger
        except AttributeError:
            pass
