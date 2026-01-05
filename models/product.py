class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Конструктор продукта.

        :param name: Название товара
        :type name: str
        :param description: Описание товара
        :type description: str
        :param price: Цена товара
        :type price: float
        :param quantity: Количество товара на складе
        :type quantity: int
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
