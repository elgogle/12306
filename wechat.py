# -*- coding=utf-8 -*-
from wxpy import *

bot = Bot()

bot.self.add()
bot.self.accept()
file_helper = bot.file_helper
friend = bot.friends().search(u'妈妈')[0]

