class Lang:
    strings = {
        "en": {
            "error_no_reply": "This command must be sent as a reply to one's message!",
        },
        "ru": {
            "error_no_reply": "Эта команда должна быть ответом на какое-либо сообщение!",
        },
    }

    def __init__(self, language_key: str):
        if language_key in self.strings.keys():
            self.chosen_lang = language_key
        else:
            raise ValueError(f"No such language: {language_key}")

    def get(self, key):
        return self.strings.get(self.chosen_lang, {}).get(key, "%MISSING STRING%")
