# Prjet eC2F  

## Prévision de la consommation d'électricité en France

Ce projet a été réalisé dans le cadre du projet fil rouge de la formation *Data Analyst* pour répondre à une des principales problématiques d’un réseau de production électrique, qui est le stockage de l'électricité produite. En effet les méthodes actuelles de stockage d'électricité consomment plus d'énergie qu'elles n'en fournissent ([Article : Stockage d'électricité](https://www.ecosources.info/dossiers/Station_stockage_transfert_pompage_turbinage))  

Afin de répondre à cette problématique, le projet « ***eC2F*** » *(Pour **E**lectrical **C**onsumption **F**orcating in **F**rance)*, a pour but
d’analyser et d’estimer la consommation électrique afin d’adapter la production d’électricité au niveau national et régional, et d'éviter les surplus de production.

## Contributeurs

Ce projet a été réalisé par :
* [Aurélien BOYER](https://www.linkedin.com/in/aurelienboyerensci/)
* [Reda KAOUA](https://www.linkedin.com/in/kaoua-reda/)
* [Geoffroy LADONNE](https://www.linkedin.com/in/geoffroy-ladonne-8b40929a/)

## Sources des données

Le jeu de données utilisé, provient de l’[Open Data Réseaux Energie (ODRE)](https://opendata.reseaux-energies.fr/explore/dataset/eco2mix-regional-cons-def/export/?disjunctive.libelle_region&disjunctive.nature&sort=-date_heure), il représente les données énergétiques régionales (au pas de 30 minutes) consolidées depuis janvier 2020 et définitives de janvier 2013 à décembre 2019, elles sont issues de l'application [éCO2mix](https://www.rte-france.com/eco2mix).

Le jeu de données présente les données énergétiques régionales telles que :
- La consommation réalisée
- La production selon les différentes filières composant le mix énergétique (thermique, nucléaire, dites 'renouvelables', pompage)
- Le solde des échanges avec les régions limitrophes

Ces données sont élaborées à partir des comptages et complétées par des forfaits. Les données sont dites consolidées lorsqu'elles ont été vérifiées et complétées (livraison en milieu de M+1). Elles deviennent définitives lorsque tous les partenaires ont transmis et vérifié l'ensemble des comptages, (livraison deuxième trimestre A+1).

Les données publiées sur le portail [« www.rte-france.com »](https://www.rte-france.com) sont publiques et leur réutilisation est permise sous réserve de mentionner la source.
Le Data Set utilisé lors de notre étude, regroupe les données définitives depuis le 1er Janvier 2013 jusqu’au 31 décembre 2019, et consolidées depuis le 1er Janvier au 30 Novembre 2020 pour chacune des régions en France métropolitaine (hors Corse).

Le Data Set ainsi utilisé contient **1.665.216 lignes** et **66 colonnes**. 


## Code et ressources utilisés

- **Python Version** : 3.8.5
- **Librairies**: 
   - pandas, 
   - numpy, 
   - sklearn, 
   - matplotlib, 
   - seaborn, 
   - 


## Fichiers du projet


