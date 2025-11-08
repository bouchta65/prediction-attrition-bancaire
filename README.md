# Prédiction de l’Attrition Client Bancaire

## Description
Ce projet vise à prédire l’attrition des clients bancaires à l’aide d’un pipeline de Machine Learning distribué avec **PySpark**, **MLlib**, **MongoDB** et **Streamlit**. L’objectif est d’identifier les clients à risque, comprendre leur comportement et proposer des stratégies pour améliorer la fidélisation.  

Le pipeline inclut toutes les étapes : préparation et exploration des données, prétraitement, construction et entraînement du modèle, évaluation et déploiement via une interface interactive.

---

## Fonctionnalités
- Configuration et exploration des données avec **PySpark**  
- Prétraitement des données : nettoyage, encodage et gestion des valeurs manquantes  
- Stockage intermédiaire dans **MongoDB** pour industrialisation  
- Construction d’un pipeline ML complet avec gestion des déséquilibres  
- Entraînement et optimisation du modèle avec **MLlib** et **CrossValidator**  
- Évaluation des performances (Accuracy, AUC-ROC, Precision, Recall, F1-score)  
- Déploiement via **Streamlit** pour visualisation et interaction en temps réel  

---

## Technologies utilisées
- **PySpark** : traitement distribué des données  
- **MLlib** : création et entraînement du modèle de classification binaire  
- **MongoDB** : stockage intermédiaire des données transformées  
- **Streamlit** : interface interactive pour visualiser les prédictions  
- **Python 3.11+** : langage principal  

---

## Structure du projet
