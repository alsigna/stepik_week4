# Stepik Django Week 4

## Existed users (login / password)
- admin / admin
- user1 / 123
- user2 / 123
- ...
- user8 / 123

## Лого специаальностей
перенос лого специальностей в media не делал
```Python
MEDIA_SPECIALITY_IMAGE_DIR = "speciality_images"
```
так как логика задания в этой части мне не понятна, это не информация загружаемая/меняемая пользователями, почему мы должны переносить эти логотипы в media. С лого компаний вопросов нет, они уехали в media