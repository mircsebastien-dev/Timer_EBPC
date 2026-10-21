# Manuel utilisateur — Timer Blackball (Timer_EBPC)

## Présentation

Timer Blackball est un chronomètre de compétition pour le billard Blackball, conçu pour un usage sur smartphone : tout tient sur un seul écran. L'application s'utilise **en portrait uniquement** — en paysage, un écran « Tournez votre téléphone » s'affiche et le chrono est mis en pause.

L'écran est divisé en deux moitiés — **joueur A** à gauche (rouge), **joueur B** à droite (bleu) — avec au centre un **cercle** affichant le décompte. Le joueur actif au timer est mis en avant visuellement.

## Démarrage rapide

1. Ouvrir la page sur le téléphone.
2. Lancer la casse : **toucher le cercle** (ou bouton « ⚡ Casse »).
3. À chaque coup joué : **double-tap sur le cercle** (ou bouton « Nouveau coup ⏭ »).
4. **Pause / Reprise** : **tap simple sur le cercle** pour mettre le chrono en pause ⏸ ; un nouveau tap reprend le décompte ▶.
5. Le joueur peut demander une extension **à tout moment pendant son tour** : **double-tap sur sa moitié**.

## Les gestes

| Zone | Tap simple | Double tap | Triple tap |
|---|---|---|---|
| **Cercle central** | Lancer la casse (avant partie) / **Pause** / Reprendre / Nouveau coup après temps écoulé | **Nouveau coup** (45 s) | — |
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
- **⚙️** (en haut à droite) : paramètres.

## Les sons

- **Bip d'avertissement** à 20 s restantes (double bip) — valeur par défaut, réglable de 15 à 25 s dans les paramètres.
- **Compte à rebours final** à 5 s : bips 5-4-3-2-1 puis **buzzer** à 0.
- Les temps indiqués dans cette section sont les valeurs par défaut ; les valeurs réelles sont celles configurées dans les paramètres.
- L'icône en haut à droite indique l'état du son : 🔇 (pas encore déverrouillé — toucher l'écran), ⏳ (sons en cours de chargement), 🔊 (prêt).
- Astuce : si aucun son ne sort après avoir misé l'écran ou changé d'application, **toucher une fois l'écran** — le son se réactive automatiquement au toucher.

## Les extensions

- Chaque joueur dispose d'**une seule extension de 30 s par partie** (par reset).
- Elle s'accorde par **double-tap sur la moitié de l'équipe** : la moitié gauche pour A, la droite pour B — indépendamment de l'équipe actuellement active au timer.
- Le double-tap **sélectionne aussi cette équipe** au timer.
- Une fois utilisée, la pastille ronde en bas de la moitié devient rouge.
- Impossible d'accorder deux extensions à la suite sans nouveau coup entre-temps.

## Écran et consommation

- L'écran reste allumé pendant qu'un chrono tourne (WakeLock) ; la reprise de veille est automatique au retour au premier plan.
- L'application s'utilise en portrait uniquement : en paysage, un écran « Tournez votre téléphone » s'affiche, le chrono est mis en pause et reprend automatiquement au retour en portrait.

## Paramètres (⚙️)

Accessibles via l'icône ⚙️. Les valeurs sont ajustables par curseurs, avec boutons de test sonore :

| Paramètre | Plage | Défaut |
|---|---|---|
| Temps par coup | 30–45 s | 45 s |
| Temps de casse | 45–90 s | 90 s (1:30) |
| Extension | 10–60 s | 30 s |
| Bip d'avertissement | 15–25 s | 20 s |

⚠️ Les paramètres sont stockés pour la **session** en cours : fermer complètement l'onglet ou le navigateur les réinitialise aux valeurs par défaut. Le bouton de test (🔊 Test bip) permet de vérifier le son avant la partie.


## Déroulé type d'une partie

1. **Avant la casse** : « Prêt ». Toucher le cercle (ou ⚡ Casse) → compte à rebours de casse 1:30 pour A.
2. **Pendant la casse** : la moitié A est active. Quand un joueur joue, double-tap cercle → nouveau coup 45 s.
3. **Coup joué** : tap simple sur la moitié du joueur qui prend le trait → l'équipe devient active. Le compteur 45 s tourne.
4. **Chaque coup joué** : double-tap cercle (ou ⏭) pour relancer 45 s. Le compteur repart pour l'équipe active.
5. **Extension** : double-tap sur la moitié de l'équipe → +30 s, l'équipe devient active, pastille rouge allumée.
6. **Temps écoulé** : buzzer, « Temps écoulé » s'affiche. Double-tap cercle (ou ⏭) pour relancer un coup.
7. **Fin de partie** : bouton **⟲ Reset** pour tout remettre à zéro (nouvelle partie, extensions restituées).
