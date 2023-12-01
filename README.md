### Статус код
если 400, то невалидные данные


### Создание заказа: 
        axios.post('https://cross-city-taxi.ru/core/api/orders/create/', {  
                from_place: "Москва, улица такая-то...",  
                to_place: "Лобня, караоке",  
                departure_time: "2023-09-21T15:00:00Z",  
                client: "Ден",  
                contact: "89123321154",  
                baby_chair: false,  
                tariff: 1
        })
### Создание отзыва: 
        axios.post('https://cross-city-taxi.ru/core/api/reviews/create/', {  
                name: "str",
                message: "str"
        })
### Создание обращения: 
        axios.post('https://cross-city-taxi.ru/core/api/feedback/create/', {  
                name: "Имя какое-то",
                phone_number: "str",
                email: "str",
                message: "str" 
        })
### Загрузка списка отзывов 
        axios.get('https://cross-city-taxi.ru/core/api/reviews/list/', {})
### Загрузка тарифов 
        axios.get('https://cross-city-taxi.ru/core/api/tariffs/list/', {})
### Загрузка городов 
        axios.get('https://cross-city-taxi.ru/core/api/cities/list/', {})


