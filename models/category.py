from models.product import Product

class Category:
    # Атрибуты класса, доступные для всех экземпляров класса
    category_count = 0  # Общее число созданных категорий
    product_count = 0  # Общее число товаров среди всех категорий

    def __init__(self, name: str, description: str, products: list):
        """
        Конструктор категории.

        :param name: Название категории
        :type name: str
        :param description: Описание категории
        :type description: str
        :param products: Список товаров в категории
        :type products: list of Product
        """
        self._name = name
        self._description = description
        self.__products = []     #неизменяемый список товаров
        for product in products:
            self.add_product(product)  #новый метод доб товаров
        Category.category_count+=1
        # Автоматическое обновление общего числа категорий и товаров
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise ValueError("Переданный аргумент не является объектом типа Product.")

    @property
    def products(self):
        return "\n".join(f"{p.name}, {p.price:.2f} руб. Остаток: {p.quantity} шт." for p in self.__products)
