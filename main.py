import vk_api
from random import choice, randrange
from vk_api.longpoll import VkLongPoll, VkEventType

TOKEN = "vk1.a.vk2tJPMm5DSKzr13_KsNaoDA2nGkc-jmU4X53UUJDHSrmAaiPROzqst5WI4AcYnV0HaGmIkMI6SZ64K9b7AwzqjDOYNeMzo6AipMARtoVqsPlb1n-GosT5sVnvmykqRmCbPORunUVH3hw2mbOJ9P1FXFceVPTEeJHdBMpsV9wCL3Xm0TC4E9zMvJ_JmthrVAlRDakLt7seSWap4u5falA"

vk_session = vk_api.VkApi(token=TOKEN)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
vars = ['камень', 'ножницы', 'бумага']

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text and event.text.lower() in vars:
        bot = choice(vars)
        if event.from_user:
            vk.messages.send(user_id = event.user_id, message = bot, random_id = randrange(1, 100000))
            if bot == "ножницы":
                if event.text.lower() == "ножницы":
                    user = "ничья :|"
                elif event.text.lower() == "камень":
                    user = "Ты победил!!!! :D"
                else:
                    user = "Ты проиграл _/(._.)|_ "
            elif bot == "бумага":
                if event.text.lower() == "бумага":
                    user = "ничья"
                elif event.text.lower() == "ножницы":
                    user = "Ты победил!!!! :D"
                else:
                    user = "Ты проиграл _/(._.)|_"
            else:
                if event.text.lower() == "камень":
                    user = "ничья"
                elif event.text.lower() == "бумага":
                    user = "Ты победил!!!! :D"
                else:
                    user = "Ты проиграл _/(._.)|_ "
            vk.messages.send(user_id=event.user_id, message=user, random_id=randrange(1, 100000))
    elif event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                vk.messages.send(user_id=event.user_id, message="ERROR", random_id=randrange(1, 100000))
