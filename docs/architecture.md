event_backend/
├── app/                                   # Основное приложение
│   ├── main.py                            # Точка входа 
│   ├── adapters/                          # Адаптеры
│   │   └── db/                            # Реализации работы с БД + ORM модели
│   │       └── models/                    # ORM-модели (SQLAlchemy)
│   ├── api/                               # Веб-слой (интерфейс)
│   │   ├── middlewares/                   # Middleware
│   │   └── v1/                            # Первая версия API
│   │       ├── dependencies/              # Зависимости (depends)
│   │       └── routers/                   # Роутеры (эндпоинты)
│   ├── config/                            # Конфигурация приложения (ключи и прочее)
│   ├── domain/                            # Домен
│   │   ├── models/                        # Доменные модели
│   │   ├── ports/                         # Порты 
│   │   ├── services/                      # Сервисы 
│   │   └── exceptions.py                  # Кастомные исключения
│   └── utils/                             # Вспомогательный код
├── docs/                                  # Документация проекта
├── tests/                                 # Тесты
│   ├── integration/                       # Интеграционные тесты
│   └── unit/                              # Юнит-тесты
└── .gitignore 
