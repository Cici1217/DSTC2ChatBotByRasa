import os
import json
import re
import sys


# 在rasa/data/file中，遍历全部的label（用户说的话）
def findLabelFile(base):
    for root, ds, fs in os.walk(base):
        for f in fs:
            fullname = os.path.join(root, f)
            if fullname.__contains__("label"):
                yield fullname


# 在rasa/data/file中，遍历全部的log（model回复的话）
def findLogFile(base):
    for root, ds, fs in os.walk(base):
        for f in fs:
            fullname = os.path.join(root, f)
            if fullname.__contains__("log"):
                yield fullname


# 本方法是错误的，按照byconstraints这种进行分类，分五个，没有意义
def method0_print_intents():
    method_transcriptions_map = {}
    base = 'rasa/data/file'

    for i in findLabelFile(base):
        all_the_text = open(i).read()
        jess_dict = json.loads(all_the_text)
        for turn in jess_dict["turns"]:
            method_label = turn.get("method-label", "")
            transcription = turn.get("transcription", "")
            if method_label:  # 确保method_label不为空
                if method_label not in method_transcriptions_map:
                    method_transcriptions_map[method_label] = []  # 如果字典中没有这个key，则添加一个空列表作为初始值
                method_transcriptions_map[method_label].append(transcription)  # 向列表中添加transcription
                # print(method_label)
                # print(transcription)
    print(len(method_transcriptions_map))
    for intent, examples in method_transcriptions_map.items():
        print(f"- intent: {intent}")
        print("  examples: |")
        for example in examples:
            print(f"    - {example}")


# domain.yml中的slots，也就是entity具体的信息
def method1_print_slots():
    informable = {
        "food": [
            "afghan",
            "african",
            "afternoon tea",
            "asian oriental",
            "australasian",
            "australian",
            "austrian",
            "barbeque",
            "basque",
            "belgian",
            "bistro",
            "brazilian",
            "british",
            "canapes",
            "cantonese",
            "caribbean",
            "catalan",
            "chinese",
            "christmas",
            "corsica",
            "creative",
            "crossover",
            "cuban",
            "danish",
            "eastern european",
            "english",
            "eritrean",
            "european",
            "french",
            "fusion",
            "gastropub",
            "german",
            "greek",
            "halal",
            "hungarian",
            "indian",
            "indonesian",
            "international",
            "irish",
            "italian",
            "jamaican",
            "japanese",
            "korean",
            "kosher",
            "latin american",
            "lebanese",
            "light bites",
            "malaysian",
            "mediterranean",
            "mexican",
            "middle eastern",
            "modern american",
            "modern eclectic",
            "modern european",
            "modern global",
            "molecular gastronomy",
            "moroccan",
            "new zealand",
            "north african",
            "north american",
            "north indian",
            "northern european",
            "panasian",
            "persian",
            "polish",
            "polynesian",
            "portuguese",
            "romanian",
            "russian",
            "scandinavian",
            "scottish",
            "seafood",
            "singaporean",
            "south african",
            "south indian",
            "spanish",
            "sri lankan",
            "steakhouse",
            "swedish",
            "swiss",
            "thai",
            "the americas",
            "traditional",
            "turkish",
            "tuscan",
            "unusual",
            "vegetarian",
            "venetian",
            "vietnamese",
            "welsh",
            "world"
        ],
        "pricerange": [
            "cheap",
            "moderate",
            "expensive"
        ],
        "name": [
            "ali baba",
            "anatolia",
            "ask",
            "backstreet bistro",
            "bangkok city",
            "bedouin",
            "bloomsbury restaurant",
            "caffe uno",
            "cambridge lodge restaurant",
            "charlie chan",
            "chiquito restaurant bar",
            "city stop restaurant",
            "clowns cafe",
            "cocum",
            "cote",
            "cotto",
            "curry garden",
            "curry king",
            "curry prince",
            "curry queen",
            "da vinci pizzeria",
            "da vince pizzeria",
            "darrys cookhouse and wine shop",
            "de luca cucina and bar",
            "dojo noodle bar",
            "don pasquale pizzeria",
            "efes restaurant",
            "eraina",
            "fitzbillies restaurant",
            "frankie and bennys",
            "galleria",
            "golden house",
            "golden wok",
            "gourmet burger kitchen",
            "graffiti",
            "grafton hotel restaurant",
            "hakka",
            "hk fusion",
            "hotel du vin and bistro",
            "india house",
            "j restaurant",
            "jinling noodle bar",
            "kohinoor",
            "kymmoy",
            "la margherita",
            "la mimosa",
            "la raza",
            "la tasca",
            "lan hong house",
            "little seoul",
            "loch fyne",
            "mahal of cambridge",
            "maharajah tandoori restaurant",
            "meghna",
            "meze bar restaurant",
            "michaelhouse cafe",
            "midsummer house restaurant",
            "nandos",
            "nandos city centre",
            "panahar",
            "peking restaurant",
            "pipasha restaurant",
            "pizza express",
            "pizza express fen ditton",
            "pizza hut",
            "pizza hut city centre",
            "pizza hut cherry hinton",
            "pizza hut fen ditton",
            "prezzo",
            "rajmahal",
            "restaurant alimentum",
            "restaurant one seven",
            "restaurant two two",
            "rice boat",
            "rice house",
            "riverside brasserie",
            "royal spice",
            "royal standard",
            "saffron brasserie",
            "saigon city",
            "saint johns chop house",
            "sala thong",
            "sesame restaurant and bar",
            "shanghai family restaurant",
            "shiraz restaurant",
            "sitar tandoori",
            "stazione restaurant and coffee bar",
            "taj tandoori",
            "tandoori palace",
            "tang chinese",
            "thanh binh",
            "the cambridge chop house",
            "the copper kettle",
            "the cow pizza kitchen and bar",
            "the gandhi",
            "the gardenia",
            "the golden curry",
            "the good luck chinese food takeaway",
            "the hotpot",
            "the lucky star",
            "the missing sock",
            "the nirala",
            "the oak bistro",
            "the river bar steakhouse and grill",
            "the slug and lettuce",
            "the varsity restaurant",
            "travellers rest",
            "ugly duckling",
            "venue",
            "wagamama",
            "yippee noodle bar",
            "yu garden",
            "zizzi cambridge"
        ],
        "area": [
            "centre",
            "north",
            "west",
            "south",
            "east"
        ]
    }
    domain_yaml_str = "slots:\n"
    for slot, values in informable.items():
        domain_yaml_str += f"  {slot}:\n    type: categorical\n    values:\n"
        for value in values:
            domain_yaml_str += f"      - {value}\n"
    print(domain_yaml_str)
    return domain_yaml_str


# 打印所有label（用户说的话）的意图和具体意图
def method2_user_classify():
    base = 'rasa/data/file'

    for i in findLabelFile(base):
        all_the_text = open(i).read()
        jess_dict = json.loads(all_the_text)
        for turn in jess_dict["turns"]:
            method_label = turn.get("semantics", "").get("cam")
            print(method_label)
            # if method_label == 'null()':
                # print(method_label)
            print("      - "+turn.get("transcription"))
    return


# 打根据用户的意图进行分类，并把对应的slot进行标注。用作nlu.yml
def method3_printIntents():
    base = 'rasa/data/file'
    labels = []
    logs = []
    for i in findLabelFile(base):
        labels.append(i)
    for i in findLogFile(base):
        logs.append(i)
    dictIntent = {'inform': [], 'request': [], 'thankyou': [], 'repeat': [], 'reqalts': [], 'affirm': [],
                  'negate': [],
                  'hello': [], 'bye': [], 'restart': [], 'confirm': [], 'ack': [], 'deny': [], 'null()': []}
    intent_matches = dictIntent.keys()
    # print(intent_matches)

    for i in range(0, len(labels)):
        labelText = open(labels[i]).read()
        labelText = json.loads(labelText)

        for turn in labelText["turns"]:
            userWord = turn.get("transcription", "")
            meanOfUser = turn.get("semantics", "").get("cam")

            # print(userWord)
            # print(meanOfUser)
            judge = False
            for intent in intent_matches:
                if intent in meanOfUser or meanOfUser == 'reqmore()':
                    judge = True
                    if meanOfUser == 'reqmore()':
                        intent = 'reqalts'
                    # 如果意图在我们的意图字典中，使用之前的正则表达式处理方法来格式化 userWord
                    pattern = re.compile(r'(\w+)=(\w+)')
                    matches = pattern.findall(meanOfUser)

                    attributes = {key: value for key, value in matches}
                    words = userWord.split()
                    formatted_words = []

                    for word in words:
                        key = next((k for k, v in attributes.items() if v == word), None)
                        if key:
                            formatted_words.append(f"[{word}]({key})")
                        else:
                            formatted_words.append(word)

                    formatted_userWord = ' '.join(formatted_words)
                    # print(formatted_userWord)

                    # 将格式化后的句子添加到意图对应的列表中
                    dictIntent[intent].append(formatted_userWord)
                    break
            if not judge:
                print(meanOfUser)

    print("nlu:")
    for key in dictIntent.keys():
        print("- intent: " + key)
        print("  examples: |")
        temp = dictIntent[key]
        for e in temp:
            print("    - " + e)


action = [
    "Hello , welcome to the Cambridge restaurant system? You can ask for restaurants by area , price range or food type . How may I help you?",
    "What kind of food would you like?",
    "What part of town do you have in mind?",
    "Would you like something in the cheap , moderate , or expensive price range?",
    "You are looking for a restaurant serving any kind of food right?",
    "You are looking for a {food} restaurant right?",
    "Ok , a restaurant in any part of town is that right?",
    "Did you say you are looking for a restaurant in the {area} of town?",
    "Let me confirm , You are looking for a restaurant and you dont care about the price range right?",
    "Let me confirm , You are looking for a restaurant in the {pricerange} price range right?",
    "{name} is in the {pricerange} price range",
    "Sure , {name} is on {addr}",
    "The phone number of {name} is {phone} .",
    "{name} serves {food} food",
    "{name} is a nice place in the {area} of town",
    "The post code of {name} is {postcode}",
    "Sorry would you like {food} or {food} food?",
    "Sorry would you like the {area} of town or you dont care",
    "Sorry would you like something in the {area} or in the {area}",
    "Sorry would you like something in the {pricerange} price range or you dont care",
    "Sorry would you like something in the {pricerange} price range or in the {pricerange} price range",
    "I am sorry but there is no other {food} restaurant that matches your request",
    "I am sorry but there is no other {food} restaurant in the {area} of town",
    "I am sorry but there is no other {food} restaurant in the {pricerange} price range",
    "Sorry but there is no other restaurant in the {pricerange} price range and the {area} of town",
    "{name} is a nice place in the {area} of town serving tasty {food} food",
    "{name} serves {food} food in the {pricerange} price range",
    "{name} is on {addr} and serves tasty {food} food",
    "The phone number of {name} is {phone} and it is on {addr} .",
    "The phone number of {name} is {phone} and its postcode is {postcode} .",
    "The phone number of {name} is {phone} and it is in the {pricerange} price range .",
    "{name} is a nice place in the {area} of town and the prices are {pricerange}",
    "{name} is on {addr} , {postcode}",
    "The phone number of {name} is {phone} and its postcode is {postcode} .",
    "Sorry but there is no other restaurant in the {pricerange} price range and the {area} of town",
    "I am sorry but there is no other {food} restaurant that matches your request",
    "I am sorry but there is no other {food} restaurant in the {pricerange} price range",
    "{name} is a great restaurant serving {pricerange} {food} food in the {area} of town .",
    "The phone number of {name} is {phone} and its postcode is {postcode}, locating at {addr} .",
    "{name} is on {addr} . Its phone number is {phone} , and it is in the {pricerange} pricerange .",
    "{name} is a great restaurant",
    "I'm sorry but there is no restaurant serving {food} food",
    "I'm sorry but there is no japanese restaurant in the {area} of town",
    "I'm sorry but there is no restaurant serving {pricerange} {food} food",
    "Sorry I am a bit confused ; please tell me again what you are looking for .",
    "Can I help you with anything else?",
    "Sorry but there is no other {food} restaurant in the {pricerange} price range and the {area} of town",
    "You are looking for a restaurant is that right?"
]


# 打印所有log（model response）的意图和具体意图
def method4_model_classify():
    judge = -1
    base = 'rasa/data/file'
    y = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    z = {'welcomemsg': [], 'request': [], 'expl-conf': [], 'offer': [], 'inform': [], 'canthelp': [], 'select': [],
         'canthelp.exception': [], 'repeat': [], 'reqmore': []}

    for i in findLogFile(base):
        all_the_text = open(i).read()
        jess_dict = json.loads(all_the_text)

        for turn in jess_dict["turns"]:
            method_len = len(turn.get("output", "").get("dialog-acts"))
            method_label = turn.get("output", "").get("dialog-acts")
            transcription = turn.get("output", "").get("transcript")
            label = method_label[0].get("act")

            judge = -1

            if method_len == 1:
                if (label == "welcomemsg"):
                    judge = 0
                elif (label == "request"):
                    slot = method_label[0].get("slots")[0][1]
                    # print(slot)
                    if slot == "food":
                        judge = 1
                        print(transcription)
                    else:
                        if slot == "area":
                            judge = 2
                        else:
                            if slot == "pricerange":
                                judge = 3
                            else:
                                print("there is error: no conclude situation")
                elif label == "expl-conf":
                    slot = method_label[0].get("slots")[0][0]
                    real_type = method_label[0].get("slots")[0][1]
                    if slot == "food":
                        if real_type == "dontcare":
                            judge = 4
                        else:
                            add = "entities:\n- food: " + real_type
                            judge = 5
                    elif slot == "area":
                        real_type = method_label[0].get("slots")[0][1]
                        # print(slot)
                        # print(real_type)
                        # print(transcription)
                        if real_type == "dontcare":
                            judge = 6
                        else:
                            judge = 7
                            add = "entities:\n- area: " + real_type
                            # print(add)
                    elif slot == "pricerange":
                        real_type = method_label[0].get("slots")[0][1]
                        if real_type == "dontcare":
                            judge = 8
                        else:
                            judge = 9
                            add = "entities:\n- pricerange: " + real_type

                elif label == 'offer':
                    judge = 40
                    slots = method_label[0].get("slots")[0]
                    type = slots[0]
                    name = slots[1]
                    add = "entities:\n- name: " + name
                    # print(add)
                    # print(transcription)
                elif label == 'canthelp':
                    slots = method_label[0].get("slots")[0]
                    type = slots[0]
                    name = slots[1]
                    if type == 'food':
                        judge = 41
                        add = "entities:\n- food: " + name
                        # print(add)
                        # print(transcription)
                    elif type == 'area':
                        judge = 42
                        add = "entities:\n- area: " + name
                        # print(add)
                        # print(transcription)
                    elif type == 'pricerange':
                        judge = 43
                        name2 = method_label[0].get("slots")[1][1]
                        add = "entities:\n- pricerange: " + name + "\n- food: " + name2
                        # print(method_label)
                        # print(add)
                        # print(transcription)
                    else:
                        print("errorerror")
                elif label == 'repeat':
                    judge = 44
                elif label == 'reqmore':
                    judge = 45
                else:
                    print("errorerrorerror")
            elif method_len == 2:
                act0 = method_label[0]['act']
                act1 = method_label[1]['act']
                slots0 = method_label[0]['slots']
                # 0:name的value
                slots1 = method_label[1]['slots']
                # print(act0)
                # print(act1)
                # print()
                if act0 == 'offer' and act1 == 'inform':
                    if slots1[0][0] == 'pricerange':
                        judge = 10
                        add = "entities:\n- name: " + slots0[0][1] + "\n- pricerange: " + slots1[0][1]
                        # print(add)
                        # print(transcription)
                    else:
                        if slots1[0][0] == 'addr':
                            judge = 11
                            add = "entities:\n- name: " + slots0[0][1] + "\n- addr: " + slots1[0][1]
                            # print(add)
                            # print(transcription)
                        else:
                            if slots1[0][0] == 'phone':
                                judge = 12
                                add = "entities:\n- name: " + slots0[0][1] + "\n- phone: " + slots1[0][1]
                                # print(add)
                                # print(transcription)
                            elif slots1[0][0] == 'food':
                                judge = 13
                                add = "entities:\n- name: " + slots0[0][1] + "\n- food: " + slots1[0][1]
                                # print(transcription)
                                # print(add)
                            elif slots1[0][0] == 'area':
                                judge = 14
                                add = "entities:\n- name: " + slots0[0][1] + "\n- area: " + slots1[0][1]
                                # print(transcription)
                                # print(add)
                            elif slots1[0][0] == 'postcode':
                                judge = 15
                                add = "entities:\n- name: " + slots0[0][1] + "\n- postcode: " + \
                                      slots1[0][1]
                                # print(transcription)
                                # print(add)
                            else:
                                print("there is error: no conclude situation")
                elif act0 == "select" and act1 == "select":
                    type0 = slots0[0][0]
                    type1 = slots1[0][0]
                    thing0 = slots0[0][1]
                    thing1 = slots1[0][1]
                    # print(type0)
                    # print(type1)
                    # print(thing0)
                    # print(thing1)
                    if type0 == "food" and type1 == "food":
                        judge = 16
                        add = "entities:\n- food: " + thing0 + "\n- food: " + thing1
                    elif type0 == "area" and type1 == "area":
                        if thing0 == 'dontcare' or thing1 == 'dontcare':
                            judge = 17
                            temp = ""
                            if thing0 == 'dontcare':
                                temp = thing1
                            else:
                                temp = thing0
                            add = "entities:\n- area: " + temp
                            # print(transcription)
                            # print(add)
                        else:
                            judge = 18
                            add = "entities:\n- area: " + thing0 + "\n- area: " + thing1
                            # print(transcription)
                            # print(add)
                    elif type0 == "pricerange" and type1 == "pricerange":
                        if thing0 == 'dontcare' or thing1 == 'dontcare':
                            judge = 19
                            temp = ""
                            if thing0 == 'dontcare':
                                temp = thing1
                            else:
                                temp = thing0
                            add = "entities:\n- pricerange: " + temp
                            # print(transcription)
                            # print(add)
                        else:
                            judge = 20
                            add = "entities:\n- pricerange: " + thing0 + "\n- pricerange: " + thing1
                            # print(transcription)
                            # print(add)
                    else:
                        print("there is error: no conclude situation")
                elif act0 == "canthelp" and act1 == "canthelp.exception":
                    lens = len(slots0)
                    if lens == 1:
                        judge = 21
                        add = "entities:\n- food: " + slots0[0][1]
                        # print(add)
                        # print(transcription)
                    elif lens == 2:
                        if slots0[0][0] == 'area' and slots0[1][0] == 'food' or slots0[1][
                            0] == 'area' and slots0[0][0] == 'food':
                            judge = 22
                            if slots0[0][0] == 'area':
                                a = slots0[0][1]
                                f = slots0[1][1]
                            else:
                                f = slots0[0][1]
                                a = slots0[1][1]
                            add = "entities:\n- food: " + f + "\n- area: " + a
                            # print(add)
                            # print(transcription)
                        elif slots0[0][0] == 'food' and slots0[1][0] == 'pricerange':
                            judge = 23
                            add = "entities:\n- food: " + slots0[0][1] + "\n- pricerange: " + \
                                  slots0[1][1]
                            # print(add)
                            # print(transcription)
                        else:
                            judge = 24
                            add = "entities:\n- pricerange: " + slots0[0][1] + "\n- area: " + \
                                  slots0[1][1]
                            # print(add)
                            # print(transcription)

                    else:
                        judge = 46
                        food = method_label[0].get("slots")[0][1]
                        if method_label[0].get("slots")[1][0] == 'area':
                            area = method_label[0].get("slots")[1][1]
                            pricerange = method_label[0].get("slots")[2][1]
                        else:
                            pricerange = method_label[0].get("slots")[1][1]
                            area = method_label[0].get("slots")[2][1]
                        add = "entities:\n- food: " + food + "\n- pricerange: " + pricerange + "\n- area: " + area

                        # print(add)
                        # print(transcription)

                else:
                    print("there is error: no conclude situation")

                # print()
                # else:
            elif method_len == 3:
                act0 = method_label[0]['act']
                act1 = method_label[1]['act']
                act2 = method_label[2]['act']
                # print(act0)
                # print(act1)
                # print(act2)
                if act0 == "offer" and act1 == "inform" and act2 == "inform":
                    name0 = method_label[0].get("slots")[0][1]
                    # print(name0)
                    type1 = method_label[1].get("slots")[0][0]
                    name1 = method_label[1].get("slots")[0][1]
                    # print(type1)
                    # print(name1)
                    type2 = method_label[2].get("slots")[0][0]
                    name2 = method_label[2].get("slots")[0][1]
                    # print(type2)
                    # print(name2)
                    # print(transcription)
                    if type1 == 'food':
                        if type2 == 'area':
                            judge = 25
                            add = "entities:\n- name: " + name0 + "\n- area: " + name2 + "\n- food: " + name1
                            # print(add)
                            # print(transcription)
                        elif type2 == 'pricerange':
                            judge = 26
                            add = "entities:\n- name: " + name0 + "\n- food: " + name1 + "\n- pricerange: " + name2
                            # print(add)
                            # print(transcription)
                        elif type2 == 'addr':
                            judge = 27
                            add = "entities:\n- name: " + name0 + "\n- addr: " + name2 + "\n- food: " + name1
                            # print(add)
                            # print(transcription)
                        else:
                            print("error")
                    elif type1 == 'phone':
                        if type2 == 'addr':
                            judge = 28
                            add = "entities:\n- name: " + name0 + "\n- phone: " + name1 + "\n- addr: " + name2
                            # print(add)
                            # print(transcription)
                        elif type2 == 'postcode':
                            judge = 29
                            add = "entities:\n- name: " + name0 + "\n- phone: " + name1 + "\n- postcode: " + name2
                            # print(add)
                            # print(transcription)
                        elif type2 == 'pricerange':
                            judge = 30
                            add = "entities:\n- name: " + name0 + "\n- phone: " + name1 + "\n- pricerange: " + name2
                            # print(add)
                            # print(transcription)
                        else:
                            print("error")
                    elif type1 == 'pricerange':
                        judge = 31
                        add = "entities:\n- name: " + name0 + "\n- area: " + name2 + "\n- pricerange: " + name1
                        # print(add)
                        # print(transcription)
                        # print(type2=='area')
                    elif type1 == 'addr':
                        judge = 32
                        add = "entities:\n- name: " + name0 + "\n- addr: " + name1 + "\n- postcode: " + name2
                        # print(add)
                        # print(transcription)
                        # print(type2=='postcode')
                    elif type1 == 'postcode':
                        judge = 33
                        add = "entities:\n- name: " + name0 + "\n- phone: " + name2 + "\n- postcode: " + name1
                        # print(add)
                        # print(transcription)
                        # print(type2=='phone')

                    else:
                        print("error")
                else:
                    if len(method_label[0].get("slots")) == 2:
                        judge = 34
                        x1 = method_label[0].get("slots")[0][0]
                        x2 = method_label[0].get("slots")[1][0]
                        if x1 == 'area':
                            a = method_label[0].get("slots")[0][1]
                            p = method_label[0].get("slots")[1][1]
                        else:
                            p = method_label[0].get("slots")[0][1]
                            a = method_label[0].get("slots")[1][1]
                        add = "entities:\n- pricerange: " + p + "\n- area: " + a
                    else:
                        # print(method_label[0].get("slots"))
                        judge = 35
                        add = "entities:\n- food: " + method_label[0].get("slots")[0][1]
                        # print(add)
                        # print(transcription)
                        # print(add)
                        # print(transcription)
            elif method_len == 4:
                act0 = method_label[0]['act']
                act1 = method_label[1]['act']
                act2 = method_label[2]['act']
                act3 = method_label[3]['act']
                slots0 = method_label[0]['slots']
                slots1 = method_label[1]['slots']
                slots2 = method_label[2]['slots']
                slots3 = method_label[3]['slots']

                type0 = slots0[0][0]
                # all name
                name0 = slots0[0][1]
                type1 = slots1[0][0]
                name1 = slots1[0][1]
                type2 = slots2[0][0]
                name2 = slots2[0][1]
                type3 = slots3[0][0]
                name3 = slots3[0][1]
                # print(slots1)
                # print(slots2)
                # print(slots3)
                # print()
                if act0 == 'offer' and act1 == 'inform' and act2 == 'inform' and act3 == 'inform':
                    if type1 == 'food':
                        judge = 37
                        # type2 all pricerange
                        # type3 all area
                        add = "entities:\n- name: " + name0 + "\n- pricerange: " + name2 + "\n- food: " + name1 + "\n- area: " + name3
                        # print(add)
                        # print(transcription)
                    elif type1 == 'addr':
                        judge = 38
                        # print(type2)#all phone
                        # print(type3)#all postcode
                        add = "entities:\n- name: " + name0 + "\n- phone: " + name2 + "\n- postcode: " + name3 + "\n- addr: " + name1
                        # print(add)
                        # print(transcription)
                    elif type1 == 'phone':
                        if type2 == 'pricerange':
                            # print(type3)#addr
                            judge = 39
                            add = "entities:\n- name: " + name0 + "\n- addr: " + name3 + "\n- phone: " + name1 + "\n- pricerange: " + name2
                            # print(add)
                            # print(transcription)
                        elif type2 == 'addr':
                            # print(type3)#postcode
                            judge = 38
                            add = "entities:\n- name: " + name0 + "\n- phone: " + name1 + "\n- postcode: " + name3 + "\n- addr: " + name2
                            # print(add)
                            # print(transcription)
                        else:
                            print("error")
                    else:
                        print("error")
                else:
                    judge = 35
                    add = "entities:\n- food: " + method_label[0]['slots'][0][1]
                    # print(add)
                    # # print(transcription)
                    # print(transcription)
            else:
                judge = 36
                # print(method_label[0]['act'])
                # print(method_label[0]['slots'])
                # print(method_label[1]['act'])
                # print(method_label[2]['act'])
                # print(method_label[3]['act'])
                # print(method_label[4]['act'])
                add = "entities:\n- food: " + method_label[0]['slots'][0][1] + "\n- pricerange: " + \
                      method_label[0]['slots'][1][1]
                # print(add)
                # print(transcription)
                # print()

            # print(transcription)
            # if real_type == "indonesian":
            #     print(transcription)

            # else:
            #     if slot == "area":
            #         print()
            #     else:
            #         if slot == "pricerange":
            #             print()
            #         else:
            #             print("there is error: no conclude situation")

            # print(judge)
            if judge==-1:
                print(method_label)

            # print(transcription)
            # print()

    return


def readInTurn():
    error_time = 0
    y = {'welcomemsg': 0, 'request': 0, 'expl-conf': 0, 'offer': 0, 'inform': 0, 'canthelp': 0, 'select': 0,
         'canthelp.exception': 0, 'repeat': 0, 'reqmore': 0}
    # 模型回答意图
    z = {'inform': 0, 'request': 0, 'thankyou': 0, 'repeat': 0, 'reqalts': 0, 'affirm': 0, 'negate': 0, 'hello': 0,
         'bye': 0, 'restart': 0, 'confirm': 0, 'ack': 0, 'deny': 0}
    # 用户的意图
    base = 'rasa/data/file'
    labels = []
    logs = []
    list_error = dict()
    for i in findLabelFile(base):
        labels.append(i)
    for i in findLogFile(base):
        logs.append(i)

    for i in range(0, len(labels)):
        # print("labels:" + labels[i])
        # print("logs:" + logs[i])
        labelText = open(labels[i]).read()
        labelText = json.loads(labelText)
        logText = open(logs[i]).read()
        logText = json.loads(logText)

        userList = []
        answerList = []
        for turn in labelText["turns"]:
            userWord = turn.get("transcription", "")
            # userWord = "user says:" + userWord
            userList.append(userWord)
            meanOfUser = turn.get("semantics", "").get("cam")

            try:
                z[turn.get("semantics", {}).get("json", [])[0].get("act")] = z[turn.get("semantics", {}).get("json",
                                                                                                             [])[0].get(
                    "act")] + 1
            except IndexError:
                list_error[meanOfUser] = 0
                error_time += 1

            if 'inform' in meanOfUser:
                # 使用正则表达式找到所有的键值对
                pattern = re.compile(r'(\w+)=(\w+)')
                matches = pattern.findall(meanOfUser)

                # 创建一个字典来存储键值对，方便查找
                attributes = {key: value for key, value in matches}

                # 对 userWord 进行分词处理
                words = userWord.split()

                # 对每个词进行检查和替换
                formatted_words = []
                for word in words:
                    # 找到当前词对应的 key
                    key = next((k for k, v in attributes.items() if v == word), None)
                    if key:
                        # 如果找到了对应的 key，按照指定格式替换
                        formatted_words.append(f"[{word}]({key})")
                    else:
                        # 如果没有找到，保持原样
                        formatted_words.append(word)

                # 将处理后的词重新组合成字符串
                formatted_userWord = ' '.join(formatted_words)
                # print(formatted_userWord)
                # print(meanOfUser)
                # print(userWord)
                # print(meanOfUser)
                # print()

            meanOfUser = "user means:" + meanOfUser
            userList.append(meanOfUser)
        for turn in logText["turns"]:
            method_label = turn.get("output", "").get("transcript")
            method_label = "model says:" + method_label
            answerList.append(method_label)

            dialog_act = turn.get("output", "").get("dialog-acts")
            for x in dialog_act:
                y[x.get("act")] = y[x.get("act")] + 1
            answerList.append(dialog_act)

        while len(userList) != 0:
            print(answerList.pop(0))
            print(answerList.pop(0))
            print(userList.pop(0))
            print(userList.pop(0))

        print('________________________________________')
    print(y)
    print(z)
    print(list_error)
    print(error_time)


def pingpang():
    file = open("story.txt", "w")
    sys.stdout = file

    # print("stories:")
    intents = ['inform', 'request', 'thankyou', 'repeat', 'reqalts', 'affirm', 'negate', 'hello', 'bye', 'restart',
               'confirm', 'ack', 'deny']
    # 用户的意图
    base = 'rasa/data/file'
    labels = []
    logs = []
    for i in findLabelFile(base):
        labels.append(i)
    for i in findLogFile(base):
        logs.append(i)

    print("stories:")
    for i in range(0, len(labels)):
        # print('________________________________________')
        print('- story: story_'+str(i))
        print('  steps:')
        labelText = open(labels[i]).read()
        labelText = json.loads(labelText)
        logText = open(logs[i]).read()
        logText = json.loads(logText)

        userList = []
        answerList = []
        for turn in labelText["turns"]:
            meanOfUser = turn.get("semantics", "").get("cam")
            # userList.append("  - intent: ")

            for here in intents:
                if here in meanOfUser or meanOfUser == 'reqmore()':
                    meanOfUser = here
                    if meanOfUser == 'reqmore()':
                        meanOfUser = 'reqalts'
                    break
            userList.append("  - intent: "+meanOfUser)
        for turn in logText["turns"]:
            method_len = len(turn.get("output", "").get("dialog-acts"))
            method_label = turn.get("output", "").get("dialog-acts")
            transcription = turn.get("output", "").get("transcript")
            label = method_label[0].get("act")
            # trans = "model says: " + transcription
            # answerList.append(trans)
            judge = -1
            add = ""
            if method_len == 1:
                if (label == "welcomemsg"):
                    judge = 0
                elif (label == "request"):
                    slot = method_label[0].get("slots")[0][1]
                    # print(slot)
                    if slot == "food":
                        judge = 1
                    else:
                        if slot == "area":
                            judge = 2
                        else:
                            if slot == "pricerange":
                                judge = 3
                            # else:
                            #     print("error0")
                elif label == "expl-conf":
                    slot = method_label[0].get("slots")[0][0]
                    real_type = method_label[0].get("slots")[0][1]
                    if slot == "food":
                        if real_type == "dontcare":
                            judge = 4
                        else:
                            add = "entities:\n- food: " + real_type
                            judge = 5
                    elif slot == "area":
                        real_type = method_label[0].get("slots")[0][1]
                        # print(slot)
                        # print(real_type)
                        # print(transcription)
                        if real_type == "dontcare":
                            judge = 6
                        else:
                            judge = 7
                            add = "entities:\n- area: " + real_type
                            # print(add)
                    elif slot == "pricerange":
                        real_type = method_label[0].get("slots")[0][1]
                        if real_type == "dontcare":
                            judge = 8
                        else:
                            judge = 9
                            add = "entities:\n- pricerange: " + real_type

                elif label == 'offer':
                    judge = 40
                    slots = method_label[0].get("slots")[0]
                    type = slots[0]
                    name = slots[1]
                    add = "entities:\n- name: " + name
                    # print(add)
                    # print(transcription)
                elif label == 'canthelp':
                    slots = method_label[0].get("slots")[0]
                    type = slots[0]
                    name = slots[1]
                    if type == 'food':
                        judge = 41
                        add = "entities:\n- food: " + name
                        # print(add)
                        # print(transcription)
                    elif type == 'area':
                        judge = 42
                        add = "entities:\n- area: " + name
                        # print(add)
                        # print(transcription)
                    elif type == 'pricerange':
                        judge = 43
                        name2 = method_label[0].get("slots")[1][1]
                        add = "entities:\n- pricerange: " + name + "\n- food: " + name2
                        # print(method_label)
                        # print(add)
                        # print(transcription)
                    # else:
                    #     print("error1")
                elif label == 'repeat':
                    judge = 44
                elif label == 'reqmore':
                    judge = 45
                elif label == 'confirm-domain':
                    judge = 47
                # else:
                #     print("error2")
            elif method_len == 2:
                act0 = method_label[0]['act']
                act1 = method_label[1]['act']
                slots0 = method_label[0]['slots']
                # 0:name的value
                slots1 = method_label[1]['slots']
                # print(act0)
                # print(act1)
                # print()
                if act0 == 'offer' and act1 == 'inform':
                    if slots1[0][0] == 'pricerange':
                        judge = 10
                        add = "entities:\n- name: " + slots0[0][1] + "\n- pricerange: " + slots1[0][1]
                        # print(add)
                        # print(transcription)
                    else:
                        if slots1[0][0] == 'addr':
                            judge = 11
                            add = "entities:\n- name: " + slots0[0][1] + "\n- addr: " + slots1[0][1]
                            # print(add)
                            # print(transcription)
                        else:
                            if slots1[0][0] == 'phone':
                                judge = 12
                                add = "entities:\n- name: " + slots0[0][1] + "\n- phone: " + slots1[0][1]
                                # print(add)
                                # print(transcription)
                            elif slots1[0][0] == 'food':
                                judge = 13
                                add = "entities:\n- name: " + slots0[0][1] + "\n- food: " + slots1[0][1]
                                # print(transcription)
                                # print(add)
                            elif slots1[0][0] == 'area':
                                judge = 14
                                add = "entities:\n- name: " + slots0[0][1] + "\n- area: " + slots1[0][1]
                                # print(transcription)
                                # print(add)
                            elif slots1[0][0] == 'postcode':
                                judge = 15
                                add = "entities:\n- name: " + slots0[0][1] + "\n- postcode: " + \
                                      slots1[0][1]
                                # print(transcription)
                                # print(add)
                            # else:
                            #     print("error3")
                elif act0 == "select" and act1 == "select":
                    type0 = slots0[0][0]
                    type1 = slots1[0][0]
                    thing0 = slots0[0][1]
                    thing1 = slots1[0][1]
                    # print(type0)
                    # print(type1)
                    # print(thing0)
                    # print(thing1)
                    if type0 == "food" and type1 == "food":
                        judge = 16
                        add = "entities:\n- food: " + thing0 + "\n- food: " + thing1
                    elif type0 == "area" and type1 == "area":
                        if thing0 == 'dontcare' or thing1 == 'dontcare':
                            judge = 17
                            temp = ""
                            if thing0 == 'dontcare':
                                temp = thing1
                            else:
                                temp = thing0
                            add = "entities:\n- area: " + temp
                            # print(transcription)
                            # print(add)
                        else:
                            judge = 18
                            add = "entities:\n- area: " + thing0 + "\n- area: " + thing1
                            # print(transcription)
                            # print(add)
                    elif type0 == "pricerange" and type1 == "pricerange":
                        if thing0 == 'dontcare' or thing1 == 'dontcare':
                            judge = 19
                            temp = ""
                            if thing0 == 'dontcare':
                                temp = thing1
                            else:
                                temp = thing0
                            add = "entities:\n- pricerange: " + temp
                            # print(transcription)
                            # print(add)
                        else:
                            judge = 20
                            add = "entities:\n- pricerange: " + thing0 + "\n- pricerange: " + thing1
                            # print(transcription)
                            # print(add)
                    # else:
                    #     print("error4")
                elif act0 == "canthelp" and act1 == "canthelp.exception":
                    lens = len(slots0)
                    if lens == 1:
                        judge = 21
                        add = "entities:\n- food: " + slots0[0][1]
                        # print(add)
                        # print(transcription)
                    elif lens == 2:
                        if slots0[0][0] == 'area' and slots0[1][0] == 'food' or slots0[1][
                            0] == 'area' and slots0[0][0] == 'food':
                            judge = 22
                            if slots0[0][0] == 'area':
                                a = slots0[0][1]
                                f = slots0[1][1]
                            else:
                                f = slots0[0][1]
                                a = slots0[1][1]
                            add = "entities:\n- food: " + f + "\n- area: " + a
                            # print(add)
                            # print(transcription)
                        elif slots0[0][0] == 'food' and slots0[1][0] == 'pricerange':
                            judge = 23
                            add = "entities:\n- food: " + slots0[0][1] + "\n- pricerange: " + \
                                  slots0[1][1]
                            # print(add)
                            # print(transcription)
                        else:
                            judge = 24
                            add = "entities:\n- pricerange: " + slots0[0][1] + "\n- area: " + \
                                  slots0[1][1]
                            # print(add)
                            # print(transcription)

                    else:
                        judge = 46
                        food = method_label[0].get("slots")[0][1]
                        if method_label[0].get("slots")[1][0] == 'area':
                            area = method_label[0].get("slots")[1][1]
                            pricerange = method_label[0].get("slots")[2][1]
                        else:
                            pricerange = method_label[0].get("slots")[1][1]
                            area = method_label[0].get("slots")[2][1]
                        add = "entities:\n- food: " + food + "\n- pricerange: " + pricerange + "\n- area: " + area
                        # print(add)
                        # print("trans:"+transcription)
                # else:
                #     print("error5")

                # print()
                # else:
            elif method_len == 3:
                act0 = method_label[0]['act']
                act1 = method_label[1]['act']
                act2 = method_label[2]['act']
                # print(act0)
                # print(act1)
                # print(act2)
                if act0 == "offer" and act1 == "inform" and act2 == "inform":
                    name0 = method_label[0].get("slots")[0][1]
                    # print(name0)
                    type1 = method_label[1].get("slots")[0][0]
                    name1 = method_label[1].get("slots")[0][1]
                    # print(type1)
                    # print(name1)
                    type2 = method_label[2].get("slots")[0][0]
                    name2 = method_label[2].get("slots")[0][1]
                    # print(type2)
                    # print(name2)
                    # print(transcription)
                    if type1 == 'food':
                        if type2 == 'area':
                            judge = 25
                            add = "entities:\n- name: " + name0 + "\n- area: " + name2 + "\n- food: " + name1
                            # print(add)
                            # print(transcription)
                        elif type2 == 'pricerange':
                            judge = 26
                            add = "entities:\n- name: " + name0 + "\n- food: " + name1 + "\n- pricerange: " + name2
                            # print(add)
                            # print(transcription)
                        elif type2 == 'addr':
                            judge = 27
                            add = "entities:\n- name: " + name0 + "\n- addr: " + name2 + "\n- food: " + name1
                            # print(add)
                            # print(transcription)
                        # else:
                        #     print("error6")
                    elif type1 == 'phone':
                        if type2 == 'addr':
                            judge = 28
                            add = "entities:\n- name: " + name0 + "\n- phone: " + name1 + "\n- addr: " + name2
                            # print(add)
                            # print(transcription)
                        elif type2 == 'postcode':
                            judge = 29
                            add = "entities:\n- name: " + name0 + "\n- phone: " + name1 + "\n- postcode: " + name2
                            # print(add)
                            # print(transcription)
                        elif type2 == 'pricerange':
                            judge = 30
                            add = "entities:\n- name: " + name0 + "\n- phone: " + name1 + "\n- pricerange: " + name2
                            # print(add)
                            # print(transcription)
                        # else:
                        #     print("error7")
                    elif type1 == 'pricerange':
                        judge = 31
                        add = "entities:\n- name: " + name0 + "\n- area: " + name2 + "\n- pricerange: " + name1
                        # print(add)
                        # print(transcription)
                        # print(type2=='area')
                    elif type1 == 'addr':
                        judge = 32
                        add = "entities:\n- name: " + name0 + "\n- addr: " + name1 + "\n- postcode: " + name2
                        # print(add)
                        # print(transcription)
                        # print(type2=='postcode')
                    elif type1 == 'postcode':
                        judge = 33
                        add = "entities:\n- name: " + name0 + "\n- phone: " + name2 + "\n- postcode: " + name1
                        # print(add)
                        # print(transcription)
                        # print(type2=='phone')

                    # else:
                    #     print("error8")
                else:
                    if len(method_label[0].get("slots")) == 2:
                        judge = 34
                        x1 = method_label[0].get("slots")[0][0]
                        x2 = method_label[0].get("slots")[1][0]
                        if x1 == 'area':
                            a = method_label[0].get("slots")[0][1]
                            p = method_label[0].get("slots")[1][1]
                        else:
                            p = method_label[0].get("slots")[0][1]
                            a = method_label[0].get("slots")[1][1]
                        add = "entities:\n- pricerange: " + p + "\n- area: " + a
                    else:
                        # print(method_label[0].get("slots"))
                        judge = 35
                        add = "entities:\n- food: " + method_label[0].get("slots")[0][1]
                        # print(add)
                        # print(transcription)
                        # print(add)
                        # print(transcription)
            elif method_len == 4:
                act0 = method_label[0]['act']
                act1 = method_label[1]['act']
                act2 = method_label[2]['act']
                act3 = method_label[3]['act']
                slots0 = method_label[0]['slots']
                slots1 = method_label[1]['slots']
                slots2 = method_label[2]['slots']
                slots3 = method_label[3]['slots']

                type0 = slots0[0][0]
                # all name
                name0 = slots0[0][1]
                type1 = slots1[0][0]
                name1 = slots1[0][1]
                type2 = slots2[0][0]
                name2 = slots2[0][1]
                type3 = slots3[0][0]
                name3 = slots3[0][1]
                # print(slots1)
                # print(slots2)
                # print(slots3)
                # print()
                if act0 == 'offer' and act1 == 'inform' and act2 == 'inform' and act3 == 'inform':
                    if type1 == 'food':
                        judge = 37
                        # type2 all pricerange
                        # type3 all area
                        add = "entities:\n- name: " + name0 + "\n- pricerange: " + name2 + "\n- food: " + name1 + "\n- area: " + name3
                        # print(add)
                        # print(transcription)
                    elif type1 == 'addr':
                        judge = 38
                        # print(type2)#all phone
                        # print(type3)#all postcode
                        add = "entities:\n- name: " + name0 + "\n- phone: " + name2 + "\n- postcode: " + name3 + "\n- addr: " + name1
                        # print(add)
                        # print(transcription)
                    elif type1 == 'phone':
                        if type2 == 'pricerange':
                            # print(type3)#addr
                            judge = 39
                            add = "entities:\n- name: " + name0 + "\n- addr: " + name3 + "\n- phone: " + name1 + "\n- pricerange: " + name2
                            # print(add)
                            # print(transcription)
                        elif type2 == 'addr':
                            # print(type3)#postcode
                            judge = 38
                            add = "entities:\n- name: " + name0 + "\n- phone: " + name1 + "\n- postcode: " + name3 + "\n- addr: " + name2
                            # print(add)
                            # print(transcription)
                        # else:
                        #     print("error9")
                    # else:
                    #     print("error10")
                else:
                    judge = 35
                    add = "entities:\n- food: " + method_label[0]['slots'][0][1]
                    # print(add)
                    # # print(transcription)
                    # print(transcription)
            else:
                judge = 36
                # print(method_label[0]['act'])
                # print(method_label[0]['slots'])
                # print(method_label[1]['act'])
                # print(method_label[2]['act'])
                # print(method_label[3]['act'])
                # print(method_label[4]['act'])
                add = "entities:\n- food: " + method_label[0]['slots'][0][1] + "\n- pricerange: " + \
                      method_label[0]['slots'][1][1]
                # print(add)
                # print(transcription)
                # print()


            modified_add = "\n".join(["    " + line for line in add.split("\n")])
            answerList.append(modified_add)
            t = "  - action: judge"
            t = t + str(judge)
            answerList.append(t)

        while len(userList) != 0:
            print(answerList.pop(0))
            trys = answerList.pop(0)
            if trys!="    ":
                print(trys)
            # print(answerList.pop(0))
            print(userList.pop(0))
    file.close()




def printResponses():
    print("responses:")
    for i in range(0, len(action)):
        print("  judge" + str(i) + ":")
        print("    - text: " + action[i])


def main():
    # printResponses()
    # pingpang()
    # method4_model_classify()

    method3_printIntents()
    # method2_user_classify()


if __name__ == '__main__':
    main()
