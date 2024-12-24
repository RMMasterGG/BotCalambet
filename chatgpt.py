from g4f.client import Client

def answer_code(text = str()):
    client = Client()
    prompt = "Ты мощный инструмент, твоя задача проверять ведённый код:"
    response = client.chat.completions.create(model="gpt-4o",
                                              messages=[{
                                                  "role": "user",
                                                  "content": f"{prompt}: {text}"}]
                                              )
    return response.choices[0].message.content