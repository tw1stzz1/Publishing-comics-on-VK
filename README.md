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
```
CLIENT_ID=00031698
GROUP_ID=222000051
VK_ACCESS_TOKEN=vk1.a.m1huGVD1bkhS9sdNJ2HmhNEdU8KPvuOlGcf-z2OLZ7iM6nmUfGnR4FvRjZQ-1R58DFVkbbn16mCzKbZ7a0VsbkP9yykaPWlr4tDHZ_g9uqeSwSOPBWYivxRifJgO2Knb2quFnGMwLh8-nD09dFQitvdsdx2enZYbFw4w-7rmYpRI8RPV-R29q8NKZhx5SUFpuPhZ2ahVGghouGHAhIZ1Yw
```
### Пример запуска кода
``` python
python main.py
```
