import requests
import json


base_url = 'https://petstore.swagger.io/v2'

# Добавляем нового питомца
print("***Добавляем нового питомца***")

pet_new = {
    "id": 257349,
    "category": {"id": 0, "name": "cat"},
    "name": "Alex",
    "photoUrls": ["string"],
    "tags": [{"id": 0, "name": "cat"}],
    "status": "available"
}

res_post = requests.post(f'{base_url}/pet', headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                         data=json.dumps(pet_new, ensure_ascii=False))

print(f'Статус ответа от сервера на POST запрос добавление питомца: {res_post.status_code}')
print(res_post.text)
print(res_post.json())
print(type(res_post.json()))


# Добавляем фото питомца
print("***Добавляем фото питомца***")

petId = 257349
pet_photo = 'Alex.jpg'
files = {'file': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')}
res_post_photo = requests.post(f'{base_url}/pet/{petId}/uploadImage', headers={'accept': 'application/json'}, files=files)

print(f"Статус ответа от сервера на POST запрос добавление фото питомца: {res_post_photo.status_code}")
print(res_post_photo.text)
print(res_post_photo.json())
print(type(res_post_photo.json()))


# Просмотр информации по питомцу по id
print("***Просмотр инфо по питомцу***")

id = 257349
res_get = requests.get(f'{base_url}/pet/{id}', headers={'accept': 'application/json'})

print(f"Статус ответа от сервера на GET запрос: {res_get.status_code}")
print(res_get.text)
print(res_get.json())
print(type(res_get.json()))


# Изменяем данные питомца
print("***Изменяем данные питомца***")

pet_new_change = {
    "id": 257349,
    "category": {"id": 0, "name": "dog"},
    "name": "Alex",
    "photoUrls": ["string"],
    "tags": [{"id": 0, "name": "dog"}],
    "status": "sold"
}

res_put = requests.put(f'{base_url}/pet', headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                       data=json.dumps(pet_new_change, ensure_ascii=False))

print(f'Статус ответа от сервера на PUT запрос: {res_put.status_code}')
print(res_put.text)
print(res_put.json())
print(type(res_put.json()))


# Удаление питомца
print("***Удаление питомца***")

petId = 257349

res_delete = requests.delete(f'{base_url}/pet/{petId}', headers={'accept': 'application/json'})

print(f'Статус ответа от сервера на DELETE запрос: {res_delete.status_code}')
print(res_delete.text)
print(res_delete.json())
print(type(res_delete.json()))
