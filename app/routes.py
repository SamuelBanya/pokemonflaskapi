from flask import Blueprint, render_template
from app.models import Pokemon

bp = Blueprint('main', __name__)

type_colors = {
    "Normal": "#A8A77A",
    "Fire": "#EE8130",
    "Water": "#6390F0",
    "Electric": "#F7D02C",
    "Grass": "#7AC74C",
    "Ice": "#96D9D6",
    "Fighting": "#C22E28",
    "Poison": "#A33EA1",
    "Ground": "#E2BF65",
    "Flying": "#A98FF3",
    "Psychic": "#F95587",
    "Bug": "#A6B91A",
    "Rock": "#B6A136",
    "Ghost": "#735797",
    "Dragon": "#6F35FC",
    "Dark": "#705746",
    "Steel": "#B7B7CE",
    "Fairy": "#D685AD"
}

@bp.route("/")
def index():
    return render_template('index.html')

@bp.route("/pokemon/<pokemonname>", methods=["GET"])
def show_pokemon(pokemonname):
    results = Pokemon.query.filter(Pokemon.name.ilike(pokemonname)).all()

    if not results:
        return render_template('pokemonnotfound.html', pokemonname=pokemonname)

    return render_template('pokemonflaskapi.html', pokemonname=pokemonname, pokemon=results, type_colors=type_colors)
