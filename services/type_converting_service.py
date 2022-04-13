from typing import Optional


class TypesConvertingService:
    def to_int(self, other: object) -> Optional[int]:
        try:
            return int(other)
        except (ValueError, TypeError):
            return None

    def to_float(self, other: object) -> Optional[float]:
        try:
            return float(other)
        except (ValueError, TypeError):
            return None
