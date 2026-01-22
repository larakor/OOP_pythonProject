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
class TestCategory(unittest.TestCase):
    def setUp(self):
        # Подготовим несколько продуктов
        self.product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        self.product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        self.product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

        # Создадим категорию с несколькими продуктами
        self.category1 = Category("Смартфоны",
                                  "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                                  [self.product1, self.product2, self.product3])

    def test_initialization(self):
        # Проверка инициализации
        self.assertEqual(self.category1._name, "Смартфоны")
        self.assertEqual(self.category1._description,
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни")
        self.assertEqual(Category.category_count, 1)  # Только одна категория создана
        self.assertEqual(Category.product_count, 3)  # Всего три товара в категории

    def test_class_counter(self):
        # Проверка счётчиков категорий и товаров
        self.assertEqual(Category.category_count, 1)  # Пока одна категория
        self.assertEqual(Category.product_count, 3)   # Три товара в категории

        # Создаём новую категорию
        category2 = Category("Электроника", "Электронные устройства", [])

        # Проверяем, что новая категория пустая
        self.assertFalse(category2.products.strip())

        # Повторно проверяем количество категорий и товаров
        self.assertEqual(Category.category_count, 2)  # Теперь категорий две
        self.assertEqual(Category.product_count, 3)   # Количество товаров не изменилось

if __name__ == '__main__':
    unittest.main()
