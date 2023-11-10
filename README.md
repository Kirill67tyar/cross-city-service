# cross-city-service
### Создание заказа:  
    axios.post('https://cross-city-taxi.ru/core/api/orders/create/', {  
            from_place: "Москва, улица такая-то...",  
            to_place: "Лобня, караоке",  
            departure_time: "2023-09-21T15:00:00Z",  
            client: "Ден",  
            contact: "89123321154",  
            baby_chair: false,  
            tariff: 1,  
            csrf_token: "DASDGFsdfaadfSDFasdf342dsf"  
    })

