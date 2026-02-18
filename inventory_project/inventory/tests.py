from django.test import TestCase

from .models import Category, Product


class CategoryModelTest(TestCase):

    def test_category_creation(self):

        category = Category.objects.create(name="Electronics")

        self.assertEqual(category.name, "Electronics")

        self.assertEqual(str(category), "Electronics")


class ProductModelTest(TestCase):

    def setUp(self):

        self.category = Category.objects.create(name="Electronics")

    def test_product_creation(self):

        product = Product.objects.create(

            name="Laptop",

            description="Gaming laptop",

            price=50000.00,

            quantity=5,

            category=self.category

        )

        self.assertEqual(product.name, "Laptop")

        self.assertEqual(product.price, 50000.00)

        self.assertEqual(product.quantity, 5)

        self.assertEqual(product.category.name, "Electronics")

        self.assertEqual(str(product), "Laptop")
 