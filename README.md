![Cover](https://github.com/Esio-01/Esio-01/blob/main/Capture%20d%E2%80%99%C3%A9cran%202021-10-15%20004253.png)
# SMTP-Sender
ONYX SMTP Sender est un tool qui vous serviras à envoyer des email html à une liste d'email (en .txt) c'est la première version du tool et je le sors un peu à la rache donc si le logiciel est obsolète c'est normal j'y taff encore ;)

Pour l'utiliser:

pip install colorama
pip install smtplib

Vous pouvez également executer le requirement.bat si vous êtes sur windows pour installer les prérequis.

## Si vous utilisez des adresse gmail:
Il est impératif d'activer l'option "Accès moins sécurisé des applications" à votre compte gmail si vous voulez envoyer des emails en masse.
Il est aussi déconseillé de dépasser l'envoie de 500 email/jours pour peine de ne plus avoir de compte gmail. 

## Comment l'utiliser?

1. Choisissez votre serveur smtp(si vous avez une adresse gmail par exemple, le serveur seras: smtp.gmail.com).
2. Ajoutez le port utilisé par le serveur (dans l'exemple de gmail, c'est le port n° 587).
3. Ajouter l'email qui va envoyer les messages.
4. Ajouter l'ID de l'email (sur gmail c'est tout votre email, sur d'autres smtp c'est juste les caractères avant le "@")
5. Spécifiez le mot de passe de votre boite email pour établir la connexion au SMTP gmail.
6. Selectionnez la liste d'email auquel vous voulez envoyer votre email html (en .txt seulement)
7. Mettez le code html de votre email dans un fichier txt que vous placerez au même endroit que le fichier
8. Spécifiez le fichier en question (.txt) pour l'email html
9. Laissez le tool se charger du reste, il enverras votre email html à tout les email présent sur le fichier txt spécifié 

## /!\ Version bêta du tool (les bugs sont présents)
- Un email invalid entraine l'arrêt total du programme en cours d'execution
- Une fois les emails envoyé, le programme s'arrête tout seul
- Se tromper de port ou d'un seul caractère lors de la configuration du SMTP fait crasher le tool
- 
