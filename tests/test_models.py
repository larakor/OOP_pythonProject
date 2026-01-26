import unittest
from models.product import Product
from models.category import Category
import pytest


@pytest.fixture(autouse=True)
def reset_class_attributes():
    """ Автоматически сбрасывать атрибуты класса перед каждым тестом """
    Category.category_count = 0
    Category.product_count = 0


# Тестируем класс Product
class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

    def test_privacy_of_price(self):
        # Проверка, что прямая попытка доступа к приватному атрибуту вызывает AttributeError
        with self.assertRaises(AttributeError):
            getattr(self.product, "__price")

        # Проверка доступности через геттер
        self.assertEqual(self.product.price, 180000.0)

    def test_getter_and_setter(self):
        # Проверка геттера и сеттера
        self.assertEqual(self.product.price, 180000.0)
        self.product.price = 200000.0
        self.assertEqual(self.product.price, 200000.0)

# Тестируем класс Category


class TestCategory:
    def setup_method(self):
        self.product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        self.product2 = Product("iPhone 15", "512GB, Space Grey", 210000.0, 8)
        self.product_list = [self.product1, self.product2]

    def test_init(self):
        category = Category("Смартфоны", "Категории мобильных устройств", [])
        assert category._name == "Смартфоны"
        assert category._description == "Категории мобильных устройств"
        assert category.products == ""
        assert Category.category_count == 1
        assert Category.product_count == 0

    def test_category_count(self):
        Category("Категория 1", "", [])
        Category("Категория 2", "", [])
        assert Category.category_count == 2

    def test_product_count(self):
        Category("Смартфоны", "Категории мобильных устройств", self.product_list)
        assert Category.product_count == len(self.product_list)


if __name__ == '__main__':
    unittest.main()
