from bs4 import BeautifulSoup
import requests
requested_pokemon = input("ENTER Pokemon Name: ")
requested_pokemon_page = requests.get(f"https://pokemondb.net/pokedex/{requested_pokemon}")

