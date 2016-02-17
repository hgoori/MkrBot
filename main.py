import sys
import telepot
from telepot.delegate import per_chat_id, create_open
from mkr_bot import MkrBot

token = sys.argv[1]
log_path = sys.argv[2]

bot = telepot.DelegatorBot(token, [
    (per_chat_id(), create_open(MkrBot, timeout=10, log_path=log_path, log_level=10),)
])
print(bot.getMe())
bot.notifyOnMessage(run_forever=True)
