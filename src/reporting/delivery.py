from __future__ import annotations

from abc import ABC, abstractmethod


class DeliveryChannel(ABC):
    @abstractmethod
    def deliver(self, payload: str, destination: str) -> None:
        pass


class EmailDelivery(DeliveryChannel):
    def deliver(self, payload: str, destination: str) -> None:
        print(f"Enviando por correo a: {destination}")
        print(payload)


class SharedFolderDelivery(DeliveryChannel):
    def deliver(self, payload: str, destination: str) -> None:
        print(f"Guardando en carpeta compartida: {destination}")
        print(payload)


class ApiDelivery(DeliveryChannel):
    def deliver(self, payload: str, destination: str) -> None:
        print(f"Enviando por API a: {destination}")
        print(payload)


class DeliveryFactory:
    @staticmethod
    def create(channel_type: str) -> DeliveryChannel:
        channel_map = {
            "email": EmailDelivery(),
            "folder": SharedFolderDelivery(),
            "api": ApiDelivery(),
        }
        key = channel_type.lower().strip()
        if key not in channel_map:
            raise ValueError(f"Unsupported delivery channel: {channel_type}")
        return channel_map[key]


class ReportDeliveryService:
    def deliver(self, payload: str, channel_type: str, destination: str) -> None:
        channel = DeliveryFactory.create(channel_type)
        channel.deliver(payload, destination)
