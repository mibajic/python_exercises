class Vuz:
    def __init__(self, kapacita, spz, motor):
        self.kapacita = kapacita
        self.spz = spz
        self.motor = motor

vozovy_park = [
            Vuz(10, "ABC", "benzinovy"),
            Vuz(50, "DEF", "elektro"),
            Vuz(80, "GHI", "hybrid"),
            Vuz(90, "JKL", "benzinovy"),
            Vuz(100, "MNO", "elektro"),
    ]

def secti_celkovou_kapacitu(seznam_vozu):
  celkova_kapacita = 0
  for vuz in seznam_vozu:
      celkova_kapacita = celkova_kapacita + vuz.kapacita
  return celkova_kapacita

def minimalni_kapacita(pozadovana_kapacita, seznam_vozu):
    vhodna_auta = []
    for i in seznam_vozu:
        if pozadovana_kapacita <= i.kapacita:
            vhodna_auta.append(i)
    return vhodna_auta
# print("vhodna auta jsou: " + str(minimalni_kapacita(16, vozovy_park)))

def nejekonomictejsi_varianta(kapacita, vzdalenost, seznam_vozu):
    vhodna_auta = minimalni_kapacita(kapacita, seznam_vozu)
    optimalni_vozy = []
    for auto in vhodna_auta:
        if vzdalenost <= 50 and auto.motor == "elektro":
            optimalni_vozy.append(auto)
        elif vzdalenost > 50 and vzdalenost < 200 and auto.motor == "hybrid":
            optimalni_vozy.append(auto)
        elif vzdalenost > 200 and auto.motor == "benzinovy":
            optimalni_vozy.append(auto)
    return optimalni_vozy
auta = nejekonomictejsi_varianta(10, 500, vozovy_park)
min_kap = []
for i in auta:
    min_kap.append(i.kapacita)


for i in vozovy_park:
    if i.kapacita == min(min_kap):
        print(i.spz )
