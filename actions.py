# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

employee_details = [{
    "id_no" : "EMP-234",
    "name" : "Himanshu Teotia",
    "status" : "active",
    "designation": "Chatbot developer"
},{
    "employee_id_no" : "EMP-235",
    "employee_name" : "Suresh",
    "employee_status" : "deactive",
    "designation": "Frontend developer"
}]

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []
