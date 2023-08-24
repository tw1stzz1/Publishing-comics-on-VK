# Publishing-comics-on-VK
Код позволяет скачивать и публиковать комиксы с сайта [xkcd](https://xkcd.com)

### Как установить
Python3 должен быть уже установлен. Используйте `pip` (или `pip3`, есть есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Переменные окружения
Переменные окружения используются для изменения конфигурации системы. Результат работы многих приложений на Python зависит от значений определённых переменных окружения.
Это избавит нас от необходимости исправлять переменные среды вручную и сделает код безопаснее: будут спрятаны конфиденциальные данные, которые требуется присвоить переменной окружения (например, токен API).

#### Пример .env файла:
Для получения данных нужно зарегестрироваться в [ВК](https://vk.com), а так же создать [группу](https://vk.com/groups?tab=admin).
После, нужно [создать приложение](https://vk.com/apps?act=manage) и получить его client_id. Client_id находится в адресной строке при редактирование приложения(приложение должно быть публичным).
Затем нужно получить личный ключ(VK_ACCESS_TOKEN) с помощью процедуры [Implicit Flow](https://vk.com/dev/implicit_flow_user).
А узнать group_id для вашей группы можно [здесь](https://regvk.com/id/)

```
CLIENT_ID=00031698
GROUP_ID=222000051
VK_ACCESS_TOKEN=vk1.a.m1huGVD1bkhS9sdNJ2HmhNEdU8KPvuOlGcf-z2OLZ7iM6nmUfGnR4FvRjZQ-1R58DFVkbbn16mCzKbZ7a0VsbkP9yykaPWlr4tDHZ_g9uqeSwSOPBWYivxRifJgO2Knb2quFnGMwLh8-nD09dFQitvdsdx2enZYbFw4w-7rmYpRI8RPV-R29q8NKZhx5SUFpuPhZ2ahVGghouGHAhIZ1Yw
```

### Пример запуска кода
``` python
python main.py
```
В процессе код будет создовать временные файлы, но по завершению удалит их.

