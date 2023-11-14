from openai import OpenAI

class MainLogic:
    def __init__(self) -> None:
        self.client = OpenAI(api_key = "")
        pass
    def setConfig(self, configs):
        self.configs = configs

    def setApiKey(self, key):
        self.client = OpenAI(api_key = key)
    
    def run(self, index, prompt):
        system_content = self.configs[index]["system"]
        user_content = self.configs[index]["user"].replace("#!!!!!#", prompt)
        try:
            completion = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_content},
                    {"role": "user", "content": user_content}
                ]
            )
            print(completion.choices)
            return completion.choices[0].message.content
        except:
            return "error"