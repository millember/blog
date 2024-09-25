
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Введите категорию продукта",
                        max_length=100,
                        verbose_name="категория",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Введите описание категории продукта",
                        null=True,
                        verbose_name="Описание категории",
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="введите наименование продукта",
                        max_length=100,
                        verbose_name="наименование",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        help_text="Введите описание продукта",
                        max_length=100,
                        verbose_name="описание",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        help_text="загрузите изображение продукта",
                        null=True,
                        upload_to="catalog/image",
                        verbose_name="изображение",
                    ),
                ),
                ("price", models.PositiveIntegerField(default=0)),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Укажите дату создания записи в БД",
                        verbose_name="дата создания",
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="Укажите дату изменения записи в БД",
                        verbose_name="дата последнего изменения",
                    ),
                ),
                (
                    "manufactured_at",
                    models.DateField(
                        blank=True,
                        help_text="Введите дату производства продукта нашего",
                        null=True,
                        verbose_name="Дата производства продукта нашего",
                    ),
                ),
                (
                    "views_counter",
                    models.PositiveIntegerField(
                        default=0,
                        help_text="Укажите количество просмотров",
                        verbose_name="Счетчик просмотров",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        help_text="введите категорию продукта",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="products",
                        to="catalog.category",
                        verbose_name="Категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
                "ordering": ["category", "name"],
            },
        ),
        migrations.CreateModel(
            name="Version",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "version_num",
                    models.PositiveIntegerField(
                        blank=True,
                        default=0,
                        help_text="Укажите номер версии продукта",
                        null=True,
                        verbose_name="Номер версии",
                    ),
                ),
                (
                    "version_name",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="Введите наименование версии продукта",
                        max_length=100,
                        null=True,
                        verbose_name="Наименование версии",
                    ),
                ),
                (
                    "active",
                    models.BooleanField(
                        default=False,
                        help_text="Введите признак текущей версии продукта",
                        verbose_name="Признак текущей версии",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="versions",
                        to="catalog.product",
                        verbose_name="продукт",
                    ),
                ),
            ],
            options={
                "verbose_name": "Версия продукта",
                "verbose_name_plural": "Версии продукта",
            },
        ),
    ]
