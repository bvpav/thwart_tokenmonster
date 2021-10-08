# Thwart Token Monster

A simple script that floods and disables ongoing malicious token grabbing operations that use [:alien: Token Monster](https://github.com/Atom345/TokenMonster/blob/main/README.md) with fake data.

## :book: Backstory

One day, some guy joined a Discord server I was in and straight up just uploaded a [Token Monster](https://github.com/Atom345/TokenMonster/blob/main/README.md) token logger, with their own webhook edited at the top, perhaps hoping to snipe some tokens and system information.

According to [the author of Token Monster](https://github.com/Atom345/TokenMonster/blob/main/README.md#mega-just-a-note), the script was intended for educational purposes and they _highly discourage using [it] against someone else_. Unfortunately, that doesn't prevent anybody from actually doing so.

So I decided to take matters into my own hands and hack up this little script that floods the _1337 pwnz0r_'s webhook with thousands of _fake, but real-looking token and system captures_ that will hopefully make the life of the script kiddie slightly more miserable than it already is :heart:

## :trophy: Features

- Generates fake Discord authentication tokens _(that shouldn't be valid :pray:)_
- Propagates fake full name, phone number, email, IP and MAC address.
- Synthesizes somewhat-beliavable system information.
- Attacker doesn't get any personally identifiable information because of the nature of Discord Webhooks.
- Deletes the webhook when it's done spamming.

## :coffee: Usage instructions

The script depends on `requests` and `faker`, which need to be installed.

1. `pip install -r requirements.txt`
2. Edit in the malicious webhook in `thwart_tokenmonster.py`
3. `python thwart_tokenmonster.py`
4. Sit back, relax and enjoy the show
5. Terminate the script and the webhook will automatically be deleted.

## :pushpin: TODO

- [X] Delete the webhook on exit
- [ ] Improve generated system information
    - [ ] Use only existing `processor` strings
    - [ ] Make `platform_version` yield more believable strings
    - [ ] Generate better `hostname`s
- [ ] Maintain compatibility with newer versions of Token Monster

### :pray: Acknowledgments

Token Monster was created by [AtomDev](https://github.com/Atom345).

README was inspired by [Token Monster's](https://github.com/Atom345/TokenMonster/blob/main/README.md)

## License

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
