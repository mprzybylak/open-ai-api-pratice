from openai import OpenAI

def main():
    client = OpenAI()

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are stand up comedian"},
        {"role": "user", "content": "Tell a joke about horses"}
    ]
    )

    print(completion.choices)

if __name__ == "__main__":
    main()