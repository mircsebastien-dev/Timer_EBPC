# Manuel utilisateur — Timer Blackball (Timer_EBPC)

## Présentation

Timer Blackball est un chronomètre de compétition pour le billard Blackball, conçu pour un usage sur smartphone : tout tient sur un seul écran, en portrait comme en paysage.

L'écran est divisé en deux moitiés — **équipe A** à gauche (rouge), **équipe B** à droite (bleu) — avec au centre un **cercle** affichant le décompte. L'équipe active au timer est mise en avant visuellement.

## Démarrage rapide

1. Ouvrir la page (index2.html) sur le téléphone.
2. Toucher une fois l'écran pour activer le son (icône 🔊 en haut à droite).
3. Lancer la casse : **toucher le cercle** (ou bouton « ⚡ Casse »).
4. À chaque coup joué : **double-tap sur le cercle** (ou bouton « Nouveau coup ⏭ »).
5. En cas de faute de temps, l'équipe peut demander une extension : **double-tap sur sa moitié**.

## Les gestes

| Zone | Tap simple | Double tap | Triple tap |
|---|---|---|---|
| **Cercle central** | Lancer la casse (avant partie) / **Pause** / Reprendre / Relancer après temps écoulé | **Nouveau coup** (45 s) | — |
| **Moitié A (gauche)** | Sélectionner A comme équipe active | **Extension 30 s pour A** (+ A devient actif) | **Nouveau coup pour A** |
| **Moitié B (droite)** | Sélectionner B comme équipe active | **Extension 30 s pour B** (+ B devient actif) | **Nouveau coup pour B** |

Notes :
- Le double-tap est détecté si les deux taps tombent dans la même zone et dans un délai de ~0,35 s. L'action s'exécute juste après ce délai (le temps de vérifier qu'un triple-tap n'arrive pas).
- Le triple-tap est prioritaire sur le double-tap : trois taps rapides sur une moitié font un nouveau coup, sans consommer l'extension.
- Pendant la **casse**, seule l'équipe A peut recevoir l'extension (c'est toujours A qui casse).

## Les boutons

- **⟲ Reset** (en haut à gauche) : remise à zéro complète — retour à l'état « Prêt », extensions restituées, casse de nouveau disponible.
- **⚡ Casse** (en bas) : lance le compte à rebours de casse (1:30 par défaut). Un seul lancement de casse par reset ; le bouton se désactive ensuite.
- **Nouveau coup ⏭** (en bas) : relance le compteur de coup (45 s par défaut) pour l'équipe sélectionnée. Utilisable dès qu'une partie est lancée, y compris après un temps écoulé.
- **⛶** (en haut à droite) : bascule le plein écran. Sur iPhone, si le plein écran n'est pas supporté, ajouter la page à l'écran d'accueil pour un affichage sans barre d'URL.
- **⚙️** (en haut à droite) : paramètres.

## Les sons

- **Bip d'avertissement** à 25 s restantes (double bip).
- **Compte à rebours final** à 5 s : bips 5-4-3-2-1 puis **buzzer** à 0.
- L'icône en haut à droite indique l'état du son : 🔇 (pas encore déverrouillé — toucher l'écran), ⏳ (sons en cours de chargement), 🔊 (prêt).
- Astuce : si aucun son ne sort après avoir misé l'écran ou changé d'application, **toucher une fois l'écran** — le son se réactive automatiquement au toucher.

## Les extensions

- Chaque équipe dispose d'**une seule extension de 30 s par partie** (par reset).
- Elle s'accorde par **double-tap sur la moitié de l'équipe** : la moitié gauche pour A, la droite pour B — indépendamment de l'équipe actuellement active au timer.
- Le double-tap **sélectionne aussi cette équipe** au timer.
- Une fois utilisée, la pastille ronde en bas de la moitié devient rouge.
- Impossible d'accorder deux extensions à la suite sans nouveau coup entre-temps.

## Écran et consommation

- L'écran reste allumé pendant qu'un chrono tourne (WakeLock) ; la reprise de veille est automatique au retour au premier plan.
- Le site fonctionne en portrait et en paysage (la disposition s'adapte).

## Paramètres (⚙️)

Accessibles via l'icône ⚙️. Les valeurs sont ajustables par curseurs, avec boutons de test sonore :

| Paramètre | Plage | Défaut |
|---|---|---|
| Temps par coup | 30–45 s | 45 s |
| Temps de casse | 45–90 s | 90 s (1:30) |
| Extension | 10–60 s | 30 s |
| Bip d'avertissement | 15–25 s | 25 s |

⚠️ Les paramètres sont stockés pour la **session** en cours : fermer complètement l'onglet ou le navigateur les réinitialise aux valeurs par défaut. Le bouton de test (🔊 Test bip) permet de vérifier le son avant la partie.


## Déroulé type d'une partie

1. **Avant la casse** : « Prêt ». Toucher le cercle (ou ⚡ Casse) → compte à rebours de casse 1:30 pour A.
2. **Pendant la casse** : la moitié A est active. Quand un joueur joue, double-tap cercle → nouveau coup 45 s.
3. **Coup joué** : tap simple sur la moitié du joueur qui prend le trait → l'équipe devient active. Le compteur 45 s tourne.
4. **Chaque coup joué** : double-tap cercle (ou ⏭) pour relancer 45 s. Le compteur repart pour l'équipe active.
5. **Extension** : double-tap sur la moitié de l'équipe → +30 s, l'équipe devient active, pastille rouge allumée.
6. **Temps écoulé** : buzzer, « Temps écoulé » s'affiche. Double-tap cercle (ou ⏭) pour relancer un coup.
7. **Fin de partie** : bouton **⟲ Reset** pour tout remettre à zéro (nouvelle partie, extensions restituées).
