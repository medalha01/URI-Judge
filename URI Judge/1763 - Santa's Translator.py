import string

christamas = {
    "brasil": "Feliz Natal!",
    "alemanha": "Frohliche Weihnachten!",
    "austria": "Frohe Weihnacht!",
    "coreia": "Chuk Sung Tan!",
    "espanha": "Feliz Navidad!",
    "grecia": "Kala Christougena!",
    "estados-unidos": "Merry Christmas!",
    "inglaterra": "Merry Christmas!",
    "australia": "Merry Christmas!",
    "portugal": "Feliz Natal!",
    "suecia": "God Jul!",
    "turquia": "Mutlu Noeller",
    "argentina": "Feliz Navidad!",
    "chile": "Feliz Navidad!",
    "mexico": "Feliz Navidad!",
    "antardida": "Merry Christmas!",
    "canada": "Merry Christmas!",
    "irlanda": "Nollaig Shona Dhuit!",
    "belgica": "Zalig Kerstfeest!",
    "italia": "Buon Natale!",
    "libia": "Buon Natale!",
    "siria": "Milad Mubarak!",
    "marrocos": "Milad Mubarak!",
    "japao": "Merii Kurisumasu!",
}
print("Escreva quit ou q para fechar o programa")
while True:
    m = input().strip()
    if m.lower() in {"quit", "q", "leave", "sair"}:
        break
    x = christamas.get(m)
    if x == None:
        print("--- NOT FOUND ---")
    else:
        print(x)
