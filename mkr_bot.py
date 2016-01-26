import telepot
from logger import Logger


class MkrBot:
    _bot = None
    _logger = None

    def __init__(self, token, log_path):
        self._logger = Logger(log_path)
        self._bot = telepot.Bot(token)

        print(self._bot.getMe())
