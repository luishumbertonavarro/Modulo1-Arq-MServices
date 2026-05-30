from typing import Dict

from .formatters import CsvFormatter, ExcelFormatter, Formatter, PdfFormatter
from .strategies import (
    AnalystStrategy,
    AuditorStrategy,
    ExecutiveStrategy,
    ProcessingStrategy,
)


class StrategyFactory:
    @staticmethod
    def create(user_type: str) -> ProcessingStrategy:
        strategy_map: Dict[str, ProcessingStrategy] = {
            "ejecutivo": ExecutiveStrategy(),
            "auditor": AuditorStrategy(),
            "analista": AnalystStrategy(),
        }
        key = user_type.lower().strip()
        if key not in strategy_map:
            raise ValueError(f"Unsupported user type: {user_type}")
        return strategy_map[key]


class FormatterFactory:
    @staticmethod
    def create(format_type: str) -> Formatter:
        formatter_map: Dict[str, Formatter] = {
            "pdf": PdfFormatter(),
            "excel": ExcelFormatter(),
            "csv": CsvFormatter(),
        }
        key = format_type.lower().strip()
        if key not in formatter_map:
            raise ValueError(f"Unsupported format type: {format_type}")
        return formatter_map[key]
