# Data Scientist-werk opnemen in een container

## Inleiding

De Data Scientist heeft puik werk geleverd, maar wel hele specifieke eisen:

* Python 3.6.2
* Bepaalde Python modules die via Pip geïnstalleerd moeten worden (Hyperopt, Catboost)

We maken daarom een container, waarin exact de juiste versies van de libraries geïnstalleerd staan.
Wanneer de container succesvol kan draaien, weten we dat we de infrastructuur werkend hebben.
Deze stabiele basis maakt het mogelijk om vervolgens technisch te gaan sleutelen.

## Stappenplan

Om de container werkend te krijgen, moeten er een paar zaken gebeuren:

1. Vastleggen van een ontwerp (in een Dockerfile)
2. Maken van de container
3. Registreren van de container in een registry
4. Testen van de container m.b.v. een Container Instance

## Vastleggen van een ontwerp

In een Dockerfile leggen we vast hoe de container eruit moet zien:

* De basis (een Linux-image)
* De bestanden die aanwezit moeten zijn (de Python-scripts in dit geval, maar initieel ook de data-bestanden)
* De versies van software die aanwezig moeten zijn (Python 3.6.2, de pip-packages)

Een Dockerfile is een eenvoudig bestand, die vaak simpelweg de naam `Dockerfile` draagt, zonder extensie.

Als je meer over Dockerfiles wilt leren, kun je kijken op https://docs.docker.com/engine/reference/builder/#format.
Voor nu volstaan echter de volgende opdrachten:

* `FROM` geeft aan welk image de basis is: er wordt vaak verdergebouwd op een bestaand Docker-image, zodat je niet altijd het wiel opnieuw hoeft uit te vinden
* Met `RUN` kun je commandline-opdrachten uitvoeren binnen de container
* Met `ENV` kun je parameters de container ingeven: aan de buitenkant kun je deze wijzigen, binnen de container kun je ze uitlezen.
* Met `COPY` kun je bestanden naar de container toe kopiëren

Op deze wijze maak je een herhaalbaar "recept" voor de juiste container.

In de map `01-maak-dockerfile` staat een raamwerk van een docker-script.
Voeg hier de volgende zaken aan toe:

## Maken van de container

Met het opslaan van de container wordt deze automatisch gebouwd in Azure Pipelines.
Kijk of dit goed gaat.

De **laatste stap** (het trainen van het model) duurt het langst: in Azure Pipelines minstens 15 minuten.
Daarom staat deze stap nu nog in commentaar. Deze halen we pas weg wanneer we het image ook daadwerkelijk registreren in ACR.

## Registreren van de container in een registry

Met het registreren van een container in een registry als Artifactory, Docker Hub of Azure Container Registry brengen we eigenlijk de voltooide container onder versiebeheer.
De voltooide container is *immutable*: je kunt er niets aan veranderen, en bij elke start is hij weer volledig identiek.

Voor ons betekent dit dat het getrainde ML-model (de *Random Forest*) dus als een *artifact* opgeslagen kan worden. Maar ook dat we oudere versies met een druk op de knop online kunnen zetten. Of tien verschillende versies naast elkaar evalueren. 

> ## Immutability
>
> **Immutability**, de eigenschap dat containers na iedere start identiek zijn aan de oorspronkelijke container, is een krachtige eigenschap. Maar er zijn natuurlijk genoeg situaties te bedenken wanneer je een heel select deel van je container juist wél mutable wilt laten zijn.
> Hoewel dat binnen een container niet mogelijk is, kunnen we wel een *mount* aanleggen in de container. Dat betekent dat je een map binnen de container hebt die in werkelijkheid op externe storage staat.
> Omdat die externe storage *wel* mutable (en bij voorkeur ook *durable*) is, worden aanpassingen toch blijvend opgeslagen.

## Testen van de container m.b.v. een Container Instance

Open de Azure Portal
Ga naar de resource group waar je in werkt (mlops-RG)
Klik hier op 'Create' linksbovenin het scherm
Zoek naar Container Instances, klik op 'Create'
Maak nu een Container Instance gebaseerd op de Azure Container Registry

