from src.base_classes.pyenum import PyEnum


class PetStatus(PyEnum):
    AVAILABLE = "available"
    PENDING = "pending"
    SOLD = "sold"
