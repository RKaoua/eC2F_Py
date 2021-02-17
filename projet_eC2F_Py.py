# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd 
import streamlit as st 
import numpy as np
from PIL import Image
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patches as patches



sns.set_theme()



@st.cache
def importation():
    df_old=pd.read_csv('energy_full.csv', sep=';')
    df_20 = pd.read_csv('df_clean_20.csv', sep=',')
    df = pd.read_csv('df_clean.csv', sep=',')
    df_annuel_som_20 = df_20.groupby(['Année', 'Mois'], as_index=False).sum()
    df_annuel_som = df.groupby(['Année', 'Mois'], as_index=False).sum()
    df_annuel_som_an = df.groupby(['Année'], as_index=False).sum()
    return df_old, df_20, df, df_annuel_som_20, df_annuel_som, df_annuel_som_an

@st.cache(persist=True)
def get_dfs(df):
    df_2013 = df[df['Année']== 2013]
    df_2014 = df[df['Année']== 2014]        
    df_2015 = df[df['Année']== 2015]        
    df_2016 = df[df['Année']== 2016]        
    df_2017 = df[df['Année']== 2017]        
    df_2018 = df[df['Année']== 2018]        
    df_2019 = df[df['Année']== 2019]   
    dfs = [df_2013, df_2014, df_2015, df_2016, df_2017, df_2018, df_2019]
    return dfs


df_old, df_20,df, df_annuel_som_20, df_annuel_som, df_annuel_som_an= importation()
st.spinner(text='In progress...')

annee = [2013, 2014, 2015,2016,2017,2018,2019]



# st.title('Bonjour à tous')

# st.text('Ceci est un texte de présentation')
# st.markdown("pip install python")


#df=pd.read_csv('df_52.csv')


# Pour afficher le code puis son résultat
# with st.echo():
#    st.dataframe(df.head(20))




#st.pyplot(figure)


# option = st.selectbox(label = 'Choisir le label', options=[1,2])

st.sidebar.title(('Menu'))

Menu = st.sidebar.radio(
     "",
     ('Le projet eC2F', 
      'Présentation du Dataset', 
      'Analyse de la Consommation', 
      'Analyse de la production',
      'Modélisation', 
      'Conclusion & Perspectives'))

st.sidebar.info("Projet DA - Promotion Bootcamp Décembre 2020     \n   \
               \n Participants :\n \
               \n [Aurélien BOYER](https://www.linkedin.com/in/aurelienboyerensci/) \n   \
                \n [Reda KAOUA](https://www.linkedin.com/in/kaoua-reda/) \n   \
                \n [Geoffroy LADONNE](https://www.linkedin.com/in/geoffroy-ladonne-8b40929a/)") 



if Menu == 'Le projet eC2F':
# Page d'accueil 
    st.title('eC2F : Electrical Consumption Forcasting in France')
    st.header('Prédiction de la consommation électrique en France')
    image = Image.open('reseau.jpg')
    st.image(image, 
          use_column_width=True)
    
    st.markdown("L’électricité est produite à partir de plusieurs sources d’énergies dites « primaires », \
                disponibles dans la nature. Ces sources si elles ne sont pas utilisées directement, doivent \
                être transformées en source d’énergie secondaire pour être exploitées et transformées en électricité.")
    
    st.markdown("En France, il existe trois filières d’électricité,  classées en fonction de l’énergie \
                primaire utilisée pour sa production : <br/><br/>\
                    <ul> \
	            <li> Les énergies fossiles : obtenues essentiellement grâce à la combustion d’hydrocarbures, \
                    charbon et gaz.</li>\
                <li> L’énergie nucléaire : obtenue lors des réactions de fission nucléaire des noyaux atomiques\
                    au sein d'un réacteur nucléaire.</li>\
                <li> Les énergies renouvelables : obtenues par des sources dont le renouvellement naturel est \
                    assez rapide pour qu'elles puissent être considérées comme inépuisables,  comme le \
                        soleil, le vent, l’hydraulique et les bioénergies.</li></ul>\
                        ",unsafe_allow_html=True )
    
    st.markdown("A l’échelle régionale, du fait des spécifications météorologiques et du parc de production\
                installé, le réseau électrique permet d’assurer les échanges avec les régions limitrophes \
                    puisque certaines régions produisent plus qu’elles ne consomment.<br/><br/> \
                    Il en va de même pour les pays limitrophes où la France reste le 1er exportateur \
                        d’électricité européen en 2019.", unsafe_allow_html=True)
                        
    st.markdown("Une des principales problématiques d’un réseau de production électrique, est le stockage \
                de l’électricité produite. En effet, actuellement le stockage électrique utilise des stations\
                de pompage-turbinage entre deux retenues d’eau situées à deux altitudes différentes, où l’eau \
                est pompée vers le bassin supérieur pendant les heures de faible consommation alors que pendant\
                les heures de pointe, l'eau passe dans une turbine qui produit un appoint d'électricité sur le\
                réseau.<br/><br/>\
                Concrètement, cette technique de stockage consomme plus d’énergie pour le pompage de l'eau que \
                le turbinage n'en crée, et engendre des pertes d’énergie allant de 15 à 30%. <br/><br/>\
                Afin de répondre à cette problématique de stockage, il est nécessaire de pouvoir adapter  la \
                production en fonction de la consommation.<br/><br/> \
                Et c’est dans cette démarche que s’inscrit notre projet « <b>eC2F</b> », qui a pour but \
                d’analyser et d’estimer la consommation électrique afin d’adapter la production d’électricité\
                au niveau national et régional.\
                    ", unsafe_allow_html=True)
    
    
elif Menu == 'Présentation du Dataset':
# Page Data Set
    st.title('Présentation du Dataset')
    st.header('Source : Open Data Réseaux Energies')

    
    st.markdown("Le jeu de données utilisé, provient de\
                <a href='https://opendata.reseaux-energies.fr/explore/dataset/eco2mix-regional-cons-def/information/?disjunctive.libelle_region&disjunctive.nature&sort=-date_heure'>\
                    l’Open Data Réseaux Energies (ODRE)</a>, il représente les\
                données énergétiques régionales (au pas de 30 minutes) consolidées depuis janvier 2020 et \
                définitives de janvier 2013 à décembre 2019, elles sont issues de l'application\
                <a href='https://www.rte-france.com/eco2mix'>éCO2mix.</a>\
                \
                    ", unsafe_allow_html=True)
    
    
    st.markdown("Le jeu de données présente les données énergétiques régionales telles que : <br/><br/>\
                <ul><li>La consommation réalisée</li>\
                    <li>La production selon les différentes filières composant le mix énergétique \
                        (thermique, nucléaire, dites 'renouvelables', pompage)</li> \
                    <li> Le solde des échanges avec les régions limitrophes </li></ul> \
                        ", unsafe_allow_html=True)
                        
    st.markdown("Ces données sont élaborées à partir des comptages et complétées par des forfaits.\
                Les données sont dites consolidées lorsqu'elles ont été vérifiées et complétées\
                (livraison en milieu de M+1). Elles deviennent définitives lorsque tous les partenaires \
                ont transmis et vérifié l'ensemble des comptages, (livraison deuxième trimestre A+1). <br/><br/> \
                Les données publiées sur le portail <a href='https://www.rte-france.com'>« www.rte-france.com »</a>\
                sont publiques et leur réutilisation est permise sous réserve de mentionner la source.<br/><br/> \
                Le Data Set utilisé lors de notre étude, regroupe les données définitives depuis le 1er Janvier \
                2013 jusqu’au 31 décembre 2019, et consolidées depuis le 1er Janvier au 30 Novembre 2020 pour \
                chacune des régions en France métropolitaine (hors Corse).<br/><br/>\
                Le Data Set ainsi utilisé contient <b><u>1.665.216 lignes</u></b> et <b><u>66 colonnes</u></b>.\
                ", unsafe_allow_html=True)
    with st.beta_expander("Présentation des variables"):
        st.header("Présentation des variables")
        st.markdown("<b>Aperçu des premières lignes du Dataset</b><br/>", unsafe_allow_html=True)
        st.write(df_old.head(20))
        
        st.markdown("<b>Description des variables </b><br/>", unsafe_allow_html=True)
        #if st.checkbox('Afficher la description des variables'):
        st.markdown("Avec ses 66 colonnes, le data set se compose des variables suivantes :\
                    <table><tr  style='background-color:#A9CCF6;'><td><b>Colonne</b></td><td><b>Nom de la variable</b></td><td><b>Format</b></td><td><b>Description</b></td></tr>\
                    <tr style='background-color:#EDF6FB;'><td>0</td><td>Code INSEE Région</td><td>Entier</td><td>Code INSEE de la Région</td></tr>\
                    <tr style='background-color:#D8EEFA;'><td>1</td><td>Région</td><td>Texte</td><td>Nom de la région</td></tr>\
                    <tr style='background-color:#EDF6FB;'><td>2</td><td>Nature</td><td>Texte</td><td>Nature de la donnée (définitive ou consolidée)</td></tr> \
                    <tr style='background-color:#D8EEFA;'><td>3 - 5</td><td>Date, Heure et Date – Heure</td><td>aaaa-mm-jj <br/>HH:MM	</td><td>Date du jour, heure de l’échantillon et le fuseau horaire</td></tr>\
                    <tr style='background-color:#EDF6FB;'><td>6</td><td>Consommation (MW)</td><td>entier</td><td>Consommation en MW</td></tr>\
                    <tr style='background-color:#D8EEFA;'><td>7</td><td>Thermique (MW)</td><td>Entier</td><td>	Production thermique en MW</td></tr>\
                    <tr style='background-color:#EDF6FB;'><td>8</td><td>Nucléaire (MW)</td><td>Entier</td><td>Production nucléaire en MW</td></tr>\
                    <tr style='background-color:#D8EEFA;'><td>9</td><td>Eolien (MW)</td><td>Entier</td><td>Production éolienne en MW</td></tr>\
                    <tr style='background-color:#EDF6FB;'><td>10</td><td>Solaire (MW)</td><td>Entier</td><td>Production solaire en MW</td></tr>\
                    <tr style='background-color:#D8EEFA;'><td>11</td><td>Hydraulique (MW)</td><td>Entier</td><td>Production hydraulique en MW</td></tr>\
                    <tr style='background-color:#EDF6FB;'><td>12</td><td>Pompage (MW)</td><td>Entier</td><td>Pompage hydraulique en MW</td></tr>\
                    <tr style='background-color:#D8EEFA;'><td>13</td><td>Bioénergies (MW)</td><td>Entier</td><td>Production Bioénergies en MW</td></tr>\
                    <tr style='background-color:#EDF6FB;'><td>14</td><td>Ech. Physiques (MW)</td><td>Entier</td><td>Solde imports/exports (flux physiques) en MW</td></tr>\
                    <tr style='background-color:#D8EEFA;'><td>15-52</td><td>Flux physiques entre régions</td><td>Entiers</td><td>Sommes des lignes électriques importatrices entre régions</td></tr>\
                    <tr style='background-color:#EDF6FB;'><td>53-64</td><td>TCO et TCH de chaque type d’énergie</td><td>Décimaux</td><td>TCO : Taux de Couverture <br/>TCH : Taux de charge</td></tr>\
                    <tr style='background-color:#D8EEFA;'><td>65</td><td>Column 64</td><td>Vide</td><td>Vide</td></tr>\
                    \
                        </table>", unsafe_allow_html=True)
       
        st.markdown("<b>Choix des variables </b><br/>", unsafe_allow_html=True)
        st.markdown("Le choix des variables les plus pertinentes à notre analyse a été fait en fonction des \
                    besoins de chaque objectif :<br/><br/>\
                    <ul><li>Pour l’analyse de la consommation et la production énergétique (par filière)\
                        au niveau national et régional, notre choix s’est porté sur les variables : \
                        <b>Régions, Date, Heure, Consommation</b> et <b>productions énergétiques</b>.</li>\
                    <li>Pour la partie modélisation par machine Learning, notre choix s’est naturellement\
                        porté sur la variable « <b>Consommation (MW)</b> » qui représente notre variable \
                        cible, ainsi que les variables : <b>Régions, Date</b> et <b>Heure</b>.</li></ul>\
                            ", unsafe_allow_html=True)
    with st.beta_expander("Analyse des valeurs manquantes"):
        st.header("Analyse des valeurs manquantes")
        st.markdown("Le tableau ci-dessous résume le nombre de valeurs manquantes et leurs proportions \
                    pour chaque variable du dataset :", unsafe_allow_html=True)
        # Tableau des valeurs manquantes
        st.markdown("<table>\
                    <tr  style='background-color:#A9CCF6;'><td><b>Variable</b></td><td><b>Nombre de NaN</b></td><td><b>Proportion de NaN</b></td></tr>\
                    <tr style='background-color:#EDF6FB;'><td>Consommation (MW)</td><td>	12	</td><td style='background-color:#E9FABA;'>< 0.1%	 </td></tr>\
                    <tr style='background-color:#D8EEFA;'><td>Thermique (MW)</td><td>	12	</td><td style='background-color:#E9FABA;'>< 0.1% </td></tr>\
                    <tr style='background-color:#EDF6FB;'><td>Nucléaire (MW)</td><td>	693.847	</td><td style='background-color:#FDCF54;'>42 %	 </td></tr>\
                    <tr style='background-color:#D8EEFA;'><td>Eolien (MW)	</td><td>108</td><td style='background-color:#E9FABA;'>	< 1% </td></tr>\
                    <tr style='background-color:#EDF6FB;'><td>Solaire (MW)</td><td>	12</td><td style='background-color:#E9FABA;'>	< 0.1% </td></tr>\
                    <tr style='background-color:#D8EEFA;'><td>Hydraulique (MW)</td><td>	12	</td><td style='background-color:#E9FABA;'>< 0.1% </td></tr>\
                    <tr style='background-color:#EDF6FB;'><td>Pompage (MW)</td><td>	728.887	</td><td style='background-color:#FDCF54;'>44 % </td></tr>\
                    <tr style='background-color:#D8EEFA;'><td>Bioénergies (MW)</td><td>	12</td><td style='background-color:#E9FABA;'>	< 0.1% </td></tr>\
                    <tr style='background-color:#EDF6FB;'><td>Ech. physiques (MW)</td><td>	12</td><td style='background-color:#E9FABA;'>	< 0.1% </td></tr>\
                    <tr style='background-color:#D8EEFA;'><td>Flux physiques entre régions</td><td>	1.633.056</td><td style='background-color:#D82C11;'>	98 % </td></tr>\
                    <tr style='background-color:#EDF6FB;'><td>TCO et TCH de chaque type d’énergie	</td><td>1.472.256	</td><td style='background-color:#D86E0F;'>88 % </td></tr>\
                    <tr style='background-color:#D8EEFA;'><td>Column 64	</td><td>1.665.216	</td><td style='background-color:#B6250E;'>100 %	 </td></tr>\
                    </table>", unsafe_allow_html=True)
        
        st.markdown("<br/>Effectivement, plusieurs variables montrent un nombre assez élevé de valeurs manquantes. \
                    Afin de mieux visualiser ces valeurs manquantes, la figure ci-dessous réalisé avec une \
                    heatmap, nous permet d’avoir la répartition des valeurs manquantes pour chaque variable : ", unsafe_allow_html=True)
        image = Image.open('heat.png')
        st.image(image, 
              use_column_width=True, caption='Analyse visuelle des valeurs manquantes')
        
        st.markdown("<br/> Cette visualisation nous permet de constater : <br/><br/>\
                    <ul><li>Les variables de Flux physiques entre régions et celles de TCO et TCH, ne sont \
                        disponibles qu’à partir d’une certaine date.</li>\
                    <li>La variable « Column 64 » elle ne représente que des valeurs manquantes.</li>\
                    <li>Les valeurs manquantes des variables « Nucléaire (MW) » et « Pompage (MW) » sont \
                        réparties tout au long du data set.</li></ul>\
                    <br/> Une analyse approfondie des valeurs manquantes a été effectué sur chaque variable,\
                        et il a été constaté : <br/><br/>\
                    <ul><li>Les 12 valeurs manquantes de la variable cible « Consommation (MW) » représente les\
                        12 premières lignes du Data Set correspondant à l’enregistrement de minuit du 1er Janvier\
                        2013. Il s'agit vraisemblablement d'un problème d'acquisition de données. </li>\
                    <li>Les valeurs manquantes des variables 'Nucléaire (MW)' et 'Pompage (MW)' ne sont présentes\
                        que dans les régions qui ne produisent pas ce type d'énergie.</li>\
                    <li>Les variables de Flux physiques entre régions et celles de TCO et TCH, ne sont disponibles\
                        que pour l’année 2020.</li>\
                            </ul>", unsafe_allow_html=True)
    # Préprocessing
    with st.beta_expander("Preprocessing des données"):
        st.header("Préprocessing des données")
        st.markdown("Le prétraitement des données a été réalisé en deux phases : \
                    <ul><li>La gestion des valeurs manquantes</li>\
                    <li>La réorganisation du Data Set</li></ul> \
                    ", unsafe_allow_html=True)
        st.markdown("<b>Gestion des valeurs manquantes</b>\
                    ", unsafe_allow_html=True)
        st.markdown("Le traitement des valeurs manquantes a été réalisé en plusieurs étapes : \
                    <ul><li>Suppression de la variable « Column 64 » </li>\
                    <li>Suppression des 12 lignes manquantes de la variable cible « Consommation (MW) »</li>\
                    <li>Remplacement des valeurs manquantes des variables de productions énergétiques par des 0</li>\
                    <li>Suppression des variables de Flux entre régions et celles de TCO et TCH du Data Set principal</li></ul>\
                        ", unsafe_allow_html=True)
        
        st.markdown("<b>Réorganisation du dataset</b>\
                    ", unsafe_allow_html=True)
        st.markdown("La réorganisation du Data Set a été réalisée comme suit : \
                    <ul><li>Remplacement du nom de la variable « Nature » par « Données définitives » et\
                        remplacement de ses deux modalités par 0 et 1. -> Données consolidées = 0 -> Données\
                        définitives = 1.</li>\
                    <li>Dissociation de la variable « Date » en variables : « Année », « Mois », « Jour » et \
                        « Jour_semaine ».</li>\
                    <li>Suppression de la colonne « Date-Heure ».</li>\
                    <li>Création d’une variable  « Prod_renouvelables_MW » qui représente la somme des variables de\
                        productions d’énergie renouvelable, à savoir : « Eoliens », « Solaire », « Hydraulique » et \
                        « Bioénergies ».</li>\
                    <li>Création d’une nouvelle  variable  « Prod_totale_MW » qui représente la somme de toutes les\
                        variables de productions.</li>\
                    <li>Ré-identification  des variables « Thermique », « Nucléaire », « Pompage » en « Prod_fossiles »,\
                        « Prod_nucleaire », et  « Prod_step ».</li>\
                    <li>Ré-identification de l'ensemble des variables en éliminant les accents, espaces et caractères\
                        spéciaux.</li>\
                            </ul>\
                        ", unsafe_allow_html=True)
            
            
elif Menu == 'Analyse de la Consommation':    
    st.title('Analyse de la consommation électrique')
    
    with st.beta_expander("Evolution de la consommation énergétique moyenne par région"):
        st.header('Evolution de la consommation énergétique moyenne par région')
        # ****************************************** Code ******************************************
        
        df_annuel_moy = df.groupby(['Année','Code_INSEE_region', 'Region'], as_index=False).mean()
        
        fig = sns.relplot(x='Année', 
                y='Consommation_MW', 
                hue='Region',  
                data=df_annuel_moy, 
                kind='line', aspect=2);
        plt.title('Evolution de la consommation énergétique moyenne par région', fontsize=18);
        
        st.pyplot(fig)
        
        st.markdown("Le graphique de l'évolution de la consommation énergétique moyenne par région nous permet \
                    de constater : \
                    <ul><li>La consommation énergétique est différente d’une région à une autre, ce qui s’explique\
                        par la différence de démographie et nombre de foyer dans chaque région, mais aussi du nombre \
                            d’industries et d’entreprises implantés. </li>\
                    <li>Une chute de la consommation moyenne annuelle dans toutes les régions en 2014, ceci s'explique\
                        par la montée de la température annuelle nationale de 1.2°C.\
                            <a href='https://www.leparisien.fr/environnement/chaleur-2014-annee-record-en-france-et-en-europe-depuis-1900-05-01-2015-4420799.php'>[Source]</a></li>\
                    <li>Un retour en 2015 à un niveau de consommation moyen similaire à celui de 2013</li>\
                    <li>Une certaine stabilité de consommation entre 2015 et 2018</li>\
                    <li>Une chute de la consommation moyenne dans certaines régions</li>\
                        ",unsafe_allow_html=True)
    
    with st.beta_expander("Répartition mensuelle de la consommation énergétique nationale"):
        st.header("Répartition mensuelle de la consommation énergétique nationale")
    
        #df_annuel_som = df.groupby(['Année', 'Mois'], as_index=False).sum()
        #st.write(df_annuel_som.head(20))
        #df_annuel_som[df_annuel_som['Année']== 2013]['Consommation_MW'].values
        annee = [2013, 2014, 2015,2016,2017,2018,2019]
        couleur =['blue', 'red', 'green', 'orange', 'cyan', 'black', 'brown', 'olive', 'pink']
        figure = plt.figure(figsize=(20,10));
        #ax = figure.add_subplot(111)
        c=0
        for an in annee:
            
            ind = df_annuel_som[df_annuel_som['Année']== an]['Mois']
            valeurs = df_annuel_som[df_annuel_som['Année']== an]['Consommation_MW'].values
            plt.plot(ind, valeurs,color=couleur[c], label=an, marker='o');
            
            c+=1
            #df_annuel_som[df_annuel_som['Année']== an].shape
            
            
    
    
        plt.legend(title='Année', title_fontsize='large', loc=9);
        plt.xlabel('Mois', fontsize=18);
        plt.ylabel('Consommation totale (MW)', fontsize=18);
        plt.xticks(np.arange(0,12,1), ['Janvier', 'Fevrier', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Aout', 'Septembre', 'Octobre', 'Novembre', 'Decembre']);
        plt.title('Répartition mensuelle de la consommation énergétique nationale par année', fontsize=20);
        
        st.pyplot(figure)
        
        st.markdown("Le graphique de répartition mensuelle de la consommation énergétique nationale nous permet\
                    de constater que : \
                    <ul><li>La consommation énergétique varie en fonction des saisons.</li>\
                        <li>Le maximum de consommation est atteint pendant l'hiver</li>\
                        <li>Le minimum de consommation est atteint pendant le mois d'Aout</li>\
                        <li>Une certaine symétrie entre le printemps et l'automne.</li></ul>\
                        Ce graphique est très riche en information car il montre la répétitivité et la saisonnalité\
                        de la variable cible Consommation en fonction des mois de l'année, et donc permet d'affirmer\
                        une importante corrélation entre ces deux variables.\
                            ", unsafe_allow_html=True)
        
        
    with st.beta_expander("Analyse de la consommation électrique en 2020"):
        st.header("Analyse de la consommation électrique en 2020")
        st.markdown("L’année 2020 a été marquée par la crise sanitaire liée au Covid-19, la figure ci-dessous représente\
                    la consommation électrique nationale de l’année 2020 en comparaison avec celle de 2019, avec mise en \
                    évidence des deux périodes de confinement décrété par le gouvernement en Mars et Octobre 2020.")
    
        annee =[2019,2020]
        couleur =['blue', 'red', 'green', 'orange', 'cyan', 'black', 'brown', 'olive', 'pink']
        fig = plt.figure(figsize=(20,10));
        ax = fig.add_subplot(111)
        ax.add_patch(
             patches.Rectangle(
                (3.5, 0.6e8),
                1.9,
                4e7,
                edgecolor = '#A9CCF6',
                facecolor = '#A9CCF6',
                fill=True
             ) )
        ax.add_patch(
             patches.Rectangle(
                (10.6, 0.6e8),
                0.4,
                4e7,
                edgecolor = '#A9CCF6',
                facecolor = '#A9CCF6',
                fill=True
             ) )
        c=0
        for an in annee:
            
            ind = df_annuel_som_20[df_annuel_som_20['Année']== an]['Mois'].values
            valeurs = df_annuel_som_20[df_annuel_som_20['Année']== an]['Consommation_MW'].values
            ax.plot(ind, valeurs,color=couleur[c], label=an, marker='o');
            
            c+=1 
        ax.text(3.82, 1.001e8, "Premier confinement")
        ax.text(10.1, 1.001e8, "Second confinement")
        plt.legend(title='Année', title_fontsize='large', loc=9);
        plt.xlabel('Mois', fontsize=18);
        plt.ylabel('Consommation totale (MW)', fontsize=18);
        ax.set_xlim(0,13)
        ax.set_xticks(np.arange(1,13,1))
        ax.set_xticklabels(['Janvier', 'Fevrier', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Aout', 'Septembre', 'Octobre', 'Novembre', 'Decembre']);
        plt.title('Analyse de la consommation éléctrique en 2020', fontsize=20);
        st.pyplot(fig)
    
    
        st.markdown("A partir de cette figure, nous constatons que la crise sanitaire liée au virus COVID-19,\
                    a eu un impact majeur et immédiat sur la consommation d’électricité en France, dès que les\
                    mesures de confinement ont été adoptées. <br/><br/>\
                    Ainsi, dès les premiers jours de confinement, une baisse importante de la consommation a été\
                    enregistrée. Au plus fort de la crise (deuxième et troisième semaines de confinement), les \
                    mesures de confinement ont pu entraîner un impact sur la consommation d’électricité supérieur\
                    à 15 % <a href='https://assets.rte-france.com/prod/public/2020-11/Rapport_hiver%202020-2021_novembre%202020%20DEF_0.pdf'>[Source]</a> .<br/><br/>\
                    Cet impact s’est par la suite réduit sur les semaines suivantes, du fait d’une reprise \
                    partielle de l’activité, notamment dans le secteur industriel.\
                    ", unsafe_allow_html=True)



 
      
elif Menu == 'Analyse de la production':
    st.title('Analyse de la production électrique')
    st.header("Visualtion de la production électrique en région")
    
    dfs = get_dfs(df)
    #st.write(dfs[0].head())
    dico = {2013:0, 2014:1, 2015:2, 2016:3, 2017:4, 2018:5, 2019:6}
    nom_region = ["","Occitanie", "Pays de la Loire", "Bourgogne-Franche-Comté", "Normandie", "Hauts-de-France",
                  "Auvergne-Rhône-Alpes","Ile-de-France", "Provence-Alpes-Côte d'Azur", "Centre-Val de Loire", 
                  "Bretagne", "Nouvelle-Aquitaine","Grand-Est"]
    annee = ["", 2013, 2014, 2015,2016,2017,2018,2019]
    #nom_region = df['Region'].unique()
    region = st.selectbox(
        'Sélectionner une Région',
        (nom_region))
    year = st.selectbox(
        'Sélectionner une Année',
        (annee))
    #st.write(nom_region)
    
    if year == '' or region =='':
        st.info("Veuillez sélectionner une région et une année")
    else:
        #st.write("oui")
        Annee = int(year)
        dfi = dfs[dico[Annee]]    
        dfi = dfi[dfi['Region']==region]
        
        valeurs = [dfi['Prod_nucleaire_MW'].values[0], dfi['Prod_fossiles_MW'].values[0], dfi['Prod_EnR_MW'].values[0]]
        valeurs = valeurs/dfi['Prod_totale_MW'].values[0]
        couleurs = ['brown', 'orange', 'green']
        labels = ['Energie Nucléaire', 'Energie fossile', 'Energie Renouvelable']
        explode = [0.0,0.0,0.1]
        
        ind=[]
        for index, v in enumerate(valeurs):
            if v==0:
                ind.append(index)
        valeurs = np.delete(valeurs, ind)
        couleurs = np.delete(couleurs, ind)
        labels = np.delete(labels, ind)  
        explode = np.delete(explode, ind)
        
        figure = plt.figure(figsize=(5,5))
        
        
        plt.pie(valeurs, 
                labels = labels,
                colors = couleurs,
                explode = explode,
                autopct = lambda x:str(round(x,2)) + '%',
                pctdistance = 0.7,
                labeldistance=1.1,
                counterclock=True,
                startangle=90,
                textprops=dict(color="k", fontsize=12),
                shadow=True)
        titre = 'Répartition de la production énergétique dans la région ' + dfi['Region'].values[0] + ' en ' + str(dfi['Année'].values[0]) 
        plt.title(titre, fontsize=14)
        if region == 'Occitanie':
            plt.legend(loc=(-0.5,0.6))
        else:
            plt.legend(loc=(-0.5,0.2))
        st.pyplot(figure)
        
        
        valeurs = [dfi['Hydraulique_MW'].values[0],dfi['Eolien_MW'].values[0], dfi['Solaire_MW'].values[0], dfi['Bioenergies_MW'].values[0]]
        labels = ['Hydraulique', 'Eolien', 'Solaire', 'Bioénergies']
        valeurs = valeurs/dfi['Prod_EnR_MW'].values[0]
        couleurs = ['purple', 'green', 'orange', 'olive']
        explode=[0.0,0.1,0.0,0.0]
        ind = []
        for index, v in enumerate(valeurs):
            if v==0:
                ind.append(index)
        valeurs = np.delete(valeurs, ind)
        couleurs = np.delete(couleurs, ind)
        labels = np.delete(labels, ind)  
        explode = np.delete(explode, ind)
                
        figure = plt.figure(figsize=(5,5))
        plt.pie(valeurs, 
                labels = labels,
                colors = couleurs,
                explode = explode,
                autopct = lambda x:str(round(x,2)) + '%',
                pctdistance = 0.7,
                labeldistance=1.1,
                counterclock=False,
                startangle=90,
                textprops=dict(color="k", fontsize=12),
                normalize=False,
                shadow=True)
        plt.legend(loc=(-0.5,0))
        titre = 'Répartition des énergies renouvelables dans la région ' + dfi['Region'].values[0] + ' en '+ str(Annee)
        titre = str(titre)
        plt.title(titre, fontsize=14)
        
        st.pyplot(figure)
    
    
    
    
    
    
    st.header("Voir aussi")
    with st.beta_expander("Production annuelle d’électricité au niveau national"):
        st.header('Production annuelle d’électricité au niveau national')
        figure = plt.figure(figsize=(20,10));
    
        plt.plot(df_annuel_som_an['Année'], df_annuel_som_an['Prod_totale_MW'],'b-', label='Production',linewidth=3);
        plt.plot(df_annuel_som_an['Année'], df_annuel_som_an['Consommation_MW'], 'k--', label='Consommation',linewidth=3);
        
        #plt.plot(df_annuel_som['Année'], df_annuel_som['Prod_ren'], 'r-', label='Production renouvelable');
        
        plt.legend();
        plt.title("Evolution de la production énergétique nationale annuelle vs consommation", fontsize=18);
        plt.xlabel("Années");
        plt.ylabel('(MW)');
        
        st.pyplot(figure)
        st.markdown("Le graphique ci-dessus nous permet de constater que la production énergétique est dans une \
                    certaine mesure proportionnelle à la consommation énergétique, avec un certain phasage de sécurité,\
                    afin d'éviter les risques de Blackout.<br/><br/>\
                    Il est également à noter, qu’une partie de l’électricité produite est destinée à l’exportation \
                    vers les pays limitrophes. En 2019, la France a exporté 57.7 TW vers l’Europe, ce qui lui vaut \
                    d’être le pays le  plus exportateur d’Europe\
                        <a href='https://bilan-electrique-2019.rte-france.com/prix-echanges-solde-france-echanges/'>[Source]</a>.<br/><br/>\
                    Cette production annuelle représente un mix des différentes filières de production. Par exemple\
                    pour l’année 2019 la production est répartie comme suit : ", unsafe_allow_html=True)
        
        df_2019 = df[df['Année']== 2019]
        df_2019_som1 = df_2019.groupby(['Année'], as_index=False).sum()
        valeurs = [df_2019_som1['Prod_nucleaire_MW'].values[0], df_2019_som1['Prod_fossiles_MW'].values[0], df_2019_som1['Prod_EnR_MW'].values[0]+df_2019_som1['Prod_STEP_MW'].values[0]]
        valeurs = valeurs/df_2019_som1['Prod_totale_MW'].values[0]
        couleurs = ['brown', 'orange', 'green']
        labels = ['Energie Nucléaire', 'Energie fossile', 'Energie Renouvelable']
        
        explode=[0.0,0.0,0.1]
                
        
        figure = plt.figure(figsize=(2.5,2.5))
        
        plt.pie(valeurs, 
                labels = labels,
                colors = couleurs,
                explode = explode,
                autopct = lambda x:str(round(x,2)) + '%',
                pctdistance = 0.7,
                labeldistance=1.1,
                counterclock=False,
                startangle=90,
                textprops=dict(color="k", fontsize=8),
                normalize=False,
                shadow=True);
        plt.title("Répartition de la production énergétique en 2019 par filières");
        st.pyplot(figure)
        
        
        
        st.markdown("Nous remarquons que la production nucléaire représente plus 71% de la production totale,\
                    suivie par les énergies\
                    renouvelables avec 20% et enfin les énergies fossiles avec moins de 8%.")
        
        image = Image.open('carte_prod_2019.png')
        st.image(image, 
              use_column_width=True, caption="Production énergétique par région pour l'année 2019")
        
        
        st.markdown("La figure 9 montre que la région Auvergne-Rhône-Alpe arrive en tête des productions pour \
                    l’année 2019 avec plus de 130TW, suivie de la région Grand-est avec plus 91 TW. <br/><br/>\
                    La production d’électricité ramenée à la maille régionale permet non seulement de couvrir les\
                    besoins de la région productrice mais contribue également à la couverture de la demande émanant\
                    de régions limitrophes et au-delà [ ]. Le réseau de transport d’électricité assure la solidarité\
                    interrégionale à deux niveaux : <br/><br/>\
                    <ul><li>D’abord d’un point de vue géographique : les régions Centre-Val de Loire ou Grand-Est qui\
                        produisent beaucoup plus qu’elles ne consomment contribuent fortement à cette solidarité. \
                        De cette façon les régions dépendant fortement de l’électricité produite dans les régions\
                        limitrophes telles que l’Île-de-France, la Bourgogne Franche-Comté ou la Bretagne ont \
                        l’assurance de pouvoir couvrir leurs besoins de consommation.</li></ul><br/> \
                    <ul><li>Ensuite d’un point de vue temporel : chaque région est amenée à recourir à des productions\
                        en dehors de son territoire pour couvrir ponctuellement ses besoins.</li></ul>\
                        ", unsafe_allow_html=True)
        
        
        
        
        
    with st.beta_expander("Production annuelle d’énergies renouvelables au niveau national"):
        st.header("Production annuelle d’énergies renouvelables au niveau national")
        fig = plt.figure(figsize=(18,10))
        ax = fig.add_subplot(111)
        ax.plot(df_annuel_som_an['Année'], (df_annuel_som_an['Prod_EnR_MW']/df_annuel_som_an['Prod_totale_MW'])*100, 'g-', label='Production total', linewidth=5, marker= 'D', markersize=8, mfc='orange');
        
        ax.set_title('Evolution du taux de la production annuelle des énergies renouvelables', fontsize=18);
        ax.set_xlabel('Année', fontsize=18);
        ax.set_ylabel('Taux (%)', fontsize=18);
        #plt.legend(loc='best');
        st.pyplot(fig)
        
        st.markdown("Ce graphique révèle une hausse de production de plus de 15% entre 2013 et 2019 avec de fortes\
                    chutes de production en 2015 et en 2017.<br/><br/>\
                    Pour expliquer cette tendance, nous allons nous intéresser à l’évolution de la production de \
                    chaque type d’énergie renouvelable :", unsafe_allow_html=True)
        
        
        fig = plt.figure(figsize=(18,10))
        ax = fig.add_subplot(111)
        ax.plot(df_annuel_som_an['Année'], (df_annuel_som_an['Prod_EnR_MW']/df_annuel_som_an['Prod_totale_MW'])*100, 'g-', label='Production total', linewidth=5, marker= 'D', markersize=8, mfc='orange');
        ax.plot(df_annuel_som_an['Année'], (df_annuel_som_an['Hydraulique_MW']/df_annuel_som_an['Prod_totale_MW'])*100, 'b--', label='Hydraulique', linewidth=3, marker= 'D', markersize=5, mfc='c');
        ax.plot(df_annuel_som_an['Année'], (df_annuel_som_an['Eolien_MW']/df_annuel_som_an['Prod_totale_MW'])*100, 'k--', label='Eolien', linewidth=3, marker= 'D', markersize=5, mfc='c');
        ax.plot(df_annuel_som_an['Année'], (df_annuel_som_an['Solaire_MW']/df_annuel_som_an['Prod_totale_MW'])*100, 'r--', label='Solaire', linewidth=3, marker= 'D', markersize=5, mfc='c');
        ax.plot(df_annuel_som_an['Année'], (df_annuel_som_an['Bioenergies_MW']/df_annuel_som_an['Prod_totale_MW'])*100, 'm--', label='Bioénergies', linewidth=3, marker= 'D', markersize=5, mfc='c');
        ax.set_title('Evolution du taux de la production annuelle des énergies renouvelables', fontsize=18);
        ax.set_xlabel('Année', fontsize=18);
        ax.set_ylabel('Taux (%)', fontsize=18);
        plt.legend(loc='best');
        st.pyplot(fig)
        
        st.markdown("Le graphique ci-dessus démontre la forte influence de la production hydroélectrique sur la \
                    production totale, car elle représente plus de 70% (comme représenté dans la matrice de \
                    corrélation dans la figure 2) de la production totale en 2013 et plus de 50% en 2019, et donc\
                    les chutes de production totale de 2015 et 2017 sont directement liées à la chute de la production\
                    hydroélectrique. <br/><br/> \
                    En effet, en moyenne et sur l’année 2015, la pluviométrie a été inférieure à la normale de plus\
                    de 15%<a href='http://www.meteofrance.fr/climat-passe-et-futur/bilans-climatiques/bilan-2015/bilan-climatique-de-l-annee-2015'>[Source]</a> ce qui a impacté la production hydraulique d’un déficit de production de plus de 11%.<br/><br/>\
                    En 2017, le cumul de précipitations a été déficitaire de plus de 10%, plaçant 2017 parmi les années\
                    les plus sèches sur la période 1959-2017 <a href='http://www.meteofrance.fr/climat-passe-et-futur/bilans-climatiques/bilan-2017/bilan-climatique-de-l-annee-2017'>[Source]</a>, ce qui a contraint la production hydroélectrique\
                    à une baisse de 16,3%. <br/><br/> \
                    Inversion de tendance pour l’année 2018, le cumul des précipitations a été légèrement excédentaire\
                    en moyenne sur l’année <a href='http://www.meteofrance.fr/climat-passe-et-futur/bilans-climatiques/bilan-2018/bilan-climatique-de-l-annee-2018'>[Source]</a>, ce qui a engendré un bond de production de 27.5% par rapport\
                    à 2017. <br/><br/>\
                    La baisse de production hydraulique en 2019 par rapport à 2018 a ainsi été en partie compensée \
                    par une augmentation des productions éolienne et solaire, portée à la fois par des conditions \
                    météorologiques plus favorables et par un parc qui continue de croître <a href='https://bilan-electrique-2019.rte-france.com/production-renouvelable/'>[Source]</a>.\
                    Le graphique révèle aussi une augmentation sur la période 2013-2019 de la production éolienne\
                    de plus de 87%, de l’énergie solaire de près de 162% et des bioénergies de près de 50%", unsafe_allow_html=True)
        
        
    
    with st.beta_expander("Production régionale d’énergies renouvelables"):
        st.header("Production régionale d’énergies renouvelables")
        image = Image.open('carte_enr_2019.png')
        st.image(image, 
              use_column_width=True, caption="Production régionale d’énergies renouvelables pour l'année 2019")
        
        df_2019_som = dfs[6].groupby(['Code_INSEE_region', 'Region'], as_index=False).sum()
        df_2019_som = df_2019_som.sort_values(by ='Prod_EnR_MW', ascending=False)
        fig = plt.figure(figsize=(20,15))
        ax = fig.add_subplot(111)
        ax.bar(df_2019_som['Region'], df_2019_som['Hydraulique_MW'], label = 'Hydraulique')
        ax.bar(df_2019_som['Region'], df_2019_som['Solaire_MW'], bottom = df_2019_som['Hydraulique_MW'], label='Solaire')
        ax.bar(df_2019_som['Region'], df_2019_som['Eolien_MW'], bottom = np.array(df_2019_som['Hydraulique_MW'])+np.array(df_2019_som['Solaire_MW']), label='Eolien')
        ax.bar(df_2019_som['Region'], df_2019_som['Bioenergies_MW'], bottom = np.array(df_2019_som['Hydraulique_MW'])+np.array(df_2019_som['Solaire_MW'])+np.array(df_2019_som['Eolien_MW']), label='Bioénergies')
        ax.set_title('Evolution de la production annuelle des énergies renouvelables', fontsize=18);
        ax.set_xlabel('Année', fontsize=18);
        ax.set_ylabel('Production en MW', fontsize=18);
        plt.legend(loc='best');
        plt.xticks(rotation=90);
        st.pyplot(fig)
        
        st.markdown("On observe sur ces deux graphiques que la région Auvergne-Rhône-Alpes arrive en tête du \
                    classement avec une production totale de plus de 60 TW d’énergies renouvelables en 2019.<br/><br/>\
                    En regardant de plus près sur la production énergétique en région Auvergne-Rhône-Alpes,\
                    nous constatons que la production d’Energie renouvelable ne représente 17% de la production\
                    totale de la région, contre 80% pour l’énergie Nucléaire et de 2% pour les énergies fossiles.", unsafe_allow_html=True)
        
        image = Image.open('ARA_2019.png')
        st.image(image, 
              use_column_width=True, caption="Production d'électricité en région Auvergne-Rhône-Alpes")
        
        
        st.markdown("On retrouve également une diversité dans le type de production d’énergie renouvelable avec \
                    plus 87% de production d’énergie hydroélectrique, et un peu plus de 6% pour les énergies \
                    éoliennes et les bioénergies.")
        
        
        # ax = df_2019_som.plot.bar(x='Region', 
        #                y=['Hydraulique_MW', 'Solaire_MW', 'Eolien_MW', 'Bioenergies_MW'], 
        #                stacked=True, figsize=(20,10),
        #                rot=0);
        # #ax.plot(df_annuel_som['Année'], df_annuel_som['Prod_EnR_MW'], 'k-', label='Production total', linewidth=5, );
        # ax.set_title('Production totale des énergies renouvelables par régions en 2019', fontsize=18);
        # ax.set_xlabel('Régions', fontsize=18);
        # ax.set_ylabel('Production en MW', fontsize=18);
        # st.bar_chart(ax)

elif Menu == 'Widgets':
    st.title('Titre temporaire')
    st.header('Régression Linéaire')
    
    nom_model = ["","Occitanie", "Pays de la Loire", "Bourgogne-Franche-Comté", "Normandie", "Hauts-de-France",
                  "Auvergne-Rhône-Alpes","Ile-de-France", "Provence-Alpes-Côte d'Azur", "Centre-Val de Loire", 
                  "Bretagne", "Nouvelle-Aquitaine","Grand-Est"]
    annee = ["", 2013, 2014, 2015,2016,2017,2018,2019]
    #nom_region = df['Region'].unique()
    # MRG = st.selectbox(
    #     'Sélectionner un Régression',
    #     (nom_region))





elif Menu == 'Modélisation':
    st.title('Modélisation')
    
    st.markdown("Compte tenu du type de données, les premiers modèles expérimentés ont été ceux faisant partie de\
                la famille des « régressions ». Quatre modèles ont été implémentés :<br/><br>\
                    <ul><li>Régression « SGD »</li>\
                        <li>Régression « RIDGE »</li>\
                        <li>Régression « LASSO »</li>\
                        <li>Régression « ELASTIC NET CV »</li></ul>\
                Ensuite, deux modèles « Séries Temporelles » ont été testées :\
                    <ul><li>Modèle SARIMAX</li>\
                        <li>Modèle ARIMA</li></ul>\
                Enfin, un modèle de réseaux de neurones a été mis en place en dernière étape.", unsafe_allow_html=True)
    
    nom_model = ["","Modèles de Régression", "Modèles de Séries Temporelles", "Modèle de Réseau de Neurones"]
        
    nom_region = df['Region'].unique()
    
    st.title('Résultats des prévisions')
    MRG = st.selectbox("Sélection un modèle pour afficher les prédictions",(nom_model))
    
    
    
    if MRG == "Modèles de Régression":
        st.header('Modèles de Régression')
            # Importation des Datasets
        df_reg = pd.read_csv('predictions_regression.csv', sep=',')
        df_reg['Date'] = pd.to_datetime(df_reg['Date'])  
        df_reg = df_reg.set_index('Date')
        # df_EN['date'] = dates
        # df_EN['date'] = pd.to_datetime(df_EN['date'])
        # df_EN = df_EN.set_index('date')
        # df_EN = df_EN.iloc[:,1:]
        df_reg = df_reg.loc['2019-01-01':'2019-12-31']
        #st.write(df_reg.head())
        
        
        countries = ["SGD Regressor", "Ridge", "Lasso","Elastic Net"]
        multiselection = st.multiselect("Select countries:", countries, default=countries)
        
        
        
        fig = plt.figure(figsize=(16,8))
        ax = fig.add_subplot(111)
        ax.plot(df_reg['y_test'], 'k-', label='Consommation réelle');
        if "SGD Regressor" in multiselection:
            ax.plot(df_reg['sgd'], '--', c='orange', label='SGD Regressor');
        if "Ridge" in multiselection:
            ax.plot(df_reg['ridge'], '--', c='red', label='Ridge');
        if "Lasso" in multiselection:
            ax.plot(df_reg['lasso'], '--', c='blueviolet', label='Lasso');
        if "Elastic Net" in multiselection:
            ax.plot(df_reg['en'], '--', c='green', label='Lasso');
        #ax.set_xticks(np.arange(1,13,1))
        #ax.set_xticklabels(['Janvier', 'Fevrier', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Aout', 'Septembre', 'Octobre', 'Novembre', 'Decembre'])
        plt.title("Predictions des modèles de Régression sur l'année 2019 pour la région 52", fontsize=18)
        plt.xlabel('Date', fontsize=18);
        plt.ylabel('Consommation (MW)', fontsize=18);
        #plt.xticks(np.arange(1,13,1), labels=['Janvier', 'Fevrier', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Aout', 'Septembre', 'Octobre', 'Novembre', 'Decembre'])
        #plt.xlim(['2019-01-01','2019-12-31'])
        plt.xticks(rotation=45);
        plt.grid(True);
        plt.legend(loc='best');
        st.pyplot(fig)
        
        st.markdown("Résultats obtenus pour les modèles de Régression :")
        st.markdown("<center><table>\
                    <tr style='background-color:#D8EEFA;'><td></td><td><b>SGD Regressor</b></td><td><b>Ridge</b></td><td><b>Lasso</b></td><td><b>Elastic Net</b></td></tr>\
                    <tr style='background-color:#EDF6FB;'><td><b>MAE</b></td><td>58948.18</td><td>58949.79</td><td>58461.96</td><td>58991.79</td></tr>\
                    <tr style='background-color:#D8EEFA;'><td><b>MSE</b></td><td>7.19e+09</td><td>6.93e+09</td><td>7.13e+09</td><td>6.99e+09</td></tr>\
                    <tr style='background-color:#EDF6FB;'><td><b>RMSE</b></td><td>84844.66</td><td>83285.45</td><td>84484.92</td><td>83638.05</td></tr>\
                    <tr style='background-color:#D8EEFA;'><td><b>Median AE</b></td><td>32936.36</td><td>34396.83</td><td>33722.25</td><td>33754.62</td></tr>\
                    <tr style='background-color:#EDF6FB;'><td><b>MAPE</b></td><td>5.28</td><td>5.34</td><td>5.21</td><td>5.33</td></tr>\
                    <tr style='background-color:#D8EEFA;'><td><b>Score R2</b></td><td>0.825189</td><td>0.831558</td><td>0.826672</td><td>0.830129</td></tr>\
                    </table></center><br/>", unsafe_allow_html=True)
        
    elif MRG == "Modèles de Séries Temporelles":
        st.header('Modèles de Séries Temporelles')
        
        
        
        
        
        
    elif MRG == "Modèle de Réseau de Neurones":
        st.header('Modèle de Réseau de Neurones')
        df_lstm = pd.read_csv('predictions_52.csv', index_col=0)
        df_lstm.index = pd.to_datetime(df_lstm.index)
        
        months = st.slider("Choisissez le mois à afficher", min_value=1, max_value=12, step=1, value=6)
        nbr_jours = st.slider("Choisissez le nombre de jours à afficher", min_value=1, max_value=15, step=1, value=5)
        #st.write(df_lstm.head(50))
        
        #import matplotlib.dates as mdates
        fig = plt.figure(figsize=(16,8))
        ax = fig.add_subplot(111)
        debut = '2019-'+str(months)+'-13'
        fin = '2019-'+str(months)+'-'+str(13+nbr_jours)
        #ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
        prevision = df_lstm.loc[debut:fin]
        
        #st.write(prevision.date_heure)
        
        plt.title("Predictions du modèle LSTM pour la région 52 entre ("+debut+") et ("+fin+")"  , fontsize=18)
        plt.xlabel('Date', fontsize=18)
        plt.ylabel('Consommation (MW)', fontsize=18)
        #plt.plot(train['Consommation_MW'])
        #plt.scatter(prevision.index, prevision['Consommation_MW'], c='k', label='Consommation réelle')
        ax.plot(prevision['Consommation_MW'],'-', c='k', label='Consommation réelle');
        ax.plot(prevision['Predictions'],'-', c='orange', label='Consommation prédite');
        
        plt.xticks(rotation=45);
        plt.grid(True)
        plt.legend(loc='best')
        
        st.pyplot(fig)
        st.markdown("Résultats obtenus pour le modèle LSTM :<br/><br/><center>RMSE =  <b>44.48</b></center>", unsafe_allow_html=True)
        st.markdown("Le modèle LSTM donnent des résultats absolument remarquables en comparaison des autres modèles, les prédictions \
                    suivent exactement les mêmes courbes que les valeurs réelles, avec un certain décalage que nous avons essayé de \
                    mesurer afin de déterminer un intervalle de confiance pour chaque modèle.")
        st.write(df_lstm.describe())
        st.markdown("De ce tableau, nous pouvons conclure que la différence moyenne entre les valeurs prédites et les valeurs réelles\
                    est de 97.4 MW sur l’année 2019, avec une différence maximale de 531.39 MW.")

else:
    st.title('Conclusion & Perspectives')
    st.header('Conclusion')
    
    st.markdown("La mission du projet, qui est d’apporter une solution à une problématique de stockage électrique, en implémentant un modèle\
               de prédiction de la consommation électrique afin de réguler la production et d’éviter les pertes du réseau,   nous a permis \
               de développer en nous, une nouvelle vision des données et une nouvelle méthodologie d’appréhension de problématiques complexes,\
               en utilisant de nouveaux outils et en mettant en pratique de nouvelles compétences. <br/><br/> \
               Pour la réalisation de ce projet, nous sommes passés par plusieurs étapes, de l’exploration des données, leurs analyses,  leurs\
               visualisations, jusqu’à l’implémentation de modèles de prédiction.<br/><br/>\
               Les résultats de modélisation nous permettent d’affirmer que c’est les modèles « Ridge » (régression) et SARIMAX (série temporelle)\
               qui ont donné les résultats les plus fiables, et qui anticipent le mieux les variations de la consommation électrique. <br/><br/>\
               Même si l’écart entre tous les modèles implémentés reste faible, le modèle ARIMA ne semble pas apporter de bons résultats. <br/><br/>\
               Quant au modèle LSTM, ses résultats de prédictions sont exceptionnels. Néanmoins il représente un désavantage conséquent qui est le \
               coût de son exécution, car ce modèle est très gourmand en ressources et en temps de calcul. <br/>", unsafe_allow_html=True)
    
    
    st.header("Perspectives d'Amélioration")
    
    st.markdown("Pour la continuité du projet, et dans l’optique d’améliorer les performances des modèles de prédictions, nous pensons qu’il serait \
                pertinent de rajouter une variable température au data set, et pouvoir étudier sa corrélation avec la consommation électrique et \
                ainsi l’utiliser dans les données d’entrée des futurs modèles.<br/><br/> \
                Avec l’impact du Covid19, il serait peut être utile de prendre en considération une variable ‘Confinement’ et/ou ‘Couvre-feu’ pour\
                pouvoir anticiper des scénarios futurs liés à d’éventuelles nouvelles mesures.", unsafe_allow_html=True)
    
    
    
    
    
    
    # display = ("male", "female")

    # options = list(range(len(display)))

    # value = st.selectbox("gender", options, format_func=lambda x: display[x])

    # st.write(value)
    

# 


# st.sidebar.selectbox(label = 'label', options=[1,2])

# add_selectbox = st.sidebar.selectbox(
#     "How would you like to be contacted?",
#     ("Email", "Home phone", "Mobile phone")
# )

# with st.beta_container():
#     st.write("This is inside the container")

#     # You can call any Streamlit command, including custom components:
#     st.bar_chart(np.random.randn(50, 3))

# st.write("This is outside the container")

