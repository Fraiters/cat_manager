from typing import Dict
from transliterate import translit


class ContextMixin:
    """ Миксин формирования контекста для классов представления """
    def get_context(self, **kwargs) -> Dict:
        """ Добавляет контекст
        (в параметрах указывается добавляемый контекст) """
        context = kwargs
        return context


class CatManagerData:
    """ Класс управления данными Cat """

    @classmethod
    def set_author(cls, view_obj: 'AddCat', form):
        """ Сопоставляет автору - имя пользователя """
        view_obj.object = form.save()
        # автор == пользователю
        view_obj.object.author = view_obj.request.user.username

    @classmethod
    def set_slug(cls, view_obj: 'AddCat', form):
        """ Сопоставляет slug - имя кота """
        view_obj.object = form.save()
        cat_name = str(view_obj.object.name).lower()
        union_cat_name = "".join(cat_name.split())
        translate_cat_name = translit(union_cat_name, 'ru', reversed=True)
        # slug = перевод имени кота + '-' + id кота
        view_obj.object.slug = translate_cat_name + "-" + str(view_obj.object.id)

