import telegram

token = "447204684:AAG8quYI85IFn-hsY-iWt2wtsTQCKcD77a8"

class TodoBot(telegram.Bot):
    def __init__(self):
        super(TodoBot, self).__init__(token=token)
        self.commands = ['/add', '/pop', '/help', '/show']

    def add_item(self, text):
        pass

    def pop_item(self):
        return None

    def help(self):
        # print out all commands and description
        pass

    def show_all(self):
        # show all items
        pass

    def process(self, text):
        # if text starts with any command, then identify it
        if text.startswith("/add"):
            self.add_item(text.split("/add")[-1])
        elif text.startswith("/pop"):
            self.pop_item()
        elif text.startswith("/help"):
            self.help()
        elif text.startswith("/show_all"):
            self.show_all()
        else:
            continue


    def process(self, update):
        return self.sendMessage(chat_id=update.message.chat.id, text=update.message)
        pass
