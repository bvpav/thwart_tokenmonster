import base64
import json
import random
import string
import time
from pprint import pp

import requests
from faker import Faker

WEBHOOK_URL = '<ENTER WEBHOOK URL HERE>'
DO_DELETE_WEBHOOK = True

faker = Faker()
num_requests = 0


def random_string(population, k):
    return ''.join(random.choices(population, k=k))


def generate_token(user_id):
    enc_id = base64.b64encode(user_id.encode('ascii')).decode('ascii')
    chars = string.ascii_letters + string.digits + '-'
    rand6 = random_string(chars, k=6)
    rand27 = random_string(chars, k=27)

    return '.'.join((enc_id, rand6, rand27))


def generate_data():
    color = random.randint(0, 0xffffff)
    user = {
        'id': random_string(string.digits, k=18),
        'username': faker.name(),
        'discriminator': random_string(string.digits, k=4),
        'email': faker.ascii_free_email(),
        'phone': faker.phone_number(),
    }
    pc = {
        'architecture': 'AMD64',
        'hostname': 'DESKTOP-' + random_string(string.ascii_uppercase + string.digits, k=7),
        'ip-address': '127.0.0.1',
        'mac-address': faker.mac_address(),
        'platform': 'Windows',
        'platform-release': '10',
        'platform-version': '10.0.' + random_string(string.digits, k=5),
        'processor': f'Intel64 Family 6 Model {random.randint(30, 80)} Stepping 1, GenuineIntel',
        'public_ip': faker.ipv4(),
    }
    pc_user = user['username'].lower().replace(' ', '-')
    pc_roaming = fr'C:\Users\{pc_user}\AppData\Roaming'
    pc_local = fr'C:\Users\{pc_user}\AppData\Local'
    token = generate_token(user['id'])
    return {'username': 'TokenMonster', 'embeds': [
        dict(title='Sniped a token.',
             color=f'{color}',
             fields=[
                 {
                     'name': '**Account Info**',
                     'value': f'💳 User ID: ||{user["id"]}||\n🧔 Username: ||{user["username"] + "#" + user["discriminator"]}||\n📬 Email: ||{user["email"]}||\n☎ Phone: ||{user["phone"]}||',
                     'inline': True
                 },
                 {
                     'name': '**PC Info**',
                     'value': f'IP: ||{pc["public_ip"]}|| \nUsername: {pc_user}\nAppData: {pc_local}\nRoaming: {pc_roaming}',
                     'inline': True
                 },
                 {
                     'name': '💰 Token',
                     'value': f'||{token}||',
                     'inline': False
                 },
                 {
                     'name': '**PC Data Dump**',
                     'value': f'```{json.dumps(pc)}```',
                     'inline': False
                 },
             ]),
    ]}


def send_data(data):
    global num_requests
    pp(data)
    print('-----')
    response = requests.post(WEBHOOK_URL, headers={'Content-Type': 'application/json'}, data=json.dumps(data))
    print(response.text)
    if 200 <= response.status_code < 300:
        num_requests += 1
        # XXX: idk what [-] and [*] mean, they just look cool
        print(f'[-] Successfully sent request #{num_requests}')


def delete_webhook():
    print('[-] Deleting webhook...')
    response = requests.delete(WEBHOOK_URL)
    if 200 <= response.status_code < 300:
        # XXX: idk what [-] and [*] mean, they just look cool
        print(f'[-] Successfully deleted webhook {WEBHOOK_URL}')


def main():
    try:
        while True:
            send_data(generate_data())
            time.sleep(3)
    finally:
        # XXX: idk what [-] and [*] mean, they just look cool
        # \r to erase the ^C in my terminal
        print(f'\r[*] Sent {num_requests} request(s) to fraudulent webhook')
        if DO_DELETE_WEBHOOK:
            delete_webhook()


if __name__ == '__main__':
    main()
