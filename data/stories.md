## happy path
* greet
  - utter_greet
  - username_form
  - form{"name": "username_form"}
  - slot{"requested_slot": "username"}
  - form{"name": null}
  - utter_introduction
* affirm

<!---
## happy path 2
* greet{"full_information": "False"}
  - action_introduction
  - utter_full_introduction
  - utter_sociodem
  - utter_sociodemsim
  - utter_sociodemnao
  - slot{"full_information": "True"}
  - utter_method

## introduction
* greet
  - utter_introduction
  - utter_sociodem

## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## hello goodbye path
* greet
  - utter_greet
* goodbye
  - utter_ask_why_leaving

  -->
