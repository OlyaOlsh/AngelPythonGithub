let tg = window.Telegram.WebApp;
    tg.expand();
    let buy = document.getElementById("buy");
    let order = document.getElementById("order");



    let p = document.createElement("p");

    p.innerText = `${tg.initDataUnsafe.user.first_name}
    ${tg.initDataUnsafe.user.last_name}`;

    buy.addEventListener("click", () => {
        document.getElementById("main").style.display = "none";
        document.getElementById("form").style.display = "block";
        document.getElementById("user_name").value =  tg.initDataUnsafe.user.first_name + " "+  tg.initDataUnsafe.user.last_name
        document.getElementById("user_email").value = "111@gmail.com"
    })

    order.addEventListener("click", () => {
        tg.close();
    });