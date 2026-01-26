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
        self._name = name
        self._description = description
        self.__price = price
        self._quantity = quantity

    @classmethod
    def new_product(cls, data: dict):
        return cls(data["name"], data["description"], data["price"], data["quantity"])

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value
        else:
            print("Цена не должна быть нулевая или отрицательная")
