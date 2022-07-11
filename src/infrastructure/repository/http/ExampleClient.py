from src.infrastructure.interfaces.IExample import IExample


class ExampleClient(IExample):
    def getAllItens(self):
        raise NotImplementedError

    def getItem(self, id):
        raise NotImplementedError

    def addItem(self, **kwargs):
        pass

