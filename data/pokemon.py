# Taken from here:
# https://github.com/olitreadwell/pokemon-classic-json/blob/main/pokedex.json

pokemon = [
    {
    "id": 1,
    "num": "001",
    "name": "Bulbasaur",
    "img": "http://www.serebii.net/pokemongo/pokemon/001.png",
    "type": ["Grass", "Poison"],
    "height": "0.71 m",
    "weight": "6.9 kg",
    "weaknesses": ["Fire", "Ice", "Flying", "Psychic"],
    "next_evolution": [
        {
        "num": "002",
        "name": "Ivysaur"
        },
        {
        "num": "003",
        "name": "Venusaur"
        }
    ]
    },
    {
    "id": 2,
    "num": "002",
    "name": "Ivysaur",
    "img": "http://www.serebii.net/pokemongo/pokemon/002.png",
    "type": ["Grass", "Poison"],
    "height": "0.99 m",
    "weight": "13.0 kg",
    "weaknesses": ["Fire", "Ice", "Flying", "Psychic"],
    "prev_evolution": [
        {
        "num": "001",
        "name": "Bulbasaur"
        }
    ],
    "next_evolution": [
        {
        "num": "003",
        "name": "Venusaur"
        }
    ]
    },
    {
    "id": 3,
    "num": "003",
    "name": "Venusaur",
    "img": "http://www.serebii.net/pokemongo/pokemon/003.png",
    "type": ["Grass", "Poison"],
    "height": "2.01 m",
    "weight": "100.0 kg",
    "weaknesses": ["Fire", "Ice", "Flying", "Psychic"],
    "prev_evolution": [
        {
        "num": "001",
        "name": "Bulbasaur"
        },
        {
        "num": "002",
        "name": "Ivysaur"
        }
    ]
    },
    {
    "id": 4,
    "num": "004",
    "name": "Charmander",
    "img": "http://www.serebii.net/pokemongo/pokemon/004.png",
    "type": ["Fire"],
    "height": "0.61 m",
    "weight": "8.5 kg",
    "weaknesses": ["Water", "Ground", "Rock"],
    "next_evolution": [
        {
        "num": "005",
        "name": "Charmeleon"
        },
        {
        "num": "006",
        "name": "Charizard"
        }
    ]
    },
    {
    "id": 5,
    "num": "005",
    "name": "Charmeleon",
    "img": "http://www.serebii.net/pokemongo/pokemon/005.png",
    "type": ["Fire"],
    "height": "1.09 m",
    "weight": "19.0 kg",
    "weaknesses": ["Water", "Ground", "Rock"],
    "prev_evolution": [
        {
        "num": "004",
        "name": "Charmander"
        }
    ],
    "next_evolution": [
        {
        "num": "006",
        "name": "Charizard"
        }
    ]
    },
    {
    "id": 6,
    "num": "006",
    "name": "Charizard",
    "img": "http://www.serebii.net/pokemongo/pokemon/006.png",
    "type": ["Fire", "Flying"],
    "height": "1.70 m",
    "weight": "90.5 kg",
    "weaknesses": ["Water", "Electric", "Rock"],
    "prev_evolution": [
        {
        "num": "004",
        "name": "Charmander"
        },
        {
        "num": "005",
        "name": "Charmeleon"
        }
    ]
    },
    {
    "id": 7,
    "num": "007",
    "name": "Squirtle",
    "img": "http://www.serebii.net/pokemongo/pokemon/007.png",
    "type": ["Water"],
    "height": "0.51 m",
    "weight": "9.0 kg",
    "weaknesses": ["Electric", "Grass"],
    "next_evolution": [
        {
        "num": "008",
        "name": "Wartortle"
        },
        {
        "num": "009",
        "name": "Blastoise"
        }
    ]
    },
    {
    "id": 8,
    "num": "008",
    "name": "Wartortle",
    "img": "http://www.serebii.net/pokemongo/pokemon/008.png",
    "type": ["Water"],
    "height": "0.99 m",
    "weight": "22.5 kg",
    "weaknesses": ["Electric", "Grass"],
    "prev_evolution": [
        {
        "num": "007",
        "name": "Squirtle"
        }
    ],
    "next_evolution": [
        {
        "num": "009",
        "name": "Blastoise"
        }
    ]
    },
    {
    "id": 9,
    "num": "009",
    "name": "Blastoise",
    "img": "http://www.serebii.net/pokemongo/pokemon/009.png",
    "type": ["Water"],
    "height": "1.60 m",
    "weight": "85.5 kg",
    "weaknesses": ["Electric", "Grass"],
    "prev_evolution": [
        {
        "num": "007",
        "name": "Squirtle"
        },
        {
        "num": "008",
        "name": "Wartortle"
        }
    ]
    },
    {
    "id": 10,
    "num": "010",
    "name": "Caterpie",
    "img": "http://www.serebii.net/pokemongo/pokemon/010.png",
    "type": ["Bug"],
    "height": "0.30 m",
    "weight": "2.9 kg",
    "weaknesses": ["Fire", "Flying", "Rock"],
    "next_evolution": [
        {
        "num": "011",
        "name": "Metapod"
        },
        {
        "num": "012",
        "name": "Butterfree"
        }
    ]
    },
    {
    "id": 11,
    "num": "011",
    "name": "Metapod",
    "img": "http://www.serebii.net/pokemongo/pokemon/011.png",
    "type": ["Bug"],
    "height": "0.71 m",
    "weight": "9.9 kg",
    "weaknesses": ["Fire", "Flying", "Rock"],
    "prev_evolution": [
        {
        "num": "010",
        "name": "Caterpie"
        }
    ],
    "next_evolution": [
        {
        "num": "012",
        "name": "Butterfree"
        }
    ]
    },
    {
    "id": 12,
    "num": "012",
    "name": "Butterfree",
    "img": "http://www.serebii.net/pokemongo/pokemon/012.png",
    "type": ["Bug", "Flying"],
    "height": "1.09 m",
    "weight": "32.0 kg",
    "weaknesses": ["Fire", "Electric", "Ice", "Flying", "Rock"],
    "prev_evolution": [
        {
        "num": "010",
        "name": "Caterpie"
        },
        {
        "num": "011",
        "name": "Metapod"
        }
    ]
    },
    {
    "id": 13,
    "num": "013",
    "name": "Weedle",
    "img": "http://www.serebii.net/pokemongo/pokemon/013.png",
    "type": ["Bug", "Poison"],
    "height": "0.30 m",
    "weight": "3.2 kg",
    "weaknesses": ["Fire", "Flying", "Psychic", "Rock"],
    "next_evolution": [
        {
        "num": "014",
        "name": "Kakuna"
        },
        {
        "num": "015",
        "name": "Beedrill"
        }
    ]
    },
    {
    "id": 14,
    "num": "014",
    "name": "Kakuna",
    "img": "http://www.serebii.net/pokemongo/pokemon/014.png",
    "type": ["Bug", "Poison"],
    "height": "0.61 m",
    "weight": "10.0 kg",
    "weaknesses": ["Fire", "Flying", "Psychic", "Rock"],
    "prev_evolution": [
        {
        "num": "013",
        "name": "Weedle"
        }
    ],
    "next_evolution": [
        {
        "num": "015",
        "name": "Beedrill"
        }
    ]
    },
    {
    "id": 15,
    "num": "015",
    "name": "Beedrill",
    "img": "http://www.serebii.net/pokemongo/pokemon/015.png",
    "type": ["Bug", "Poison"],
    "height": "0.99 m",
    "weight": "29.5 kg",
    "weaknesses": ["Fire", "Flying", "Psychic", "Rock"],
    "prev_evolution": [
        {
        "num": "013",
        "name": "Weedle"
        },
        {
        "num": "014",
        "name": "Kakuna"
        }
    ]
    },
    {
    "id": 16,
    "num": "016",
    "name": "Pidgey",
    "img": "http://www.serebii.net/pokemongo/pokemon/016.png",
    "type": ["Normal", "Flying"],
    "height": "0.30 m",
    "weight": "1.8 kg",
    "weaknesses": ["Electric", "Rock"],
    "next_evolution": [
        {
        "num": "017",
        "name": "Pidgeotto"
        },
        {
        "num": "018",
        "name": "Pidgeot"
        }
    ]
    },
    {
    "id": 17,
    "num": "017",
    "name": "Pidgeotto",
    "img": "http://www.serebii.net/pokemongo/pokemon/017.png",
    "type": ["Normal", "Flying"],
    "height": "1.09 m",
    "weight": "30.0 kg",
    "weaknesses": ["Electric", "Rock"],
    "prev_evolution": [
        {
        "num": "016",
        "name": "Pidgey"
        }
    ],
    "next_evolution": [
        {
        "num": "018",
        "name": "Pidgeot"
        }
    ]
    },
    {
    "id": 18,
    "num": "018",
    "name": "Pidgeot",
    "img": "http://www.serebii.net/pokemongo/pokemon/018.png",
    "type": ["Normal", "Flying"],
    "height": "1.50 m",
    "weight": "39.5 kg",
    "weaknesses": ["Electric", "Rock"],
    "prev_evolution": [
        {
        "num": "016",
        "name": "Pidgey"
        },
        {
        "num": "017",
        "name": "Pidgeotto"
        }
    ]
    },
    {
    "id": 19,
    "num": "019",
    "name": "Rattata",
    "img": "http://www.serebii.net/pokemongo/pokemon/019.png",
    "type": ["Normal"],
    "height": "0.30 m",
    "weight": "3.5 kg",
    "weaknesses": ["Fighting"],
    "next_evolution": [
        {
        "num": "020",
        "name": "Raticate"
        }
    ]
    },
    {
    "id": 20,
    "num": "020",
    "name": "Raticate",
    "img": "http://www.serebii.net/pokemongo/pokemon/020.png",
    "type": ["Normal"],
    "height": "0.71 m",
    "weight": "18.5 kg",
    "weaknesses": ["Fighting"],
    "prev_evolution": [
        {
        "num": "019",
        "name": "Rattata"
        }
    ]
    },
    {
    "id": 21,
    "num": "021",
    "name": "Spearow",
    "img": "http://www.serebii.net/pokemongo/pokemon/021.png",
    "type": ["Normal", "Flying"],
    "height": "0.30 m",
    "weight": "2.0 kg",
    "weaknesses": ["Electric", "Rock"],
    "next_evolution": [
        {
        "num": "022",
        "name": "Fearow"
        }
    ]
    },
    {
    "id": 22,
    "num": "022",
    "name": "Fearow",
    "img": "http://www.serebii.net/pokemongo/pokemon/022.png",
    "type": ["Normal", "Flying"],
    "height": "1.19 m",
    "weight": "38.0 kg",
    "weaknesses": ["Electric", "Rock"],
    "prev_evolution": [
        {
        "num": "021",
        "name": "Spearow"
        }
    ]
    },
    {
    "id": 23,
    "num": "023",
    "name": "Ekans",
    "img": "http://www.serebii.net/pokemongo/pokemon/023.png",
    "type": ["Poison"],
    "height": "2.01 m",
    "weight": "6.9 kg",
    "weaknesses": ["Ground", "Psychic"],
    "next_evolution": [
        {
        "num": "024",
        "name": "Arbok"
        }
    ]
    },
    {
    "id": 24,
    "num": "024",
    "name": "Arbok",
    "img": "http://www.serebii.net/pokemongo/pokemon/024.png",
    "type": ["Poison"],
    "height": "3.51 m",
    "weight": "65.0 kg",
    "weaknesses": ["Ground", "Psychic"],
    "prev_evolution": [
        {
        "num": "023",
        "name": "Ekans"
        }
    ]
    },
    {
    "id": 25,
    "num": "025",
    "name": "Pikachu",
    "img": "http://www.serebii.net/pokemongo/pokemon/025.png",
    "type": ["Electric"],
    "height": "0.41 m",
    "weight": "6.0 kg",
    "weaknesses": ["Ground"],
    "next_evolution": [
        {
        "num": "026",
        "name": "Raichu"
        }
    ]
    },
    {
    "id": 26,
    "num": "026",
    "name": "Raichu",
    "img": "http://www.serebii.net/pokemongo/pokemon/026.png",
    "type": ["Electric"],
    "height": "0.79 m",
    "weight": "30.0 kg",
    "weaknesses": ["Ground"],
    "prev_evolution": [
        {
        "num": "025",
        "name": "Pikachu"
        }
    ]
    },
    {
    "id": 27,
    "num": "027",
    "name": "Sandshrew",
    "img": "http://www.serebii.net/pokemongo/pokemon/027.png",
    "type": ["Ground"],
    "height": "0.61 m",
    "weight": "12.0 kg",
    "weaknesses": ["Water", "Grass", "Ice"],
    "next_evolution": [
        {
        "num": "028",
        "name": "Sandslash"
        }
    ]
    },
    {
    "id": 28,
    "num": "028",
    "name": "Sandslash",
    "img": "http://www.serebii.net/pokemongo/pokemon/028.png",
    "type": ["Ground"],
    "height": "0.99 m",
    "weight": "29.5 kg",
    "weaknesses": ["Water", "Grass", "Ice"],
    "prev_evolution": [
        {
        "num": "027",
        "name": "Sandshrew"
        }
    ]
    },
    {
    "id": 29,
    "num": "029",
    "name": "Nidoran ♀ (Female)",
    "img": "http://www.serebii.net/pokemongo/pokemon/029.png",
    "type": ["Poison"],
    "height": "0.41 m",
    "weight": "7.0 kg",
    "weaknesses": ["Ground", "Psychic"],
    "next_evolution": [
        {
        "num": "030",
        "name": "Nidorina"
        },
        {
        "num": "031",
        "name": "Nidoqueen"
        }
    ]
    },
    {
    "id": 30,
    "num": "030",
    "name": "Nidorina",
    "img": "http://www.serebii.net/pokemongo/pokemon/030.png",
    "type": ["Poison"],
    "height": "0.79 m",
    "weight": "20.0 kg",
    "weaknesses": ["Ground", "Psychic"],
    "prev_evolution": [
        {
        "num": "029",
        "name": "Nidoran(Female)"
        }
    ],
    "next_evolution": [
        {
        "num": "031",
        "name": "Nidoqueen"
        }
    ]
    },
    {
    "id": 31,
    "num": "031",
    "name": "Nidoqueen",
    "img": "http://www.serebii.net/pokemongo/pokemon/031.png",
    "type": ["Poison", "Ground"],
    "height": "1.30 m",
    "weight": "60.0 kg",
    "weaknesses": ["Water", "Ice", "Ground", "Psychic"],
    "prev_evolution": [
        {
        "num": "029",
        "name": "Nidoran(Female)"
        },
        {
        "num": "030",
        "name": "Nidorina"
        }
    ]
    },
    {
    "id": 32,
    "num": "032",
    "name": "Nidoran ♂ (Male)",
    "img": "http://www.serebii.net/pokemongo/pokemon/032.png",
    "type": ["Poison"],
    "height": "0.51 m",
    "weight": "9.0 kg",
    "weaknesses": ["Ground", "Psychic"],
    "next_evolution": [
        {
        "num": "033",
        "name": "Nidorino"
        },
        {
        "num": "034",
        "name": "Nidoking"
        }
    ]
    },
    {
    "id": 33,
    "num": "033",
    "name": "Nidorino",
    "img": "http://www.serebii.net/pokemongo/pokemon/033.png",
    "type": ["Poison"],
    "height": "0.89 m",
    "weight": "19.5 kg",
    "weaknesses": ["Ground", "Psychic"],
    "prev_evolution": [
        {
        "num": "032",
        "name": "Nidoran(Male)"
        }
    ],
    "next_evolution": [
        {
        "num": "034",
        "name": "Nidoking"
        }
    ]
    },
    {
    "id": 34,
    "num": "034",
    "name": "Nidoking",
    "img": "http://www.serebii.net/pokemongo/pokemon/034.png",
    "type": ["Poison", "Ground"],
    "height": "1.40 m",
    "weight": "62.0 kg",
    "weaknesses": ["Water", "Ice", "Ground", "Psychic"],
    "prev_evolution": [
        {
        "num": "032",
        "name": "Nidoran(Male)"
        },
        {
        "num": "033",
        "name": "Nidorino"
        }
    ]
    },
    {
    "id": 35,
    "num": "035",
    "name": "Clefairy",
    "img": "http://www.serebii.net/pokemongo/pokemon/035.png",
    "type": ["Normal"],
    "height": "0.61 m",
    "weight": "7.5 kg",
    "weaknesses": ["Fighting"],
    "next_evolution": [
        {
        "num": "036",
        "name": "Clefable"
        }
    ]
    },
    {
    "id": 36,
    "num": "036",
    "name": "Clefable",
    "img": "http://www.serebii.net/pokemongo/pokemon/036.png",
    "type": ["Normal"],
    "height": "1.30 m",
    "weight": "40.0 kg",
    "weaknesses": ["Fighting"],
    "prev_evolution": [
        {
        "num": "035",
        "name": "Clefairy"
        }
    ]
    },
    {
    "id": 37,
    "num": "037",
    "name": "Vulpix",
    "img": "http://www.serebii.net/pokemongo/pokemon/037.png",
    "type": ["Fire"],
    "height": "0.61 m",
    "weight": "9.9 kg",
    "weaknesses": ["Water", "Ground", "Rock"],
    "next_evolution": [
        {
        "num": "038",
        "name": "Ninetales"
        }
    ]
    },
    {
    "id": 38,
    "num": "038",
    "name": "Ninetales",
    "img": "http://www.serebii.net/pokemongo/pokemon/038.png",
    "type": ["Fire"],
    "height": "1.09 m",
    "weight": "19.9 kg",
    "weaknesses": ["Water", "Ground", "Rock"],
    "prev_evolution": [
        {
        "num": "037",
        "name": "Vulpix"
        }
    ]
    },
    {
    "id": 39,
    "num": "039",
    "name": "Jigglypuff",
    "img": "http://www.serebii.net/pokemongo/pokemon/039.png",
    "type": ["Normal"],
    "height": "0.51 m",
    "weight": "5.5 kg",
    "weaknesses": ["Fighting"],
    "next_evolution": [
        {
        "num": "040",
        "name": "Wigglytuff"
        }
    ]
    },
    {
    "id": 40,
    "num": "040",
    "name": "Wigglytuff",
    "img": "http://www.serebii.net/pokemongo/pokemon/040.png",
    "type": ["Normal"],
    "height": "0.99 m",
    "weight": "12.0 kg",
    "weaknesses": ["Fighting"],
    "prev_evolution": [
        {
        "num": "039",
        "name": "Jigglypuff"
        }
    ]
    },
    {
    "id": 41,
    "num": "041",
    "name": "Zubat",
    "img": "http://www.serebii.net/pokemongo/pokemon/041.png",
    "type": ["Poison", "Flying"],
    "height": "0.79 m",
    "weight": "7.5 kg",
    "weaknesses": ["Electric", "Ice", "Psychic", "Rock"],
    "next_evolution": [
        {
        "num": "042",
        "name": "Golbat"
        }
    ]
    },
    {
    "id": 42,
    "num": "042",
    "name": "Golbat",
    "img": "http://www.serebii.net/pokemongo/pokemon/042.png",
    "type": ["Poison", "Flying"],
    "height": "1.60 m",
    "weight": "55.0 kg",
    "weaknesses": ["Electric", "Ice", "Psychic", "Rock"],
    "prev_evolution": [
        {
        "num": "041",
        "name": "Zubat"
        }
    ]
    },
    {
    "id": 43,
    "num": "043",
    "name": "Oddish",
    "img": "http://www.serebii.net/pokemongo/pokemon/043.png",
    "type": ["Grass", "Poison"],
    "height": "0.51 m",
    "weight": "5.4 kg",
    "weaknesses": ["Fire", "Ice", "Flying", "Psychic"],
    "next_evolution": [
        {
        "num": "044",
        "name": "Gloom"
        },
        {
        "num": "045",
        "name": "Vileplume"
        }
    ]
    },
    {
    "id": 44,
    "num": "044",
    "name": "Gloom",
    "img": "http://www.serebii.net/pokemongo/pokemon/044.png",
    "type": ["Grass", "Poison"],
    "height": "0.79 m",
    "weight": "8.6 kg",
    "weaknesses": ["Fire", "Ice", "Flying", "Psychic"],
    "prev_evolution": [
        {
        "num": "043",
        "name": "Oddish"
        }
    ],
    "next_evolution": [
        {
        "num": "045",
        "name": "Vileplume"
        }
    ]
    },
    {
    "id": 45,
    "num": "045",
    "name": "Vileplume",
    "img": "http://www.serebii.net/pokemongo/pokemon/045.png",
    "type": ["Grass", "Poison"],
    "height": "1.19 m",
    "weight": "18.6 kg",
    "weaknesses": ["Fire", "Ice", "Flying", "Psychic"],
    "prev_evolution": [
        {
        "num": "043",
        "name": "Oddish"
        },
        {
        "num": "044",
        "name": "Gloom"
        }
    ]
    },
    {
    "id": 46,
    "num": "046",
    "name": "Paras",
    "img": "http://www.serebii.net/pokemongo/pokemon/046.png",
    "type": ["Bug", "Grass"],
    "height": "0.30 m",
    "weight": "5.4 kg",
    "weaknesses": ["Fire", "Ice", "Poison", "Flying", "Bug", "Rock"],
    "next_evolution": [
        {
        "num": "047",
        "name": "Parasect"
        }
    ]
    },
    {
    "id": 47,
    "num": "047",
    "name": "Parasect",
    "img": "http://www.serebii.net/pokemongo/pokemon/047.png",
    "type": ["Bug", "Grass"],
    "height": "0.99 m",
    "weight": "29.5 kg",
    "weaknesses": ["Fire", "Ice", "Poison", "Flying", "Bug", "Rock"],
    "prev_evolution": [
        {
        "num": "046",
        "name": "Paras"
        }
    ]
    },
    {
    "id": 48,
    "num": "048",
    "name": "Venonat",
    "img": "http://www.serebii.net/pokemongo/pokemon/048.png",
    "type": ["Bug", "Poison"],
    "height": "0.99 m",
    "weight": "30.0 kg",
    "weaknesses": ["Fire", "Flying", "Psychic", "Rock"],
    "next_evolution": [
        {
        "num": "049",
        "name": "Venomoth"
        }
    ]
    },
    {
    "id": 49,
    "num": "049",
    "name": "Venomoth",
    "img": "http://www.serebii.net/pokemongo/pokemon/049.png",
    "type": ["Bug", "Poison"],
    "height": "1.50 m",
    "weight": "12.5 kg",
    "weaknesses": ["Fire", "Flying", "Psychic", "Rock"],
    "prev_evolution": [
        {
        "num": "048",
        "name": "Venonat"
        }
    ]
    },
    {
    "id": 50,
    "num": "050",
    "name": "Diglett",
    "img": "http://www.serebii.net/pokemongo/pokemon/050.png",
    "type": ["Ground"],
    "height": "0.20 m",
    "weight": "0.8 kg",
    "weaknesses": ["Water", "Grass", "Ice"],
    "next_evolution": [
        {
        "num": "051",
        "name": "Dugtrio"
        }
    ]
    },
    {
    "id": 51,
    "num": "051",
    "name": "Dugtrio",
    "img": "http://www.serebii.net/pokemongo/pokemon/051.png",
    "type": ["Ground"],
    "height": "0.71 m",
    "weight": "33.3 kg",
    "weaknesses": ["Water", "Grass", "Ice"],
    "prev_evolution": [
        {
        "num": "050",
        "name": "Diglett"
        }
    ]
    },
    {
    "id": 52,
    "num": "052",
    "name": "Meowth",
    "img": "http://www.serebii.net/pokemongo/pokemon/052.png",
    "type": ["Normal"],
    "height": "0.41 m",
    "weight": "4.2 kg",
    "weaknesses": ["Fighting"],
    "next_evolution": [
        {
        "num": "053",
        "name": "Persian"
        }
    ]
    },
    {
    "id": 53,
    "num": "053",
    "name": "Persian",
    "img": "http://www.serebii.net/pokemongo/pokemon/053.png",
    "type": ["Normal"],
    "height": "0.99 m",
    "weight": "32.0 kg",
    "weaknesses": ["Fighting"],
    "prev_evolution": [
        {
        "num": "052",
        "name": "Meowth"
        }
    ]
    },
    {
    "id": 54,
    "num": "054",
    "name": "Psyduck",
    "img": "http://www.serebii.net/pokemongo/pokemon/054.png",
    "type": ["Water"],
    "height": "0.79 m",
    "weight": "19.6 kg",
    "weaknesses": ["Electric", "Grass"],
    "next_evolution": [
        {
        "num": "055",
        "name": "Golduck"
        }
    ]
    },
    {
    "id": 55,
    "num": "055",
    "name": "Golduck",
    "img": "http://www.serebii.net/pokemongo/pokemon/055.png",
    "type": ["Water"],
    "height": "1.70 m",
    "weight": "76.6 kg",
    "weaknesses": ["Electric", "Grass"],
    "prev_evolution": [
        {
        "num": "054",
        "name": "Psyduck"
        }
    ]
    },
    {
    "id": 56,
    "num": "056",
    "name": "Mankey",
    "img": "http://www.serebii.net/pokemongo/pokemon/056.png",
    "type": ["Fighting"],
    "height": "0.51 m",
    "weight": "28.0 kg",
    "weaknesses": ["Flying", "Psychic", "Fairy"],
    "next_evolution": [
        {
        "num": "057",
        "name": "Primeape"
        }
    ]
    },
    {
    "id": 57,
    "num": "057",
    "name": "Primeape",
    "img": "http://www.serebii.net/pokemongo/pokemon/057.png",
    "type": ["Fighting"],
    "height": "0.99 m",
    "weight": "32.0 kg",
    "weaknesses": ["Flying", "Psychic", "Fairy"],
    "prev_evolution": [
        {
        "num": "056",
        "name": "Mankey"
        }
    ]
    },
    {
    "id": 58,
    "num": "058",
    "name": "Growlithe",
    "img": "http://www.serebii.net/pokemongo/pokemon/058.png",
    "type": ["Fire"],
    "height": "0.71 m",
    "weight": "19.0 kg",
    "weaknesses": ["Water", "Ground", "Rock"],
    "next_evolution": [
        {
        "num": "059",
        "name": "Arcanine"
        }
    ]
    },
    {
    "id": 59,
    "num": "059",
    "name": "Arcanine",
    "img": "http://www.serebii.net/pokemongo/pokemon/059.png",
    "type": ["Fire"],
    "height": "1.91 m",
    "weight": "155.0 kg",
    "weaknesses": ["Water", "Ground", "Rock"],
    "prev_evolution": [
        {
        "num": "058",
        "name": "Growlithe"
        }
    ]
    },
    {
    "id": 60,
    "num": "060",
    "name": "Poliwag",
    "img": "http://www.serebii.net/pokemongo/pokemon/060.png",
    "type": ["Water"],
    "height": "0.61 m",
    "weight": "12.4 kg",
    "weaknesses": ["Electric", "Grass"],
    "next_evolution": [
        {
        "num": "061",
        "name": "Poliwhirl"
        },
        {
        "num": "062",
        "name": "Poliwrath"
        }
    ]
    },
    {
    "id": 61,
    "num": "061",
    "name": "Poliwhirl",
    "img": "http://www.serebii.net/pokemongo/pokemon/061.png",
    "type": ["Water"],
    "height": "0.99 m",
    "weight": "20.0 kg",
    "weaknesses": ["Electric", "Grass"],
    "prev_evolution": [
        {
        "num": "060",
        "name": "Poliwag"
        }
    ],
    "next_evolution": [
        {
        "num": "062",
        "name": "Poliwrath"
        }
    ]
    },
    {
    "id": 62,
    "num": "062",
    "name": "Poliwrath",
    "img": "http://www.serebii.net/pokemongo/pokemon/062.png",
    "type": ["Water", "Fighting"],
    "height": "1.30 m",
    "weight": "54.0 kg",
    "weaknesses": ["Electric", "Grass", "Flying", "Psychic", "Fairy"],
    "prev_evolution": [
        {
        "num": "060",
        "name": "Poliwag"
        },
        {
        "num": "061",
        "name": "Poliwhirl"
        }
    ]
    },
    {
    "id": 63,
    "num": "063",
    "name": "Abra",
    "img": "http://www.serebii.net/pokemongo/pokemon/063.png",
    "type": ["Psychic"],
    "height": "0.89 m",
    "weight": "19.5 kg",
    "weaknesses": ["Bug", "Ghost", "Dark"],
    "next_evolution": [
        {
        "num": "064",
        "name": "Kadabra"
        },
        {
        "num": "065",
        "name": "Alakazam"
        }
    ]
    },
    {
    "id": 64,
    "num": "064",
    "name": "Kadabra",
    "img": "http://www.serebii.net/pokemongo/pokemon/064.png",
    "type": ["Psychic"],
    "height": "1.30 m",
    "weight": "56.5 kg",
    "weaknesses": ["Bug", "Ghost", "Dark"],
    "prev_evolution": [
        {
        "num": "063",
        "name": "Abra"
        }
    ],
    "next_evolution": [
        {
        "num": "065",
        "name": "Alakazam"
        }
    ]
    },
    {
    "id": 65,
    "num": "065",
    "name": "Alakazam",
    "img": "http://www.serebii.net/pokemongo/pokemon/065.png",
    "type": ["Psychic"],
    "height": "1.50 m",
    "weight": "48.0 kg",
    "weaknesses": ["Bug", "Ghost", "Dark"],
    "prev_evolution": [
        {
        "num": "063",
        "name": "Abra"
        },
        {
        "num": "064",
        "name": "Kadabra"
        }
    ]
    },
    {
    "id": 66,
    "num": "066",
    "name": "Machop",
    "img": "http://www.serebii.net/pokemongo/pokemon/066.png",
    "type": ["Fighting"],
    "height": "0.79 m",
    "weight": "19.5 kg",
    "weaknesses": ["Flying", "Psychic", "Fairy"],
    "next_evolution": [
        {
        "num": "067",
        "name": "Machoke"
        },
        {
        "num": "068",
        "name": "Machamp"
        }
    ]
    },
    {
    "id": 67,
    "num": "067",
    "name": "Machoke",
    "img": "http://www.serebii.net/pokemongo/pokemon/067.png",
    "type": ["Fighting"],
    "height": "1.50 m",
    "weight": "70.5 kg",
    "weaknesses": ["Flying", "Psychic", "Fairy"],
    "prev_evolution": [
        {
        "num": "066",
        "name": "Machop"
        }
    ],
    "next_evolution": [
        {
        "num": "068",
        "name": "Machamp"
        }
    ]
    },
    {
    "id": 68,
    "num": "068",
    "name": "Machamp",
    "img": "http://www.serebii.net/pokemongo/pokemon/068.png",
    "type": ["Fighting"],
    "height": "1.60 m",
    "weight": "130.0 kg",
    "weaknesses": ["Flying", "Psychic", "Fairy"],
    "prev_evolution": [
        {
        "num": "066",
        "name": "Machop"
        },
        {
        "num": "067",
        "name": "Machoke"
        }
    ]
    },
    {
    "id": 69,
    "num": "069",
    "name": "Bellsprout",
    "img": "http://www.serebii.net/pokemongo/pokemon/069.png",
    "type": ["Grass", "Poison"],
    "height": "0.71 m",
    "weight": "4.0 kg",
    "weaknesses": ["Fire", "Ice", "Flying", "Psychic"],
    "next_evolution": [
        {
        "num": "070",
        "name": "Weepinbell"
        },
        {
        "num": "071",
        "name": "Victreebel"
        }
    ]
    },
    {
    "id": 70,
    "num": "070",
    "name": "Weepinbell",
    "img": "http://www.serebii.net/pokemongo/pokemon/070.png",
    "type": ["Grass", "Poison"],
    "height": "0.99 m",
    "weight": "6.4 kg",
    "weaknesses": ["Fire", "Ice", "Flying", "Psychic"],
    "prev_evolution": [
        {
        "num": "069",
        "name": "Bellsprout"
        }
    ],
    "next_evolution": [
        {
        "num": "071",
        "name": "Victreebel"
        }
    ]
    },
    {
    "id": 71,
    "num": "071",
    "name": "Victreebel",
    "img": "http://www.serebii.net/pokemongo/pokemon/071.png",
    "type": ["Grass", "Poison"],
    "height": "1.70 m",
    "weight": "15.5 kg",
    "weaknesses": ["Fire", "Ice", "Flying", "Psychic"],
    "prev_evolution": [
        {
        "num": "069",
        "name": "Bellsprout"
        },
        {
        "num": "070",
        "name": "Weepinbell"
        }
    ]
    },
    {
    "id": 72,
    "num": "072",
    "name": "Tentacool",
    "img": "http://www.serebii.net/pokemongo/pokemon/072.png",
    "type": ["Water", "Poison"],
    "height": "0.89 m",
    "weight": "45.5 kg",
    "weaknesses": ["Electric", "Ground", "Psychic"],
    "next_evolution": [
        {
        "num": "073",
        "name": "Tentacruel"
        }
    ]
    },
    {
    "id": 73,
    "num": "073",
    "name": "Tentacruel",
    "img": "http://www.serebii.net/pokemongo/pokemon/073.png",
    "type": ["Water", "Poison"],
    "height": "1.60 m",
    "weight": "55.0 kg",
    "weaknesses": ["Electric", "Ground", "Psychic"],
    "prev_evolution": [
        {
        "num": "072",
        "name": "Tentacool"
        }
    ]
    },
    {
    "id": 74,
    "num": "074",
    "name": "Geodude",
    "img": "http://www.serebii.net/pokemongo/pokemon/074.png",
    "type": ["Rock", "Ground"],
    "height": "0.41 m",
    "weight": "20.0 kg",
    "weaknesses": ["Water", "Grass", "Ice", "Fighting", "Ground", "Steel"],
    "next_evolution": [
        {
        "num": "075",
        "name": "Graveler"
        },
        {
        "num": "076",
        "name": "Golem"
        }
    ]
    },
    {
    "id": 75,
    "num": "075",
    "name": "Graveler",
    "img": "http://www.serebii.net/pokemongo/pokemon/075.png",
    "type": ["Rock", "Ground"],
    "height": "0.99 m",
    "weight": "105.0 kg",
    "weaknesses": ["Water", "Grass", "Ice", "Fighting", "Ground", "Steel"],
    "prev_evolution": [
        {
        "num": "074",
        "name": "Geodude"
        }
    ],
    "next_evolution": [
        {
        "num": "076",
        "name": "Golem"
        }
    ]
    },
    {
    "id": 76,
    "num": "076",
    "name": "Golem",
    "img": "http://www.serebii.net/pokemongo/pokemon/076.png",
    "type": ["Rock", "Ground"],
    "height": "1.40 m",
    "weight": "300.0 kg",
    "weaknesses": ["Water", "Grass", "Ice", "Fighting", "Ground", "Steel"],
    "prev_evolution": [
        {
        "num": "074",
        "name": "Geodude"
        },
        {
        "num": "075",
        "name": "Graveler"
        }
    ]
    },
    {
    "id": 77,
    "num": "077",
    "name": "Ponyta",
    "img": "http://www.serebii.net/pokemongo/pokemon/077.png",
    "type": ["Fire"],
    "height": "0.99 m",
    "weight": "30.0 kg",
    "weaknesses": ["Water", "Ground", "Rock"],
    "next_evolution": [
        {
        "num": "078",
        "name": "Rapidash"
        }
    ]
    },
    {
    "id": 78,
    "num": "078",
    "name": "Rapidash",
    "img": "http://www.serebii.net/pokemongo/pokemon/078.png",
    "type": ["Fire"],
    "height": "1.70 m",
    "weight": "95.0 kg",
    "weaknesses": ["Water", "Ground", "Rock"],
    "prev_evolution": [
        {
        "num": "077",
        "name": "Ponyta"
        }
    ]
    },
    {
    "id": 79,
    "num": "079",
    "name": "Slowpoke",
    "img": "http://www.serebii.net/pokemongo/pokemon/079.png",
    "type": ["Water", "Psychic"],
    "height": "1.19 m",
    "weight": "36.0 kg",
    "weaknesses": ["Electric", "Grass", "Bug", "Ghost", "Dark"],
    "next_evolution": [
        {
        "num": "080",
        "name": "Slowbro"
        }
    ]
    },
    {
    "id": 80,
    "num": "080",
    "name": "Slowbro",
    "img": "http://www.serebii.net/pokemongo/pokemon/080.png",
    "type": ["Water", "Psychic"],
    "height": "1.60 m",
    "weight": "78.5 kg",
    "weaknesses": ["Electric", "Grass", "Bug", "Ghost", "Dark"],
    "prev_evolution": [
        {
        "num": "079",
        "name": "Slowpoke"
        }
    ]
    },
    {
    "id": 81,
    "num": "081",
    "name": "Magnemite",
    "img": "http://www.serebii.net/pokemongo/pokemon/081.png",
    "type": ["Electric"],
    "height": "0.30 m",
    "weight": "6.0 kg",
    "weaknesses": ["Fire", "Water", "Ground"],
    "next_evolution": [
        {
        "num": "082",
        "name": "Magneton"
        }
    ]
    },
    {
    "id": 82,
    "num": "082",
    "name": "Magneton",
    "img": "http://www.serebii.net/pokemongo/pokemon/082.png",
    "type": ["Electric"],
    "height": "0.99 m",
    "weight": "60.0 kg",
    "weaknesses": ["Fire", "Water", "Ground"],
    "prev_evolution": [
        {
        "num": "081",
        "name": "Magnemite"
        }
    ]
    },
    {
    "id": 83,
    "num": "083",
    "name": "Farfetch'd",
    "img": "http://www.serebii.net/pokemongo/pokemon/083.png",
    "type": ["Normal", "Flying"],
    "height": "0.79 m",
    "weight": "15.0 kg",
    "weaknesses": ["Electric", "Rock"]
    },
    {
    "id": 84,
    "num": "084",
    "name": "Doduo",
    "img": "http://www.serebii.net/pokemongo/pokemon/084.png",
    "type": ["Normal", "Flying"],
    "height": "1.40 m",
    "weight": "39.2 kg",
    "weaknesses": ["Electric", "Rock"],
    "next_evolution": [
        {
        "num": "085",
        "name": "Dodrio"
        }
    ]
    },
    {
    "id": 85,
    "num": "085",
    "name": "Dodrio",
    "img": "http://www.serebii.net/pokemongo/pokemon/085.png",
    "type": ["Normal", "Flying"],
    "height": "1.80 m",
    "weight": "85.2 kg",
    "weaknesses": ["Electric", "Rock"],
    "prev_evolution": [
        {
        "num": "084",
        "name": "Doduo"
        }
    ]
    },
    {
    "id": 86,
    "num": "086",
    "name": "Seel",
    "img": "http://www.serebii.net/pokemongo/pokemon/086.png",
    "type": ["Water"],
    "height": "1.09 m",
    "weight": "90.0 kg",
    "weaknesses": ["Electric", "Grass"],
    "next_evolution": [
        {
        "num": "087",
        "name": "Dewgong"
        }
    ]
    },
    {
    "id": 87,
    "num": "087",
    "name": "Dewgong",
    "img": "http://www.serebii.net/pokemongo/pokemon/087.png",
    "type": ["Water", "Ice"],
    "height": "1.70 m",
    "weight": "120.0 kg",
    "weaknesses": ["Electric", "Grass", "Fighting", "Rock"],
    "prev_evolution": [
        {
        "num": "086",
        "name": "Seel"
        }
    ]
    },
    {
    "id": 88,
    "num": "088",
    "name": "Grimer",
    "img": "http://www.serebii.net/pokemongo/pokemon/088.png",
    "type": ["Poison"],
    "height": "0.89 m",
    "weight": "30.0 kg",
    "weaknesses": ["Ground", "Psychic"],
    "next_evolution": [
        {
        "num": "089",
        "name": "Muk"
        }
    ]
    },
    {
    "id": 89,
    "num": "089",
    "name": "Muk",
    "img": "http://www.serebii.net/pokemongo/pokemon/089.png",
    "type": ["Poison"],
    "height": "1.19 m",
    "weight": "30.0 kg",
    "weaknesses": ["Ground", "Psychic"],
    "prev_evolution": [
        {
        "num": "088",
        "name": "Grimer"
        }
    ]
    },
    {
    "id": 90,
    "num": "090",
    "name": "Shellder",
    "img": "http://www.serebii.net/pokemongo/pokemon/090.png",
    "type": ["Water"],
    "height": "0.30 m",
    "weight": "4.0 kg",
    "weaknesses": ["Electric", "Grass"],
    "next_evolution": [
        {
        "num": "091",
        "name": "Cloyster"
        }
    ]
    },
    {
    "id": 91,
    "num": "091",
    "name": "Cloyster",
    "img": "http://www.serebii.net/pokemongo/pokemon/091.png",
    "type": ["Water", "Ice"],
    "height": "1.50 m",
    "weight": "132.5 kg",
    "weaknesses": ["Electric", "Grass", "Fighting", "Rock"],
    "prev_evolution": [
        {
        "num": "090",
        "name": "Shellder"
        }
    ]
    },
    {
    "id": 92,
    "num": "092",
    "name": "Gastly",
    "img": "http://www.serebii.net/pokemongo/pokemon/092.png",
    "type": ["Ghost", "Poison"],
    "height": "1.30 m",
    "weight": "0.1 kg",
    "weaknesses": ["Ground", "Psychic", "Ghost", "Dark"],
    "next_evolution": [
        {
        "num": "093",
        "name": "Haunter"
        },
        {
        "num": "094",
        "name": "Gengar"
        }
    ]
    },
    {
    "id": 93,
    "num": "093",
    "name": "Haunter",
    "img": "http://www.serebii.net/pokemongo/pokemon/093.png",
    "type": ["Ghost", "Poison"],
    "height": "1.60 m",
    "weight": "0.1 kg",
    "weaknesses": ["Ground", "Psychic", "Ghost", "Dark"],
    "prev_evolution": [
        {
        "num": "092",
        "name": "Gastly"
        }
    ],
    "next_evolution": [
        {
        "num": "094",
        "name": "Gengar"
        }
    ]
    },
    {
    "id": 94,
    "num": "094",
    "name": "Gengar",
    "img": "http://www.serebii.net/pokemongo/pokemon/094.png",
    "type": ["Ghost", "Poison"],
    "height": "1.50 m",
    "weight": "40.5 kg",
    "weaknesses": ["Ground", "Psychic", "Ghost", "Dark"],
    "prev_evolution": [
        {
        "num": "092",
        "name": "Gastly"
        },
        {
        "num": "093",
        "name": "Haunter"
        }
    ]
    },
    {
    "id": 95,
    "num": "095",
    "name": "Onix",
    "img": "http://www.serebii.net/pokemongo/pokemon/095.png",
    "type": ["Rock", "Ground"],
    "height": "8.79 m",
    "weight": "210.0 kg",
    "weaknesses": ["Water", "Grass", "Ice", "Fighting", "Ground", "Steel"]
    },
    {
    "id": 96,
    "num": "096",
    "name": "Drowzee",
    "img": "http://www.serebii.net/pokemongo/pokemon/096.png",
    "type": ["Psychic"],
    "height": "0.99 m",
    "weight": "32.4 kg",
    "weaknesses": ["Bug", "Ghost", "Dark"],
    "next_evolution": [
        {
        "num": "097",
        "name": "Hypno"
        }
    ]
    },
    {
    "id": 97,
    "num": "097",
    "name": "Hypno",
    "img": "http://www.serebii.net/pokemongo/pokemon/097.png",
    "type": ["Psychic"],
    "height": "1.60 m",
    "weight": "75.6 kg",
    "weaknesses": ["Bug", "Ghost", "Dark"],
    "prev_evolution": [
        {
        "num": "096",
        "name": "Drowzee"
        }
    ]
    },
    {
    "id": 98,
    "num": "098",
    "name": "Krabby",
    "img": "http://www.serebii.net/pokemongo/pokemon/098.png",
    "type": ["Water"],
    "height": "0.41 m",
    "weight": "6.5 kg",
    "weaknesses": ["Electric", "Grass"],
    "next_evolution": [
        {
        "num": "099",
        "name": "Kingler"
        }
    ]
    },
    {
    "id": 99,
    "num": "099",
    "name": "Kingler",
    "img": "http://www.serebii.net/pokemongo/pokemon/099.png",
    "type": ["Water"],
    "height": "1.30 m",
    "weight": "60.0 kg",
    "weaknesses": ["Electric", "Grass"],
    "prev_evolution": [
        {
        "num": "098",
        "name": "Krabby"
        }
    ]
    },
    {
    "id": 100,
    "num": "100",
    "name": "Voltorb",
    "img": "http://www.serebii.net/pokemongo/pokemon/100.png",
    "type": ["Electric"],
    "height": "0.51 m",
    "weight": "10.4 kg",
    "weaknesses": ["Ground"],
    "next_evolution": [
        {
        "num": "101",
        "name": "Electrode"
        }
    ]
    },
    {
    "id": 101,
    "num": "101",
    "name": "Electrode",
    "img": "http://www.serebii.net/pokemongo/pokemon/101.png",
    "type": ["Electric"],
    "height": "1.19 m",
    "weight": "66.6 kg",
    "weaknesses": ["Ground"],
    "prev_evolution": [
        {
        "num": "100",
        "name": "Voltorb"
        }
    ]
    },
    {
    "id": 102,
    "num": "102",
    "name": "Exeggcute",
    "img": "http://www.serebii.net/pokemongo/pokemon/102.png",
    "type": ["Grass", "Psychic"],
    "height": "0.41 m",
    "weight": "2.5 kg",
    "weaknesses": ["Fire", "Ice", "Poison", "Flying", "Bug", "Ghost", "Dark"],
    "next_evolution": [
        {
        "num": "103",
        "name": "Exeggutor"
        }
    ]
    },
    {
    "id": 103,
    "num": "103",
    "name": "Exeggutor",
    "img": "http://www.serebii.net/pokemongo/pokemon/103.png",
    "type": ["Grass", "Psychic"],
    "height": "2.01 m",
    "weight": "120.0 kg",
    "weaknesses": ["Fire", "Ice", "Poison", "Flying", "Bug", "Ghost", "Dark"],
    "prev_evolution": [
        {
        "num": "102",
        "name": "Exeggcute"
        }
    ]
    },
    {
    "id": 104,
    "num": "104",
    "name": "Cubone",
    "img": "http://www.serebii.net/pokemongo/pokemon/104.png",
    "type": ["Ground"],
    "height": "0.41 m",
    "weight": "6.5 kg",
    "weaknesses": ["Water", "Grass", "Ice"],
    "next_evolution": [
        {
        "num": "105",
        "name": "Marowak"
        }
    ]
    },
    {
    "id": 105,
    "num": "105",
    "name": "Marowak",
    "img": "http://www.serebii.net/pokemongo/pokemon/105.png",
    "type": ["Ground"],
    "height": "0.99 m",
    "weight": "45.0 kg",
    "weaknesses": ["Water", "Grass", "Ice"],
    "prev_evolution": [
        {
        "num": "104",
        "name": "Cubone"
        }
    ]
    },
    {
    "id": 106,
    "num": "106",
    "name": "Hitmonlee",
    "img": "http://www.serebii.net/pokemongo/pokemon/106.png",
    "type": ["Fighting"],
    "height": "1.50 m",
    "weight": "49.8 kg",
    "weaknesses": ["Flying", "Psychic", "Fairy"]
    },
    {
    "id": 107,
    "num": "107",
    "name": "Hitmonchan",
    "img": "http://www.serebii.net/pokemongo/pokemon/107.png",
    "type": ["Fighting"],
    "height": "1.40 m",
    "weight": "50.2 kg",
    "weaknesses": ["Flying", "Psychic", "Fairy"]
    },
    {
    "id": 108,
    "num": "108",
    "name": "Lickitung",
    "img": "http://www.serebii.net/pokemongo/pokemon/108.png",
    "type": ["Normal"],
    "height": "1.19 m",
    "weight": "65.5 kg",
    "weaknesses": ["Fighting"]
    },
    {
    "id": 109,
    "num": "109",
    "name": "Koffing",
    "img": "http://www.serebii.net/pokemongo/pokemon/109.png",
    "type": ["Poison"],
    "height": "0.61 m",
    "weight": "1.0 kg",
    "weaknesses": ["Ground", "Psychic"],
    "next_evolution": [
        {
        "num": "110",
        "name": "Weezing"
        }
    ]
    },
    {
    "id": 110,
    "num": "110",
    "name": "Weezing",
    "img": "http://www.serebii.net/pokemongo/pokemon/110.png",
    "type": ["Poison"],
    "height": "1.19 m",
    "weight": "9.5 kg",
    "weaknesses": ["Ground", "Psychic"],
    "prev_evolution": [
        {
        "num": "109",
        "name": "Koffing"
        }
    ]
    },
    {
    "id": 111,
    "num": "111",
    "name": "Rhyhorn",
    "img": "http://www.serebii.net/pokemongo/pokemon/111.png",
    "type": ["Ground", "Rock"],
    "height": "0.99 m",
    "weight": "115.0 kg",
    "weaknesses": ["Water", "Grass", "Ice", "Fighting", "Ground", "Steel"],
    "next_evolution": [
        {
        "num": "112",
        "name": "Rhydon"
        }
    ]
    },
    {
    "id": 112,
    "num": "112",
    "name": "Rhydon",
    "img": "http://www.serebii.net/pokemongo/pokemon/112.png",
    "type": ["Ground", "Rock"],
    "height": "1.91 m",
    "weight": "120.0 kg",
    "weaknesses": ["Water", "Grass", "Ice", "Fighting", "Ground", "Steel"],
    "prev_evolution": [
        {
        "num": "111",
        "name": "Rhyhorn"
        }
    ]
    },
    {
    "id": 113,
    "num": "113",
    "name": "Chansey",
    "img": "http://www.serebii.net/pokemongo/pokemon/113.png",
    "type": ["Normal"],
    "height": "1.09 m",
    "weight": "34.6 kg",
    "weaknesses": ["Fighting"]
    },
    {
    "id": 114,
    "num": "114",
    "name": "Tangela",
    "img": "http://www.serebii.net/pokemongo/pokemon/114.png",
    "type": ["Grass"],
    "height": "0.99 m",
    "weight": "35.0 kg",
    "weaknesses": ["Fire", "Ice", "Poison", "Flying", "Bug"]
    },
    {
    "id": 115,
    "num": "115",
    "name": "Kangaskhan",
    "img": "http://www.serebii.net/pokemongo/pokemon/115.png",
    "type": ["Normal"],
    "height": "2.21 m",
    "weight": "80.0 kg",
    "weaknesses": ["Fighting"]
    },
    {
    "id": 116,
    "num": "116",
    "name": "Horsea",
    "img": "http://www.serebii.net/pokemongo/pokemon/116.png",
    "type": ["Water"],
    "height": "0.41 m",
    "weight": "8.0 kg",
    "weaknesses": ["Electric", "Grass"],
    "next_evolution": [
        {
        "num": "117",
        "name": "Seadra"
        }
    ]
    },
    {
    "id": 117,
    "num": "117",
    "name": "Seadra",
    "img": "http://www.serebii.net/pokemongo/pokemon/117.png",
    "type": ["Water"],
    "height": "1.19 m",
    "weight": "25.0 kg",
    "weaknesses": ["Electric", "Grass"],
    "prev_evolution": [
        {
        "num": "116",
        "name": "Horsea"
        }
    ]
    },
    {
    "id": 118,
    "num": "118",
    "name": "Goldeen",
    "img": "http://www.serebii.net/pokemongo/pokemon/118.png",
    "type": ["Water"],
    "height": "0.61 m",
    "weight": "15.0 kg",
    "weaknesses": ["Electric", "Grass"],
    "next_evolution": [
        {
        "num": "119",
        "name": "Seaking"
        }
    ]
    },
    {
    "id": 119,
    "num": "119",
    "name": "Seaking",
    "img": "http://www.serebii.net/pokemongo/pokemon/119.png",
    "type": ["Water"],
    "height": "1.30 m",
    "weight": "39.0 kg",
    "weaknesses": ["Electric", "Grass"],
    "prev_evolution": [
        {
        "num": "118",
        "name": "Goldeen"
        }
    ]
    },
    {
    "id": 120,
    "num": "120",
    "name": "Staryu",
    "img": "http://www.serebii.net/pokemongo/pokemon/120.png",
    "type": ["Water"],
    "height": "0.79 m",
    "weight": "34.5 kg",
    "weaknesses": ["Electric", "Grass"],
    "next_evolution": [
        {
        "num": "121",
        "name": "Starmie"
        }
    ]
    },
    {
    "id": 121,
    "num": "121",
    "name": "Starmie",
    "img": "http://www.serebii.net/pokemongo/pokemon/121.png",
    "type": ["Water", "Psychic"],
    "height": "1.09 m",
    "weight": "80.0 kg",
    "weaknesses": ["Electric", "Grass", "Bug", "Ghost", "Dark"],
    "prev_evolution": [
        {
        "num": "120",
        "name": "Staryu"
        }
    ]
    },
    {
    "id": 122,
    "num": "122",
    "name": "Mr. Mime",
    "img": "http://www.serebii.net/pokemongo/pokemon/122.png",
    "type": ["Psychic"],
    "height": "1.30 m",
    "weight": "54.5 kg",
    "weaknesses": ["Bug", "Ghost", "Dark"]
    },
    {
    "id": 123,
    "num": "123",
    "name": "Scyther",
    "img": "http://www.serebii.net/pokemongo/pokemon/123.png",
    "type": ["Bug", "Flying"],
    "height": "1.50 m",
    "weight": "56.0 kg",
    "weaknesses": ["Fire", "Electric", "Ice", "Flying", "Rock"]
    },
    {
    "id": 124,
    "num": "124",
    "name": "Jynx",
    "img": "http://www.serebii.net/pokemongo/pokemon/124.png",
    "type": ["Ice", "Psychic"],
    "height": "1.40 m",
    "weight": "40.6 kg",
    "weaknesses": ["Fire", "Bug", "Rock", "Ghost", "Dark", "Steel"]
    },
    {
    "id": 125,
    "num": "125",
    "name": "Electabuzz",
    "img": "http://www.serebii.net/pokemongo/pokemon/125.png",
    "type": ["Electric"],
    "height": "1.09 m",
    "weight": "30.0 kg",
    "weaknesses": ["Ground"]
    },
    {
    "id": 126,
    "num": "126",
    "name": "Magmar",
    "img": "http://www.serebii.net/pokemongo/pokemon/126.png",
    "type": ["Fire"],
    "height": "1.30 m",
    "weight": "44.5 kg",
    "weaknesses": ["Water", "Ground", "Rock"]
    },
    {
    "id": 127,
    "num": "127",
    "name": "Pinsir",
    "img": "http://www.serebii.net/pokemongo/pokemon/127.png",
    "type": ["Bug"],
    "height": "1.50 m",
    "weight": "55.0 kg",
    "weaknesses": ["Fire", "Flying", "Rock"]
    },
    {
    "id": 128,
    "num": "128",
    "name": "Tauros",
    "img": "http://www.serebii.net/pokemongo/pokemon/128.png",
    "type": ["Normal"],
    "height": "1.40 m",
    "weight": "88.4 kg",
    "weaknesses": ["Fighting"]
    },
    {
    "id": 129,
    "num": "129",
    "name": "Magikarp",
    "img": "http://www.serebii.net/pokemongo/pokemon/129.png",
    "type": ["Water"],
    "height": "0.89 m",
    "weight": "10.0 kg",
    "weaknesses": ["Electric", "Grass"],
    "next_evolution": [
        {
        "num": "130",
        "name": "Gyarados"
        }
    ]
    },
    {
    "id": 130,
    "num": "130",
    "name": "Gyarados",
    "img": "http://www.serebii.net/pokemongo/pokemon/130.png",
    "type": ["Water", "Flying"],
    "height": "6.50 m",
    "weight": "235.0 kg",
    "weaknesses": ["Electric", "Rock"],
    "prev_evolution": [
        {
        "num": "129",
        "name": "Magikarp"
        }
    ]
    },
    {
    "id": 131,
    "num": "131",
    "name": "Lapras",
    "img": "http://www.serebii.net/pokemongo/pokemon/131.png",
    "type": ["Water", "Ice"],
    "height": "2.49 m",
    "weight": "220.0 kg",
    "weaknesses": ["Electric", "Grass", "Fighting", "Rock"]
    },
    {
    "id": 132,
    "num": "132",
    "name": "Ditto",
    "img": "http://www.serebii.net/pokemongo/pokemon/132.png",
    "type": ["Normal"],
    "height": "0.30 m",
    "weight": "4.0 kg",
    "weaknesses": ["Fighting"]
    },
    {
    "id": 133,
    "num": "133",
    "name": "Eevee",
    "img": "http://www.serebii.net/pokemongo/pokemon/133.png",
    "type": ["Normal"],
    "height": "0.30 m",
    "weight": "6.5 kg",
    "weaknesses": ["Fighting"],
    "next_evolution": [
        {
        "num": "134",
        "name": "Vaporeon"
        },
        {
        "num": "135",
        "name": "Jolteon"
        },
        {
        "num": "136",
        "name": "Flareon"
        }
    ]
    },
    {
    "id": 134,
    "num": "134",
    "name": "Vaporeon",
    "img": "http://www.serebii.net/pokemongo/pokemon/134.png",
    "type": ["Water"],
    "height": "0.99 m",
    "weight": "29.0 kg",
    "weaknesses": ["Electric", "Grass"],
    "prev_evolution": [
        {
        "num": "133",
        "name": "Eevee"
        }
    ]
    },
    {
    "id": 135,
    "num": "135",
    "name": "Jolteon",
    "img": "http://www.serebii.net/pokemongo/pokemon/135.png",
    "type": ["Electric"],
    "height": "0.79 m",
    "weight": "24.5 kg",
    "weaknesses": ["Ground"],
    "prev_evolution": [
        {
        "num": "133",
        "name": "Eevee"
        }
    ]
    },
    {
    "id": 136,
    "num": "136",
    "name": "Flareon",
    "img": "http://www.serebii.net/pokemongo/pokemon/136.png",
    "type": ["Fire"],
    "height": "0.89 m",
    "weight": "25.0 kg",
    "weaknesses": ["Water", "Ground", "Rock"],
    "prev_evolution": [
        {
        "num": "133",
        "name": "Eevee"
        }
    ]
    },
    {
    "id": 137,
    "num": "137",
    "name": "Porygon",
    "img": "http://www.serebii.net/pokemongo/pokemon/137.png",
    "type": ["Normal"],
    "height": "0.79 m",
    "weight": "36.5 kg",
    "weaknesses": ["Fighting"]
    },
    {
    "id": 138,
    "num": "138",
    "name": "Omanyte",
    "img": "http://www.serebii.net/pokemongo/pokemon/138.png",
    "type": ["Rock", "Water"],
    "height": "0.41 m",
    "weight": "7.5 kg",
    "weaknesses": ["Electric", "Grass", "Fighting", "Ground"],
    "next_evolution": [
        {
        "num": "139",
        "name": "Omastar"
        }
    ]
    },
    {
    "id": 139,
    "num": "139",
    "name": "Omastar",
    "img": "http://www.serebii.net/pokemongo/pokemon/139.png",
    "type": ["Rock", "Water"],
    "height": "0.99 m",
    "weight": "35.0 kg",
    "weaknesses": ["Electric", "Grass", "Fighting", "Ground"],
    "prev_evolution": [
        {
        "num": "138",
        "name": "Omanyte"
        }
    ]
    },
    {
    "id": 140,
    "num": "140",
    "name": "Kabuto",
    "img": "http://www.serebii.net/pokemongo/pokemon/140.png",
    "type": ["Rock", "Water"],
    "height": "0.51 m",
    "weight": "11.5 kg",
    "weaknesses": ["Electric", "Grass", "Fighting", "Ground"],
    "next_evolution": [
        {
        "num": "141",
        "name": "Kabutops"
        }
    ]
    },
    {
    "id": 141,
    "num": "141",
    "name": "Kabutops",
    "img": "http://www.serebii.net/pokemongo/pokemon/141.png",
    "type": ["Rock", "Water"],
    "height": "1.30 m",
    "weight": "40.5 kg",
    "weaknesses": ["Electric", "Grass", "Fighting", "Ground"],
    "prev_evolution": [
        {
        "num": "140",
        "name": "Kabuto"
        }
    ]
    },
    {
    "id": 142,
    "num": "142",
    "name": "Aerodactyl",
    "img": "http://www.serebii.net/pokemongo/pokemon/142.png",
    "type": ["Rock", "Flying"],
    "height": "1.80 m",
    "weight": "59.0 kg",
    "weaknesses": ["Water", "Electric", "Ice", "Rock", "Steel"]
    },
    {
    "id": 143,
    "num": "143",
    "name": "Snorlax",
    "img": "http://www.serebii.net/pokemongo/pokemon/143.png",
    "type": ["Normal"],
    "height": "2.11 m",
    "weight": "460.0 kg",
    "weaknesses": ["Fighting"]
    },
    {
    "id": 144,
    "num": "144",
    "name": "Articuno",
    "img": "http://www.serebii.net/pokemongo/pokemon/144.png",
    "type": ["Ice", "Flying"],
    "height": "1.70 m",
    "weight": "55.4 kg",
    "weaknesses": ["Fire", "Electric", "Rock", "Steel"]
    },
    {
    "id": 145,
    "num": "145",
    "name": "Zapdos",
    "img": "http://www.serebii.net/pokemongo/pokemon/145.png",
    "type": ["Electric", "Flying"],
    "height": "1.60 m",
    "weight": "52.6 kg",
    "weaknesses": ["Ice", "Rock"]
    },
    {
    "id": 146,
    "num": "146",
    "name": "Moltres",
    "img": "http://www.serebii.net/pokemongo/pokemon/146.png",
    "type": ["Fire", "Flying"],
    "height": "2.01 m",
    "weight": "60.0 kg",
    "weaknesses": ["Water", "Electric", "Rock"]
    },
    {
    "id": 147,
    "num": "147",
    "name": "Dratini",
    "img": "http://www.serebii.net/pokemongo/pokemon/147.png",
    "type": ["Dragon"],
    "height": "1.80 m",
    "weight": "3.3 kg",
    "weaknesses": ["Ice", "Dragon", "Fairy"],
    "next_evolution": [
        {
        "num": "148",
        "name": "Dragonair"
        },
        {
        "num": "149",
        "name": "Dragonite"
        }
    ]
    },
    {
    "id": 148,
    "num": "148",
    "name": "Dragonair",
    "img": "http://www.serebii.net/pokemongo/pokemon/148.png",
    "type": ["Dragon"],
    "height": "3.99 m",
    "weight": "16.5 kg",
    "weaknesses": ["Ice", "Dragon", "Fairy"],
    "prev_evolution": [
        {
        "num": "147",
        "name": "Dratini"
        }
    ],
    "next_evolution": [
        {
        "num": "149",
        "name": "Dragonite"
        }
    ]
    },
    {
    "id": 149,
    "num": "149",
    "name": "Dragonite",
    "img": "http://www.serebii.net/pokemongo/pokemon/149.png",
    "type": ["Dragon", "Flying"],
    "height": "2.21 m",
    "weight": "210.0 kg",
    "weaknesses": ["Ice", "Rock", "Dragon", "Fairy"],
    "prev_evolution": [
        {
        "num": "147",
        "name": "Dratini"
        },
        {
        "num": "148",
        "name": "Dragonair"
        }
    ]
    },
    {
    "id": 150,
    "num": "150",
    "name": "Mewtwo",
    "img": "http://www.serebii.net/pokemongo/pokemon/150.png",
    "type": ["Psychic"],
    "height": "2.01 m",
    "weight": "122.0 kg",
    "weaknesses": ["Bug", "Ghost", "Dark"]
    },
    {
    "id": 151,
    "num": "151",
    "name": "Mew",
    "img": "http://www.serebii.net/pokemongo/pokemon/151.png",
    "type": ["Psychic"],
    "height": "0.41 m",
    "weight": "4.0 kg",
    "weaknesses": ["Bug", "Ghost", "Dark"]
    }
]