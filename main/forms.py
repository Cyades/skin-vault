from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "weapon", "exterior","category","quality","price","description","quantity"]
    
    
    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_weapon(self):
        weapon = self.cleaned_data["weapon"]
        return strip_tags(weapon)

    def clean_exterior(self):
        exterior = self.cleaned_data["exterior"]
        return strip_tags(exterior)

    def clean_category(self):
        category = self.cleaned_data["category"]
        return strip_tags(category)

    def clean_quality(self):
        quality = self.cleaned_data["quality"]
        return strip_tags(quality)

    def clean_price(self):
        price = self.cleaned_data["price"]
        return strip_tags(price)

    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)

    def clean_quantity(self):
        quantity = self.cleaned_data["quantity"]
        return strip_tags(quantity)
