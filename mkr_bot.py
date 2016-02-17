import telepot
from logger import Logger
from commander import Commander


class MkrBot(telepot.helper.ChatHandler):
    _logger = None
    _commander = None

    def __init__(self, seed_tuple, timeout, log_path, log_level):
        super(MkrBot, self).__init__(seed_tuple, timeout)
        self._logger = Logger(log_path, log_level)
        self._commander = Commander()

    def on_message(self, msg):
        # check valid users
        # ...

        contents_type, chat_type, chat_id = telepot.glance(msg)

        if contents_type is 'text':
            self._handle_command(msg['text'])
            self.sender.sendMessage(msg['text'])
            return

        # self._logger.log('{0}, {1}, {2}'.format(contents_type, chat_type, chat_id))

    def _handle_command(self, text):
        # parse text
        self._commander.handle_command(text)