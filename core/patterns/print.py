from abc import ABCMeta, abstractmethod

import xlsxwriter


class PrinterWeb(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def print(self, output):
        raise NotImplementedError()


class XLSPrinter(PrinterWeb):

    def print(self, output):
        book = xlsxwriter.Workbook(output)
        sheet = book.add_worksheet('report')
        sheet.write(0, 0, 'Hello, world!')
        book.close()

        return output


class ProxyXLSPrinter(PrinterWeb):

    def __init__(self):
        self.printer = None

    def other_method(self):
        print("other_method")

    def print(self, output):
        if not self.printer:
            self.printer = XLSPrinter()
        return self.printer.print(output)