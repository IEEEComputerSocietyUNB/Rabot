# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk import Action
from rasa_core_sdk.events import SlotSet

class ActionIntroduction(Action):

    def name(self) -> Text:
        return "action_introduction"

    def submit(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(responses="utter_introduction")

        return []

#def name(self) -> Text:
#    """Unique identifier of the form"""

#    return "action_introduction"

#@staticmethod
#def required_slots(tracker: Tracker) -> List[Text]:
#    """A list of required slots that the form has to fill"""

#    return ["know_more"]

#def submit(
#    self,
#    dispatcher: CollectingDispatcher,
#    tracker: Tracker,
#    domain: Dict[Text, Any],
#) -> List[Dict]:
#    """Define what the form has to do after all required slots are filled"""

    # utter submit template
#    dispatcher.utter_message(template="utter_full_introduction")
#    return []
