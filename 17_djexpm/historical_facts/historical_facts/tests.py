from django.test import TestCase
from .models import Category

# models test 
class CategoryModelTest(TestCase):
    """

    """

    def test_creation_category(self):
        category = Category.objects.create(
            name = 'Electronic',
            description = 'Electronic articles and gadgets.'
        )

        self.assertEqual(category.name, 'Electronic')
        self.assertEqual(category.description, 'Electronic articles and gadgets.')


    def test_method_str_return_name(self):
        category = Category.objects.create(name = 'Books')
        self.assertEqual(category.name, 'Books')