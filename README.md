### Файлы
В данном проекте вы можете встретить файлы:
- DECISIONS.md описывает самостоятельные технические решения;
- LEARNING_NOTES.md описывает ход моего обучения технологиям. 

### Основные команды для работы с проектом
1. Команда сборки контейнеров с последующим запуском:
```docker compose up --build```

2. Команда для заполнения базы данных тестовыми данными:
```docker compose exec api poetry run python -m app.cli.seed```

3. Команда для запуска тестов:
```docker compose exec api poetry run pytest```

4. Команда для проверки форматирования кода:
```docker compose exec api poetry run ruff format --check .```

Если вам требуется проверка на потенциальные ошибки, то запустите команду:
```docker compose exec api poetry run ruff check .```

5. Команда запуска статического анализатора типов mypy:
```docker compose exec api poetry run mypy app```

6. По завершению работы остановите контейнеры с помощью команды:
```docker compose down```