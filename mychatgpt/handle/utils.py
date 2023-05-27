import openai

openai.api_key = "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"

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "


def openai_fun(question):
    #helo=input('What is your question?')

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=question,
        temperature=0.9,
        max_tokens=60,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )

    answer=response.choices[0].text
    return answer

