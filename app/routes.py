from flask import Blueprint, render_template
from app.models import Pokemon

bp = Blueprint('main', __name__)

@bp.route("/")
def index():
    return render_template('index.html')

@bp.route("/pokemon/<pokemonname>", methods=["GET"])
def show_pokemon(pokemonname):
    results = Pokemon.query.filter(Pokemon.name.ilike(pokemonname)).all()

    if not results:
        return render_template('pokemonnotfound.html', pokemonname=pokemonname)

    return render_template('pokemonflaskapi.html', pokemonname=pokemonname, pokemon=results)
