# Projet de Gestion de Comptes Bancaires

Ce projet vise à développer la logique d'une application de gestion de comptes bancaires en utilisant la programmation orientée objet. L'application gérera les opérations bancaires courantes et sera testée à l'aide de `pytest`. Étant donné que l'application interagit avec une base de données (BDD), le mocking sera utilisé pour simuler les interactions avec celle-ci. Un pipeline de CI/CD sera également configuré à l'aide de GitHub Actions.

## Table des Matières

- [Fonctionnalités](#fonctionnalités)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Tests](#tests)
- [CI/CD](#cicd)
- [Contribuer](#contribuer)
- [Licence](#licence)

## Fonctionnalités

- Création de comptes bancaires
- Dépôt et retrait d'argent
- Consultation du solde
- Transfert d'argent entre comptes
- Historique des transactions

## Installation

1. Clonez le dépôt :
    ```bash
    git clone https://github.com/votre-utilisateur/votre-repo.git
    cd votre-repo
    ```

2. Créez un environnement virtuel et activez-le :
    ```bash
    python -m venv env
    source env/bin/activate  # Pour Windows: .\env\Scripts\activate
    ```

3. Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```

## Utilisation

Après avoir installé les dépendances, vous pouvez commencer à utiliser l'application en exécutant le script principal. Par exemple :

```bash
python main.py
```



## Tests

Nous utilisons pytest pour tester notre application. Pour exécuter les tests, utilisez la commande suivante :

bash

pytest

Les tests utilisent le mocking pour simuler les interactions avec la BDD. Cela permet de tester la logique de l'application sans dépendre d'une base de données réelle.


## CI/CD

Le pipeline de CI/CD est configuré à l'aide de GitHub Actions. Chaque commit déclenche une série de tâches automatisées, notamment :

    Linting du code
    Exécution des tests unitaires
    Déploiement (si applicable)

Le fichier de configuration pour GitHub Actions se trouve dans le répertoire .github/workflows.
Contribuer

## Les contributions sont les bienvenues ! Pour contribuer :

    Forkez le dépôt
    Créez une branche pour votre fonctionnalité (git checkout -b feature/AmazingFeature)
    Commitez vos modifications (git commit -m 'Add some AmazingFeature')
    Poussez votre branche (git push origin feature/AmazingFeature)
    Ouvrez une Pull Request

## Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.


N'hésitez pas à adapter ce README en fonction des spécificités et des détails de votre projet.

