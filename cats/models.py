from django.db.models import Model, IntegerField, CharField, TextField, ImageField, SlugField
from django.urls import reverse


class Cat(Model):
    """ Модель Кот """
    class Meta:
        verbose_name = 'Кот'

    name = CharField(max_length=100, verbose_name="Имя")
    age = IntegerField(null=True, verbose_name="Возраст")
    breed = CharField(max_length=100, blank=True, verbose_name="Порода")
    weight = IntegerField(null=True, verbose_name="Вес")
    photo = ImageField(upload_to="photos/", blank=True, verbose_name="Фото")
    description = TextField(blank=True, verbose_name="Описание")
    author = CharField(max_length=100, verbose_name="Автор")
    slug = SlugField(max_length=100, unique=True, db_index=True, verbose_name="URL")

    def get_absolute_url(self):
        """ Получение url кота """
        return reverse("cat_id", args=[self.slug])

    def __str__(self):
        return self.name
