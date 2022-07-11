from src.domain.entities.Example import Example
from src.infrastructure.interfaces import IExample


class CalculateExamples:
    iExample: IExample

    def __int__(self, iExample: IExample):
        if not issubclass(iExample, IExample.IExample):
            raise TypeError
        self.iExample = iExample

    def calculateValuesWithSameName(self, example1: Example, example2: Example):
        if example1.name == example2.name:
            result = example1.value + example2.value
            self.iExample.addItem(result=result)
