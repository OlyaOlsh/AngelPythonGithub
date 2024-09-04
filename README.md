<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shop</title>
<style>
  /* Установка шрифта Montserrat для всего приложения */
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600&display=swap');

/* Сброс стилей для всех элементов */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Основные стили для body */
body {
    font-family: 'Montserrat', sans-serif;
    background-color: #f4f4f4; /* Легкий светло-серый фон */
    color: #333; /* Темный текст для хорошего контраста */
}

/* Стили для основного контейнера */
#main {
    max-width: 600px; /* Ограничение максимальной ширины */
    margin: 20px auto; /* Центрируем контейнер */
    padding: 20px; /* Внутренние отступы */
    background-color: #ffffff; /* Белый фон для контента */
    border-radius: 8px; /* Скругление углов */
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1); /* Легкая тень */
}

/* Стиль для формы */
form {
    display: flex;
    flex-direction: column;
    gap: 15px; /* Пространство между элементами */
}

/* Стиль для полей ввода */
input {
    height: 48px; /* Высота поля ввода, чтобы соответствовать кнопке */
    border: 2px solid #cccccc; /* Светло-серая рамка */
    border-radius: 5px; /* Скругленные углы */
    padding: 0 12px; /* Горизонтальные внутренние отступы */
    font-size: 16px; /* Размер шрифта */
    transition: border-color 0.3s, box-shadow 0.3s; /* Плавный переход */

    max-width: 600px; /* Ограничение максимальной ширины */
    margin: 20px auto; /* Центрируем контейнер */
}

/* Стиль полей ввода при фокусе и наведении */
input:focus {
    border-color: #4caf50; /* Зеленая рамка при фокусе */
    box-shadow: 0 0 5px rgba(76, 175, 80, 0.5); /* Легкая тень при фокусе */
}

/* Стили для кнопок */
button {
    height: 48px; /* Высота кнопки, чтобы соответствовать полям ввода */
    padding: 0 12px; /* Горизонтальные внутренние отступы */
    font-size: 16px; /* Размер шрифта */
    border: none; /* Убираем рамку */
    border-radius: 5px; /* Скругленные углы */
    background-color: #007BFF; /* Основной цвет кнопки (синий) */
    color: #ffffff; /* Белый текст */
    cursor: pointer; /* Указатель мыши при наведении */
    transition: background-color 0.3s, transform 0.2s; /* Плавные переходы */

    margin: 20px auto; /* Центрируем контейнер */
}

/* Стили для кнопок при наведении */
button:hover {
    background-color: #0056b3; /* Более темный синий цвет */
    transform: translateY(-2px); /* Легкий подъем кнопки при наведении */
}

/* Стили для состояния активности кнопки */
button:active {
    transform: translateY(1px); /* Легкое опускание кнопки при клике */
}

/* Пример медиа-запросов для мобильных устройств */
@media (max-width: 480px) {
    #main {
        padding: 15px; /* Уменьшение отступов на мобильных */
    }

    input, button {
        font-size: 14px; /* Уменьшение размера шрифта для мобильных */
    }
}
</style>
</head>
<body>
    <div id ="main">
        <h1>Онлайн магазин</h1>
        <p>Вы можете добавить сюда любой функционал</p>
        <button id="buy">Купить</button>
    </div>
    <form id =form">
        <input type="text" placeholder = "Имя" id ="user_name">
        <input type="text" placeholder = "Email" id ="user_email">
        <input type="text" placeholder = "Телефон" id ="user_phone">
        <button id="order">Оформить</button>
    </form>
<script src="https://telegram.org/js/telegram-web-app.js"></script>
</body>
</html>

<!--
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Choose a Master</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f8;
        }
        .container {
            max-width: 400px;
            margin: 20px auto;
            background-color: #ffffff;
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        .header {
            padding: 20px;
            background-color: #d8e5ff;
            border-bottom: 1px solid #ccc;
        }
        .header h1 {
            margin: 0;
            font-size: 18px;
            color: #333;
        }
        .header p {
            margin: 5px 0 0;
            font-size: 14px;
            color: #666;
        }
        .master-list {
            list-style: none;
            padding: 0;
            margin: 0;
        }
        .master-item {
            display: flex;
            align-items: center;
            padding: 15px;
            border-bottom: 1px solid #eee;
        }
        .master-item img {
            border-radius: 50%;
            width: 50px;
            height: 50px;
            margin-right: 15px;
        }
        .master-info {
            flex-grow: 1;
        }
        .master-info h2 {
            margin: 0;
            font-size: 16px;
            color: #333;
        }
        .master-info p {
            margin: 2px 0;
            font-size: 14px;
            color: #666;
        }
        .rating {
            font-size: 14px;
            color: #ffbf00;
            display: flex;
            align-items: center;
        }
        .rating span {
            margin-left: 5px;
            color: #333;
        }
        .bottom-nav {
            display: flex;
            justify-content: space-around;
            padding: 10px;
            background-color: #d8e5ff;
        }
        .bottom-nav a {
            text-decoration: none;
            color: #333;
            font-size: 14px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .bottom-nav a img {
            width: 20px;
            height: 20px;
        }
    </style>
</head>
<body>

<div class="container">
    <div class="header">
        <h1>SnipStyle</h1>
        <p>55 Tib street, Manchester</p>
        <p>Wash & BlowDry Incl. Treatment</p>
    </div>

    <ul class="master-list">
        <li class="master-item">
            <img src="/static/foto1.jpg" alt="Ann Berrington">
            <div class="master-info">
                <h2>Ann Berrington</h2>
                <p>40 min | 35£</p>
            </div>
            <div class="rating">
                ⭐<span>4.9</span>
            </div>
        </li>
        <li class="master-item">
            <img src="/static/foto2.jpg" alt="Jordan Dutton">
            <div class="master-info">
                <h2>Jordan Dutton</h2>
                <p>40 min | 35£</p>
            </div>
            <div class="rating">
                ⭐<span>4.8</span>
            </div>
        </li>
        <li class="master-item">
            <img src="/static/foto3.jpg" alt="Susan Evans">
            <div class="master-info">
                <h2>Susan Evans</h2>
                <p>40 min | 45£</p>
            </div>
            <div class="rating">
                ⭐<span>5.0</span>
            </div>
        </li>
    </ul>

    <div class="bottom-nav">
        <a href="#">
            <img src="/static/icon1.png" alt="Explore">
            Explore
        </a>
        <a href="#">
            <img src="/static/icon2.png" alt="Favourites">
            Favourites
        </a>
        <a href="#">
            <img src="/static/icon3.png" alt="Bookings">
            Bookings
        </a>
        <a href="#">
            <img src="/static/icon4.png" alt="Profile">
            Profile
        </a>
    </div>
</div>

</body>
</html>
-->
