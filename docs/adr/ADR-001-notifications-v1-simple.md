# ADR-001 — Implémentation initiale du service de notification avec logique conditionnelle

## Statut
Accepté

## Date
2026-03-25

## Contexte
Le module de notification de l’application bibliothèque doit envoyer un rappel à un utilisateur lorsque la date de retour d’un livre approche.

Dans la première version, le service doit supporter un envoi selon une méthode choisie dynamiquement (`email` ou `sms`).
L’objectif initial est de produire une solution simple et directement fonctionnelle.

La première implémentation retenue est la suivante :

- une classe `User` contenant les coordonnées de contact (`email`, `phone`) ;
- une classe `NotificationService` avec une méthode `send_reminder(user, method)` ;
- un traitement conditionnel basé sur la valeur de `method`.

Exemple de comportement :
- si `method == "email"` : envoi par email ;
- si `method == "sms"` : envoi par SMS ;
- sinon : levée d’une erreur `ValueError("Unknown method")`.

## Décision
Nous avons retenu dans un premier temps une implémentation centralisée avec branchement conditionnel dans `NotificationService`.

Le choix consiste à :
- construire le message directement dans le service ;
- décider du canal d’envoi avec un `if / elif / else` ;
- exécuter l’action correspondante dans cette même méthode.

## Justification
Cette décision a été prise pour aller vite et livrer une première version simple.

À ce stade :
- le nombre de canaux reste limité ;
- la logique est courte ;
- le coût d’implémentation est faible ;
- le comportement est facile à comprendre immédiatement.

Cette approche est acceptable pour une première itération, mais elle reste volontairement simple.

## Conséquences positives
- Mise en œuvre rapide ;
- Faible nombre de classes ;
- Compréhension immédiate du flux ;
- Démonstration rapide du besoin fonctionnel.

## Conséquences négatives
- Le service mélange orchestration et logique spécifique des canaux ;
- La structure repose sur des conditions explicites ;
- Chaque nouveau canal impose de modifier la classe `NotificationService` ;
- Le code devient progressivement difficile à maintenir ;
- Une duplication de logique d’envoi commence à apparaître.

## Code smell identifié
Cette version présente déjà plusieurs signes de fragilité :
- utilisation de `if/elif` sur le type de notification ;
- violation potentielle du principe Open/Closed ;
- duplication de structure entre email et SMS ;
- faible extensibilité vers d’autres canaux comme push ou WhatsApp.

## Alternatives envisagées
### 1. Introduire dès le départ une abstraction par canal
Non retenue à cette étape pour éviter une abstraction jugée prématurée.

### 2. Créer un service séparé par type d’envoi
Non retenue dans la première version pour garder une implémentation minimale.

## Décision retenue
Conserver une version initiale simple avec une logique conditionnelle dans `NotificationService`.

## Impacts sur les tests
Les tests de cette version doivent valider :
- l’envoi correct si la méthode vaut `email` ;
- l’envoi correct si la méthode vaut `sms` ;
- l’exception levée si la méthode n’est pas reconnue.