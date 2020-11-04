from requests.exceptions import ConnectionError


class Laura:
    __notificator_list = ["telegram"]

    def __init__(self, app_name, **kwargs):
        if "notificator" in kwargs.keys():
            if kwargs["notificator"] in self.__notificator_list:
                self.notificator = kwargs["notificator"]
        self.__app_name = app_name

    def connection_handler(self, func):
        def inner_function(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except ConnectionError as e:
                return {"app_name": self.__app_name, "function": func.__name__}

        return inner_function

