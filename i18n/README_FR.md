# Le blog Rublog, Le dépôt Github

Ce projet s'inspire de [WordPressXMLRPCTools](https://github.com/zhaoolee/WordPressXMLRPCTools), ce qui m'a fourni des idées.

Étant donné que je n'aime pas xmlrpc, j'utilise donc l'API Rest de WordPress pour la mise à jour.

La bibliothèque API de WordPress provient de [wordpress-markdown-blog-loader](https://github.com/binxio/wordpress-markdown-blog-loader), avec de légères modifications.

[Cliquez ici pour sauter le sommaire du blog et voir les instructions de dépôt.](#Écrire des articles Markdown avec Github Actions et les mettre à jour automatiquement sur WordPress)

[Cliquez ici, Instructions d'utilisation de l'entrepôt](#Guide d'utilisation)

[中文简体](../README.md) --- [English](README_EN.md) --- [Deutsch](README_DE.md) --- [Français](README_FR.md) --- [Español](README_ES.md) --- [Русский](README_RU.md) --- [繁體中文](README_ZH-CHT.md) --- [日本語](README_JP.md)

---start---

## Table des matières (mis à jour le 27 juillet 2024)

[Comment utiliser GitHub Actions pour publier des articles Markdown sur un site WordPress](https://www.rxx0.com/?p=4150) &emsp; &emsp; Date de publication : 27 juillet 2024 - 05:24

[Astuces pour déboguer les GitHub Actions avec act](https://www.rxx0.com/software/diao-shi-github-actions-de-4-chong-gong-ju.html)  
Date de publication : 27 juillet 2024 - 04:55

[Deux méthodes pour résoudre le problème de Permission denied (publickey) lorsque SourceTree se connecte à GitHub via SSH](https://www.rxx0.com/software/liang-chong-fang-fa-jie-jue-sourcetree-tong-guo-ssh-lian-jie-github-permission-denied-publickey-wen-ti.html)

Date de publication : 26 juillet 2024 - 10:58

[Test de la publication automatique d'articles avec Python & Markdown](https://www.rxx0.com/software/test-python-and-markdown-to-automatically-publish-articles.html)&emsp; &emsp; Date de publication : 24 juillet 2024 - 16:10

---End---  

## Écrire des articles Markdown avec Github Actions et les mettre à jour automatiquement sur WordPress

- Le format le plus confortable pour écrire un blog est Markdown ;

- La manière la plus stress - free de gérer un blog est WordPress ;

- La meilleure plateforme pour promouvoir un blog est Github.

Ce projet vous permet d'écrire des blogs avec Markdown. Après avoir poussé (push) les mises à jour vers Github, Github Actions met automatiquement les articles à jour sur WordPress et met également à jour l'URL de l'article dans README.md.

![Instructions du dépôt (repo 为英文“repurchase agreement”缩写，这里按“回购协议说明”推测来翻译，“dépôt”在金融领域有类似含义，如果 repo 还有其他特定含义，可能需要调整。 若单纯 “说明” 翻译为“Instructions” 或 “Explications” 都可以)

如果 “repo” 是一个产品或系统特定名称等，不做翻译，可译为：Instructions de repo  ](../posted/readme/images/rxx0_2024-07-25_21-55-47.png)

### Quels sont les avantages d'utiliser Github Actions?

Github Actions nous permet d'exécuter le code sans avoir à installer d'environnement de développement.

![Exécution d'Actions GitHub](../posted/readme/images/rxx0_2024-07-25_22-06-46.png)

Il suffit de créer un nouvel article Markdown, puis de le mettre à jour dans le dépôt. Github Actions mettra automatiquement l'article à jour sur WordPress et mettra à jour le lien de l'article dans README.md.

![Mettre à jour le lien de l'article dans le readme](../posted/readme/images/rxx0_2024-07-25_22-09-41.png)

## Guide d'utilisation

### Les plugins à installer pour WordPress

- [Rankmath](https://rankmath.com/wordpress/plugin/seo-suite) Plugin SEO

### Obtenir la configuration de WordPress nécessaire

Ce qui est soumis à un traitement particulier est uniquement le mot de passe de connexion de WordPress. Ce mot de passe de connexion n'est pas le mot de passe du backend pour se connecter à la page web. Il est nécessaire de générer séparément un mot de passe d'application RestAPI.

Les mots de passe d'application permettent d'authentifier via des systèmes non interactifs (tels que XML-RPC ou l'API REST) sans avoir à fournir votre mot de passe réel. Les mots de passe d'application peuvent être révoqués à tout moment. Ils ne peuvent pas être utilisés pour vous connecter à votre site web de manière traditionnelle.

Le mode de génération est le suivant :

![Générer un mot de passe d'application RestAPI](../posted/readme/images/rxx0_2025-03-01_09-03-37.png)

![Générer un mot de passe d'application RestAPI](../posted/readme/images/rxx0_2025-03-01_10-36-02.png)

### Comment protéger le mot de passe de son compte WordPress?

Github dispose d'une fonction de secrets qui peut protéger les informations clés telles que le nom d'utilisateur et le mot de passe. Seules les Github Actions peuvent accéder à ces informations clés.

Ce projet nécessite la configuration de trois secrets.

- Remplissez le nom d'utilisateur de connexion à WordPress. Le nom de variable est USERNAME.
- Remplissez le mot de passe de l'application WordPress RestAPI. Le nom de variable est PASSWORD.
- Renseignez le nom de domaine de WordPress. Le nom de variable est HOST.

![le secret nécessaire pour l'entrepôt](../posted/readme/images/rxx0_2024-07-27_11-07-35.png)

### Autoriser Github Actions à écrire de nouveau dans le dépôt

Les fonctionnalités de protection de sécurité de Github deviennent de plus en plus complètes. Il est nécessaire d'accorder ce droit séparément. Les méthodes d'ouverture sont les suivantes :

![Le droit d'écriture inverse nécessaire pour l'entrepôt](../posted/readme/images/rxx0_2024-07-27_11-45-46.png)

### Comment créer un nouvel article?

Renommez le dossier `example` dans le répertoire `posted`, copiez-le dans le dossier `need_post` et continuez d'éditer le fichier Markdown `index.md` dans le dossier.

Le dossier "images" stocke les images citées, ou vous pouvez directement citer des images du Web, des images CDN ou des images hébergées sur des plateformes d'hébergement d'images.

![Comment créer un nouvel article](../posted/readme/images/rxx0_2024-07-25_22-15-07.png)

### Gestion des articles : Comment classifier les articles et ajouter des étiquettes de mots-clés?

Dans le haut du fichier `.md`, remplissez les informations d'initialisation suivantes pour terminer la configuration du titre (title), des étiquettes (tags) et des catégories (categories). **Tout le contenu ci - dessous est obligatoire.**

```tag and category
author: xinyu2ru
categories:
- logiciel
date: 2024-07-24 08:21:00
excerpt: Écrivez ici le résumé de l'article. Ce paragraphe devrait apparaître dans le résumé de l'article.
image: images/banner.jpg
status: publier
title: Écrivez ici le titre de l'article
focus-keywords: markdown upload wordpress
```

- **L'auteur doit exister**
- Le répertoire de catégories de "categories" doit obligatoirement exister.
- L'image de la bannière doit obligatoirement exister.

## Quelle est la différence entre les étiquettes (tags) et les catégories?

Les étiquettes (tags) sont des mots clés pour un article individuel. Par exemple, les étiquettes de la banane sont **jaune**, **sucrée** (les étiquettes sont les attributs de la banane).
La classification (catégories) est l'attribution de cet article. Par exemple, la classification de la banane est **fruit**, **plante**

## Comment l'utiliser?

Après avoir terminé les configurations ci-dessus

Chaque fois que vous ajoutez ou mettez à jour un article dans le dossier `need_post`, il suffit d'exécuter les instructions git!

```git
git pull && git add _posts && git commit -m "update" && git push

```

On peut également utiliser divers logiciels de gestion de Git pour soumettre les mises à jour sur GitHub.

### L'effet d'affichage du README.md de Github, (les articles nouvellement ajoutés sont classés en tête)

![Mettre à jour le lien de l'article dans le readme](../posted/readme/images/rxx0_2024-07-25_22-09-41.png)

## Comment effectuer l'opération de mise à jour du blog avec un téléphone portable?

Pomme de pin Note permet d'écrire en Markdown de manière élégante et confortable.

说明：“锤子便签”官方英文名为“Pomme de pin Note ”  ，如果这里不按官方的来，“锤子”直译为“Marteau”  ，即“Marteau Note permet d'écrire en Markdown de manière élégante et confortable.”  也可以。  

Obsidian, est également le logiciel d'édition que j'utilise principalement actuellement. Il est disponible sur ordinateur et sur téléphone portable.

## Mettre à jour

- Le plugin SEO a été changé de Yoast à Rank Math (le 11 février 2025 à 11:51)
- Mettre à jour ce fichier README (1er mars 2025 09:32)
