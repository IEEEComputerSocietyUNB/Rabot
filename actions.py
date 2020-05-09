# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

# class ActionFacilitySearch(Action):

#     def name(self) -> Text:
#         return "action_facility_search"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         facility = tracker.get_slot("facility")
#         address = "123 Quarantine Street"
#         dispatcher.utter_message(text="Sure, I'm on it!")
#         dispatcher.utter_message(text=f"The address is {address}")

#         return [SlotSet("address", address)]

class ActionDebugBot(Action):
    def name(self) -> Text:
        return "action_debug_bot"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]):
            import ipdb; ipdb.set_trace()
            dispatcher.utter_message(text="Debug away, captain!")