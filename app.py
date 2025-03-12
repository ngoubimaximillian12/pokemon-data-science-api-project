from flask import Flask, jsonify
import requests

app = Flask(__name__)
base_url = "https://pokeapi.co/api/v2/pokemon"

@app.route("/")
def home():
    return "Welcome to the Pokémon API! Use /pokemon/<name>"

@app.route("/pokemon/<name>")
def get_pokemon(name):
    url = f"{base_url}/{name.lower()}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return jsonify({
            "Name": data["name"].title(),
            "HP": data["stats"][0]["base_stat"],
            "Attack": data["stats"][1]["base_stat"],
            "Defense": data["stats"][2]["base_stat"],
            "Speed": data["stats"][5]["base_stat"],
            "Sp. Attack": data["stats"][3]["base_stat"],
            "Sp. Defense": data["stats"][4]["base_stat"]
        })
    else:
        return jsonify({"Error": "Pokémon not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
