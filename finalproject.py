import time
import random

nft = {"Biker": 50, "Cyclist": 100, "Skateboarder": 200, "Surfer": 500, "Grom": 2000, "Snowboarder": 5000, "Rider": 10000}
nft1 = {"Biker1": 100, "Cyclist1": 200, "Skateboarder1": 400, "Surfer1": 1000, "Grom1": 4000, "Snowboarder1": 10000, "Rider1": 20000}
updates2x = ["gold:", "radioctive:", "blood:"]
updates4x = ["emerald:", "diamond:", "chocolate:"]
updates10x = ["rainbow:", "snow:", "steel:"]

def create():
    print("Вы попали на крипто-биржу GearBank")

    name = input("Введите свой никнейм\n > ")

    if len(name) == 0:
        print("Никнейм должен состоять минимум из одного символа!")
        create()

    time.sleep(.5)

    print(f"Создаю дату по вашему никнейму: {name}")

    time.sleep(.5)

    plr_data = {name+"heal": 0, name+"gear": 0, name+"Capital": 10000000000, "Name":name, name+"Nft":[]}
    for i in range(10):
        print("_"* 50)
    return plr_data

def buy_token():
    global data

    prom = 0
    mult_cap = False

    try:
        strt = int(input("Введите ставку\n > "))
    except:
        strt = 0
        print("Error")
        buy_token()

    if strt < 10:
        print("Ставка должна быть 10$ минимум !")
    elif data[data["Name"]+"Capital"] < strt:
        print("В вашем капитале меньше денег чем вы хотите поставить")
    else:

        data[data["Name"]+"Capital"] -= strt
        if coin == "heal":
            rand = strt / 3
            b = 1
        elif coin == "gear":
            b = strt /3
            rand = strt / 1.6
        strt = 0

        for i in range(1,6):

            main_rand = random.randint(0, 50)

            if main_rand <= 49:
                prom += random.randint(round(b), round(rand))
                print(f"Вы получили {prom}$ на {i} ходу")
                strt += prom
                prom = 0
            else:
                print("Джекпот!")
                mult_cap = True

        if mult_cap == True:
            mult_cap = False

            prom_rand = random.randint(2, 4)
            print(f"Вы поднимите свой капитал из за джекпота в {prom_rand} раза")
            strt *= prom_rand

        print(f"Всего вы получили {strt} $")
        data_name = data["Name"]
        data[data_name+coin] += strt

def sell_token():
    global data

    try:
        num = int(input("Сколько вы хотите снять денег?\n> "))
    except:
        num = 0
        print("Error")
        sell_token()

    if data[data["Name"]+coin] < num:
        print(f"У вас нету стольких {coin}Coin")
    else:
        data[data["Name"]+coin] -= num
        data[data["Name"]+"Capital"] += round(num * 0.8)
        print(f"Вы продали {num}$ и получили {round(num * 0.8)}$")

def token():
    global data

    l = list(nft)
    num = 1
    lst = {}

#22

    for i in range(10):
        x = random.randint(1, 22)
        rand_nft = random.choice(l)

        if x <= 13:
            mutation = random.choice(updates2x)
            num = 2
        elif x <20>13:
            mutation = random.choice(updates4x)
            num = 4
        else:
            mutation = random.choice(updates10x)
            num = 10

        cost = round(nft[rand_nft] * num/random.randint(1, 3))
        nd = mutation + rand_nft

        if nd in lst:

            print("Повторка")

            x = random.randint(1, 22)
            rand_nft = random.choice(l)

            if x <= 13:
                mutation = random.choice(updates2x)
                num = 2
            elif x < 20 > 13:
                mutation = random.choice(updates4x)
                num = 4
            else:
                mutation = random.choice(updates10x)
                num = 10

            cost = nft[rand_nft] * num
            nd = mutation + rand_nft

        lst.update({nd: cost})
        if coin == "heal":
            print(f"{nd} - {cost}hc - {i}")
        else:
            print(f"{nd} - {cost*2}hc - {i}")

    chse = input("Введите индекс для покупки эксклюзива \n> ")
    ll = list(lst)
    if coin == "heal":
        if int(chse) > len(ll) or chse.isdigit() == False :
            print("Error")
        elif data[data["Name"]+coin] < lst[ll[int(chse)]]:
            print("нету денег")
        else:
            el_l = ll[int(chse)]
            data[data["Name"]+coin] -= lst[el_l]
            data[data["Name"]+"Nft"].append(ll[int(chse)])
    else:
        if chse.isdigit() == False or not lst[ll[int(chse)]]:
            print("Error")
        elif data[data["Name"]+coin] < lst[ll[int(chse)]]*2:
            print("нету денег")
        else:
            el_l = ll[int(chse)]
            data[data["Name"]+coin] -= lst[el_l]*2
            data[data["Name"]+"Nft"].append(ll[int(chse)])
def credit():
    global data

    while True:

        work = input("Работайте, вводя пустоту, чтобы выйти введите что то другое\t > ")

        if work != "":
            break
        else:
            data[data["Name"]+"Capital"] += 1
            print(data[data["Name"]+"Capital"])

def buy_nft():
    global data
    global nft

    i = ""
    if coin == "heal":
        i = 0
    elif coin == "gear":
        i = 1
    if i == 0:
        chose = input(f"Виды нфт\n{nft}\nЧтобы купить за токены что либо введите имя\n> ")
    else:
        chose = input(f"Виды нфт\n{nft1}\nЧтобы купить за токены что либо введите имя\n> ")
    for key, value in nft.items():

        if chose == key:
            if i == 0:
                if nft[key] > data[data["Name"]+coin]:
                    print("Не достаточно токенов")
                else:
                    data[data["Name"]+"Nft"].append(key)

                    data[data["Name"]+coin] -= nft[key]
                    print(data[data["Name"]+"Nft"], data[data["Name"]+coin])
            else:
                if nft1[key+"1"] > data[data["Name"] + coin]:
                    print("Не достаточно токенов")

                else:
                    data[data["Name"] + "Nft"].append(key)

                    data[data["Name"] + coin] -= nft1[key+"1"]
                    print(data[data["Name"] + "Nft"], data[data["Name"] + coin])

def sell_nft():
    global data

    d = []

    if coin == "heal":
        i = 0
    elif coin == "gear":
        i = 1
    chose = input(f"Виды нфт\n{nft}\nЧтобы продать за токены под процентом 90 что либо введите имя\n> ")

    for m in data[data["Name"]+"Nft"]:
        d.append(m[m.find(":")+1:])

    if chose in d:
        print(f"Нашел {chose}")
        for key in data[data["Name"]+"Nft"]:
            if chose == key[key.find(":")+1:]:
                print(key)
                data[data["Name"]+"Nft"].remove(key)
                mutation = key[:key.find(":")]

                if mutation+":" in updates2x:
                    x = 2
                elif mutation+":" in updates4x:
                    x = 4
                elif mutation+":" in updates10x:
                    x = 10
                else:
                    x = 1

                if i == 0:
                    data[data["Name"]+coin] += (nft[key[key.find(":")+1:]] *  x) * 0.9
                else:
                    data[data["Name"]+coin] += (nft1[key[key.find(":")+1:]] * x) * 0.9

def rules():
    global data

    pnft = data[data["Name"]+"Nft"]
    plnft = input("Введите нфт на которых хотите добавить мутацию или поменять (вводите полностью)\n> ")
    if plnft in data[data["Name"]+"Nft"]:

        i = pnft.index(plnft)

        rand = random.randint(1, 5)

        if rand > 0:
            print("Повезло!")
            print("Выбираю какой x добавить")
            rnd = random.randint(1, 5)
            if rnd == 1:
                print("Выпало 10x !!!")
                ran = random.choice(updates10x)
                pnft[i] = ran + plnft[plnft.find(":") + 1:]
            elif rnd > 1 < 4:
                print("Выпало 4x")
                ran = random.choice(updates4x)
                pnft[i] = ran + plnft[plnft.find(":") + 1:]
            else:
                print("Выпало 2x")
                ran = random.choice(updates2x)
                pnft[i] = ran + plnft[plnft.find(":") + 1:]
        else:
            pnft.remove(plnft)
            print("Не повезло")
    else:
        print("Error")

def upgrade_nft():
    global data

    d = []
    i = 0
    pnft = data[data["Name"]+"Nft"]
    l = list(nft)
    plnft = input("Введи название нфт\n > ")


    for m in data[data["Name"]+"Nft"]:
        d.append(m[m.find(":")+1:])

    for key, value in nft.items():
        i += 1
        if key == plnft and plnft in d:
            rand = random.randint(1, 3)
            mutation = pnft[d.index(plnft)][:pnft[d.index(plnft)].find(":")+1]

            for t in range(1, 4):
                print(t)
                time.sleep(1)
            j = d.index(plnft)
            if rand == 3:
                if not plnft == "Rider":
                    print(i)

                    pnft[j] = mutation+l[i]
                    print("Вы успешно обновили нфт до следующего уровня")
                else:
                    print("Rider Нельзя обновить!")
            else:
                print("Не повезло")
                pnft.remove(mutation+plnft)

def curse():
    global data
    global coin

    print(f"Ваш токен - {coin}")
    toke = "hc"

    if coin == "heal":
        toke = "hc"
        tn = 50
    else:
        toke = "gc"
        tn = 100

    while True:
        tkn = data[data["Name"] + coin]
        capital = data[data["Name"] + "Capital"]
        tok = random.randint(1, tn)
        mon = random.randint(1, 50)

        print(f"{tok}{toke} - {mon}$")

        chs = input("Выберите что вы хотите сделать: К - купить, П - продать, В - выход\n> ").lower()
        if chs == "к":
            if data[data["Name"]+"Capital"] < mon:
                print("Не хватает денег на сделку")
            else:
                data[data["Name"]+"Capital"] -= mon
                data[data["Name"]+coin] += tok
                print(f"Вы купили токены, теперь у вас {tkn}{toke}")
                time.sleep(.2)
        elif chs == "п":
            if data[data["Name"]+coin] < tok:
                print("Не хватает токенов на сделку")
            else:
                data[data["Name"]+"Capital"] += mon
                data[data["Name"]+coin] -= tok
                print(f"Вы продали токены, теперь у вас {capital}$")
                time.sleep(.6)
        elif chs == "в":
            break
def work():
    global data

    rand = random.randint(1, 2)
    time.sleep(1)
    if rand == 1:
        print("Повезло!")
        data[data["Name"]+"Capital"] += 100

    else:
        print("Не повезло")
        
data = create()
coin = "heal"

while True:

    chose = input("1. Купить токен 2. Продать токен 3. Торговля 4. Посмотреть свой ключ 5. Работа 6. Купить нфт\n7. Продать нфт 8. Попробовать добавить мутацию на нфт 9. Обновить нфт  10. Изменить основной токен 11. Посмотреть курс 12. Временная работа 13. Выход\n > ")

    if chose == "1":
        buy_token()
    elif chose == "2":
        sell_token()
    elif chose == "3":
        token()
    elif chose == "4":
        print(data)
    elif chose == "5":
        credit()
    elif chose == "6":
        buy_nft()
    elif chose == "7":
        sell_nft()
    elif chose == "8":
        rules()
    elif chose == "9":
        upgrade_nft()
    elif chose == "10":
        while True:
            coin = input("Введите токен \n > ")
            if not coin == "heal" and not coin == "gear":
                print("Не понял перепиши еще раз")
            else:
                print(f"Ваш текущий токен - {coin}")
                break
    elif chose == "11":
        curse()
    elif chose == "12":
        work()
    elif chose == "13":
        print("Выхожу...")
        time.sleep(0.5)
        break
    else:
        print("Не понял функции")