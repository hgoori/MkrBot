import telepot


class MkrBot:
    _bot = None

    def __init__(self, token):
        self._bot = telepot.Bot(token)
        print(self._bot.getMe())
