# actions.py
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionJudge0(Action):
    def name(self) -> Text:
        return "judge0"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            "Hello, welcome to the Cambridge restaurant system? You can ask for restaurants by area, price range or food type. How may I help you?")
        return []


class ActionJudge1(Action):
    def name(self) -> Text:
        return "judge1"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            "What kind of food would you like?")
        return []


class ActionJudge2(Action):
    def name(self) -> Text:
        return "judge2"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            "What part of town do you have in mind?")
        return []


class ActionJudge3(Action):
    def name(self) -> Text:
        return "judge3"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            "Would you like something in the cheap , moderate , or expensive price range?")
        return []


class ActionJudge4(Action):
    def name(self) -> Text:
        return "judge4"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            "You are looking for a restaurant serving any kind of food right?")
        return []


class ActionJudge5(Action):

    def name(self) -> Text:
        return "judge5"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        food = tracker.get_slot('food')
        dispatcher.utter_message(text=f"You are looking for a {food} restaurant right?")

        return []


class ActionJudge6(Action):
    def name(self) -> Text:
        return "judge6"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            "Ok , a restaurant in any part of town is that right?")
        return []


class ActionJudge7(Action):

    def name(self) -> Text:
        return "judge7"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        area = tracker.get_slot('area')
        dispatcher.utter_message(text=f"Did you say you are looking for a restaurant in the {area} area of town?")
        return []


class ActionJudge8(Action):
    def name(self) -> Text:
        return "judge8"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            "Let me confirm , You are looking for a restaurant and you dont care about the price range right?")
        return []


class ActionJudge9(Action):

    def name(self) -> Text:
        return "judge9"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        pricerange = tracker.get_slot('pricerange')
        dispatcher.utter_message(
            text=f"Let me confirm , You are looking for a restaurant in the {pricerange} price range right?")
        return []


class ActionJudge10(Action):
    def name(self) -> Text:
        return "judge10"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot('name')
        pricerange = tracker.get_slot('pricerange')
        dispatcher.utter_message(text=f"{name} is in the {pricerange} price range.")
        return []


class ActionJudge11(Action):
    def name(self) -> Text:
        return "judge11"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot('name')
        addr = tracker.get_slot('addr')
        dispatcher.utter_message(text=f"Sure, {name} is on {addr}.")
        return []


class ActionJudge12(Action):
    def name(self) -> Text:
        return "judge12"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot('name')
        phone = tracker.get_slot('phone')
        dispatcher.utter_message(text=f"The phone number of {name} is {phone} .")
        return []


class ActionJudge13(Action):
    def name(self) -> Text:
        return "judge13"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot('name')
        food = tracker.get_slot('food')
        dispatcher.utter_message(text=f"{name} serves {food} food")
        return []


class ActionJudge14(Action):
    def name(self) -> Text:
        return "judge14"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot('name')
        area = tracker.get_slot('area')
        dispatcher.utter_message(text=f"{name} is a nice place in the {area} of town")
        return []


class ActionJudge15(Action):
    def name(self) -> Text:
        return "judge15"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot('name')
        postcode = tracker.get_slot('postcode')
        dispatcher.utter_message(text=f"The post code of {name} is {postcode}")
        return []


class ActionJudge16(Action):
    def name(self) -> Text:
        return "judge16"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        food_options = tracker.get_latest_entity_values("food")  # 假设用户可能提到了两种食物
        food_options_list = list(food_options)
        if len(food_options_list) > 1:
            dispatcher.utter_message(
                text=f"Sorry would you like {food_options_list[0]} or {food_options_list[1]} food?")
        else:
            dispatcher.utter_message(text="Sorry, could you please specify the food type again?")
        return []


class ActionJudge17(Action):
    def name(self) -> Text:
        return "judge17"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        area = tracker.get_slot('area')
        dispatcher.utter_message(text=f"Sorry would you like the {area} of town or you dont care")
        return []


class ActionJudge18(Action):
    def name(self) -> Text:
        return "judge18"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        area = tracker.get_latest_entity_values("food")  # 假设用户可能提到了两种食物
        area_list = list(area)
        if len(area_list) > 1:
            dispatcher.utter_message(
                text=f"Sorry would you like something in the {area_list[0]} or in the {area_list[1]}")
        else:
            dispatcher.utter_message(text="Sorry, could you please specify the food type again?")
        return []


class ActionJudge19(Action):
    def name(self) -> Text:
        return "judge19"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        pricerange = tracker.get_slot('pricerange')
        dispatcher.utter_message(
            text=f"Sorry would you like something in the {pricerange} price range or you dont care")
        return []


class ActionJudge20(Action):
    def name(self) -> Text:
        return "judge20"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        p = tracker.get_latest_entity_values("pricerange")  # 假设用户可能提到了两种食物
        pricerange = list(p)
        if len(pricerange) > 1:
            dispatcher.utter_message(
                text=f"Sorry would you like something in the {pricerange[0]} price range or in the {pricerange[1]} price range")
        else:
            dispatcher.utter_message(text="Sorry, could you please specify the food type again?")
        return []


class ActionJudge21(Action):
    def name(self) -> Text:
        return "judge21"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        food = tracker.get_slot('food')
        dispatcher.utter_message(
            text=f"I am sorry but there is no other {food} restaurant that matches your request")
        return []


class ActionJudge22(Action):
    def name(self) -> Text:
        return "judge22"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        food = tracker.get_slot('food')
        area = tracker.get_slot('area')
        dispatcher.utter_message(text=f"I am sorry but there is no other {food} restaurant in the {area} of town")
        return []


class ActionJudge23(Action):
    def name(self) -> Text:
        return "judge23"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        food = tracker.get_slot('food')
        pricerange = tracker.get_slot('pricerange')
        dispatcher.utter_message(
            text=f"I am sorry but there is no other {food} restaurant in the {pricerange} price range")
        return []


class ActionJudge24(Action):
    def name(self) -> Text:
        return "judge24"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        pricerange = tracker.get_slot('pricerange')
        area = tracker.get_slot('area')
        dispatcher.utter_message(
            text=f"Sorry but there is no other restaurant in the {pricerange} price range and the {area} of town")
        return []


class ActionJudge25(Action):
    def name(self) -> Text:
        return "judge25"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot('name')
        area = tracker.get_slot('area')
        food = tracker.get_slot('food')
        dispatcher.utter_message(text=f"{name} is a nice place in the {area} of town serving tasty {food} food")
        return []


class ActionJudge26(Action):
    def name(self) -> Text:
        return "judge26"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot('name')
        food = tracker.get_slot('food')
        pricerange = tracker.get_slot('pricerange')
        dispatcher.utter_message(text=f"{name} serves {food} food in the {pricerange} price range")
        return []


class ActionJudge27(Action):
    def name(self) -> Text:
        return "judge27"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot('name')
        addr = tracker.get_slot('addr')
        food = tracker.get_slot('food')
        dispatcher.utter_message(text=f"{name} is on {addr} and serves tasty {food} food")
        return []


class ActionJudge28(Action):
    def name(self) -> Text:
        return "judge28"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot('name')
        addr = tracker.get_slot('addr')
        phone = tracker.get_slot('phone')
        dispatcher.utter_message(text=f"The phone number of {name} is {phone} and it is on {addr} .")
        return []


class ActionJudge29(Action):
    def name(self) -> Text:
        return "judge29"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot('name')
        postcode = tracker.get_slot('postcode')
        phone = tracker.get_slot('phone')
        dispatcher.utter_message(text=f"The phone number of {name} is {phone} and its postcode is {postcode} .")
        return []


class ActionJudge30(Action):
    def name(self) -> Text:
        return "judge30"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot('name')
        pricerange = tracker.get_slot('pricerange')
        phone = tracker.get_slot('phone')
        dispatcher.utter_message(
            text=f"The phone number of {name} is {phone} and it is in the {pricerange} price range .")
        return []


class ActionJudge31(Action):
    def name(self) -> Text:
        return "judge31"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot('name')
        pricerange = tracker.get_slot('pricerange')
        area = tracker.get_slot('area')
        dispatcher.utter_message(text=f"{name} is a nice place in the {area} of town and the prices are {pricerange}")
        return []


class ActionJudge32(Action):
    def name(self) -> Text:
        return "judge32"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot('name')
        addr = tracker.get_slot('addr')
        postcode = tracker.get_slot('postcode')
        dispatcher.utter_message(text=f"{name} is on {addr} , {postcode}")
        return []


class ActionJudge33(Action):
    def name(self) -> Text:
        return "judge33"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot('name')
        phone = tracker.get_slot('phone')
        postcode = tracker.get_slot('postcode')
        dispatcher.utter_message(text=f"The phone number of {name} is {phone} and its postcode is {postcode} .")
        return []


class ActionJudge34(Action):
    def name(self) -> Text:
        return "judge34"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        pricerange = tracker.get_slot('pricerange')
        area = tracker.get_slot('area')
        dispatcher.utter_message(
            text=f"Sorry but there is no other restaurant in the {pricerange} price range and the {area} of town")
        return []


class ActionJudge35(Action):
    def name(self) -> Text:
        return "judge35"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        food = tracker.get_slot('food')
        dispatcher.utter_message(text=f"I am sorry but there is no other {food} restaurant that matches your request")
        return []


class ActionJudge36(Action):
    def name(self) -> Text:
        return "judge36"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        food = tracker.get_slot('food')
        pricerange = tracker.get_slot('pricerange')
        dispatcher.utter_message(
            text=f"I am sorry but there is no other {food} restaurant in the {pricerange} price range")
        return []


class ActionJudge37(Action):
    def name(self) -> Text:
        return "judge37"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        food = tracker.get_slot('food')
        pricerange = tracker.get_slot('pricerange')
        name = tracker.get_slot('name')
        area = tracker.get_slot('area')
        dispatcher.utter_message(
            text=f"{name} is a great restaurant serving {pricerange} {food} food in the {area} of town .")
        return []


class ActionJudge38(Action):
    def name(self) -> Text:
        return "judge38"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        postcode = tracker.get_slot('postcode')
        phone = tracker.get_slot('phone')
        name = tracker.get_slot('name')
        addr = tracker.get_slot('addr')
        dispatcher.utter_message(
            text=f"The phone number of {name} is {phone} and its postcode is {postcode}, locating at {addr} .")
        return []


class ActionJudge39(Action):
    def name(self) -> Text:
        return "judge39"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        pricerange = tracker.get_slot('pricerange')
        phone = tracker.get_slot('phone')
        name = tracker.get_slot('name')
        addr = tracker.get_slot('addr')
        dispatcher.utter_message(
            text=f"{name} is on {addr} . Its phone number is {phone} , and it is in the {pricerange} pricerange .")
        return []


class ActionJudge40(Action):
    def name(self) -> Text:
        return "judge40"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot('name')
        dispatcher.utter_message(text=f"{name} is a great restaurant")
        return []


class ActionJudge41(Action):
    def name(self) -> Text:
        return "judge41"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        food = tracker.get_slot('food')
        dispatcher.utter_message(text=f"I'm sorry but there is no restaurant serving {food} food")
        return []


class ActionJudge42(Action):
    def name(self) -> Text:
        return "judge42"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        area = tracker.get_slot('area')
        dispatcher.utter_message(text=f"I'm sorry but there is no japanese restaurant in the {area} of town")
        return []


class ActionJudge43(Action):
    def name(self) -> Text:
        return "judge43"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        pricerange = tracker.get_slot('pricerange')
        food = tracker.get_slot('food')

        dispatcher.utter_message(text=f"I'm sorry but there is no restaurant serving {pricerange} {food} food")
        return []


class ActionJudge46(Action):
    def name(self) -> Text:
        return "judge46"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        pricerange = tracker.get_slot('pricerange')
        food = tracker.get_slot('food')
        area = tracker.get_slot('area')
        dispatcher.utter_message(
            text=f"Sorry but there is no other {food} restaurant in the {pricerange} price range and the {area} of town")
        return []


class ActionJudge44(Action):
    def name(self) -> Text:
        return "judge44"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            "Sorry I am a bit confused ; please tell me again what you are looking for .")
        return []


class ActionJudge45(Action):
    def name(self) -> Text:
        return "judge45"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            "Can I help you with anything else?")
        return []


class ActionJudge47(Action):
    def name(self) -> Text:
        return "judge47"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            "You are looking for a restaurant is that right?")
        return []
