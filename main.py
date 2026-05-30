from src.reporting import (
    BaseReportContent,
    ReportDeliveryService,
    FormatterFactory,
    HeaderDecorator,
    ReportData,
    ReportService,
    WatermarkDecorator,
)


def caso_1() -> None:
    data = ReportData(revenue=150000, expenses=80000)
    service = ReportService()
    # Strategy: se elige la estrategia segun el tipo de usuario.
    raw = service.generate("ejecutivo", data)

    content = BaseReportContent(raw)
    # Factory: se crea el formateador segun el formato pedido.
    formatter = FormatterFactory.create("pdf")
    output = formatter.format(content.get_content())
    delivery_service = ReportDeliveryService()
    delivery_service.deliver(output, "email", "ejecutivo@finantech.com")


def caso_2() -> None:
    data = ReportData(revenue=200000, expenses=90000)
    service = ReportService()
    # Strategy: cambia el procesamiento para el usuario auditor.
    raw = service.generate("auditor", data)

    content = BaseReportContent(raw)
    # Decorator: agrega un encabezado sin modificar el contenido base.
    content = HeaderDecorator(content, "FINANTECH SOLUTIONS - CONFIDENTIAL")
    # Factory: crea el formateador de salida.
    formatter = FormatterFactory.create("excel")
    output = formatter.format(content.get_content())
    delivery_service = ReportDeliveryService()
    delivery_service.deliver(output, "folder", "\\\\Servidor\\Reportes\\Auditoria")


def caso_3() -> None:
    data = ReportData(revenue=175000, expenses=110000)
    service = ReportService()
    # Strategy: aplica la logica de procesamiento para analista.
    raw = service.generate("analista", data)

    content = BaseReportContent(raw)
    # Decorator: se pueden encadenar mejoras opcionales.
    content = HeaderDecorator(content, "FINANTECH SOLUTIONS - INTERNAL USE")
    content = WatermarkDecorator(content, "ANALYSIS COPY")
    # Factory: selecciona el formato final del reporte.
    formatter = FormatterFactory.create("csv")
    output = formatter.format(content.get_content())
    delivery_service = ReportDeliveryService()
    delivery_service.deliver(output, "api", "https://api.finantech.local/reportes")


if __name__ == "__main__":
    caso_1()
    caso_2()
    caso_3()
