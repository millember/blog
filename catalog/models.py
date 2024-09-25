from django.db import models


# Create your models here.


# создаем модель категории как одного ко многим
class Category(models.Model):
    # наименование, описание
    name = models.CharField(
        max_length=100, verbose_name="категория", help_text="Введите категорию продукта"
    )
    description = models.TextField(
        verbose_name="Описание категории",
        help_text="Введите описание категории продукта",
        blank=True,
        null=True,
    )


    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f"{self.name} {self.description}"


# создаем модель продуктов как многих к одной категории. Ссылка на категорию
# создаем класс и наследуемся от models.Model
class Product(models.Model):
    # имя, порода, фото, дата рождения
    # создаем поля и прописываем их параметры
    name = models.CharField(
        max_length=100,
        verbose_name="наименование",
        help_text="введите наименование продукта",
    )
    description = models.TextField(
        max_length=100, verbose_name="описание", help_text="Введите описание продукта"
    )
    image = models.ImageField(
        upload_to="catalog/image",
        blank=True,
        null=True,
        verbose_name="изображение",
        help_text="загрузите изображение продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="введите категорию продукта",
        blank=True,
        null=True,
        related_name="products",
    )
    price = models.PositiveIntegerField(
        default=0,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name="дата создания",
        help_text="Укажите дату создания записи в БД",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="дата последнего изменения",
        help_text="Укажите дату изменения записи в БД",
    )

    manufactured_at = models.DateField(
        verbose_name="Дата производства продукта нашего",
        help_text="Введите дату производства продукта нашего",
        blank=True,
        null=True,
    )
    views_counter = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров",
        help_text="Укажите количество просмотров",
        default=0
    )

    # Класс мета
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["category", "name"]

    # строковое представление объекта
    def __str__(self):
        return f"{self.name} {self.category} {self.created_at}"


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        related_name="versions",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="продукт",
    )

    version_num = models.PositiveIntegerField(
        verbose_name="Номер версии",
        help_text="Укажите номер версии продукта",
        default=0,
        null=True,
        blank=True,
    )

    version_name = models.CharField(
        max_length=100,
        verbose_name="Наименование версии",
        help_text="Введите наименование версии продукта",
        default="",
        null=True,
        blank=True,
    )

    active = models.BooleanField(
        verbose_name="Признак текущей версии",
        help_text="Введите признак текущей версии продукта",
        default=False,
    )

    class Meta:
        verbose_name = "Версия продукта"
        verbose_name_plural = "Версии продукта"

    def __str__(self):
        return f"{self.product} {self.version_num} {self.version_name} {self.active}"
