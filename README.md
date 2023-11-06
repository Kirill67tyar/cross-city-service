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



### Пояснения:  
'https://cross-city-taxi.ru/core/api/orders/create/' - url для создания заказа (только post-запрос)  

from_place - Место отправления, максимальная длина - 100, placeholder - "Например: Москва"  

to_place - Место прибытия, максимальная длина - 100, placeholder - "Например: Казань"  

departure_time - Время отправления строго в формате YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]  
                    Например - "2023-09-21T15:00:00Z"  

client - Имя клиента,  максимальная длина - 100, placeholder - "Например: Александр"  

contact - телефон/tg_account/email клиента, максимальная длина - 150, placeholder - "+7(***)***-**-**"  

baby_chair - с детским креслом или без, допустимое значение true или false,  
                можно сделать в виде переключателя (Switches) или checkbox  

tariff - любой id из get запроса https://cross-city-taxi.ru/core/api/tariffs/list/  

csrf_token - в куках берётся значение по ключу csrftoken,  
                например в csrftoken=DASDGFsdfaadfSDFasdf342dsf  
                будет браться часть после "=" - DASDGFsdfaadfSDFasdf342dsf  
