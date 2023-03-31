import openai

class Chatgpt:
    def __init__(self) -> None:
        openai.api_key = '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'

    def write_code(self, prompt_text):
        response = openai.Completion.create(
            model="code-davinci-002",
            prompt=prompt_text,
            temperature=0,
            max_tokens=256,
        )

        return response

    def text_out(self, prompt_text: str):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt_text,
            max_tokens=400,
            temperature=0.9,
        )
        return response

    def generate_image(self, prompt_text):
        response = openai.Image.create(
            prompt=prompt_text,
            n=1,
            size="1024x1024"
        )
        return response
