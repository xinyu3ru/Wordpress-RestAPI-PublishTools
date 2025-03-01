# Rublog-Blog, Github-Repository

Dieses Projekt basiert auf [WordPressXMLRPCTools](https://github.com/zhaoolee/WordPressXMLRPCTools) und hat mir die Inspiration gegeben.  

Angesichts dessen, dass ich xmlrpc nicht mag, nutze ich die RestAPI von WordPress zum Update.

Die WordPress API-Bibliothek stammt von [wordpress-markdown-blog-loader](https://github.com/binxio/wordpress-markdown-blog-loader) und wurde leicht modifiziert.

[Klicken Sie hier, überspringen Sie das Blog-Inhaltsverzeichnis und sehen Sie die Beschreibung des Ladenspeichers.](#Markdown-Artikel mit Github Actions schreiben und automatisch auf WordPress aktualisieren)

[Klicken Sie hier, Anweisungen zur Lagerbenutzung](#bedienungsanleitung)

[中文简体](../README.md) --- [English](README_EN.md) --- [Deutsch](README_DE.md) --- [Français](README_FR.md) --- [Español](README_ES.md) --- [Русский](README_RU.md) --- [繁體中文](README_ZH-CHT.md) --- [日本語](README_JP.md)

---start---

## Inhaltsverzeichnis (aktualisiert am 27. Juli 2024)

[Wie man mit GitHub Actions Markdown-Artikel auf eine WordPress-Website veröffentlicht](https://www.rxx0.com/?p=4150)&emsp; &emsp; Veröffentlichungsdatum: 27. Juli 2024 - 05:24

[Tricks zum Debuggen von GitHub Actions mit act](https://www.rxx0.com/software/diao-shi-github-actions-de-4-chong-gong-ju.html)  
Veröffentlichungsdatum: 27. Juli 2024 - 04:55

[Zwei Methoden zur Lösung des Problems "Permission denied (publickey)" bei der SSH-Verbindung von SourceTree mit GitHub](https://www.rxx0.com/software/liang-chong-fang-fa-jie-jue-sourcetree-tong-guo-ssh-lian-jie-github-permission-denied-publickey-wen-ti.html)  
Veröffentlichungsdatum: 26. Juli 2024 - 10:58  

[Test von Python & Markdown zur automatischen Veröffentlichung von Artikeln](https://www.rxx0.com/software/test-python-and-markdown-to-automatically-publish-articles.html) &emsp; &emsp; Veröffentlichungszeit: 24. Juli 2024 - 16:10

---End---  

## Markdown-Artikel mit Github Actions schreiben und automatisch auf WordPress aktualisieren

- Das bequemste Format zum Schreiben von Blogs ist Markdown.

- Die bequemste Methode, eine Blogseite zu verwalten, ist WordPress.

- Die beste Plattform, um eine Blog-Website zu promovieren, ist Github.

Dieses Projekt ermöglicht es Ihnen, Blogs in Markdown zu schreiben. Nachdem Sie die Aktualisierungen auf Github gepusht haben, aktualisiert Github Actions automatisch die Artikel auf WordPress und aktualisiert die Artikel-URL in der README.md.

![Repo-Beschreibung](../posted/readme/images/rxx0_2024-07-25_21-55-47.png)

### Was sind die Vorteile der Verwendung von Github Actions?

Github Actions ermöglicht es uns, den Code auszuführen, ohne eine Entwicklungsumgebung installieren zu müssen.

![github actions laufen ](../posted/readme/images/rxx0_2024-07-25_22-06-46.png)

Man muss nur eine neue Markdown-Datei erstellen und diese in das Repository aktualisieren. Github Actions wird die Datei automatisch auf WordPress aktualisieren und den Link zur Datei in der README.md aktualisieren.

![Aktualisiere den Artikellink im README](../posted/readme/images/rxx0_2024-07-25_22-09-41.png)

## Bedienungsanleitung

### Die Plugins, die für WordPress installiert werden müssen

- [Rankmath](https://rankmath.com/wordpress/plugin/seo-suite) SEO-Plugin

### Den benötigten WordPress-Konfigurationseintrag erhalten

Besondere Behandlung findet nur für das WordPress-Anmelde-Passwort statt. Dieses Anmelde-Passwort ist nicht das Hintergrund-Passwort für die Webseite-Anmeldung. Es ist erforderlich, ein separates RestAPI-Anwendungspasswort zu generieren.

Anwendungs-Passwörter ermöglichen die Authentifizierung über nicht interaktive Systeme wie XML-RPC oder REST API, ohne dass Sie Ihr tatsächliches Passwort angeben müssen. Anwendungs-Passwörter können jederzeit widerrufen werden. Sie können nicht verwendet werden, um auf Ihre Website auf traditionelle Weise einzuloggen.

Die Generierungsweise ist wie folgt:

![Generieren Sie ein RestAPI-Anwendungskennwort](../posted/readme/images/rxx0_2025-03-01_09-03-37.png)

![Generieren Sie ein RestAPI-Anwendungskennwort](../posted/readme/images/rxx0_2025-03-01_10-36-02.png)

### Wie schützt man das Passwort seines WordPress-Kontos?

Github hat eine Secrets - Funktion, mit der sensible Informationen wie Benutzernamen und Passwörter geschützt werden können. Nur Github Actions kann auf diese sensiblen Informationen zugreifen.

Für dieses Projekt müssen drei Secrets eingerichtet werden.

- Füllen Sie den Anmeldenamen für WordPress aus. Der Variablenname lautet USERNAME.
- Füllen Sie das Anwendungspasswort der WordPress RestAPI aus. Der Variablenname ist PASSWORD.
- Füllen Sie die Domain von WordPress aus. Der Variablenname ist HOST.

![Das, was der Lagerhaus benötigt, ist das Geheimnis.  ](../posted/readme/images/rxx0_2024-07-27_11-07-35.png)

### Erlaube es, dass Github Actions in das Repository zurückschreibt

Die Sicherungseigenschaften von Github werden immer vollständiger. Es ist erforderlich, diese Berechtigung separat zu erteilen. Die Öffnungsweise ist wie folgt:

![Die Rückschreiberecht, das das Lager benötigt](../posted/readme/images/rxx0_2024-07-27_11-45-46.png)

### Wie erstelle ich einen neuen Artikel?

Benennen Sie den Ordner `example` im Verzeichnis `posted` um, kopieren Sie ihn in den Ordner `need_post` und bearbeiten Sie weiterhin die `index.md`-Markdown-Datei im Ordner.

Das images -Verzeichnis enthält die verlinkten Bilder oder verwendet direkt Netzwerkbilder, CDN -Bilder oder Bilder aus einem Bildhosting -Service.

![Wie erstelle ich einen neuen Artikel?](../posted/readme/images/rxx0_2024-07-25_22-15-07.png)

### Artikelverwaltung: Wie kann man Artikel kategorisieren und Schlüsselworttags hinzufügen?

Füllen Sie die folgenden Initialisierungsinformationen am Anfang der `.md`-Datei aus, um die Einstellungen für Titel (title), Tags (tags) und Kategorien (categories) abzuschließen. **Alle folgenden Inhalte sind erforderliche Felder**.

```tag and category
author: xinyu2ru
categories:
- software
date: 2024-07-24 08:21:00
excerpt: Hier wird der Abstract des Artikels geschrieben. Dieser Text sollte im Artikelabstract erscheinen.
image: images/banner.jpg
status: publish
title: Hier wird der Titel des Artikels geschrieben
focus-keywords: markdown upload wordpress
```

- author muss vorhanden sein
- Das Kategorieverzeichnis von "categories" muss vorhanden sein.
- Das Banner-Bild muss vorhanden sein.

## Was ist der Unterschied zwischen Tags und Kategorien?

Tags sind Schlagwörter für einzelne Artikel. Beispielsweise haben die Tags für Banane **gelb**, **süß** (Tags sind die Eigenschaften der Banane).
Kategorien sind die Zugehörigkeit dieses Artikels. Beispielsweise gehört die Kategorie der Banane zu **Obst** und **Pflanze**.

## Wie wird es verwendet?

Nach Abschluss der obigen Konfiguration

Jedes Mal nachdem Sie einen Artikel im Ordner `need_post` neu hinzufügen oder aktualisieren, können Sie einfach die Git-Befehle ausführen!

```git
git pull && git add _posts && git commit -m "Aktualisierung" && git push
```

Man kann auch verschiedene Git-Verwaltungsprogramme verwenden, um die Aktualisierungen auf GitHub einzureichen.

### Die Anzeigeeffekte von der README.md auf Github (Die neu hinzugefügten Artikel stehen an erster Stelle)

![Aktualisiere den Artikellink in der README](../posted/readme/images/rxx0_2024-07-25_22-09-41.png)

## Wie kann man die Aktualisierung eines Blogs mit einem Mobiltelefon durchführen?

Hammer Notes ermöglicht es, Markdown auf elegant und bequeme Weise zu schreiben.  

Obsidian, das ist auch das Hauptbearbeitungsprogramm, das ich derzeit verwende. Es kann sowohl auf dem Computer als auch auf dem Handy genutzt werden.

## Aktualisierung

- Das SEO-Plugin wurde von Yoast auf Rank Math geändert (11. Februar 2025, 11:51)
- Aktualisiere diese README-Datei (1. März 2025 09:32)
