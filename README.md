KÄYNNISTÄMINEN:

Lataa ja asenna python, jos sitä ei vielä ole: https://www.python.org/downloads/release/python-3144/

Lataa UV: "pip install uv"

Luo virtuaaliympäristö: "uv venv"

Aktivoi virtuaaliympäristö: ".venv\Scripts\activate"

Asenna riippuvuudet: "uv pip install -r requirements.txt"

Käynnistä: "uv run fastapi dev"

TEKOÄLYN KÄYTTÖ PROJEKTISSA:

Käytetty .gitignoren tekemissä

Käytetty riippuvuuksien selvityksessä, kun ohjelma ei käynnistynyt.

Selvitin tekoälyn avulla, miten saan responsen siinä järjestyksessä kuin haluan ja opein, mitä response model tarkoittaa.

Käytin selvittääkseni itselle aikaisemmin livekoodausvideosta sokeasti kopioitua koodia

Käytin myös selvittääkseni edellä mainitussa videossa ilmi tulleen, mutta selvittämättä jääneen ongelman, miksi events listaa ei näkynyt get_player_by_id:ssä. tekoäly teki "PlayerReadWithEvents" funktion tätä varten.

Käytettiin apuna query-koodin tekemisessä (esimerkiksi miten syntaksi toimii, kun on kaksi ehtoa (where ketjuttaminen))

Käytettiin requirements.txt tekemisessä, virtuaaliympäristön uudelleen asennuksessa (ongelma oli, että tiedostoon tuli kaiken maailman tiktok-kirjastoja sun muita, joita olen käyttänyt omissa projekteissa)

Tekoälyn tuotokset todettiin toimiviksi ihan kokeilemalla ja syy niiden käyttöön oli ajan ja hermojen säästäminen.
