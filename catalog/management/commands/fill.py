import json

from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    # Здесь мы получаем данные из фикстур с категориями
    @staticmethod
    def json_read_categories():
        with open('categories.json', 'r', encoding='utf-8') as f:
            categories_data = f.read()

        return json.loads(categories_data)

    # Здесь мы получаем данные из фикстур с продуктами
    @staticmethod
    def json_read_products():
        with open('products.json', 'r', encoding='utf-8') as f:
            products_data = f.read()

        return json.loads(products_data)

    def handle(self, *args, **options):
        # Удалите все продукты и все категории
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Создайте списки для хранения объектов
        product_for_create = []
        category_for_create = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_for_create.append(
                Category(id=category['pk'],
                         name=category["fields"]["name"],
                         description=category["fields"]["description"])
            )
        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            product_for_create.append(
                Product(pk=product["pk"],
                        name=product["fields"]["name"],
                        description=product["fields"]["description"],
                        price=product["fields"]["price"],
                        photo=product["fields"]["photo"],
                        category=Category.objects.get(pk=product["fields"]["category"]),
                        created_at=product["fields"]["created_at"],
                        updated_at=product["fields"]["updated_at"],
                        manufactured_at=product["fields"]["manufactured_at"])
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)