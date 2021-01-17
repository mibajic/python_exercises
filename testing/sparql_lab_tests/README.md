# Automatizované testy funkčnosti aplikace SPARQLab ![image](https://user-images.githubusercontent.com/38294198/104660941-d5c6fa80-56c7-11eb-8256-13d54914d764.png)
Testovací scénáře byly vytvořeny v rámci semestrálního projektu předmětu 4IZ440 - Propojená data. 

Cílem práce je: 
* procvičit SPARQL manuálním testováním a sběrem dotazů při psaní testovacích scénářů 
* otestovat funkčnost aplikace SPARQLab
* poskytnout katedře nástroj k automatickému testování funkčnosti

## O aplikaci SPARQLab ![image](https://user-images.githubusercontent.com/38294198/104661060-0eff6a80-56c8-11eb-892c-f8f98b7f987b.png)
Aplikace [SPARQLab](https://doc.lmcloud.vse.cz/sparqlab/) byla vyvinuta Katedrou informačního a znalostního inženýrství na Vysoké škole ekonomické v Praze za účelem poskytnout studentům interaktivní nástroj k procvičování dotazovacího jazyka SPARQL.


## Návod ke spouštění testů ![image](https://user-images.githubusercontent.com/38294198/104661060-0eff6a80-56c8-11eb-892c-f8f98b7f987b.png)
* [chrome driver](https://chromedriver.chromium.org/) je už stažen a přidán do složky s testy, nicméně je nutné ho přidat i do systémové proměnné PATH
* poté je nutné ve souboru test_sparql_lab.py ve funkci setUp nastavit správnou cestu do souboru 
* dále je potřeba nainstalovat následující knihovny:
```
pip install selenium
pip install unittest
```
Testy je možné spouštět pomocí příkazu:
```
python test_sparql_lab.py
```
nebo přímo v IDE.
