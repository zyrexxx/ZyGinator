# disnake-ext-paginator

#### **disnake-ext-paginator** создавай многостраничные ембеды.
---
## Поддерживыемые версии

Required dependencies [requirements.txt](https://github.com/zyrexxx/disnake-ext-paginator/blob/main/requirements.txt)
```py
python >=3.8, <= 3.10
disnake >= 2.4.0    #(it's really recommended to use 2.6.0)
```

To install the required dependencies you can run:

- with bash
```
pip install -r requirements.txt
```

- with poetry
```
poetry install
```
---
## Installation

- использование гит
```
git clone https://github.com/zyrexxx/disnake-ext-paginator
```
- или
```pip install git+https://github.com/zyrexxx/disnake-ext-paginator```

---
## использование

### быстрый запуск
```python
from disnake_ext_paginator import Paginator
import disnake
from disnake.ext import commands

bot = commands.Bot(
    command_prefix=commands.when_mentioned,
    intents=disnake.Intents.default()
)

@bot.slash_command()
async def test_command(inter: disnake.ApplicationCommandInteraction) -> None:

    # Create a list of embeds to paginate.
    embeds = [
        disnake.Embed(
            title="Первый ембед"
        ),
        disnake.Embe(
            title="Второй ембед"
        ),
        disnake.Embed(
            title="Третий ембед"
        ),
    ]
    await Paginator().start(inter, pages=embeds)

bot.run('TOKEN')
```

### дополнительно 

##### Чтобы использовать пользовательские кнопки, передайте соответствующий аргумент при запуске paginator.

```python
from disnake_ext_paginator import Paginator
import disnake
from disnake.ext import commands

bot = commands.Bot(
    command_prefix=commands.when_mentioned,
    intents=disnake.Intents.default()
)

@bot.slash_command()
async def test_command(inter: disnake.ApplicationCommandInteraction) -> None:

    # Создайте список вставок для разбивки на страницы.
    embeds = [
        disnake.Embed(
            title="Первый ембед"
        ),
        disnake.Embe(
            title="Второй ембед"
        ),
        disnake.Embed(
            title="Третий ембед"
        ),
    ]
    paginator = Paginator(
        timeout=400,
        previous_button=disnake.ui.Button(...),
        next_button=disnake.ui.Button(...),
        trash_button=disnake.ui.Button(...),
        page_counter_separator="-",
        page_counter_style=disnake.ButtonStyle.danger,
        initial_page=1,
        on_timeout_message="Paginator expired",
        interaction_check=False # это позволит всем пользователям взаимодействовать с paginator
    )
    await paginator.start(inter, pages=embeds)

bot.run('TOKEN')
```
## документация
-----
## `class disnake_ext_paginator.Paginator(...)`
```python
class disnake_ext_paginator.Paginator(
    timeout: Union[int, float, None] = 60,
    previous_button: Optional[disnake.ui.Button] = None,
    next_button: Optional[disnake.ui.Button] = None,
    trash_button: Optional[disnake.ui.Button] = None,
    page_counter_separator: str = "/",
    page_counter_style: disnake.ButtonStyle = disnake.ButtonStyle.grey,
    initial_page: int = 0,
    on_timeout_message: Optional[str] = None,
    interaction_check: bool = True,
    interaction_check_message = Union[disnake.Embed, str] = disnake.Embed(...),
    ephemeral: bool = False,
    persistent: bool = False
)
```

**timeout: `int`**
    
- Через какое время должен истечь тайм-аут разбиения на страницы после последнего взаимодействия. (В секундах) (Переопределяет значение по умолчанию 60)
- 
> ## Примечание
> Если вы используете постоянный разбиитель на страницы, то для этого должно быть установлено значение `None`.


**previous_button: `disnake.ui.Button`**
    
- Переопределяет предыдущую кнопку по умолчанию. Если не указано или "Нет", будет использоваться кнопка по умолчанию.

**next_button: `disnake.ui.Button`**
- Переопределяет кнопку "next" по умолчанию. Если не указано или "none", будет использоваться кнопка по умолчанию.


**trash_button: `disnake.ui.Button`**
- Переопределяет кнопку корзины по умолчанию. Если не указано или "none", будет использоваться кнопка по умолчанию.

**page_counter_separator: `str`**

- 
**page_counter_style: `disnake.ButtonStyle`**
- Страница, с которой начинается нумерация страниц.

**on_timeout_message: `Optional[str]`**

- Переопределяет строку Переопределяет строку `on_timeout` по умолчанию, установленную как встроенный нижний колонтитул.
Если `None`, сообщение `on_timeout` не появится.

**interaction_check: `bool`**
-Сообщение для отправки в случае сбоя `interaction_check`, например, пользователь
кто не является владельцем команды, пытался взаимодействовать с paginator.
Эту функцию можно отключить, установив для `interaction_check` значение `False` Эту функцию можно отключить, установив для `interaction_check` значение `False`

**ephemeral: `bool`**
- Должен ли пагинатор быть виден только вызывающему команду или
никому другому.

**persistent: `bool`**
- Делает `Paginator` настойчивым.

> ## Warning
> Вы должны обратить внимание при использовании постоянных пагинаторов, если они используются в обычном режиме с несколькими вызовами команд, память может быть полностью заполнена, что приведет к сбою бота.

-----
## `def disnake_ext_paginator.Paginator.start(...)`
```python
def disnake_ext_paginator.Paginator.start(
    interaction: disnake.ApplicationCommandInteraction,
    pages: list[disnake.Embed]
)

```
