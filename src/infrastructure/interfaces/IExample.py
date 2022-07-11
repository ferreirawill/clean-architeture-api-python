import abc


class IExample(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def getAllItens(self):
        raise NotImplementedError

    @abc.abstractmethod
    def getItem(self, id):
        raise NotImplementedError

    @abc.abstractmethod
    def addItem(self, **kwargs):
        raise NotImplementedError
