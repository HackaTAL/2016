![HACKATAL 2016](https://raw.githubusercontent.com/HackaTAL/2016/gh-pages/hackatal2016.jpg)

# HACKATAL 2016
---------------
**(hackathon dans le domaine du TAL)**

[![Google](https://raw.githubusercontent.com/HackaTAL/2016/gh-pages/logo-google.png)](http://www.google.fr)
[![Systran](https://raw.githubusercontent.com/HackaTAL/2016/gh-pages/logo-systran.png)](http://www.systran.fr)
[![Recast](https://raw.githubusercontent.com/HackaTAL/2016/gh-pages/logo-recast.png)](http://www.recast.ai)

[![Inalco](https://raw.githubusercontent.com/HackaTAL/2016/gh-pages/logo-inalco.png)](http://www.inalco.fr)
[![LIMSI](https://raw.githubusercontent.com/HackaTAL/2016/gh-pages/logo-limsi.png)](http://www.limsi.fr)
[![LIPN](https://raw.githubusercontent.com/HackaTAL/2016/gh-pages/logo-lipn.png)](http://lipn.univ-paris13.fr)
[![Vocal Apps](https://raw.githubusercontent.com/HackaTAL/2016/gh-pages/logo-vocalapps.png)](http://vocal-apps.com)

### TL;DR

Sujet : recherche d’information (détection d’évènements sportifs et développement de chatbots)  
Thématique : Euro 2016  
Site web : http://hackatal.github.io/2016  
Dates : 2-3-4 juillet 2016  
Lieu : [Google Paris, 8 rue de Londres, Paris 9ème](https://goo.gl/maps/yPgc5XcT5B92)  
Les inscriptions sont terminées...  
Repas (samedi soir, dimanche midi) et boissons (bières, pauses cafés, jus, etc) fournis

### Description

Dans le cadre de la conférence jointe JEP-TALN-RECITAL 2016, aura lieu la première édition de HackaTAL, un hackathon sur des problématiques liées au TAL. L’objectif est de réunir la communauté autour de données et de briques logicielles pour échanger, modéliser, prototyper, coder, implémenter, développer, expérimenter, tester, évaluer... et bien plus encore !

Les tâches proposées concernent la détection d'évènement et l'implémentation de système de gestion de dialogue. La thématique retenue est l’Euro 2016 (qui a lieu du 10 juin au 10 juillet), ce qui permettra d'apporter un cas d'application pratique, des données (tweets et données structurées) et pourrait également rendre possible des expériences en quasi-temps-réel.

### Tâches

**1. Détection d’évènements**

*Description*

Détection d’évènements et/ou de faits saillants liés à la compétition sportive à partir de tweets collectés dans différentes langues (français, anglais et arabe). L'objectif est de de mettre en place des approches innovantes de détection d’évènements dont les expérimentations et résultats seront discutés lors de l’atelier TALN (le 4 juillet). Les évènements extraits peuvent être liés au sport en lui-même (composition d’équipes, résultats de matches, etc.) ou satellites (scandales, rumeurs, suspicion de triche ou de dopage, insultes).

*Sous tâches*

- prétraitements et annotation des tweets (entités, relations, citations, opinions, etc.),
- classification non-supervisée des tweets (clustering),
- détection supervisée ou non d'évènements,
- visualisation graphique des tweets et évènements détectés.

*Données*

- [Tweets fournis pas Systran sur l'Euro 2016](http://helium.lab.parisdescartes.fr:2232/tweets/train_euro2016/)
- [README](http://helium.lab.parisdescartes.fr:2232/tweets/train_euro2016/README.txt)

**2. Gestion de dialogues**

*Description*

Développer un assistant dialogique répondant à des requêtes en langue naturelle sur le domaine du football et de l’euro 2016. L'objectif est d'implémenter des agents conversationnels simples (chatbots) qui interagissent avec des humains et peuvent déclencher des actions sur la plateforme (obtenir des informations sur les matches, équipes et joueurs, jouer des vidéos, avertir lors de faits marquants). Ils pourront s'appuyer sur toute base de donnée structurée disponible décrivant la compétition et les évènements qui y sont liés.

*Sous tâches*

- développement d'interfaces web pour l'interaction,
- traitements TAL de l'entrée utilisateur avec une visée de compréhension (NLU),
- implémentation du module de gestion du dialogue (état, interaction, transitions),
- implémentation du module de génération de texte.

*Ébauche de système*

- [Interface web simple en JS (chat et chargeuur d'images/video)](bot-slack)
- [Architecture de base pour faire un bot Slack avec Node.js](bot-web-chat)

### Prix SYSTRAN

Un prix sera décerné à l’issue du HackaTAL pour récompenser les approches les plus innovantes et/ou performantes.

Systran offrira au gagnat un voyage pour deux à San Diego, vols et nuits hôtels pour 1 semaine (conditions et dates à définir) !

### Planning prévisionnel

Cet évènement se tiendra du 2 au 4 juillet 2016, chez Google et à l'Inalco.

**Attention** Pour des questions de logistique et de sécurité, merci de vous présenter chez Google préférentiellement aux horaires suivants : le samedi à 14h, à 16h ou à 19h et dimanche à 9h, 12h ou 15h.

Samedi 2 juillet ([Google Paris, 8 rue de Londres, Paris 9ème](https://goo.gl/maps/yPgc5XcT5B92))

- 14h-15h : présentation du hackathon, café
- 15h-16h : précisions sur les objectifs, échanges, constitution d'équipes
- 16h-19h : développements en équipes
- 19h-20h : présentations scientifiques et technologiques
- 20h-21h : pause repas
- 21h-00h : développements en équipes

Dimanche 3 juillet ([Google Paris, 8 rue de Londres, Paris 9ème](https://goo.gl/maps/yPgc5XcT5B92))

- 09h-10h : accueil, café
- 10h-12h : développements en équipes
- 12h-13h : pause repas
- 13h-14h : présentation des premiers résultats
- 14h-19h : développements en équipes

Lundi 4 juillet ([Inalco, 65 rue des granfs moulins, Paris 13ème](https://goo.gl/maps/rZd6MBx5tR32) salle 5.18)

- 14h-17h : présentation des résultats, discussions, remise de prix

### Organisation pratique

BYOD (amenez votre ordinateur)  
Pas de critères pour participer, HackaTAL est ouvert à tous !  
Aucune préparation n'est requise de la part des participants en amont de l'évènement.  
Données et logiciels seront mis à disposition sur https://github.com/HackaTAL/2016  
Nourritures et boissons gracieusement offerts par nos hôtes - merci Google !  

### Organisateurs

- Jasmine Anteunis (Recast)
- Guillaume Dubuisson Duplessis (LIMSI)
- Joseph Le Roux (LIPN)
- Djamel Mostefa (Systran)
- Damien Nouvel (ERTIM)
- Alexander Pak (Google)
- Amandine Périnet (Adecco for Google)
- Paul Renvoise (Recast)
- Hicham Tahiri (Vocal Apps)
- Nadi Tomeh (LIPN)
- Guillaume Wisniewski (LIMSI)

[![Cap Digital](https://raw.githubusercontent.com/HackaTAL/2016/gh-pages/logo-capdigital.png)](http://www.capdigital.com)
Cap Digital est partenaire de l'évènement
