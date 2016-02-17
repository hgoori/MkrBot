class Commander:
    _cmd_map = dict()

    def __init__(self):
        pass

    def load(self):
        self._cmd_map.clear()

        # load command from file
        # _register(cmd1, handler1)
        # _register(cmd2, handler2)
        # ...

    def _register(self, cmd, handler):
        # put to _cmd_map
        pass

    def handle_command(self, text):
        # return command or handler if command detected
        pass