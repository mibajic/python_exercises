# SPARQLab 
![image](https://user-images.githubusercontent.com/38294198/104658598-7961dc00-56c3-11eb-9677-047485b18775.png)

## O aplikaci 
Aplikace [SPARQLab](https://doc.lmcloud.vse.cz/sparqlab/) byla vyvinuta Katedrou znalostního a webového inženýrství na Vysoké škole ekonomické v Praze za účelem poskytnout studentům interaktivní nástroj k procvičování dotazovacího jazyka SPARQL.

Cíle tohoto semestrálního projektu jsou: 
* procvičit SPARQL manuálním testováním a sběrem dotazů při psaní testovacích scénářů 
* otestovat funkčnost aplikace SPARQLab
* poskytnout katedře nástroj k automatickému testování funkčnosti

![image](https://user-images.githubusercontent.com/38294198/104654292-233d6a80-56bc-11eb-90eb-372ad30b6bde.png)

## Návod ke spouštění testů
* [chrome driver](https://chromedriver.chromium.org/) je už stažen a přidán do složky s testy, nicméně je nutné ho přidat i do systémové proměnné PATH
* poté je nutné ve souboru test_sparql_lab.py ve funkci setUp nastavit správnou cestu do souboru 
* dále je potřeba nainstalovat následující knihovny:
```
pip install selenium
pip install unittest
```
Testy je možné spouštět promocí příklazu:
```
python test_sparql_lab.py
```
nebo přímo v Python editoru (testováno v PyCharm).
