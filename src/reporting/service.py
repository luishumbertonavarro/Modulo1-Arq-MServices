from .factories import StrategyFactory
from .models import ReportData


class ReportService:
    def generate(self, user_type: str, data: ReportData) -> str:
        strategy = StrategyFactory.create(user_type)
        return strategy.process(data)
