'''
Imports
'''
from src.include.globals import *


class MRE_LogArea(QTextEdit):
    '''
    LogArea class
    Creates a log widget.
    '''

    def __init__(self, win: QMainWindow):
        '''
        Constructor
        '''
        super().__init__()
        self.win = win
        self.level = LOG_INFO
        self.setReadOnly(True)
        self.log("Log level set to '" + LOG_LABELS[self.level] + "'", self.level)
        return

    def log(self, text: str, log_level: int):
        '''
        Diplays the 'text' if the current log level is 'log_level'.
        '''

        # check
        if self.level == LOG_OFF:
            return
        elif self.level != LOG_ALL:
            if self.level != log_level:
                return

        # time
        output = str(self.getTimeStamp()) + " >> "

        if log_level == LOG_ALL:
            output += text

        elif log_level == LOG_CRITICAL:
            output += self.logCRITICAL(text)

        elif log_level == LOG_ERROR:
            output += self.logERROR(text)

        elif log_level == LOG_WARN:
            output += self.logWARNING(text)

        elif log_level == LOG_INFO:
            output += self.logINFO(text)

        elif log_level == LOG_DEBUG:
            output += self.logDEBUG(text)

        else:
            return

        output += "\n"
        self.append(output)

        return

    def logDEBUG(self, log: str):
        '''
        Creates a log message for debugging messages.
        '''
        return "<span style='color: forestgreen'>" + log + "</span>"

    def logINFO(self, log: str):
        '''
        Creates a log message for info messages.
        '''
        return "<span style='color: royalblue'>" + log + "</span>"

    def logWARNING(self, log: str):
        '''
        Creates a log message for warning messages.
        '''
        return "<span style='color: orange'>" + log + "</span>"

    def logERROR(self, log: str):
        '''
        Creates a log message for error messages.
        '''
        return "<span style='color: red'>" + log + "</span>"

    def logCRITICAL(self, log: str):
        '''
        Creates a log message for critical messages.
        '''
        return "<span style='color: mediumpurple'>" + log + "</span>"

    def getTimeStamp(self):
        '''
        Creates a timestamp of the current time.
        '''
        now = datetime.now()
        return now.strftime("%d/%m/%Y %H:%M:%S")

    def setLogLevel(self, level: int):
        '''
        Sets the current log level to 'level'.
        '''
        self.level = level
        return

    def clearLog(self):
        '''
        Clears all messages from the log.
        '''
        self.clear()
        return
