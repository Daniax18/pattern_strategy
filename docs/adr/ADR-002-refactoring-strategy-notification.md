# ADR-002 — Refactoring du service de notification avec le pattern Strategy

## Statut
Accepté

## Date
2026-03-25

## Contexte
L’implémentation initiale du service de notification repose sur une logique conditionnelle :

- `if method == "email"`
- `elif method == "sms"`
- `else raise ValueError(...)`

Cette version fonctionne, mais elle révèle plusieurs défauts de conception :
- le service doit connaître tous les canaux ;
- chaque nouveau canal impose une modification de la méthode `send_reminder` ;
- la logique est peu extensible ;
- le service centralise trop de responsabilités.

Avec l’évolution du besoin, il devient nécessaire de refactorer pour rendre le système plus maintenable et extensible.

## Décision
Nous remplaçons la logique conditionnelle par une stratégie injectable.

La nouvelle conception repose sur :
- une interface abstraite `NotificationStrategy` ;
- des implémentations concrètes comme `EmailNotification` et `SmsNotification` ;
- une classe `NotificationService` recevant une stratégie dans son constructeur.

Exemple :
- `NotificationService(EmailNotification())`
- `NotificationService(SmsNotification())`

Le service ne choisit plus le canal lui-même.
Il délègue l’envoi à la stratégie fournie.

## Justification
Le pattern Strategy est adapté ici car plusieurs comportements d’envoi doivent partager le même contrat :

`send(user, message)`

Cette décision permet de :
- supprimer les conditions sur le type de canal ;
- séparer les responsabilités ;
- respecter davantage le principe Open/Closed ;
- rendre le service métier plus simple ;
- faciliter les tests unitaires.

Le service devient responsable de l’orchestration métier, tandis que chaque stratégie gère sa propre façon d’envoyer la notification.

## Conséquences positives
- Suppression du `if/elif/else` ;
- Réduction du couplage ;
- Code plus propre et plus lisible ;
- Ajout d’un canal possible via une nouvelle classe ;
- Tests plus ciblés ;
- Meilleure évolutivité.

## Conséquences négatives
- Augmentation du nombre de classes ;
- Besoin d’introduire une abstraction supplémentaire ;
- L’instanciation de la bonne stratégie doit être faite par le code appelant.

## Alternatives envisagées
### 1. Conserver le `if/elif` et ajouter de nouveaux cas
Rejetée, car cette approche aggrave le couplage et la maintenance.

### 2. Ajouter plusieurs méthodes dans `NotificationService`
Rejetée, car cela ferait de `NotificationService` une classe trop chargée.

### 3. Utiliser une factory seule
Non retenue comme solution principale, car le vrai besoin ici est la variation du comportement d’envoi, pas uniquement la création d’objets.

## Décision retenue
Refactorer vers une architecture basée sur le pattern Strategy avec une interface `NotificationStrategy`.

## Structure retenue
- `NotificationStrategy` : contrat abstrait ;
- `EmailNotification` : implémentation email ;
- `SmsNotification` : implémentation SMS ;
- `NotificationService` : service orchestrateur basé sur l’injection d’une stratégie.

## Impacts sur les tests
Les tests doivent vérifier :
- qu’un `NotificationService` utilisant `EmailNotification` renvoie `True` ;
- qu’un `NotificationService` utilisant `SmsNotification` renvoie `True` ;
- que le comportement du service ne dépend plus d’une chaîne `method`.

Le refactoring doit être validé par des tests unitaires passant après modification.