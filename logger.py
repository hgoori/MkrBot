import logging


class Logger:
    _level = logging.INFO

    def __init__(self, path, level=logging.INFO):
        self._level = level
        logging.basicConfig(filename=path, level=self._level, format='%(asctime)s:%(levelname)s:%(message)s')

    def log_debug(self, log):
        logging.info(log)
        self._log_debug(log)

    def log(self, log):
        logging.info(log)
        self._log_debug(log)

    def log_warning(self, log):
        logging.warning(log)
        self._log_debug(log)

    def log_error(self, log):
        logging.error(log)
        self._log_debug(log)

    def log_fatal(self, log):
        logging.fatal(log)
        self._log_debug(log)

    def _log_debug(self, log):
        if self._level == logging.DEBUG:
            print(log)
