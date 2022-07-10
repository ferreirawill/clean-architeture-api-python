class ApplicationException(Exception):
    def __init__(self, errorInfo, exception: Exception = None) -> None:
        super().__init__()
        self.exception = exception
        self.errorInfo = errorInfo


class DataException(ApplicationException):
    pass


class ServiceException(ApplicationException):
    pass
