# "Aidez MacGyver à s'échapper !"

**GitHub :** https://github.com/anselmia/MacGyver.git

## **1. Présentation:**

Le but de parcourir un labyrinthe, d'où le héro, Mac Gyver, doit tenter de s’échapper après avoir collectés les différents objets sur la carte et rejoindre la position du garde à l’aide des flèches directionnelles du clavier tout en évitant de croiser les ennemis qui se déplacent !

## **2. Prérequis :**

Installer les dépendances : "pip install -r requirements.txt"
Utiliser python 3

## **3. Paramétrage :**

**Fichier settings :**

* **SIZE_OF_SPRITE :** taille des objets à afficher (côté du carré en pixels).
      Attention toutes les images du jeu doivent avoir le mème format.
* **MAP_PATH :** chemin d'accès vers la carte à utiliser pour   représenter le labyrinthe.
* **FPS :** cadence de la boucle du jeu (en image/s)
* **ENEMY_MOVE_TIME :** période de déplacement des ennemis (en s)
* **NUMBER_OF_TILES :** Nombre d'éléments à trouver sur la carte.
    Attention une spritesheet est utilisée pour charger l'image des objets.
    SIZE_OF_SPRITE et NUMBER_OF_TILES doivent correspondrent au format et au nombre de sprites dans la spritesheet.
* **NUMBER_OF_ENEMIES :** Nombre d'ennemis sur la carte.
    Attention une spritesheet est utilisée pour charger l'image des ennemis.
    SIZE_OF_SPRITE et NUMBER_OF_ENEMIES doivent correspondrent au format et au nombre de sprites dans la spritesheet.
* **Caractères pour interpréter la carte au format text** 
  * **START_CHAR :** position de départ du héro (Attention de ne pas le bloquer)
  * **END_CHAR :** Position du gardien
  * **PATH_CHAR :** chemin permettant de se déplacer
  * **WALL_CHAR :** mur
* **Images du jeu** (Doivent être au format de SIZE_OF_SPRITE)
  * **HERO_IMAGE :** image du héro (format png ou jpg)
  * **FOND_IMAGE :** image du chemin (format png ou jpg)
  * **WALL_IMAGE :** image du mur (format png ou jpg)
  * **GUARDIAN_IMAGE :** image du guardien (format png ou jpg)
  * **TILES_IMAGE :** image des objets (format png ou jpg)
      Attention : Impérativement utilsé un spritesheet dont tous les sprites font la taille de SIZE_OF_SPRITE et sont présents sur la même rangée.
  * **ENEMIES_IMAGE :**  image des ennemis (format png ou jpg)
      Attention : Impérativement utilsé un spritesheet dont tous les sprites font la taille de SIZE_OF_SPRITE et sont présents sur la même rangée.
  * **Musique et son du jeu :**
    * **MUSIC :** musique de fond du jeu (format mp3 ou wav)
    * **SOUND_ITEM :** son lorsqu'un objet est récupéré (format mp3 ou wav)
    * **SOUND_WIN :** son lors de la victoire (format mp3 ou wav)
    * **SOUND_LOOSE :** son lors de la défaite (format mp3 ou wav)

Pour modifier la map, modifier le fichier map.txt. Il faut respecter les caractères définis dans le fichier settings.
Attention à toujours utiliser une et une seule fois les caractères représentant les position de départ et du gardien.

## **4. Lancement du jeu :**

Pour lancer le jeu, il suffit de lancer le fichier *app.py*.
Pour se déplacer, utiliser les touches directionelles du clavier.

#### Bon jeu !
