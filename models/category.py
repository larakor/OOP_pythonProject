from models.product import Product

class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        self._name = name
        self._description = description
        self.__products = []
        for product in products:
            self.add_product(product)
        Category.category_count += 1

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise ValueError("Переданный аргумент не является объектом типа Product.")

    @property
    def products(self):
        return "\n".join(f"{p.name}, {p.price:.2f} руб. Остаток: {p.quantity} шт." for p in self.__products)
