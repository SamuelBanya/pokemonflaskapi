from typing import Optional, List
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db

pokemon_types = sa.Table("pokemon_types", 
db.metadata, 
sa.Column("pokemon_id", sa.ForeignKey("pokemon.id"), primary_key=True),
sa.Column("type_id", sa.ForeignKey("type.id"), primary_key=True),
)

pokemon_weaknesses = sa.Table("pokemon_weaknesses", 
db.metadata, 
sa.Column("pokemon_id", sa.ForeignKey("pokemon.id"), primary_key=True),
sa.Column("weakness_id", sa.ForeignKey("weakness.id"), primary_key=True),
)

class Type(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(32), unique=True)

class Weakness(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(32), unique=True)

class NextEvolution(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    num: so.Mapped[str] = so.mapped_column(sa.String(3))
    name: so.Mapped[str] = so.mapped_column(sa.String(64))

    pokemon_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey("pokemon.id"))
    pokemon: so.Mapped["Pokemon"] = so.relationship(back_populates="next_evolution")

class Pokemon(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    num: so.Mapped[str] = so.mapped_column(sa.String(3), unique=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(64), unique=True)
    img: so.Mapped[str] = so.mapped_column(sa.String(120), unique=True)
    types: so.Mapped[List["Type"]] = so.relationship(secondary=pokemon_types, backref="pokemons")
    height: so.Mapped[str] = so.mapped_column(sa.String(64))
    weight: so.Mapped[str] = so.mapped_column(sa.String(64))
    weaknesses: so.Mapped[List["Weakness"]] = so.relationship(secondary=pokemon_weaknesses, backref="pokemons")
    next_evolution: so.Mapped[List["NextEvolution"]] = so.relationship(back_populates="pokemon", cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Pokemon {self.name}>'