from src.base_classes.pyenum import PyEnum


class OrderStatus(PyEnum):
    PLACED = 'placed'
    APPROVED = 'approved'
    DELIVERED = 'delivered'
