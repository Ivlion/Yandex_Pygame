# Flight
### Описание проекта
В данной игре вы играете за человечка с джетпаком, вам необходимо уворачиваться от летящих ракет и собирать монетки (чем больше тем лучше).
Со временем скорость ракет увеличивается.
Результаты сохраняются в csv файл и их можно посмотреть в виде таблицы.
### Реализация
Были созданы классы для персонажа и для мобов (ракет монет). При столкновении персонажа с мобом моб изменяет характеристики персонажа, при этом самоуничтожаясь. Изначально мобы рандомно спавнятся за правой границей экрана, при прохождении левой границы самоуничтожаются.
Также создано окно ввода имени для сохранения результата и окно вывода таблицы всех результатов.

**Необходимые библиотеки**
- Pygame(Создание самой игры)
- PyQt6(Окно сохранения и окно вывода таблицы результатов)
- sys(Необходима для запуска окон PyQt6)
- ramdom(Рандомная генерация мобов)
- csv(Работа с csv файлом)
- ctypes(Отключение масштабирования)
- threading(Выделение окон PyQt6 в отдельный поток)