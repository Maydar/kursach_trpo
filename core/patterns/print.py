from abc import abstractmethod, ABC

import xlsxwriter


class Printer(ABC):

    @abstractmethod
    def print(self, output):
        raise NotImplementedError()


class XLSPrinter(Printer):

    def print(self, output):
        book = xlsxwriter.Workbook(output)
        sheet = book.add_worksheet('report')
        sheet.write(0, 0, 'report')
        book.close()

        return output


class ProxyXLSPrinter(Printer):

    def __init__(self):
        self.printer = None

    def print(self, output):
        if not self.printer:
            self.printer = XLSPrinter()
        return self.printer.print(output)