import sys

from mkr_bot import MkrBot

token = sys.argv[1]
log_path = sys.argv[2]

bot = MkrBot(token, log_path)
