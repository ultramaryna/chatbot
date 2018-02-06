# -*- coding: utf-8 -*-
name_xxx =''

answers = {

        'welcome':[
                    'Cześć, {name}!',
                    'Hej',
                    'Dzień dobry, {name}. Masz jakieś pytania o smog?'
                    ],
        'enigma': [
                    'I tu mnie masz! Nie wiem, co powiedzieć.',
                    'Hmm, chyba nie umiem odpowiedzieć. Czy możesz sformułować swoje pytanie inaczej?'
                    ],
        'ask': [
                    'Śmiało, zadaj pytanie',
                    'Co cię ciekawi?',
                    'Co chcesz wiedzieć?',
                    'Pytaj, jestem tu, by z Tobą porozmawiać :)'
                    ],
        'how_are_you':[
                    'Całkiem nieźle, dzięki że pytasz :)',
                    ],
        'name':[
                    'Jestem ChatBotem smogowym, na razie nie mam imienia.',
                    ],
        'date':[
                    'Dziś mamy kolejny dzień 2018 roku. Nie wiem jaki dzień tygodnia.',
                    ],
        'time':[
                    'Nie mam zegarka',
                    ],
        'location': [
                    'Twoja lokalizacja to {sensor}'],
        # 'weather':[
        #             'Dziś mamy całkiem ładny dzień w Krakowie.',
        #             ],
        'if_smog': [
                    'Tak, teraz mamy duży smog.',
                    'Dziś mamy wyjatkow czyste powietrze.',
                    'Dzisiaj w Twojej okolicy poziom zanieczyszczenia powietrza wynosi {pollution_level}. Dane zmierzył czujnik w miejscu: {sensor}'
                    ],
        'if_smog_1': [
                    'Powietrze jest dzisiaj bardzo czyste! To świetny dzień, by wyjść na zewnątrz! Dane zmierzył czujnik w miejscu: {sensor}'
                    ],
        'if_smog_2': [
                    'Dzisiaj powietrze jest czyste. Nie ma się czym martwić, możesz wyjść na zewnątrz. Dane zmierzył czujnik w miejscu: {sensor}'
                    ],
        'if_smog_3': [
                    'Bywało gorzej, ale powietrze nie jest dziś najczystsze. Możesz wyjść, ale to nie jest dobry moment na aktywność fizyczną na powietrzu. Dane zmierzył czujnik w miejscu: {sensor}'
                    ],
        'if_smog_4': [
                    'Uch, powietrze jest zanieczyszczone. Jeśli możesz, zostań w domu. Dane zmierzył czujnik w miejscu: {sensor}'
                    ],
        'if_smog_5': [
                    'Dzisiaj smog jest naprawdę duży. Używaj maski antysmogowej lub zostań w domu. To nie jest dobry czas na sport na powietrzu! Dane zmierzył czujnik w miejscu: {sensor}'
                    ],
        'if_smog_6': [
                    'Powietrze jest BARDZO ZŁE. Zostań w domu.'
                    ],
        'if_rain_rain': [
                    'Tak, dziś pada. Niestety.',
                    'Pada i to jak!',
                    'Kap kap kap'
                    ],
        'if_rain_chancerain': [
                    'Możliwe opady ;(',
                    ],
        'if_rain_snow': [
                    'Dzisiaj pada śnieg. Nie widzisz?',
                    ],
        'if_rain_no': [
                    'Dziś nie będzie padać',
                    ],

        'temperature': [
                    'Temperatura wynosi dziś {temperature}°C',
                    ],
        'pressure': [
                    'Ciśnienie wynosi dziś {pressure}hPa',
                    ],
        'what_smog': [
                    'Smog (dymgła) to nienaturalne zjawisko atmosferyczne polegające na współwystępowaniu zanieczyszczenia powietrza wskutek działalności człowieka oraz niekorzystnych zjawisk naturalnych: znacznego zamglenia i bezwietrznej pogody.',
                    ],
        'harm_smog': [
                    'Wchodzące w skład smogu związki chemiczne, pyły i znaczna wilgotność stanowią zagrożenie dla zdrowia człowieka. Są czynnikami alergizującymi i mogą wywołać astmę oraz jej napady, a także powodować zaostrzenie przewlekłego zapalenia oskrzeli, niewydolność oddechową lub paraliż układu krwionośnego.'
                    ],

        'dusts': [
                    'Aerozole atmosferyczne (pyły zawieszone) to  ciekłe krople lub stałe cząstki pochodzenia naturalnego, jak w przypadku aerozolu soli morskiej lub pyłów mineralnych, albo cząstki produkowane przez człowieka (zanieczyszczenia), jak to jest w przypadku aerozolu kropli lub cząstek stałych siarczanów. Często prekursorami aerozoli atmosferycznych są tlenki siarki i azotu, które są przekształcane w procesach chemicznych i fotochemicznych w aerozole atmosferyczne. W skład smogu wchodzą pyły zawieszone PM2.5 i PM10.'
                    ],
        'dusts_level':[
                    'Poziom pyłów zawieszonych na dziś ###',
                    ],
        'PM2.5': [
                    'Pył PM2,5 zawiera cząstki o średnicy mniejszej niż 2,5 mikrometra, które mogą docierać do górnych dróg oddechowych, płuc oraz przenikać do krwi. Docelowa wartość średnioroczna dla pyłu PM2,5 wynosi 25 µg/m3, poziom dopuszczalny 25 µg/m3, a poziom dopuszczalny powiększony o margines tolerancji dla 2012 r. 27 µg/m3.'
                    ],
        'PM10': [
                    'Pył PM10 składa się z mieszaniny cząstek zawieszonych w powietrzu, będących mieszaniną substancji organicznych i nieorganicznych. Pył zawieszony może zawierać substancje toksyczne takie jak wielopierścieniowe węglowodory aromatyczne (np. benzo/a/piren), metale ciężkie oraz dioksyny i furany. Pył PM10 zawiera cząstki o średnicy mniejszej niż 10 mikrometrów, które mogą docierać do górnych dróg oddechowych i płuc. Poziom dopuszczalny dla stężenia średniodobowego wynosi 50 µg/m3 i może być przekraczany nie więcej niż 35 dni w ciągu roku. Poziom dopuszczalny dla stężenia średniorocznego wynosi 40 µg/m3, a poziom alarmowy 200 µg/m3.'
                    ],

        'protect': [
                    'Przede wszystkim staraj się jak najkrócej przebywać na zewnątrz. Możesz też zaopatrzyć się ma maskę gazową lub oczyszczacz powietrza.',
                    ],
        'mask':     [
                    'Maska antysmogowa chroni przed zanieczyszczonym powietrzem. Na pewno pomoże, ale prawdopodobnie i tak nie zatrzyma zanieczyszczeń w 100%. Warto ją mieć, jeśli smog w Twoim mieście jest duży, a Ty często przebywasz na zewnątrz. Pamiętaj tylko, by wybrać dobry model!'
        ],
        'mask-advice': [
                    'Przykro mi, ale nie reklamuję żadnych produktów, więc nie mogę polecić konkretnego modelu ani sklepu.'
                    ],
        'mask-price': [
                    'Ceny się różnią, ale przygotuj się na wydanie co najmniej 100 zł. Pamiętaj, że to nie koniec wydatków, do maski trzeba regularnie kupować filtry.'
                    ],
        'air-cleaner': [
                    'Podstawową zasadą działania oczyszczacza jest przefiltrowanie powietrza w pomieszczeniu. Urządzenie zasysa powietrze, a następnie odfiltrowuje z niego zanieczyszczenia. Oczyszczacz znacznie polepsza jakość powietrza w pomieszczeniu.'
                    ],
        'smog-prevent': [
                    'Należy przede wszystkim zmienić standardy piecyków spalających węgiel w domostwach lub wybrać alternatywne, ekologiczne formy ich ogrzewania. Powinniśmy popularyzować publiczne środki transportu, ograniczać ruch kołowy w centrach miast i stosować nowoczesne technologie w przemyśle.'
                    ],
        'no_data': [
                    'Przykro mi, ale nie udzieliłeś zgody na geolokalizację, więc nie wiem nic o stanie powietrza w Twojej okolicy.'
                    ],
        'future': [
                    'Niestety nie mam informacji na temat prognozy pogody i jakości powietrza na kolejne dni. Nie jestem wróżką.'
                    ],


    }

gifs = {
        'welcome':[
                    'https://media.giphy.com/media/3o6fJ2ilZ4nOYQm2EU/giphy.gif',
                    'https://media.giphy.com/media/3ornk57KwDXf81rjWM/giphy.gif',
                    'https://media.giphy.com/media/mW05nwEyXLP0Y/giphy.gif'
                    ],

        'if_smog': [
                    'https://media.giphy.com/media/xEjTM5COAKyNa/giphy.gif',
                    'https://media.giphy.com/media/bfZy3DHuJUc12/giphy.gif',
                    'https://media.giphy.com/media/l3q2LxWDA08yHvGso/giphy.gif'
                    ],
        'if_rain_rain': [
                    'https://media.giphy.com/media/yoJC2Olx0ekMy2nX7W/giphy.gif',
                    'https://media.giphy.com/media/3o7btWO4T2Wp97lbgc/giphy.gif',
                    'https://media.giphy.com/media/3osxYcKIttf3N5GTsY/giphy.gif'
                    ],
        'if_rain_chancerain': [
                    'https://media.giphy.com/media/yoJC2Olx0ekMy2nX7W/giphy.gif',
                    'https://media.giphy.com/media/3o7btWO4T2Wp97lbgc/giphy.gif',
                    'https://media.giphy.com/media/3osxYcKIttf3N5GTsY/giphy.gif'
                    ],
        'if_rain_snow': [
                    'https://media.giphy.com/media/l2JHRxJ6gFSaWbOBW/giphy.gif',
                    'https://media.giphy.com/media/l49FiX2pvMPPmCfSw/giphy.gif',
                    'https://media.giphy.com/media/26tneSGWphvmFlUju/giphy.gif'
                    ],
        'what_smog': [
                    'https://media.giphy.com/media/xEjTM5COAKyNa/giphy.gif',
                    'https://media.giphy.com/media/bfZy3DHuJUc12/giphy.gif',
                    'https://media.giphy.com/media/l3q2LxWDA08yHvGso/giphy.gif'
                    ],
        'enigma': [
                    'https://media.giphy.com/media/xhN4C2vEuapCo/giphy.gif',
                    'https://media.giphy.com/media/xDQ3Oql1BN54c/giphy.gif',
                    ],
        'future': [
                    'https://media.giphy.com/media/BZUXTEvJSPsUo/giphy.gif',
                    'https://media.giphy.com/media/xT1XGx85kYUIFWI4wg/giphy.gif',
                    'https://media.giphy.com/media/3QxZMGDo7FCLu/giphy.gif',
                    ]

    }

images = {
        '01d':[
                    'clear.svg'
                    ],
        '01n':[
                    'clear.svg'
                    ],
        '02d':[
                    'partlysunny.svg'
                    ],
        '02n':[
                    'partlysunny.svg'
                    ],
        '03d':[
                    'cloudy.svg'
                    ],
        '03n':[
                    'cloudy.svg'
                    ],
        '04d':[
                    'cloudy.svg'
                    ],
        '04n':[
                    'cloudy.svg'
                    ],
        '09d':[
                    'rain.svg'
                    ],
        '09n':[
                    'rain.svg'
                    ],
        '10d':[
                    'chancerain.svg'
                    ],
        '10n':[
                    'chancerain.svg'
                    ],
        '11d':[
                    'tstorms.svg'
                    ],
        '11n':[
                    'tstorms.svg'
                    ],
        '13d':[
                    'sleet.svg'
                    ],
        '13n':[
                    'snow.svg'
                    ],
        '50d':[
                    'fog.svg'
                    ],
        '50n':[
                    'fog.svg'
                    ],

    }
