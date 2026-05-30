from abc import ABC, abstractmethod


class Formatter(ABC):
    @abstractmethod
    def format(self, content: str) -> str:
        pass


class PdfFormatter(Formatter):
    def format(self, content: str) -> str:
        return f"SALIDA_PDF\n{content}"


class ExcelFormatter(Formatter):
    def format(self, content: str) -> str:
        return f"SALIDA_EXCEL\n{content}"


class CsvFormatter(Formatter):
    def format(self, content: str) -> str:
        escaped = content.replace("\n", ";")
        return f"SALIDA_CSV\n{escaped}"
