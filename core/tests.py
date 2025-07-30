from django.test import TestCase
from django.contrib.admin.sites import site
from .models import Item, Category
from .admin import ItemAdmin

class ItemModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Books")
        self.item = Item.objects.create(
            name="Test Book",
            description="A test description",
            price=19.99,
            category=self.category
        )

    def test_item_str(self):
        self.assertEqual(str(self.item), "Test Book")

    def test_category_str(self):
        self.assertEqual(str(self.category), "Books")

class AdminTest(TestCase):
    def test_item_admin_registered(self):
        self.assertIn(Item, site._registry)

    def test_category_admin_registered(self):
        self.assertIn(Category, site._registry)
