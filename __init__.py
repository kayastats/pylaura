
import telebot
import logging


class Laura:
    __notificator_list = ["telegram"]
    __logger = logging.getLogger(__name__)

    def __init__(self, app_name, **kwargs):
        self._telebot_status = False
        if "notificator" in kwargs.keys():
            if kwargs["notificator"] in self.__notificator_list:
                self.notificator = kwargs["notificator"]
                if kwargs["notificator"].lower() == 'telegram':
                    self.bot = telebot.TeleBot(kwargs["bot_key"])
                    self.chat_id = kwargs["chat_id"]
                    self._telebot_status = True
        self.__app_name = app_name

    def __telebot_reporter(self, message):
        self.bot.send_message(self.chat_id, message)

    def connection_handler(self, func):
        def inner_function(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except Exception as e:

                report = {"app_name": self.__app_name, "function": func.__name__, "error": str(e),
                          "type": type(e).__name__}

                if self._telebot_status:

                    self.__telebot_reporter(
                        "pyLaura: Exception rased \nApp: {0} \nFunction name: {1} \nType: {2} \nException message: {3}".format(
                            report["app_name"],
                            report["function"],
                            report["type"],
                            report["error"]
                        ))

                else:
                    return report

        return inner_function
