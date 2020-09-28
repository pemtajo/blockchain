import logging, os


class Log:
    def __init__(self, name=""):
        self.looger = logging.getLogger(name)
        self.looger.setLevel(logging.INFO)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        os.makedirs("log", exist_ok=True)
        handlerFile = logging.FileHandler("log/log%s.log" % name)
        handlerFile.setFormatter(formatter)
        self.looger.addHandler(handlerFile)

    def info(self, msg):
        self.looger.info(msg)

    def error(self, msg):
        self.looger.error(msg)
