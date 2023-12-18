from openai import OpenAI

class MainLogic:
    def __init__(self) -> None:
        self.client = OpenAI(api_key = "")
        self.lastClipboard = ""
        pass
    def setConfig(self, configs):
        self.configs = configs

    def setApiKey(self, key):
        self.client = OpenAI(api_key = key)
    
    def run(self, index):
        return self.configs[index]["prompt"] + "\n"
        
