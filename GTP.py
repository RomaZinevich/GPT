import openai

# Встановлення ключа API
openai.api_key = "ape-key" #свій убрав

def ask_gpt(question):

    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=question,
        max_tokens=3000,
        n=1,
        stop=None,
        temperature=0.5,
    )

    answer = response.choices[0].text.strip()
    return answer


while True:
    question = input("Питання: ") #Напишм мені проект "Розробка системи збору портативних комп'ютерів на основі сумісності деталей та вподобань" з розділами...
    if question.lower() == 'quit': #Напишм мені до проекту "Розробка системи збору портативних комп'ютерів на основі сумісності деталей та вподобань" Infrastructure Architecture Document
        break

    try:
        answer = ask_gpt(question)
        print(f"Відповідь ChatGPT: {answer}\n")
    except Exception as e:
        print(f"Сталася помилка: {e}")