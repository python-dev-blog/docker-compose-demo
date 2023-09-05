# Docker Compose

[Ссылка на видео по docker-compose]()

[Список основных Docker кмоманд](https://github.com/python-dev-blog/docker-demo)

### Запуск приложения

```
git clone git@github.com:python-dev-blog/docker-compose-demo.git
cd docker-compose-demo
docker-compose up
```

### Запуск контейнеров

- `docker inspect` - запускает все сервисы и контейнеры на основе вашего docker-compose.yml файла
- `docker-compose up -d` - запускает все контейнеры в фоновом режиме (не блокирует консоль)
- `docker-compose up postgres>` - запускает определенный сервис (вместо postgres подставьте нужный)
- `docker-compose --profile dev up` - запускает только те контейнеры, которые относятся к профилю dev
- `docker-compose start` - запускает остановленные контейнеры
- `docker-compose build` - собирает образы
- `docker-compose up --build` - запускает и одновременно пересобирает образы, если они были изменены с момента последнего запуска или если они еще не были созданы
- `docker-compose restart` - перезапустить контейнеры


### Остановка контейнеров

- `docker-compose down` - останавливает и удаляет все контейнеры и сети, созданные с помощью `docker-compose up`
- `docker-compose down --remove-orphans` - если какие-либо контейнеры остаются после остановки всех сервисов, которые изначально их создали, то эти оставшиеся контейнеры также будут удалены
- `docker-compose down --volumes` - останавливает контейнеры и удаляет связанные с ними volumes
- `docker-compose stop` - останавливает контейнеры, созданные с помощью `docker-compose up`, без их удаления

### Состояние контейнеров

- `docker-compose logs` - просмотреть логи
- `docker logs <container_name>` - посмотреть логи конкретного контейнера
- `docker-compose ps` - просмотреть статус запущенных контейнеров
- `docker-compose top` - отображает информцию о процессах внутри контейнеров
- `docker inspect <container_id>` - показывает json с настройками контейнера и его состоянием

### Масштабирование

- `docker-compose up -d --scale <service_name>=<num_instances>` - масштабирует количество запущенных контейнеров для указанного сервиса

### Выполнение команд внутри контейнера

- `docker-compose exec <container_id> <command>` - позволяет выполнять команды внутри контейнера, например `docker exec 7cbde5a06bbb pytest api/tests.py`
- `docker exec -it <container_id> /bin/sh` - открыть консоль контейнера
