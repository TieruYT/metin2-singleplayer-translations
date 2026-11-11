# Metin2 Singleplayer - traductions de la communauté

[English](README.md) | [Polski](README_PL.md) | [Türkçe](README_TR.md) | [Deutsch](README_DE.md) | **Français** | [Español](README_ES.md) | [Italiano](README_IT.md) | [Português](README_PT.md) | [Română](README_RO.md) | [Magyar](README_HU.md) | [Nederlands](README_NL.md) | [Čeština](README_CS.md) | [Dansk](README_DA.md) | [Ελληνικά](README_EL.md) | [Русский](README_RU.md) | [العربية](README_AR.md) | [한국어](README_KO.md)

Ce dépôt contient les textes de **Metin2 Singleplayer** - le client du jeu,
les noms des objets et des monstres, les messages du serveur, les quêtes, le
chat des bots, le lanceur Windows et le panneau web classique - afin que les joueurs puissent traduire
le jeu dans leur propre langue. Il ne contient que des traductions : aucun
code du jeu.

Chaque pull request est vérifiée automatiquement, et les traductions acceptées
entrent dans le jeu dans les versions suivantes.

## Ce qu'il y a ici

| dossier | contenu |
|---|---|
| `template/` | tous les textes du jeu, la colonne `translation` vide. Le point de départ d'une nouvelle langue. |
| `de/` `fr/` `pt/` `ro/` `tr/` | les langues que le jeu possède déjà, avec leur traduction actuelle : corrige-la et complète ce qui manque (lignes avec `status` `new`). |
| `hu/` `es/` `it/` `cs/` `nl/` `da/` `el/` `ru/` `ar/` `ko/` | nouvelles langues, entièrement traduites avec l'aide de l'IA : locuteurs natifs, corrigez ce qui sonne faux. |
| `en_US/` | anglais américain : le texte source anglais (orthographe britannique) en orthographe américaine (color, armor, defense...). |
| `tools/validate.py` | la vérification que passe chaque pull request. |

L'anglais est la source et le polonais est affiché à côté comme référence ;
aucun des deux n'a son propre dossier.

Chaque dossier de langue contient les mêmes fichiers CSV, découpés en parties
pour que GitHub puisse les afficher et les modifier (700 lignes au plus par
fichier) :

| fichiers | contenu |
|---|---|
| `1_klient_NN.csv` | le client : fenêtres, boutons, infobulles, compétences, règles |
| `2_przedmioty_potwory_NN.csv` | noms des objets et des monstres, descriptions des objets |
| `3_gra_serwer_NN.csv` | les messages propres au serveur (chat, lignes système) |
| `4_questy_NN.csv` | les dialogues des quêtes |
| `5_boty_czat_NN.csv` | le chat des bots, les bavardages des monstres, les phrases du serveur |
| `6_launcher_NN.csv` | le lanceur Windows |
| `7_panel_NN.csv` | le panneau web classique (le panneau d'administration sur le port 7788, dans le navigateur) |

Chaque fichier a les colonnes :

| colonne | |
|---|---|
| `id` | la clé de la ligne. **Ne jamais la modifier.** |
| `english` | le texte à traduire. **Ne jamais le modifier.** |
| `polski` | le même texte en polonais, comme référence (peut être vide). |
| `translation` | **ta traduction - la seule colonne que tu modifies.** Vide = le jeu affiche l'anglais. |
| `notes` | où le texte apparaît, ce qui doit être conservé, une limite de longueur. |
| `status` | `new` (non traduit), `done` (traduit), `check` (identique à l'anglais - vérifie-le). Tu peux le mettre à `done`. |

## Comment traduire

### A. Dans le navigateur (petites modifications)

1. Ouvre le fichier, par ex. [`fr/1_klient_01.csv`](fr/1_klient_01.csv).
   GitHub l'affiche comme un tableau ; utilise le champ de recherche au-dessus
   pour trouver une ligne.
2. Clique sur le crayon (**Edit this file**). La première fois, GitHub crée
   une copie (un fork) pour toi.
3. Modifie uniquement la colonne `translation` des lignes voulues. Un texte
   contenant une virgule, des guillemets ou un retour à la ligne est entre
   guillemets doubles (`"comme, ceci"`) ; un guillemet à l'intérieur s'écrit
   deux fois (`""`).
4. Clique sur **Commit changes...**, puis **Propose changes**, puis **Create
   pull request**. Dis en une phrase ce que tu as traduit.

### B. Dans un tableur (beaucoup de lignes)

1. Télécharge les fichiers (ouvre un fichier, **Download raw file** ; ou le
   bouton vert **Code**, **Download ZIP**, pour tout).
2. Ouvre-les dans un tableur :
   - **Google Sheets** : Fichier > Importer > Importer. Fonctionne sans réglage.
   - **LibreOffice Calc** : ouvre le fichier ; choisis le jeu de caractères
     **UTF-8**, le séparateur **virgule**, et règle les colonnes sur **Texte**.
   - **Excel** : ne double-clique pas sur le fichier (Excel lirait mal les
     lettres). Utilise Données > À partir d'un fichier texte/CSV, origine du
     fichier **65001 : Unicode (UTF-8)**, délimiteur **Virgule**. Enregistre
     en **CSV UTF-8 (délimité par des virgules)**.
3. Remplis la colonne `translation`. Ne renomme pas les fichiers, n'ajoute ni
   ne supprime de colonnes, ne modifie pas `id` et `english`. Trier et
   filtrer ne pose pas de problème.
4. Enregistre en CSV (UTF-8, séparé par des virgules) sous le même nom.
5. Sur GitHub, ouvre le dossier de la langue, **Add file > Upload files**,
   dépose tes fichiers, puis **Propose changes** et **Create pull request**.

Tu n'as pas besoin de tout traduire d'un coup - envoie ce que tu as.

## Règles

1. **Uniquement la colonne `translation`.** `id` et `english` restent tels
   quels ; la vérification refuse un fichier où ils ont été modifiés.
2. **Garde chaque variable et chaque code exactement comme dans l'anglais,
   dans le même ordre** - ils sont remplis par le jeu :
   - variables printf : `%s` `%d` `%u` `%ld` `%.1f` `%5d` ... et `%%` (un signe pourcent) ;
   - espaces réservés : `{0}` `{#0}` `{name}` `{skrot}` ... ;
   - `[ENTER]` est un retour à la ligne dans une fenêtre de quête ; `[WAIT]`,
     `[DELAY value;5]`, `[COLOR r;1|g;0|b;0]` sont ses commandes ;
   - couleurs `|cffff0000` ... `|r`, liens `|H` ... `|h`, `|E` ... `|e`.

   Tu peux les déplacer dans la phrase selon les besoins de ta langue, mais
   les variables de type `%` doivent rester dans le même ordre. Un texte entre
   crochets comme `[Guild]` ou `[PT]` est du texte ordinaire : traduis-le.
3. **Lettres.** Le jeu affiche chaque langue dans une page de code Windows,
   donc seules ses lettres peuvent être affichées - pas d'emoji, pas de
   symboles comme `→` ou `✓` :

   | page de code | langues | lettres |
   |---|---|---|
   | 1250 | pl, cs, sk, hu, ro, hr, sl, sr (latin), bs, sq | ą ć ę ł ń ó ś ź ż, á č ď é ě í ň ř š ť ú ů ý ž, ő ű, ă â î ş ţ |
   | 1251 | ru, uk, bg, be, mk, sr (cyrillique) | а б в г д ... я, є і ї ґ, ў, ђ ј љ њ ћ џ |
   | 1252 | de, fr, es, it, pt, nl, da, sv, no, fi, ca, id ... | à á â ã ä å æ ç è é ê ë ì í î ï ñ ò ó ô õ ö ø ù ú û ü ß œ |
   | 1253 | el | α β γ δ ... ω, ά έ ή ί ό ύ ώ |
   | 1254 | tr, az | ç ğ ı İ ö ş ü, â î û |
   | 1257 | lt, lv, et | ā č ē ģ ī ķ ļ ņ š ū ž, ą ę ė į ų |

   Roumain : la page de code n'a que **ş ţ avec cédille**, pas ș ț avec
   virgule. Le lanceur (`6_launcher_*`) est un programme Windows à part et
   accepte toutes les lettres. Le panneau web (`7_panel_*`), une page dans le
   navigateur, aussi : les deux sont en **UTF-8**, toute lettre de toute langue.
4. **Le chat des bots** (lignes dont les notes disent « ASCII letters
   only ») : les bots écrivent comme des joueurs, en lettres simples a-z sans
   accents.
5. **Longueur.** Là où les notes disent « max N characters », le jeu n'a pas
   de place pour plus.
6. **Retours à la ligne** uniquement là où l'anglais en a ou où les notes
   disent « new lines allowed ».
7. **Le panneau web** (`7_panel_*`) : ses textes vont dans une page web, alors
   garde les balises HTML de l'anglais exactement telles quelles (`<b>`, `</b>`,
   `<a href="...">`, `<br>` et les espaces réservés du type `<number>` entre
   chevrons) et n'ajoute aucun `<`, `>` ou `javascript:` de ton cru. Ses
   variables sont `%s`, `%d`, `%(name)s` et `{name}` ; un `%(name)s` nommé peut
   changer de place. Un `%` suivi d'une espace (`25% a character`) est un signe
   pour cent. Une langue avec au moins un texte du panneau traduit apparaît dans
   le choix de langue du panneau ; ce qui n'est pas traduit s'affiche en anglais.

## Une nouvelle langue

1. Copie tout le dossier `template/` dans un dossier nommé avec le code ISO
   639-1 à deux lettres de ta langue (`hu`, `es`, `cs`, `pl`... - voir
   [la liste](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes)).
   Tu peux le faire dans un tableur : télécharge `template/`, traduis, puis
   envoie les fichiers dans le nouveau dossier (**Add file > Upload files**,
   tape `xx/` devant le nom pour créer le dossier).
2. Traduis et ouvre une pull request.

Une nouvelle langue demande un peu de travail dans le jeu avant que les
joueurs puissent la choisir (les langues hors de la page de code 1250 ont
aussi besoin d'un nouveau client), elle peut donc arriver quelques versions
après la première traduction.

## La vérification

Chaque pull request exécute `tools/validate.py` (GitHub Actions). Elle
signale, à la ligne où elle l'a trouvé :

- un `id` absent de `template/`, ou présent deux fois ;
- une colonne `english` modifiée ;
- des variables, espaces réservés, balises ou codes couleur différents de
  l'anglais ;
- dans la feuille du panneau web, d'autres balises HTML que l'anglais, ou un
  `<`, `>` ou `javascript:` de son cru ;
- une lettre hors de la page de code de la langue, une tabulation, un
  caractère de contrôle, un retour à la ligne là où il n'est pas permis, un
  texte trop long.

Seules les lignes modifiées par ta pull request sont jugées ; les problèmes
déjà présents dans les fichiers sont comptés, pas retenus contre toi. Pour la
lancer toi-même (Python 3, rien à installer) : `python tools/validate.py fr`.

## Licence

En ouvrant une pull request, tu acceptes que ta traduction soit utilisée dans
Metin2 Singleplayer et partagée aux mêmes conditions que le projet :
[CC BY-NC-ND 4.0](LICENSE). Les contributeurs sont crédités dans le projet.
Metin2 lui-même et ses textes originaux appartiennent à Ymir Interactive et
Webzen.
