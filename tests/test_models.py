import unittest
from models.product import Product
from models.category import Category
import pytest

@pytest.fixture(autouse=True)
def reset_class_attributes():
    """Автоматически сбрасывать атрибуты класса перед каждым тестом"""
    Category.category_count = 0
    Category.product_count = 0

# Тестируем класс Product
class TestProduct(unittest.TestCase):
    def test_product_initialization(self):
        p = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        self.assertEqual(p.name, "Samsung Galaxy S23 Ultra")
        self.assertEqual(p.description, "256GB, Серый цвет, 200MP камера")
        self.assertEqual(p.price, 180000.0)
        self.assertEqual(p.quantity, 5)


# Тестируем класс Category
class TestCategory(unittest.TestCase):
    def setUp(self):
        self.product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        self.product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        self.product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
        self.category1 = Category("Смартфоны", "Смартфоны, как средство...",
                                  [self.product1, self.product2, self.product3])

    def test_category_initialization(self):
        self.assertEqual(self.category1.name, "Смартфоны")
        self.assertEqual(self.category1.description, "Смартфоны, как средство...")
        self.assertListEqual(self.category1.products, [self.product1, self.product2, self.product3])

    def test_category_counts(self):
        # Проверка увеличения значения в ноыой категории
        initial_categories = Category.category_count
        new_category = Category("Ноутбуки", "Различные ноутбуки", [])
        final_categories = Category.category_count
        self.assertEqual(final_categories, initial_categories + 1)

    def test_total_products_count(self):
        # Проверяем правильный подсчёт товаров
        expected_total_products = len(self.category1.products)
        actual_total_products = Category.product_count
        self.assertEqual(actual_total_products, expected_total_products)


# Запуск теста
if __name__ == '__main__':
    unittest.main()
