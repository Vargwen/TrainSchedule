# 🚉 SNCF Train Notification Bot


> Recevez vos prochains départs de train directement sur Telegram chaque matin.

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![AWS](https://img.shields.io/badge/AWS-Lambda-orange.svg)
![Telegram](https://img.shields.io/badge/Telegram-Bot-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

---

## 📖 Présentation
Ce projet permet de surveiller les prochains départs d'une gare SNCF spécifique. Il est conçu pour être flexible :
- **Mode Local :** Interactif, idéal pour une vérification rapide avec saisie clavier.
- **Mode Cloud (AWS) :** Automatisé, pour recevoir une notification tous les matins à 7h00 sans avoir à allumer son PC.

---

## 🛠️ Architecture du Projet

| Fichier | Rôle |
| :--- | :--- |
| `isMyTrainOnTime.py` | Point d'entrée **Local** (interactif). |
| `lambda_function.py` | Point d'entrée **AWS Lambda** (automatisé). |
| `stationID.py` | Recherche de l'ID technique d'une gare par son nom. |
| `nextTrain.py` | Extraction des prochains départs via l'API SNCF. |
| `callBot.py` | Gestion de l'envoi des messages vers l'API Telegram. |

---

## ⚙️ Configuration

### 1. Variables d'environnement
Le projet nécessite les clés suivantes (à placer dans un fichier `.env` en local ou dans la console AWS) :

| Clé | Description |
| :--- | :--- |
| `SNCF_TOKEN` | Votre clé API Navitia / SNCF. |
| `TELEGRAM_TOKEN` | Le token de votre Bot (via BotFather). |
| `CHAT_ID` | Votre ID utilisateur Telegram. |

### 2. Installation
```bash
# Installation des dépendances
pip install -r requirements.txt
