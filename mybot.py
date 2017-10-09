import telegram

token = "447204684:AAG8quYI85IFn-hsY-iWt2wtsTQCKcD77a8"

class TodoBot(telegram.Bot):
    def __init__(self):
        super(TodoBot, self).__init__(token=token)
        self.commands = ['/add', '/pop', '/help', '/show']
        self.items = []

    def add_item(self, text):
        self.items.append(text)

    def pop_item(self):
        return self.items.pop()

    def help(self):
        # print out all commands and description
        return "All stuff is pretty forward"

    def show_all(self):
        # show all items
        return self.items

    def process(self, text):
        message = ""
        # if text starts with any command, then identify it
        if text.startswith("/add"):
            self.add_item(text.split("/add")[-1])
        elif text.startswith("/pop"):
            message = self.pop_item()
        elif text.startswith("/help"):
            message = self.help()
        elif text.startswith("/show_all"):
            message = self.show_all()
        else:
            continue

        if message:
            return self.sendMessage(chat_id=update.message.chat.id, text=update.message.text)
        else:
            continue
