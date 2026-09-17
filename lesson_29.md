1) Установить Jenkins на ВМ
2) Написать простой пайплайн `todoapp-php ci/cd`, состоящий из этапов:
- initialize - этап выводит приветственное сообщение "Start deploy ToDo app; Build ${BUILD_NUMBER}"
- checkout - этап клонирует репозиторий https://github.com/AnastasiyaGapochkina01/simplest-todo
- test - этап проводит тестирование кода; команда `phpunit --log-junit test-results.xml` (**!! ВАЖНО: тесты могут падать**)
- build and push image - этап собирает и пушит docker image
- deploy - этап деплоит собранный image на удаленный хост
- clean - этап удаляет все неиспользуемые docker images и запускается только если отмечен чекбокс "clean"

