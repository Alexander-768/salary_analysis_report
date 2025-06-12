import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df_of_inflantion = pd.read_csv('inflation.csv', sep=';') # датафрейм с инфляцией
# читаем данные с двух листов
df_of_wages_from_2017 = pd.read_excel('tab3-zpl_2024.xlsx', sheet_name='с 2017 г.') # датафрейм с зарплатами по отраслям c 2017 по 2024
df_of_wages_from_2000 = pd.read_excel('tab3-zpl_2024.xlsx', sheet_name='2000-2016 гг.') # датафрейм с зарплатами по отраслям c 2000 по 2016
df_of_wages_from_2017.dropna(inplace=True) # убираем строки с пропусками
df_of_wages_from_2017['Unnamed: 0'] = df_of_wages_from_2017['Unnamed: 0'].apply(lambda x: x.lower().strip()) # приводим столбцы с отраслями к единому формату(без пробелов в нижнем регистре)
# находим нужные нам отрасли
mine_branches_2017 = df_of_wages_from_2017[(df_of_wages_from_2017['Unnamed: 0'] == 'образование') | (df_of_wages_from_2017['Unnamed: 0'] == 'добыча полезных ископаемых')  | (df_of_wages_from_2017['Unnamed: 0'] == 'строительство') ]
df_of_wages_from_2000.dropna(inplace=True) # убираем строки с пропусками
df_of_wages_from_2000['Unnamed: 0'] = df_of_wages_from_2000['Unnamed: 0'].apply(lambda x: x.lower().strip()) # приводим столбцы с отраслями к единому формату(без пробелов в нижнем регистре)
# находим нужные нам отрасли

mine_branches_2000 = df_of_wages_from_2000[(df_of_wages_from_2000['Unnamed: 0'] == 'образование') | (df_of_wages_from_2000['Unnamed: 0'] == 'добыча полезных ископаемых')  | (df_of_wages_from_2000['Unnamed: 0'] == 'строительство') ]
# переименуем первый столбец
mine_branches_2017.rename(columns={'Unnamed: 0': 'Отрасль'}, inplace=True)
mine_branches_2000.rename(columns={'Unnamed: 0': 'Отрасль'}, inplace=True)
# объеденим данные в один датафрейм
wages = mine_branches_2000.merge(mine_branches_2017, on='Отрасль')
# Делаем "Отрасль" индексом и транспонируем
df = wages.set_index("Отрасль").T

