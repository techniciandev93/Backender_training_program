from pydantic import BaseModel, ValidationError


class Product(BaseModel):
    name: str
    price: float


class User(BaseModel):
    name: str
    age: int
    products: list[Product]


if __name__ == '__main__':
    user_info = {
        "name": "Anton",
        "age": 'sdfsdf',
        "products": [
            {
                "name": "bread",
                "price": 125,
            },
            {
                "name": "coffee",
                "price": 200,
            },
        ]
    }

    try:
        person = User(**user_info)
    except ValidationError as error:
        print(error.json())

    user_info['age'] = 30
    person = User(**user_info)
    person_json = person.json()
    imported_person = User.parse_raw(person_json)
    print(imported_person)
