import IPython
from IPython.display import clear_output, HTML, display
from rasa_core.agent import Agent
import time

messages = ["Olá! Você pode conversar comigo nesta janela. Digite 'stop' para terminar a conversa."]
agent = Agent.load('models/dialogue')

def chatlogs_html(messages):
    messages_html = "".join(["<p>{}</p>".format(m) for m in messages])
    chatbot_html = """<div class="chat-window" {}</div>""".format(messages_html)
    return chatbot_html


while True:
    clear_output()
    display(HTML(chatlogs_html(messages)))
    time.sleep(0.3)
    a = input()
    messages.append(a)
    if a == 'stop':
        break
    responses = agent.handle_message(a)
    for r in responses:
        messages.append(r.get("text"))