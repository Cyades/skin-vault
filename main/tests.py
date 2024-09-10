from django.test import TestCase, Client
from django.utils import timezone
from .models import Product

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/skibidi/')
        self.assertEqual(response.status_code, 404)

    def test_product_skin(self):
        desc = Product.objects.create(
            name = "Dragon Lore",
            weapon = "AWP",
            exterior = "Factory New",
            category = "Normal",
            quality = "Covert",
            price = 18257,
            description = "Its eye-catching design consists of an olive green base color and a large, fire-breathing dragon that spans across the entire length of the sniper rifle. The Butt, Scope, and Barrel all feature a similar pattern consisting mainly of black and green colors.",
            quantity = 1,
        )
        self.assertTrue(desc.is_product_available)