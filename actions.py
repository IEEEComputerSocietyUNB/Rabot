# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

 from typing import Any, Text, Dict, List

 from rasa_sdk import Action, Tracker
 from rasa_sdk.executor import CollectingDispatcher
 from rasa_core_sdk import Action
 from rasa_core_sdk.events import SlotSet

 class StoreIntroductionIntent(Action):
     """Stores the bot use case in a slot"""

     def name(self):
         return "store_introduction_intent"

     def run(self, dispatcher, tracker, domain):

         # we grab the whole user utterance here as there are no real entities
         # in the use case
         message = tracker.latest_message.get('text')

         return [SlotSet('intent_message', message)]


#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message("Hello World!")
#
#         return []
