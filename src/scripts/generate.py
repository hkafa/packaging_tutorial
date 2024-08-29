from uuid import uuid4


def generate_id():
    generated_id = uuid4()
    print(generated_id)
    return generated_id


def add_numbers(a: int, b: int):
    return a + b


