Pré requis, avoir un jre 1.7 installé et les crédentials d'identtification à  Twitter.

1-⁠détarrer
2 Se placer à la racine du jar
3 Mettre à jour le fichier de propriétés App.properties 
4 Exécuter : java -jar tweet_basic-retriever.jar

Afin de créer les crédentials d'identtification à  Twitter, il faut créer une application Twitter en suivant les étapes suivantes:
⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠
1) go to t URL: https://apps.twitter.com/

select: create twitter application
fill in form then agree then ok

-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠
2) IF you are asked for a portable phone number,
   in another web browser window, add portable phone number to your
   twitter account:  https://twitter.com/settings/devices

-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠-⁠
3) once you application is create you should get the following information

with in particular the two following keys:

App.TwitterConsumerKey=...
App.TwitterSecretKey=...


4) ---------------------------------------------------------------------------------

MENU: Key and Access token (from my Twitter Application subsite)


select "CREATE MY ACCESS TOKEN"

You should get the following information with the two following supplementary keys:
App.TwitterAccessToken=...
App.TwitterAccessTokenSecret=...


5) Put the 4 codes into .../⁠tweet_basic-⁠retriever/⁠App.properties

App.TwitterConsumerKey=
App.TwitterSecretKey=
App.TwitterAccessToken=
App.TwitterAccessTokenSecret=

6) in .../⁠tweet_basic-⁠retriever/⁠App.properties
provide the following 2 parameters:

App.InputFile=

(format is 1 tweet id per line e.g. :
535745777336086528
535175951156776960
535113272543178753
...)


App.OutputPath=

7) cd .../tweet_basic-retriever/ ; java -jar  tweet_basic-retriever.jar