# ADR-003 — Ajout du canal Push sans modification du service métier

## Statut
Accepté

## Date
2026-03-25

## Contexte
Après refactoring, le système de notification repose sur une interface `NotificationStrategy` et plusieurs implémentations concrètes.

Le besoin évolue encore avec l’ajout d’un nouveau canal :
- notification push pour l’application mobile.

L’objectif est de vérifier que l’architecture mise en place permet bien d’ajouter ce nouveau canal sans modifier le code existant de `NotificationService`.

## Décision
Nous ajoutons une nouvelle implémentation concrète :

- `PushNotification(NotificationStrategy)`

Cette classe implémente la méthode :
- `send(user, message)`

Aucune modification n’est apportée :
- ni à `NotificationService` ;
- ni à l’interface `NotificationStrategy` ;
- ni aux stratégies existantes `EmailNotification` et `SmsNotification`.

L’extension se fait uniquement par ajout d’une nouvelle classe conforme au contrat existant.

## Justification
Cette décision valide concrètement le principe Open/Closed :

- le système est **fermé à la modification** du service principal ;
- il est **ouvert à l’extension** par ajout de nouvelles stratégies.

L’architecture issue du refactoring précédent est donc confirmée comme extensible.

Le service métier continue à fonctionner de la même manière :
- il crée le message ;
- il appelle `self.strategy.send(user, message)` ;
- il ne connaît pas le détail du canal utilisé.

## Conséquences positives
- Ajout du push sans régression sur le service métier ;
- Aucun changement de logique dans `NotificationService` ;
- Réutilisation immédiate de l’architecture existante ;
- Validation du choix du pattern Strategy ;
- Meilleure capacité d’évolution future.

## Conséquences négatives
- Chaque nouveau canal ajoute une nouvelle classe ;
- La sélection de la bonne stratégie reste à gérer à l’extérieur du service ;
- Le modèle actuel ne valide pas encore finement les coordonnées requises selon le canal.

## Alternatives envisagées
### 1. Ajouter un nouveau `elif method == "push"` dans l’ancienne version
Rejetée, car cela aurait réintroduit le problème initial.

### 2. Modifier `NotificationService` pour traiter le push directement
Rejetée, car cela casserait le bénéfice du refactoring précédent.

## Décision retenue
Ajouter `PushNotification` comme nouvelle stratégie conforme à `NotificationStrategy`, sans modifier le service métier existant.

## Impacts sur les tests
Les tests doivent démontrer :
- que `EmailNotification` fonctionne toujours ;
- que `SmsNotification` fonctionne toujours ;
- que `PushNotification` fonctionne via le même service ;
- qu’aucune modification n’a été nécessaire dans `NotificationService`.

Exemple de validation :
- `NotificationService(EmailNotification()).send_reminder(user)` retourne `True`
- `NotificationService(SmsNotification()).send_reminder(user)` retourne `True`
- `NotificationService(PushNotification()).send_reminder(user)` retourne `True`