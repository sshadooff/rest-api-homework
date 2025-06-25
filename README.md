# Запуск

python main.py

# Добавление нового поста

curl http://127.0.0.1:5000/post/ -X POST -H "Content-Type: application/json" -d "{\"id\": 1, \"body\": \"This is my first post.\", \"author\": \"Tatyana\"}"

# Чтение поста по известному id

curl http://127.0.0.1:5000/post/1/

# Обновление поста по известному id

curl http://127.0.0.1:5000/post/1/ -X PUT -H "Content-Type: application/json" -d "{\"id\": 2, \"body\": \"This is my first post.\", \"author\": \"Tatyana\"}"

# Удаление поста по известному id

curl http://127.0.0.1:5000/post/2/ -X DELETE

# Пример выполнения

C:\Users\Татьяна>curl http://127.0.0.1:5000/post/ -X POST -H "Content-Type: application/json" -d "{\"id\": 1, \"body\": \"This is my first post.\", \"author\": \"Tatyana\"}"
{"id":1}

C:\Users\Татьяна>curl http://127.0.0.1:5000/post/1/
{"author":"Tatyana","body":"This is my first post.","id":1}

C:\Users\Татьяна>curl http://127.0.0.1:5000/post/1/ -X PUT -H "Content-Type: application/json" -d "{\"id\": 2, \"body\": \"This is my first post.\", \"author\": \"Tatyana\"}"
{"author":"Tatyana","body":"This is my first post.","id":2}

C:\Users\Татьяна>curl http://127.0.0.1:5000/post/2/
{"author":"Tatyana","body":"This is my first post.","id":2}

C:\Users\Татьяна>curl http://127.0.0.1:5000/post/2/ -X DELETE
Delete post with id 2
