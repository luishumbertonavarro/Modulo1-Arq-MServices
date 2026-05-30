from __future__ import annotations

from abc import ABC, abstractmethod

from .models import ReportData


class ProcessingStrategy(ABC):
    @abstractmethod
    def process(self, data: ReportData) -> str:
        pass


class ExecutiveStrategy(ProcessingStrategy):
    def process(self, data: ReportData) -> str:
        profit = data.revenue - data.expenses
        return (
            "Reporte Ejecutivo\n"
            f"Ingresos: {data.revenue:.2f}\n"
            f"Gastos: {data.expenses:.2f}\n"
            f"Utilidad: {profit:.2f}\n"
        )


class AuditorStrategy(ProcessingStrategy):
    def process(self, data: ReportData) -> str:
        profit = data.revenue - data.expenses
        margin = (profit / data.revenue * 100) if data.revenue else 0.0
        return (
            "Reporte de Auditoria\n"
            f"Ingresos: {data.revenue:.2f}\n"
            f"Gastos: {data.expenses:.2f}\n"
            f"Utilidad: {profit:.2f}\n"
            f"Margen: {margin:.2f}%\n"
        )


class AnalystStrategy(ProcessingStrategy):
    def process(self, data: ReportData) -> str:
        ratio = (data.expenses / data.revenue) if data.revenue else 0.0
        return (
            "Reporte de Analisis\n"
            f"Ingresos: {data.revenue:.2f}\n"
            f"Gastos: {data.expenses:.2f}\n"
            f"Relacion de Gastos: {ratio:.4f}\n"
            "Sugerencia: revisar los centros de costo con relacion mayor a 0.60\n"
        )
