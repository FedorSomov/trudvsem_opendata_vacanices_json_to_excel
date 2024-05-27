[Русский](#русский) | [English](#english)

# Русский
# TRUDVSEM.RU Парсер вакансий

Этот проект представляет собой скрипт для парсинга вакансий из JSON файлов, предоставленных порталом "Работа в России". Скрипт обрабатывает данные и сохраняет их в формате Excel.

## Содержание

- [Описание](#описание)
- [Установка python версии](#установка_py)
- [Установка exe версии](#установка_exe)
- [Использование](#использование)
- [Первый запуск](#первый_запуск)
- [Коды региона](#регионы)
- [Файлы вакансий](#вакансии)
- [Контакты](#контакты)

## Описание

Скрипт парсит данные о вакансиях из JSON файлов, фильтрует их по региону и сохраняет в Excel файл. Данные можно загрузить с портала "Работа в России" (https://trudvsem.ru/opendata/datasets).


## установка_py


1. Склонируйте репозиторий:

    ```bash
    git clone https://github.com/FedorSomov/trudvsem_opendata_vacanices_json_to_excel.git
    cd repository
    ```

2. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

## установка_exe


1. Перейдите в папку `dist` на [странице репозитория](https://github.com/FedorSomov/trudvsem_opendata_vacanices_json_to_excel/tree/main/dist).

2. Скачайте исполняемый файл `project_name.exe` и файл конфигурации `config.ini`:

    - [Скачать project_name.exe](https://github.com/FedorSomov/trudvsem_opendata_vacanices_json_to_excel/main/dist/project_name.exe)
    - [Скачать config.ini](https://github.com/FedorSomov/trudvsem_opendata_vacanices_json_to_excel/raw/main/config.ini)

3. Поместите оба файла в одну папку на вашем компьютере.

## Использование

### Использование Python версии

1. Положите файлы вакансий в папку `vacancies`.

2. Обновите файл конфигурации `config.ini` с нужными параметрами:

    ```ini
    [Settings]
    region_code = 4600000000000
    output_file = output.xlsx
    ```

3. Запустите скрипт:

    ```bash
    python script.py
    ```

### Использование exe версии

1. Положите файлы вакансий в папку `vacancies`.

2. Обновите файл конфигурации `config.ini` с нужными параметрами:

    ```ini
    [Settings]
    region_code = 4600000000000
    output_file = output.xlsx
    ```

3. Запустите исполняемый файл `project_name.exe`

## первый_запуск

При запуске .py или .exe первым делом будет проверена на наличие папка vacancies. Так что её можно не создавать вручную - скрипт создаст её сам.

## регионы


Файл region_codes.txt содержит наименования всех регионов и их коды по состоянию на 27.05.2024
Список регионов и коды можно найти на портале "Работа в России" (https://opendata.trudvsem.ru/json/regions.json).


## вакансии

Вакансии по округам можно взять отсюда: https://trudvsem.ru/opendata/datasets
Не рекомендую брать все вакансии одним файлом - объем довольно большой. 
Для более плавной работы рекомендую обрабатывать округ за округом.

## Контакты

Автор: Сомов-Туманский Фёдор Михайлович  
Телефон/WhatsApp: +79313429628  
Email: f.m.somov@ya.ru  

**Лучше писать на WhatsApp, там отвечаю быстрее**








# English
# TRUDVSEM.RU Vacancies Parser

This project is a script for parsing job vacancies from JSON files provided by the "Work in Russia" portal. The script processes the data and saves it in Excel format.

## Table of Contents

- [Description](#description)
- [Installation for Python Version](#installation_py)
- [Installation for Executable Version](#installation_exe)
- [Usage](#usage)
- [First Run](#first_run)
- [Region Codes](#regions)
- [Job Vacancy Files](#vacancies)
- [Contacts](#contacts)

## Description

The script parses job vacancy data from JSON files, filters them by region, and saves them in an Excel file. Data can be downloaded from the "Work in Russia" portal (https://trudvsem.ru/opendata/datasets).

## Installation for Python Version

1. Clone the repository:

    ```bash
    git clone https://github.com/FedorSomov/trudvsem_opendata_vacanices_json_to_excel.git
    cd repository
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Installation for Executable Version

1. Navigate to the `dist` folder on the [repository page](https://github.com/username/repository/tree/main/dist).

2. Download the executable file `project_name.exe` and the configuration file `config.ini`:

    - [Download project_name.exe](https://github.com/FedorSomov/trudvsem_opendata_vacanices_json_to_excel/main/dist/Json_To_Xslx.exe)
    - [Download config.ini](https://github.com/FedorSomov/trudvsem_opendata_vacanices_json_to_excel/main/dist/config.ini)

3. Place both files in the same folder on your computer.

## Usage

### Using the Python Version

1. Place the job vacancy files in the `vacancies` folder.

2. Update the `config.ini` file with the necessary parameters:

    ```ini
    [Settings]
    region_code = 4600000000000
    output_file = output.xlsx
    ```

3. Run the script:

    ```bash
    python script.py
    ```

### Using the Executable Version

1. Place the job vacancy files in the `vacancies` folder.

2. Update the `config.ini` file with the necessary parameters:

    ```ini
    [Settings]
    region_code = 4600000000000
    output_file = output.xlsx
    ```

3. Run the executable file `project_name.exe`.

## First Run

When running .py or .exe for the first time, the script will check for the existence of the `vacancies` folder. So you don't need to create it manually - the script will create it itself.

## Region Codes


region_codes.txt contains all regions and codes. Update at 27.05.2024
A list of regions and codes can be found on the "Work in Russia" portal (https://opendata.trudvsem.ru/json/regions.json).

## Job Vacancy Files

Job vacancies by regions can be obtained from here: https://trudvsem.ru/opendata/datasets. It is not recommended to take all vacancies in one file - the volume is quite large. For smoother operation, I recommend processing one region at a time.

## Contacts

Author: Fedor Somov-Tumansky  
Phone/WhatsApp: +79313429628  
Email: f.m.somov@ya.ru  

**It's better to write on WhatsApp, I respond faster**
