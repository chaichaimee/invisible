<div align="center">
  <img src="https://www.nvaccess.org/wp-content/uploads/2015/10/NVDA_logo_standard_transparent.png" alt="NVDA Logo" width="220">
</div>

# Invisible

*Faites taire le bruit. Façonnez la voix. Prenez le contrôle de votre navigation.*

**Auteur :** Chai Chaimee  
**Dépôt :** [github.com/chaichaimee/invisible](https://github.com/chaichaimee/invisible)

---

## Pourquoi se contenter de pages web bruyantes ?

Les sites web modernes regorgent de répétitions, mentions sponsorisées, bannières de cookies, compteurs de commentaires, barres latérales et contenu généré automatiquement que les lecteurs d'écran doivent lire à voix haute — encore et encore.

**Invisible** vous redonne le contrôle.

Décidez exactement quels mots, phrases ou motifs NVDA doit ignorer totalement — ou remplacer discrètement par quelque chose de plus court, plus propre ou totalement silencieux.

Ce n'est pas seulement du filtrage. C'est une **curation audio personnelle** pour le web.

## Puissant mais élégamment simple

- Masquer le texte complètement — NVDA se comporte comme s'il n'avait jamais existé
- Remplacer les étiquettes gênantes par des marqueurs courts (« Sponsored · Advertisement » → « skip »)
- Appliquer les règles à une seule page, un domaine entier ou des motifs URL complexes (regex)
- Support complet des expressions régulières pour une précision chirurgicale
- Effet instantané — pas besoin de recharger la page
- Interface contextuelle : double appui ouvre « Ajouter un site » avec l'URL actuelle préremplie
- Support clic droit + touche Suppr pour une gestion rapide
- Fichiers .json portables par site — faciles à sauvegarder ou partager

## Commencez en moins de 30 secondes

1. Allez sur n'importe quelle page où NVDA lit quelque chose que vous voulez faire taire ou modifier.

2. Appuyez sur **NVDA + Shift + W**  
   - Appui simple → ouvre la fenêtre principale de gestion  
   - Double appui (rapide) → ouvre la boîte de dialogue « Ajouter un site » avec l'URL actuelle déjà remplie

3. Dans la boîte de dialogue **Ajouter un site** :  
   - Conservez ou modifiez le nom affiché  
   - Choisissez la portée :  
     - Page unique uniquement  
     - Site entier (domaine)  
     - Expression régulière (correspondance URL avancée)  
   - Cliquez sur **Enregistrer**

4. Vous êtes maintenant dans le gestionnaire de règles du site :  
   - Saisissez le motif à cibler  
   - Entrez le texte de remplacement — ou laissez vide pour un silence total  
   - Cochez « Utiliser comme expression régulière » si nécessaire  
   - Cliquez sur **Ajouter** (ou **Mettre à jour** lors de l'édition)  
   Les modifications s'appliquent instantanément — retournez naviguer et écouter.

Vous pouvez revenir à tout moment avec **NVDA+Shift+W** (appui simple) pour modifier, ajouter des règles, supprimer des entrées ou changer de site.

## Exemples concrets qui font gagner du temps tous les jours

| Motif cible                 | Remplacement  | Regex ? | Ce que vous entendez à la place |
|-----------------------------|---------------|---------|---------------------------------|
| Advertisement               | (vide)        | Non     | — complètement ignoré —         |
| Sponsored                   | skip          | Non     | « skip »                        |
| · [0-9,]+ comments?         | (vide)        | Oui     | — pas de compte de commentaires |
| Breaking News:              | News:         | Non     | Plus court et propre            |
| ^Cookie notice.*accept      | (vide)        | Oui     | Bannière silencée               |

## Astuces pro pour utilisateurs avancés

- Clic droit sur un site ou une entrée → menu contextuel Éditer / Supprimer
- Appuyez sur la touche **Suppr** sur l'élément sélectionné pour suppression instantanée
- Utilisez la correspondance littérale la plus longue en premier → évite les problèmes de mots partiels
- Importez des règles depuis un autre fichier .json directement dans n'importe quel site
- Le mode regex supporte les groupes de remplacement — très puissant pour le contenu dynamique

## Soutenez le projet

Si Invisible a amélioré votre expérience de navigation quotidienne, envisagez de soutenir son développement continu.

[**Faire un don via GitHub Sponsors**](https://github.com/chaichaimee)

---

© 2026 Chai Chaimee · Extension NVDA Invisible · Publiée sous GNU GPL v2+