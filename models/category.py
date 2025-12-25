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
        self.name = name
        self.description = description
        self.products = products
        # Автоматическое обновление общего числа категорий и товаров
        Category.category_count += 1
        Category.product_count += len(self.products)
