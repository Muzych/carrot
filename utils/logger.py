from functools import wraps
import os
import datetime
import loguru


def singleton_class_decorator(cls):
    _instance = {}

    @wraps(cls)
    def wrapper_class(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return wrapper_class


@singleton_class_decorator
class Logger:
    def __init__(self):
        self.logger_add()

    def get_project_path(self, project_path=None):
        if project_path is None:
            project_path = os.path.realpath("..")
        return project_path

    def get_log_path(self):
        project_path = self.get_project_path()
        project_log_dir = os.path.join(project_path, "log")
        project_log_filename = "runtime_{}.log".format(datetime.date.today())
        project_log_path = os.path.join(project_log_dir, project_log_filename)
        return project_log_path

    def logger_add(self):
        loguru.logger.add(
            sink=self.get_log_path(),
            rotation="500 MB",
            retention="30 days",
            format="{time:MMMM D, YYYY > HH:mm:ss!UTC} | {level} | {message}",
            compression="zip",
            encoding="utf-8",
            enqueue=True,
        )

    @property
    def get_logger(self):
        return loguru.logger


logger = Logger().get_logger
