from app import create_app, db
from app.models import Pokemon, Type, Weakness, NextEvolution
from data.pokemon import pokemon

app = create_app()

with app.app_context():
    print("Dropping all tables...")
    db.drop_all()
    print("Creating all tables...")
    db.create_all()

    type_cache = {}
    weakness_cache = {}

    for entry in pokemon:
        pkmn = Pokemon(
            id=entry["id"],
            num=entry["num"],
            name=entry["name"],
            img=entry["img"],
            height=entry["height"],
            weight=entry["weight"],
        )

        # Types:
        for t in entry["type"]:
            if t not in type_cache:
                type_obj = Type(name=t)
                db.session.add(type_obj)
                type_cache[t] = type_obj
            pkmn.types.append(type_cache[t])
        
        # Weaknesses:
        for w in entry["weaknesses"]:
            if w not in weakness_cache:
                weakness_obj = Weakness(name=w)
                db.session.add(weakness_obj)
                weakness_cache[w] = weakness_obj
            pkmn.weaknesses.append(weakness_cache[w])

        # Next Evolution:
        for evo in entry.get("next_evolution", []):
            evo_entry = NextEvolution(num=evo["num"], name=evo["name"])
            pkmn.next_evolution.append(evo_entry)

        db.session.add(pkmn)

    db.session.commit()
    print("Data seeded.")
