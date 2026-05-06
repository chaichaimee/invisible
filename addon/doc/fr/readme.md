<p align="center">
  <img src="https://www.nvaccess.org/wp-content/uploads/2015/10/NVDA_logo_standard_transparent.png" alt="Logo NVDA" width="220">
</p>

# Invisible

<p align="center"><i>Faites taire le superflu. Façonnez la voix. Maîtrisez votre expérience de navigation.</i></p>

<p align="center">
  <strong>Auteur :</strong> Chai Chaimee<br>
  <strong>Dépôt :</strong> <a href="https://github.com/chaichaimee/invisible">github.com/chaichaimee/invisible</a>
</p>

---

## Pourquoi s'accommoder de pages Web bruyantes ?

Les sites Web modernes regorgent de répétitions, de mentions publicitaires, d'avis relatifs aux cookies, de compteurs de commentaires, de barres latérales et de contenus générés automatiquement que les lecteurs d'écran doivent lire à haute voix — encore et encore.

**Invisible** vous redonne le contrôle.

Décidez exactement quels mots, phrases ou motifs NVDA doit ignorer complètement — ou remplacez-les discrètement par quelque chose de plus court, de plus propre ou par le silence absolu.

<br><br>

Il ne s'agit pas seulement de filtrage. C'est une **curation audio personnelle** pour le Web.

## Puissant et pourtant élégamment simple

*   Masquer complètement le texte — NVDA agit comme s'il n'avait jamais existé
*   Remplacer les étiquettes agaçantes par de courts indicateurs (« Sponsorisé · Publicité » → « passer »)
*   Appliquer des règles à une page, un domaine entier ou des motifs d'URL complexes (regex)
*   Prise en charge complète des expressions régulières pour une précision chirurgicale
*   Effet instantané — aucun rechargement de page requis
*   Interface contextuelle : le geste double-frappe ouvre « Ajouter un site » avec l'URL actuelle pré-remplie
*   Prise en charge du clic droit + touche Suppr pour une gestion rapide
*   Fichiers .json portables par site — faciles à sauvegarder ou à partager

## Commencez en moins de 30 secondes

1.  Allez sur n'importe quelle page où NVDA lit quelque chose que vous souhaitez faire taire ou modifier.

2.  Appuyez sur **NVDA + Maj + W**<br><br>
    → Simple frappe → ouvre la fenêtre de gestion principale<br>
    → Double frappe (rapide) → ouvre le dialogue « Ajouter un nouveau site » avec l'URL actuelle déjà remplie

3.  Dans le dialogue **Ajouter un site** :<br><br>
    • Conservez ou modifiez le nom d'affichage<br>
    • Choisissez la portée :<br>
    &nbsp;&nbsp;– Page unique uniquement<br>
    &nbsp;&nbsp;– Site Web complet (domaine)<br>
    &nbsp;&nbsp;– Expression régulière (correspondance d'URL avancée)<br><br>
    Cliquez sur **Enregistrer**

4.  Vous êtes maintenant dans le gestionnaire de règles du site :<br><br>
    • Tapez le motif que vous souhaitez cibler<br>
    • Entrez le texte de remplacement — ou laissez vide pour un silence complet<br>
    • Cochez « Utiliser comme expression régulière » si nécessaire<br>
    • Cliquez sur **Ajouter** (ou **Mettre à jour** lors de l'édition)<br><br>
    Les changements s'appliquent instantanément — reprenez votre navigation et écoutez.

<br>

Vous pouvez revenir à tout moment avec **NVDA + Maj + W** (simple frappe) pour éditer, ajouter d'autres règles, supprimer des entrées ou basculer entre les sites.

## Exemples concrets qui font gagner du temps chaque jour

| Motif cible | Remplacement | Regex ? | Ce que vous entendez à la place |
| :--- | :--- | :--- | :--- |
| Publicité | (vide) | Non | — complètement ignoré — |
| Sponsorisé | passer | Non | « passer » |
| · [0-9,]+ commentaires? | (vide) | Oui | — pas de décompte de commentaires — |
| Flash info : | Info : | Non | Plus court et plus propre |
| ^Avis relatif aux cookies.*accepter | (vide) | Oui | Texte de la bannière réduit au silence |

## Conseils de pro pour les utilisateurs avancés

*   Clic droit sur n'importe quel site ou entrée → menu contextuel avec Modifier / Supprimer
*   Appuyez sur la touche **Suppr** sur l'élément sélectionné pour une suppression instantanée
*   Utilise la correspondance littérale de type "plus long en premier" → évite les problèmes de mots partiels
*   Importez des règles d'un autre fichier .json directement dans n'importe quel site
*   Le mode Regex prend en charge les groupes de remplacement — très puissant pour le contenu dynamique

<br><br>

## Me soutenir

Si cet outil vous a facilité la vie, envisagez de soutenir la prochaine mise à jour par un petit don.

<br>

[<img src="https://img.shields.io/badge/Donate-Support%20Me-blue?style=for-the-badge&logo=stripe" alt="Soutenez-moi">](https://buy.stripe.com/dRm9AU1xQ3Ds22N6VK1VK01)

<br>

Votre soutien compte énormément. Construisons quelque chose de formidable ensemble.

<br>

<p align="center">© 2026 Chai Chaimee NVDA Add-on Publié sous licence GNU</p>