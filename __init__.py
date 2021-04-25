from mycroft import MycroftSkill, intent_file_handler


class Myhome(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('myhome.intent')
    def handle_myhome(self, message):
        self.speak_dialog('myhome')


def create_skill():
    return Myhome()

