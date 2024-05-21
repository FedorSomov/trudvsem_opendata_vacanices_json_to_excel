################################################
# Автор: Сомов-Туманский Фёдор Михайлович
# Контакты: телефон/whatsapp = +79313429628
#			email = f.m.somov@ya.ru
#
# Лучше писать на WhatsApp, там отвечаю быстрее
#################################################
#
# Для работы необходимо положить файлы с соответствующими данным
# в папки. Наименование файлов неважно, расширение JSON для файлов вакансий
# Файл с вакансиями в папку: vacancies
#
# Ссылки, откуда были взяты последние файлы:
# Вакансии Северо-Западного федерального округа из ЕЦП «Работа в России»
# https://opendata.trudvsem.ru/json/vacancy_5.json
#
# Вакансии Центрального федерального округа из ЕЦП «Работа в России»
# https://opendata.trudvsem.ru/json/vacancy_9.json
#
# ################################################

######################################
# Не забыть про pip!
# Импорт модулей:
# json - для работы с json файлами
# time - для отображения таймеров
# glob - для работы с папками
# pandas - для перевода словаря в дата фрейм и последующей записи в excel
# os - для работы с системными данными
# configparser - для работы с INI файлами
######################################

import json
import time
import pandas as pd
import glob
import os
import configparser

# Предупреждаем пользователя, что бы не трогал без надобности.
print('------------------------------------------------',
      'Скрипт запущен. Пожалуйста, ожидайте сообщения о том, что "выполнение скрипта полностью завершено".',
      '------------------------------------------------', sep='\n')
# Задаем начало отсчета выполнения скрипта

tic = time.perf_counter()


def mapping(vac_dict):
    """Делаем подстановку в полученные данные"""

    source_mapping = {
        'COMPANY': 'companycode',
        'INTERNET_RESOURCE': 'INTERNET_RESOURCE',
        'EMPLOYMENT_SERVICE': 'EMPLOYMENT_SERVICE',
        'HR_SERVICE': 'HR_SERVICE',
        'RECRUITMENT_AGENCY': 'RECRUITMENT_AGENCY',
        '': ''
    }

    if 'Источник' in vac_dict:
        vac_dict['Источник'] = source_mapping.get(vac_dict['Источник'], vac_dict['Источник'])

    accomodation_mapping = {
        'FLAT': 'FLAT',
        'HOUSE': 'HOUSE',
        'DORMITORY': 'DORMITORY',
        'ROOM': 'ROOM',
        '': ''
    }

    if 'Вид предоставляемого жилья' in vac_dict:
        vac_dict['Вид предоставляемого жилья'] = accomodation_mapping.get(vac_dict['Вид предоставляемого жилья'],
                                                                          vac_dict['Вид предоставляемого жилья'])

    return vac_dict


def ensure_directory_exists(directory):
    """Проверяем существование папки и создаем её при необходимости."""
    if not os.path.exists(directory):
        os.makedirs(directory)
        print('------------------------------------------------',
              f'Создана директория: {directory}',
              '------------------------------------------------', sep='\n')


def save_to_excel(data, file_path):
    while True:
        try:
            pd.DataFrame(data, dtype="string").to_excel(file_path, index=False)

            print(f'------------------------------------------------',
                  f'Данные записаны в {file_path}',
                  f'------------------------------------------------', sep='\n')
            break
        except PermissionError:
            print(f"Не удалось записать данные в {file_path}. Файл, возможно, открыт в другой программе.")
            input("Пожалуйста, закройте файл и нажмите любую клавишу для продолжения...")


def check_files():
    try:
        vacancies_directory = 'vacancies'
        ensure_directory_exists(vacancies_directory)

        # Получаем список файлов в директории
        files = glob.glob(os.path.join(vacancies_directory, '*.json'))

        files.sort(key=os.path.getmtime, reverse=True)
        latest_file = files[0]
        print('------------------------------------------------',
              'Файл в формате JSON найден.',
              '------------------------------------------------', sep='\n')
    except:
        print('------------------------------------------------',
              'Файлы в формате JSON не найдены. ПРОВЕРЬТЕ ФАЙЛЫ',
              '------------------------------------------------', sep='\n')
        raise SystemExit

    last_modified = os.path.getmtime(latest_file)
    rus_date = time.strftime('%d.%m.%Y %H:%M:%S', time.localtime(last_modified))
    print('-------------ДАТЫ ОБНОВЛЕНИЯ ФАЙЛОВ-------------')
    print('Самый свежий файл: ', latest_file)
    print('Дата последней модификации самого свежего файла: ', rus_date)

    return latest_file


def parser(file_path=None):
    """ Задаем список, в который будем записывать словари из json вакансий"""
    vac_data_list = []
    nodata = ''
    """ Для смены региона - поменять переменную region_code в .INI файле на код региона из справочника """

    # Чтение конфигурации из ini файла
    config = configparser.ConfigParser()
    config.read('config.ini')

    # Получаем значение region_code из ini файла
    region_code = config.get('Settings', 'region_code')
    output_file = config.get('Settings', 'output_file')

    print('------------------------------------------------',
          'Начинаем разбор файла',
          '------------------------------------------------', sep='\n')
    print(f" Файл {file_path}")
    with open(file_path, encoding='utf-8') as f:
        data_vac = json.load(f)

    for vac in data_vac['vacancies']:
        if region_code not in vac['state_region_code']:
            continue
        vac_dict = {'ID Вакансии': vac.get('id', nodata), 'Квоты, соцзащита': vac.get('social_protected_ids', nodata),
                    'Наименование Вакансии': vac.get('vacancy_name', nodata),
                    'Сфера труда': vac.get('professionalSphereName', nodata),
                    'Код комании ЕАИС': int(vac['company'].get('companycode', nodata)) if str(
                        vac['company'].get('companycode', nodata)).isdigit() else vac['company'].get('companycode',
                                                                                                     nodata),
                    'ИНН': int(vac['company'].get('inn', nodata)) if str(
                        vac['company'].get('inn', nodata)).isdigit() else vac['company'].get('inn', nodata),
                    'ОГРН': int(vac['company'].get('ogrn', nodata)) if str(
                        vac['company'].get('ogrn', nodata)).isdigit() else vac['company'].get('ogrn', nodata),
                    'КПП': int(vac['company'].get('kpp', nodata)) if str(
                        vac['company'].get('kpp', nodata)).isdigit() else vac['company'].get('kpp', nodata),
                    '"Наименование компании': vac['company'].get('name', nodata),
                    'Образование': vac.get('education', nodata),
                    'Опыт': int(vac.get('required_experience', nodata)) if str(
                        vac.get('required_experience', nodata)).isdigit() else vac.get('required_experience', nodata),
                    'График работы': vac.get('schedule_type', nodata), 'Занятость': vac.get('busy_type', nodata),
                    'Мин зарплата': int(vac.get('salary_min', nodata)) if str(
                        vac.get('salary_min', nodata)).isdigit() else vac.get('salary_min', nodata),
                    'Макс зарплата': int(vac.get('salary_max', nodata)) if str(
                        vac.get('salary_max', nodata)).isdigit() else vac.get('salary_max', nodata),
                    'Ссылка на вакансию': vac.get('vac_url', nodata), 'Дата обновления': vac.get('date_create', nodata),
                    'Код профессии': int(vac.get('code_profession', nodata)) if str(
                        vac.get('code_profession', nodata)).isdigit() else vac.get('code_profession', nodata),
                    'Регион Вакансии': int(vac['state_region_code']) if str(
                        vac.get('state_region_code', nodata)).isdigit() else vac.get('state_region_code', nodata),
                    'Адрес': vac.get('vacancy_address', nodata),
                    'Рабочих мест': int(vac.get('work_places', nodata)) if str(
                        vac.get('work_places', nodata)).isdigit() else vac.get('work_places', nodata),
                    'Дата создания': vac.get('date_modify', nodata),
                    'Квота': "да" if (vac.get('is_quoted')) else 'нет',
                    'Источник': (vac.get('original_source_type', nodata)),
                    "Возможность предоставления жилья": "да" if (vac.get('accommodation_capability')) else '',
                    "Вид предоставляемого жилья": (vac.get('accommodation_type', nodata))}

        vac_dict = mapping(vac_dict)

        vac_data_list.append(vac_dict)

    print('------------------------------------------------',
          'Разбор файла закончен',
          'Переносим полученные данные в DataFramePandas',
          'И записываем данные в Excel',
          '------------------------------------------------', sep='\n')
    save_to_excel(vac_data_list, output_file)


file_path = check_files()
parser(file_path)
toc = time.perf_counter()
print('------------------------------------------------',
      f'Скрипт выполнен за: {toc - tic:0.1f} секунд',
      'Файл output.xlsx в корневой папке скрипта',
      'выполнение скрипта полностью завершено',
      '------------------------------------------------', sep='\n')
