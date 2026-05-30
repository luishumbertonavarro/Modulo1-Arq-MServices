from __future__ import annotations

from abc import ABC, abstractmethod


class ReportContent(ABC):
    @abstractmethod
    def get_content(self) -> str:
        pass


class BaseReportContent(ReportContent):
    def __init__(self, content: str) -> None:
        self._content = content

    def get_content(self) -> str:
        return self._content


class ContentDecorator(ReportContent):
    def __init__(self, wrapped: ReportContent) -> None:
        self._wrapped = wrapped

    def get_content(self) -> str:
        return self._wrapped.get_content()


class HeaderDecorator(ContentDecorator):
    def __init__(self, wrapped: ReportContent, header: str) -> None:
        super().__init__(wrapped)
        self._header = header

    def get_content(self) -> str:
        return f"{self._header}\n{super().get_content()}"


class WatermarkDecorator(ContentDecorator):
    def __init__(self, wrapped: ReportContent, watermark: str) -> None:
        super().__init__(wrapped)
        self._watermark = watermark

    def get_content(self) -> str:
        return f"{super().get_content()}\n[WATERMARK: {self._watermark}]"


class EncryptionDecorator(ContentDecorator):
    def get_content(self) -> str:
        raw = super().get_content()
        return f"[ENCRYPTED]{raw[::-1]}"
