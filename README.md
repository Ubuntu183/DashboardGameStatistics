# DashboardGameStatistics

## Описание
Данный дашборд представляет собой инструмент анализа статистики игр, который позволяет пользователям просматривать данные по годам, жанрам и платформам.

## Страницы

### Общая Статистика
- **График Игр по Годам**: Показывает количество игр, выпущенных каждый год.
- **Топ-5 Платформ**: Выводит пять самых популярных платформ в определённом году.
- **Топ-5 Жанров**: Отображает пять самых популярных жанров в определённом году.

### Статистика по Платформам
- **Количество Игр**: Карточка с количеством игр для выбранной платформы.
- **Продажи в Долларах**: Карточка с общими продажами игр на выбранной платформе.
- **Популярная Игра**: Карточка с самой популярной игрой на платформе.
- **Топ Игр**: Таблица с лучшими играми по платформе.
- **Диаграмма Жанров**: Диаграмма, показывающая распределение жанров игр на платформе.

### Статистика по Жанрам
- **Выбор Жанра**: Пользователи могут выбрать жанр для анализа.
- **Выбор Года**: Пользователи могут выбрать год для анализа.
- **Количество Игр в Году**: Карточка с количеством игр выбранного жанра, выпущенных в выбранном году.
- **Продажи**: Карточка с продажами игр выбранного жанра в выбранном году.
- **Популярная Игра**: Карточка с самой популярной игрой выбранного жанра.
- **Топ Жанров**: Таблица с лучшими жанрами.
- **Диаграмма Платформ**: Диаграмма, показывающая распределение игр выбранного жанра по платформам.

## Ссылка на датасет
<https://www.kaggle.com/datasets/thedevastator/global-video-game-sales>

## Установка и запуск

1. Клонирование репозитория 

```git clone https://github.com/Ubuntu183/DashboardGameStatistics```

2. Создание виртуального окружения

```python -m venv venv```

3. Активация виртуального окружения

```source venv/bin/activate```

4. Установка зависимостей

```pip install dash pandas```
```pip install dash-bootstrap-components```
```import dash_bootstrap_components as dbc```

5. Запуск приложения

```python3 app.py```
