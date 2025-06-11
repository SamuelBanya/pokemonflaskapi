from flask import Blueprint, render_template
from app.models import Pokemon

bp = Blueprint('main', __name__)

type_colors = {
    "normal": "#A8A77A",
    "fire": "#EE8130",
    "water": "#6390F0",
    "electric": "#F7D02C",
    "grass": "#7AC74C",
    "ice": "#96D9D6",
    "fighting": "#C22E28",
    "poison": "#A33EA1",
    "ground": "#E2BF65",
    "flying": "#A98FF3",
    "psychic": "#F95587",
    "bug": "#A6B91A",
    "rock": "#B6A136",
    "ghost": "#735797",
    "dragon": "#6F35FC",
    "dark": "#705746",
    "steel": "#B7B7CE",
    "fairy": "#D685AD"
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
