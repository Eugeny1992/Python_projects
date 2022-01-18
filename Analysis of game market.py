#!/usr/bin/env python
# coding: utf-8

# <div class="alert alert-success">
# <font size="5"><b>Комментарий ревьюера 3</b></font>
# 
# Привет. Исправления увидел. Перспективные платформы ты выбрал корректно. С маркерами также разобрался. Больше нереальных данных в анализе нет. Все помарки исправлены, и теперь работа выполнена хорошо. Я рад, что ты справился со всеми трудностями проекта, молодец. Поздравляю со сданным проектом. Надеюсь, он был интересен и познавателен. Успехов в дальнейшем пути :)
# 
# </div>

# <div class="alert alert-info">
# <font size="5"><b>Комментарий ревьюера 2</b></font>
# 
# Привет еще раз. Спасибо, что доделал работу. Оформление комментариев по работе сохраняется. Только обозначим, что это вторая итерация. 
# 
# </div>

# <div class="alert alert-info">
# <font size="5"><b>Комментарий ревьюера</b></font>
# 
# Привет, Евгений! Спасибо, что прислал задание:) Извини за задержку при проверке. Меня зовут Слепцов Артем и я буду проверять твой проект) Ты проделал большую работу над проектом. Он выполнен уже на достойном уровне. Однако есть моменты, которые еще можно улучшить. Будет здорово, если ты, надеюсь, не против, если я буду на ты, будешь отвечать на комментарии и участвовать в диалоге. Если обращение на ты неприемлемо, то прошу сообщить. 
# 
# Мои комментарии обозначены пометкой **Комментарий ревьюера**. Далее в файле ты сможешь найти их в похожих ячейках:
#     
# <div class="alert alert-success">Успех: Если фон комментария зелёный - всё сделано правильно. Рекомендации укажу таким же цветом;</div>
#         
# <div class="alert alert-warning">Совет: Оранжевый - некритичные замечания;</div>
#         
# <div class="alert alert-danger">Ошибка: Красный - нужно переделать. </div>
#         
# Не удаляй эти комментарии и постарайся учесть их в ходе выполнения данного проекта. Свои же комментарии ты можешь обозначать любым заметным способом. 
# 
# </div>

# # Задача

# Интернет-магазину «Стримчик», который продаёт по всему миру компьютерные игры, необходимо выявить определяющие успешность игры закономерности. Это позволит сделать ставку на потенциально популярный продукт и спланировать рекламные кампании. Для анализа будем использовать данные из открытых источников о продажах игр, оценки пользователей и экспертов, жанры и платформы до 2016 года включительно. 

# В используемом датасете иммеются следующие столбы:
# Name — название игры,
# Platform — платформа,
# Year_of_Release — год выпуска,
# Genre — жанр игры,
# NA_sales — продажи в Северной Америке (миллионы проданных копий),
# EU_sales — продажи в Европе (миллионы проданных копий),
# JP_sales — продажи в Японии (миллионы проданных копий),
# Other_sales — продажи в других странах (миллионы проданных копий),
# Critic_Score — оценка критиков (максимум 100),
# User_Score — оценка пользователей (максимум 10),
# Rating — рейтинг от организации ESRB

# <div class="alert alert-warning">
# <font size="5"><b>Комментарий ревьюера</b></font>
# 
# Совет: Правильно, что есть краткое вступление в работу, описание того, что надо делать. В работе следует приводить информацию о входных данных: какие столбцы есть в таблице, их названия и какую информацию они несут. Так работа выглядит презентабельно. Подробнее смотри методичку по оформлению проектов. Она располагается в Notion в разделе "Как оформлять проект".
# 
# </div>

# ## Откроем файл с данными и изучим общую информацию

# <div class="alert alert-warning">
# <font size="5"><b>Комментарий ревьюера</b></font>
# 
# Совет: Я заметил, что ячейки в твоей тетрадке начинаются не с 1. Перед отправкой работы рекомендую перезапускать ноутбук, чтобы убедиться, что все ячейки выполняются корректно.
# 
# </div>

# <div class="alert alert-success">
# <font size="5"><b>Комментарий ревьюера 2</b></font>
# 
# Успех: В полном перезапуске проекта тебе поможет Kernel => Restart & Run All.
# 
# </div>

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats as st
df = pd.read_csv('/datasets/games.csv')


# In[2]:


df.info()


# В нашем датасете 11 столбцов и 16715 строк. Имена столбцов написано в разном регистре, многие стобцы имеют пропуски. Стоблцы Year_of_Release, Critic_Score имеют неверный тип данных, у них должен быть тип данных integer.

# <div class="alert alert-success">
# <font size="5"><b>Комментарий ревьюера</b></font>
# 
# Успех: Правильно, что весь импорт ты проводишь в первой ячейке работы. Так твой коллега, запускающий работу, будет в курсе используемых в ней библиотек и сможет при необходимости быстро настроить окружение. 
# 
# </div>

# ## Подготовим данные

# Переименуем столбцы и приведем их названия к нижнему регистру

# In[3]:


df.columns


# In[4]:


df.rename(str.lower, axis='columns', inplace=True)


# <div class="alert alert-warning">
# <font size="5"><b>Комментарий ревьюера</b></font>
# 
# Совет: Не следует переименовывать столбцы через атрибут columns, потому что так ты неявно учитываешь порядок столбцов. Если порядок столбцов поменяется, код перестанет работать. Используй вместо этого метод rename().
#     
# </div>

# <div class="alert alert-success">
# <font size="5"><b>Комментарий ревьюера 2</b></font>
# 
# Успех: Такой метод заметно лучше. 
# 
# </div>

# In[5]:


df.columns


# ----------------------

# Избавимся от пропусков и дубликатов в датасете.

# In[6]:


df.isna().sum()


# Пропусков в столбце name всего два, это очень мало в объеме всего датасета, значит их можно удалить. Пропусков в стобце year_of_release 269, что не очень много, поэтому удалим их. Пропусков в столбце genre всего два, это очень мало в объеме всего датасета, значит их можно удалить. Пропусков в стобце critic_score достаточное количество, поэтому заменим  их нулями. Аббревиатура TBD в столбце user_score означает to be determined (подлежит уточнению), так как таких значений в датасете 2424, то их нельзя удалить, заменим их нулями. Пропуски в стобце rating заменим на NA, так как их большое количество.

# In[7]:


#удалим строки с пропусками в столбцах name, year_of_release, genre
df.dropna(subset=['name', 'year_of_release', 'genre'], inplace=True)
df.reset_index(drop=True)


# <div class="alert alert-success">
# <font size="5"><b>Комментарий ревьюера</b></font>
# 
# Успех: Соглашусь, такое количество пропусков мы вполне можем убрать из данных.
# 
# </div>

# In[8]:


df['critic_score'] = df['critic_score'].fillna(0)
df['user_score'] = df['user_score'].fillna(0)
df[df['user_score'] == 'tbd'] = 0
df['rating'] = df['rating'].fillna('NA')


# <div class="alert alert-success">
# <font size="5"><b>Комментарий ревьюера</b></font>
# 
# Успех: Верно, по своей сути tbd и является пропуском. Отлично, что определяешь неявные пропущенные значения.
# 
# </div>

# <div class="alert alert-warning">
# <font size="5"><b>Комментарий ревьюера</b></font>
# 
# Совет: Но пропуски можно оставить в данных. Смотри, 0 - это нереальные данные, которыми мы помечаем пропуски. В итоге при анализе данных столбцов мы должны каждый раз отфильтровывать такие значения, т.к. анализировать их не надо. В итоге, в одном из пунктов можно забыть про такие значения и случайно включить маркерные значения в анализ, что вызовет ошибку в результатах работы.
# 
# </div>

# In[9]:


#найдем дубликаты
df.duplicated().sum()


# In[10]:


#удалим дубликаты
df.drop_duplicates().reset_index(drop=True)


# Дубликаты и пропуски отсутствуют.

# --------------------

# Приведем типы данных в столбцах year_of_release и critic_score к целочисленному, потмоу что данных в этих столбцах должны иметь целочисленное значение. В столбце user_score изменим тип данных на float.

# In[11]:


df['year_of_release'] = df['year_of_release'].astype('int')
df['critic_score'] = df['critic_score'].astype('int')
df['user_score'] = df['user_score'].astype('float')


# -----------------

# Посчитаем суммарные продажи во всех регионах и запишем их в отдельный столбец total_sales.

# In[12]:


df['total_sales'] = df['na_sales'] + df['jp_sales'] + df['eu_sales'] + df['other_sales']


# <div class="alert alert-success">
# <font size="5"><b>Комментарий ревьюера</b></font>
# 
# Успех: Да, восстановить пропущенные значения мы не можем. Данных для этого недостаточно. Лучше работать с меньшим количеством данных хорошего качества.
#     
# Ошибки в данных устранены. Данные подготовлены к дальнейшему анализу. 
# 
# </div>

# ## Проведем исследовательский анализ данных

# Посмотрим, сколько игр выпускалось в разные годы. Выясним, важны ли данные за все периоды.

# In[13]:


df.groupby('year_of_release')['name'].count().sort_values()


# Важны все данные, начиная с 2010 года, так как платформы которые были популярны до этого уже вымерли. 

# <div class="alert alert-success">
# <font size="5"><b>Комментарий ревьюера</b></font>
# 
# Успех: Как думаешь, с чем связан спад в индустрии последних лет?
# 
# </div>

# <div class="alert alert-info">Спад индустрии последних лет связан с развитием мобильного гейминга.</div>

# <div class="alert alert-success">
# <font size="5"><b>Комментарий ревьюера 2</b></font>
# 
# Успех: Соглашусь с твоим предположением. 
# 
# </div>

# ---------------

# Посмотрим, как менялись продажи по платформам.

# In[14]:


pd.pivot_table(df, values=['total_sales'], index=['platform'], aggfunc='sum').sort_values(by='total_sales')


# Наибольшие суммарные продажи у платформ: PS2, X360, PS3, Wii, PS. Построим для них графики распределения суммарных продаж по годам.

# In[15]:


platform = ['PS2', 'X360', 'PS3', 'Wii', 'PS']

for i in platform:
    a= df.query('platform == @i')['year_of_release']
    a.hist(bins = 15)
    plt.title(i)
    plt.show()
    print('peak =', a.value_counts().index[0], ', duration =', a.value_counts().index.max() - a.value_counts().index.min())


# Для PS2 пик продаж в 2005 году, для X360 и PS3 пик продаж приходится на 2011 год, для Wii пик продаж пришелся на 2008 год, а для PS пик пришелся на 1998 год. Это вероятно связано с годом выхода этих платформ и соответственно с ростом популярности игр на них. Новые платформы появляются примерно раз в 3-4 года. Продолжительность существования платформ колеблется в пределах от 9 до 11 лет. В дальнейший расчет не стоит включать устаревшие платформы.

# <div class="alert alert-warning">
# <font size="5"><b>Комментарий ревьюера</b></font>
# 
# Совет: Значение средней продолжительности существования платформы приведено. Однако выводы ты делаешь по графикам. Стоит также привести расчет данного значения. Подумай, стоит ли включать в расчет все платформы. Будут ли выбросы по продолжительности существования платформ?
# 
# </div>

# <div class="alert alert-success">
# <font size="5"><b>Комментарий ревьюера 2</b></font>
# 
# Успех: Здорово, что ты привел расчет периода жизни каждой платформы. Полученные значения подтверждают ранее сделанные выводы. 
# 
# </div>

# ------------------------------

# Возьмем данные за актуальный период c 2010 года, эти данные помогут построить прогноз на 2017 год.

# In[16]:


df_act = df.query('year_of_release >= 2010').reset_index(drop = True)
df_act.head(10)


# <div class="alert alert-danger">
# <font size="5"><b>Комментарий ревьюера</b></font>
# 
# Ошибка: Актуальный период назван. Его следует уменьшить. Сейчас у тебя в периоде содержится несколько этапов развития индустрии: становление рынка, рост продаж до 2008 года, пик 2008 и 2009 годов, а также сокращение рынка последних годов. Также большей части платформ уже нет в 2016 году, в построении прогноза на 2017 год они нам не помогут. При уменьшении периода в рассмотрение попадут только последние поколения платформ, а также будем рассматривать только конечный на данный момент интервал развития игровой индустрии. 
# 
# </div>

# <div class="alert alert-success">
# <font size="5"><b>Комментарий ревьюера 2</b></font>
# 
# Успех: Анализ такого периода позволит нам увеличить точность и качество прогноза на 2017 год. 
# 
# </div>

# Найдем топ-5 перспективных платформ для нового датасета за актуальный период.

# In[17]:



for i in df_act['platform'].unique():
    plt.subplots(figsize=(6, 2))
    plt.title(i)
    plt.scatter(x=pd.pivot_table(df_act, values=['total_sales'], index=['platform', 'year_of_release'], aggfunc='sum').loc[i].index, y=pd.pivot_table(df_act, values=['total_sales'], index=['platform', 'year_of_release'], aggfunc='sum').loc[i])
    plt.show()


# Перспективными платформами являются только XOne и PS4, остальные платформы имеют ярко выраженную тенденцию к снижению количества продаж до нуля

# <div class="alert alert-danger">
# <font size="5"><b>Комментарий ревьюера</b></font>
# 
# Ошибка: Какие платформы мы можем назвать перспективными на 2017 год? Оцени динамику продаж по платформам за последние годы. 
# 
# </div>

# <div class="alert alert-danger">
# <font size="5"><b>Комментарий ревьюера 2</b></font>
# 
# Ошибка: Ты выводишь актуальные платформы. Но актуальные и перспективные - это разные свойства. Посмотри на динамику продаж по платформам актуального периода, выбери платформы с ростом продаж за последние годы. Нас просят определить именно перспективные платформы. 
# 
# </div>

# -----------------

# Построим график «ящик с усами» по глобальным продажам игр в разбивке по платформам

# In[18]:


pop_platform = ['XOne', 'PS4']

for i in pop_platform:
    plt.subplots(figsize=(25, 5))
    plt.boxplot(df_act.query('platform == @i')['total_sales'], vert=False)
    plt.title(i)
    plt.show()
    print('median =', df_act.query('platform == @i')['total_sales'].median())
    


# <div class="alert alert-danger">
# <font size="5"><b>Комментарий ревьюера</b></font>
# 
# Ошибка: Диаграмму размаха нас просят построить для каждой платформы актуального периода. Для этого тебе не нужно строить сводные таблицы, используй данные каждой платформы для визуализации уровня продаж по ним. 
# 
# </div>

# <div class="alert alert-warning">
# <font size="5"><b>Комментарий ревьюера 2</b></font>
#  
# Совет: Подумай, из-за чего формируется разница между платформами. Не забывай делать выводы по каждому пункту анализа. 
# </div>

# <div class="alert alert-info">Разница между платформами формируется по различным причинам: новизна платформы, количество эксклюзивных игр выходящих на них, стоимость самих платформ, мобильность платформ...</div>

# --------------

# Посмотрим, как влияют на продажи внутри одной популярной платформы отзывы пользователей и критиков

# In[19]:


pop_platform = ['XOne', 'PS4']

for i in pop_platform:
    df_act.query('platform == @i')
    plt.subplots(figsize=(15,3))
    print('Зависимость количества продаж от оценок пользователей')
    plt.title(i)
    plt.scatter(y=df_act.query('platform == @i' and 'user_score > 0')['total_sales'], x=df_act.query('platform == @i' and 'user_score > 0')['user_score'])
    plt.show()
    
    plt.subplots(figsize=(15,3))
    print('Зависимость количества продаж от оценок критиков')
    plt.title(i)
    plt.scatter(y=df_act.query('platform == @i' and 'critic_score > 0')['total_sales'], x=df_act.query('platform == @i' and 'critic_score > 0')['critic_score'])
    plt.show()


# Видна прямолинейная зависимость количества продаж от оценок пользователей и критиков 

# Построим диаграмму рассеяния по данным глобальных продаж для каждой из платформ

# In[20]:


pivot = pd.pivot_table(df_act, values=['total_sales'], index=['platform'], aggfunc='sum').sort_values(by='total_sales')

plt.subplots(figsize=(15,5))
plt.title('Количество глабальных продаж каждой из платформ')
plt.scatter(x=pivot.index, y=pivot['total_sales'])
plt.show()


# Из диаграммы рассения виден резкий рост продаж у платфор, начиная с PS4

# Посчитаем корреляцию между отзывами и продажами

# In[21]:


pop_platform = ['XOne', 'PS4']

for i in pop_platform:
    print('Корреляция количества проданных игр на платформе', i, 'с оценкой пользователей равна', df_act.query('platform == @i').query('user_score > 0').corr().loc['user_score', 'total_sales'])
    print('Корреляция количества проданных игр на платформе', i, 'с оценкой критиков равна', df_act.query('platform == @i').query('critic_score > 0').corr().loc['critic_score', 'total_sales'], '\n')


# Имеем положительную корреляцию между отзывами пользователей и критиков и количеством продаж, однако связь с оценками критиков сильнее, чем с оценками пользователей. Скорее всего потому что оценки критиков беспрестарстнее и объективнее.

# <div class="alert alert-danger">
# <font size="5"><b>Комментарий ревьюера</b></font>
# 
# Ошибка: Опять же рассматривай платформы в отдельности. Построй по каждой платформе график зависимости числа проданных игр от оценок критиков или пользователей. Рассчитай по 2 значения корреляции для каждой платформы. Корреляции рассчитываются на полных данных, а не на данных после применения группировки. 
# 
# </div>

# <div class="alert alert-danger">
# <font size="5"><b>Комментарий ревьюера 2</b></font>
# 
# Ошибка: Теперь ты делаешь все верно. Однако при расчете корреляций ты учитываешь маркерные значения 0, которыми мы заполнили пропуски. Этого делать не стоит. Мы не можем анализировать нереальные значения наравне с реальными. Отфильтруй их из анализа и посмотри на получаемые результаты. 
# 
# </div>

# ----------------------------

# Посмотрим на общее распределение количества игр по жанрам

# In[22]:


df_act.groupby('genre')['total_sales'].sum().sort_values()


# Больше всего продаж игр жанров: Action, Shooter, Role-Playing, Sports, Misc. Меньше всего продаж игр жанров: Puzzle, Strategy, Adventure, Simulation, Fighting

# <div class="alert alert-success">
# <font size="5"><b>Комментарий ревьюера</b></font>
# 
# Успех: Анализ популярности жанров проведен. Однако не стоит забывать, что производство игр в жанрах Action или Shooter обходится сильно дороже, чем производство Puzzle-игр. 
# 
# </div>

# ## Составим портрет пользователя каждого региона (NA, EU, JP)

# Определим для пользователя каждого региона (NA, EU, JP) самые популярные платформы

# In[23]:


pivot_platform = pd.pivot_table(df_act, values=['na_sales', 'eu_sales', 'jp_sales'], index=['platform'], aggfunc='sum')
pivot_platform['platform'] = pivot_platform.index


# - У пользователей NA самые популярные платформы: 

# In[24]:


pivot_platform.sort_values(by='na_sales').tail().index


# In[25]:


plt.title('Количество глобальных продаж каждой из платформ')
plt.scatter(y=pivot_platform.query('platform == "Wii" or platform == "XOne" or platform == "PS4" or platform == "PS3" or platform == "X360"')['na_sales'], x=pivot_platform.query('platform == "Wii" or platform == "XOne" or platform == "PS4" or platform == "PS3" or platform == "X360"')['platform'])
plt.show()

plt.title('Доли продаж по каждой из этих платформ')
plt.scatter(y=(pivot_platform.query('index == "Wii" or index == "XOne" or index == "PS4" or index == "PS3" or index == "X360"')['na_sales'] / pivot_platform['na_sales'].sum()), x=pivot_platform.query('platform == "Wii" or platform == "XOne" or platform == "PS4" or platform == "PS3" or platform == "X360"')['platform'])
plt.show()


# - У пользователей EU самые популярные платформы:

# In[26]:


pivot_platform.sort_values(by='eu_sales').tail().index


# In[27]:


plt.title('Количество глобальных продаж каждой из платформ')
plt.scatter(y=pivot_platform.query('platform == "3DS" or platform == "PC" or platform == "PS4" or platform == "PS3" or platform == "X360"')['eu_sales'], x=pivot_platform.query('platform == "3DS" or platform == "PC" or platform == "PS4" or platform == "PS3" or platform == "X360"')['platform'])
plt.show()

plt.title('Доли продаж по каждой из этих платформ')
plt.scatter(y=(pivot_platform.query('platform == "3DS" or platform == "PC" or platform == "PS4" or platform == "PS3" or platform == "X360"')['eu_sales'] / pivot_platform['eu_sales'].sum()), x=pivot_platform.query('platform == "3DS" or platform == "PC" or platform == "PS4" or platform == "PS3" or platform == "X360"')['platform'])
plt.show()


# - У пользователей JP самые популярные платформы:

# In[28]:


pivot_platform.sort_values(by='jp_sales').tail().index


# In[29]:


plt.title('Количество глобальных продаж каждой из платформ')
plt.scatter(y=pivot_platform.query('platform == "PSV" or platform == "DS" or platform == "PSP" or platform == "PS3" or platform == "3DS"')['jp_sales'], x=pivot_platform.query('platform == "PSV" or platform == "DS" or platform == "PSP" or platform == "PS3" or platform == "3DS"')['platform'])
plt.show()

plt.title('Доли продаж по каждой из этих платформ')
plt.scatter(y=(pivot_platform.query('platform == "PSV" or platform == "DS" or platform == "PSP" or platform == "PS3" or platform == "3DS"')['jp_sales'] / pivot_platform['jp_sales'].sum()), x=pivot_platform.query('platform == "PSV" or platform == "DS" or platform == "PSP" or platform == "PS3" or platform == "3DS"')['platform'])
plt.show()


# -----------------

# Определим для пользователя каждого региона (NA, EU, JP) самые популярные жанры

# In[30]:


pivot_genre = pd.pivot_table(df_act, values=['na_sales', 'eu_sales', 'jp_sales'], index=['genre'], aggfunc='sum')
pivot_genre['genre'] = pivot_genre.index


# - У пользователе NA самые популярные жанры:

# In[31]:


pivot_genre.sort_values(by='na_sales').tail().index


# In[32]:


plt.title('Количество глобальных продаж каждого жанра')
plt.scatter(y=pivot_genre.query('genre == "Misc" or genre == "Role-Playing" or genre == "Sports" or genre == "Shooter" or genre == "Action"')['na_sales'], x=pivot_genre.query('genre == "Misc" or genre == "Role-Playing" or genre == "Sports" or genre == "Shooter" or genre == "Action"')['genre'])
plt.show()

plt.title('Доли продаж по каждому жанру')
plt.scatter(y=(pivot_genre.query('genre == "Misc" or genre == "Role-Playing" or genre == "Sports" or genre == "Shooter" or genre == "Action"')['na_sales'] / pivot_genre['na_sales'].sum()), x=pivot_genre.query('genre == "Misc" or genre == "Role-Playing" or genre == "Sports" or genre == "Shooter" or genre == "Action"')['genre'])
plt.show()


# - У пользователе EU самые популярные жанры:

# In[33]:


pivot_genre.sort_values(by='eu_sales').tail().index


# In[34]:


plt.title('Количество глобальных продаж каждого жанра')
plt.scatter(y=pivot_genre.query('genre == "Misc" or genre == "Role-Playing" or genre == "Sports" or genre == "Shooter" or genre == "Action"')['eu_sales'], x=pivot_genre.query('genre == "Misc" or genre == "Role-Playing" or genre == "Sports" or genre == "Shooter" or genre == "Action"')['genre'])
plt.show()

plt.title('Доли продаж по каждому жанру')
plt.scatter(y=(pivot_genre.query('genre == "Misc" or genre == "Role-Playing" or genre == "Sports" or genre == "Shooter" or genre == "Action"')['eu_sales'] / pivot_genre['eu_sales'].sum()), x=pivot_genre.query('genre == "Misc" or genre == "Role-Playing" or genre == "Sports" or genre == "Shooter" or genre == "Action"')['genre'])
plt.show()


# - У пользователе JP самые популярные жанры:

# In[35]:


pivot_genre.sort_values(by='jp_sales').tail().index


# In[36]:


plt.title('Количество глобальных продаж каждого жанра')
plt.scatter(y=pivot_genre.query('genre == "Misc" or genre == "Role-Playing" or genre == "Adventure" or genre == "Platform" or genre == "Action"')['jp_sales'], x=pivot_genre.query('genre == "Misc" or genre == "Role-Playing" or genre == "Adventure" or genre == "Platform" or genre == "Action"')['genre'])
plt.show()

plt.title('Доли продаж по каждому жанру')
plt.scatter(y=(pivot_genre.query('genre == "Misc" or genre == "Role-Playing" or genre == "Adventure" or genre == "Platform" or genre == "Action"')['jp_sales'] / pivot_genre['jp_sales'].sum()), x=pivot_genre.query('genre == "Misc" or genre == "Role-Playing" or genre == "Adventure" or genre == "Platform" or genre == "Action"')['genre'])
plt.show()


# --------------

# Определим, влияет ли рейтинг ESRB на продажи в отдельном регионе

# In[37]:


pivot_rating = pd.pivot_table(df_act, values=['na_sales', 'eu_sales', 'jp_sales'], index=['rating'], aggfunc='sum')
pivot_rating['rating'] = pivot_rating.index


# - Распределение продаж в зависимости от ESRB для пользователей NA

# In[38]:


pivot_rating.sort_values(by='na_sales', ascending=False).index


# In[39]:


plt.title('Количество глобальных продаж каждого рейтинга')
plt.scatter(y=pivot_rating['na_sales'], x=pivot_rating['rating'])
plt.show()

plt.title('Доли продаж по каждому рейтингу')
plt.scatter(y=(pivot_rating['na_sales'] / pivot_rating['na_sales'].sum()), x=pivot_rating['rating'])
plt.show()


# - Распределение продаж в зависимости от ESRB для пользователей EU

# In[40]:


pivot_rating.sort_values(by='eu_sales', ascending=False).index


# In[41]:


plt.title('Количество глобальных продаж каждого рейтинга')
plt.scatter(y=pivot_rating['eu_sales'], x=pivot_rating['rating'])
plt.show()

plt.title('Доли продаж по каждому рейтингу')
plt.scatter(y=(pivot_rating['eu_sales'] / pivot_rating['eu_sales'].sum()), x=pivot_rating['rating'])
plt.show()


# - Распределение продаж в зависимости от ESRB для пользователей JP

# In[42]:


pivot_rating.sort_values(by='jp_sales', ascending=False).index


# In[43]:


plt.title('Количество глобальных продаж каждого рейтинга')
plt.scatter(y=pivot_rating['jp_sales'], x=pivot_rating['rating'])
plt.show()

plt.title('Доли продаж по каждому рейтингу')
plt.scatter(y=(pivot_rating['jp_sales'] / pivot_rating['jp_sales'].sum()), x=pivot_rating['rating'])
plt.show()


# Для пользователей всех регионов самые низкие продажи для рейтинга RP, а самые высокие продажи для рейтингов E, M, T, NA. Рейтинг мало влияет на продажи в каждом регионе примерно одинаково

# <div class="alert alert-danger">
# <font size="5"><b>Комментарий ревьюера</b></font>
# 
# Ошибка: Обрати внимание - ты не учитываешь игры без рейтинга. В результате огромная часть игр просто выпадает из анализа. Найди способ учесть их при группировке значений по рейтингу.
#     
# </div>

# <div class="alert alert-success">
# <font size="5"><b>Комментарий ревьюера 2</b></font>
# 
# Успех: Здорово, ты обнаружил важную особенность данных - большая часть игр японского региона не имеет рейтинга. Как думаешь, какова причина такого явления?
# 
# </div>

# <div class="alert alert-danger">
# <font size="5"><b>Комментарий ревьюера</b></font>
# 
# Ошибка: Помимо вывода топ-5 значений нам важно вывести и уровень продаж по ним, а также рассчитать доли каждой платформы, каждого жанра или рейтинга. Далее стоит визуализировать все полученные таблицы. Крайне не хватает графиков в данном разделе работы. Дополни данный раздел работы. 
# 
# </div>

# <div class="alert alert-success">
# <font size="5"><b>Комментарий ревьюера 2</b></font>
# 
# Успех: Анализ проведен полностью. Старайся всегда визуализировать получаемую в работе информацию.
# 
# </div>

# ## Проверим гипотезы

# Проверим нулевую гипотезу: средние пользовательские рейтинги платформ Xbox One и PC одинаковые

# In[44]:


st.ttest_ind(df_act.query('platform == "XOne"').query('user_score > 0')['user_score'], df_act.query('platform == "PC"').query('user_score > 0')['user_score']).pvalue


# Уровень значимости p-value очень высокий, значит мы не можем опровергнуть нулевую гепотезу. Средние пользовательские рейтинги платформ Xbox One и PC одинаковые.

# <div class="alert alert-success">
# <font size="5"><b>Комментарий ревьюера</b></font>
# 
# Успех: Гипотезы сформулированы и проверены верно. 
# 
# </div>

# ----------------------

# Проверим нулевую гипотезу: средние пользовательские рейтинги жанров Action (англ. «действие», экшен-игры) и Sports (англ. «спортивные соревнования») равны

# In[45]:


st.ttest_ind(df_act.query('genre == "Action"').query('user_score > 0')['user_score'], df_act.query('genre == "Sports"').query('user_score > 0')['user_score']).pvalue


# Уровень значимости p-value очень мал, значит мы можем отклонить нулевую гепотезу. Средние пользовательские рейтинги жанров Action и Sports не равны.

# <div class="alert alert-success">
# <font size="5"><b>Комментарий ревьюера</b></font>
# 
# Совет: Проверка второй гипотезы также выполнена корректно. Аккуратнее с использованием слов "принимаем" и "истина". На самом деле данная гипотеза может быть и не верна, но на имеющихся на настоящий момент данных получить различия мы не можем. Лучше использовать формулировку "не можем отклонить нулевую гипотезу".
# 
# </div>

# <div class="alert alert-danger">
# <font size="5"><b>Комментарий ревьюера 2</b></font>
# 
# Ошибка: Извини, что не указал в прошлый раз. В выборки опять же попали нереальные значения 0, которыми отмечены пропуски. Отфильтруй их из выборок при проведении обоих тестов. Посмотри, как изменятся результаты. 
# 
# </div>

# ## Вывод

# В ходе исследования я выявил следующие определяющие успешность игры закономерности:

# - максимальные продажи имеют игры, которые выходили на платформах PS3, X360, PS4, 3DS, Wii; 

# - наибольшие продажи имеют игры жанров Action, Shooter, Role-Playing, Sports, Misc; 

# - лучше всего продаются игры с рейтингом E, M, T по классификации ESRB; 

# - чем выше рейтинг пользователей и критиков тем больше продаж имеют игры. 

# - самые перспективные платформы это PS4, XOne

# Полученные результаты ислледования и выводы позволят интернет-магазине «Стримчик» сделать ставку на потенциально популярный продукт и спланировать рекламные кампании, что увеличит продажи. Отделу рекламы стоит сделать упор на перспективные платформы PS4 и XOne, так же стоит обратить внимание на игры которые имеют высокие рейтинги и делать упор на эти игры и на платформы под которые они выходят.

# <div class="alert alert-danger">
# <font size="5"><b>Комментарий ревьюера</b></font>
# 
# Ошибка: Скорректируй выводы после исправления помарок выше. 
# 
# </div>

# <div class="alert alert-success">
# <font size="5"><b>Комментарий ревьюера 2</b></font>
# 
# Успех: Выводы сделаны. Приведены ответы на главные вопросы проекта. В выводах можно приводить полученные ранее значения. Также можно расписать все, что было сделано в ходе проведения работы. Еще лучше будет, если приведешь рекомендации для компании по дальнейшим действиям. 
# 
# </div>

# <div class="alert alert-info">
# <font size="5"><b>Комментарий ревьюера</b></font>
# 
# Если тебе нравится тема визуализации, то можешь изучить и методы библиотеки seaborn. Она позволяет строить довольно презентабельные графики. Рекомендую ресурс https://www.python-graph-gallery.com/. В нем содержится большая библиотека графиков с готовым кодом, который можно использовать при работе.
# 
# Ты проделал большую работу, молодец! Однако критичные помарки все же есть. С ними важно поработать и их исправить. При необходимости задавай вопросы. Жду твою работу :)
# 
# </div>

# <div class="alert alert-info">
# <font size="5"><b>Комментарий ревьюера 2</b></font>
# 
# Часть помарок исправлена. Однако осталось еще несколько критичных помарок, которые следует скорректировать. Удели им внимание. Как сделаешь, присылай работу снова. Буду ждать :)
# 
# </div>
