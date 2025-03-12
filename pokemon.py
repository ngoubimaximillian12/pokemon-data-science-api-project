import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBRegressor
from flask import Flask, jsonify

base_url = "https://pokeapi.co/api/v2/pokemon"

# Fetch Pokémon Data Function
def get_pokemon_data(limit=100):
    pokemon_data = []
    for pokemon_id in range(1, limit + 1):
        url = f"{base_url}/{pokemon_id}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            pokemon_data.append({
                "ID": pokemon_id, "Name": data["name"].title(),
                "Height": data["height"], "Weight": data["weight"],
                "Base Experience": data["base_experience"],
                "HP": next(stat["base_stat"] for stat in data["stats"] if stat["stat"]["name"] == "hp"),
                "Attack": next(stat["base_stat"] for stat in data["stats"] if stat["stat"]["name"] == "attack"),
                "Defense": next(stat["base_stat"] for stat in data["stats"] if stat["stat"]["name"] == "defense"),
                "Speed": next(stat["base_stat"] for stat in data["stats"] if stat["stat"]["name"] == "speed"),
                "Sp. Attack": next(stat["base_stat"] for stat in data["stats"] if stat["stat"]["name"] == "special-attack"),
                "Sp. Defense": next(stat["base_stat"] for stat in data["stats"] if stat["stat"]["name"] == "special-defense"),
                "Type 1": data["types"][0]["type"]["name"]
            })
    return pd.DataFrame(pokemon_data)

df = get_pokemon_data(limit=100)
df.to_csv("data/pokemon_100.csv", index=False)
