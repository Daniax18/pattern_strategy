# ADR — Module de notifications bibliothèque

## Liste des décisions
- ADR-001 : Implémentation initiale avec logique conditionnelle
- ADR-002 : Refactoring avec le pattern Strategy
- ADR-003 : Ajout du canal Push sans modification du service métier

## Résumé
Le module a évolué en trois étapes :
1. une première version simple avec `if/elif` dans `NotificationService` ;
2. un refactoring vers une abstraction `NotificationStrategy` ;
3. une extension par ajout de `PushNotification` sans modification du service principal.

## Fichiers concernés
- `models/user.py`
- `services/notification_service.py`
- `services/strategies.py`
- `tests/test_notifications.py`
- `main.py`