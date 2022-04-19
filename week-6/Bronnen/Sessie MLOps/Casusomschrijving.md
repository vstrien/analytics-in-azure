# MLOps

In een vlaag van verruimende wetgeving is het mogelijk geworden om zorgverzekering-klanten ook aanbiedingen te doen voor andere verzekeringen. Onze Data Scientists zijn hier uiteraard direct onderzoek naar gaan doen. 

De eerste specifieke vraag waar de Data Scientists zich over gebogen hebben, is een stuk cross-selling tussen zorgverzekering en een autoverzekering. Welke klanten kunnen we het beste bellen om een aanbieding te doen?

Het resultaat is verwerkt in een Jupyter notebook waarin de data in batch beoordeeld wordt.

## Afwijkingen van de praktijk

Uiteraard is deze casus fictief: in Nederland is het (waarschijnlijk?) niet toegestaan om zorg-klanten te benaderen voor andere verzekeringen. Ook gebruiken de Data Scientists binnen Achmea meer R dan Python-modellen.

Het gaat hier echter niet om deze specifieke inhoud: in plaats van de zorg-klanten zouden we ook naar andere schade-klanten kunnen kijken. Cross-selling is universeel, en het gaat hier om het MLOps-proces, niet om het precieze ML-model (waarschijnlijk zou een XGBoost hier veel beter werken dan een Random Forest, maar ook dat is hier irrelevant).

Ook op technisch vlak zijn een paar zaken een klein beetje anders geregeld binnen Achmea:

* Binnen Achmea wordt OpenShift gebruikt, terwijl we in de cursus Kubernetes gebruiken. OpenShift is óók Kubernetes, maar dan met wat extra's die het clusterbeheer wat makkelijker maken. De principes van het publiceren en beschikbaar stellen van containers in Kubernetes werken echter ook in OpenShift.
* Binnen Achmea wordt Artifactory gebruikt, terwijl we in de cursus ACR (Azure Container Registry) gebruiken. Ook dit is voor ons niet heel belangrijk: de werking van versiebeheer en tagging is gelijk binnen de twee producten, en het gaat er ons vooral om dat we de werking van een "artifact registry" meemaken. Opnieuw is Artifactory vooral veel uitgebreider dan ACR, omdat je er ook allerhande andere "build packages" in kwijt kunt (en niet alleen containers).
* Binnen Achmea wordt Data Science vooral in R gedaan. Ook hier blijven de principes hetzelfde: er zijn dependencies, de code moet gesplitst worden, en we maken een container waar alle dependencies aanwezig zijn.

## Opdracht

Omdat we voor de meesten met hele nieuwe techniek aan de slag gaan, hebben we drie varianten van de training:

* Basis: we doorlopen de volledige MLOps pipeline, maar we beperken ons tot de containertechnieken:
  * Het opbouwen van een container
  * Het registreren van een container in de registry
  * De deployment van een container naar een cluster
* Gevorderd: We breiden de container uit met eigen code
* Pythonista: We doorlopen het hele MLOps-stuk: we nemen een bestaand ML model van een Data Scientist, vertalen dat naar een bruikbaar Python-script
* Die hard: We doen het volledige stuk in Azure ML Studio, zodat we ook alle krachtige ingebouwde MLOps-mogelijkheden hiervan gebruiken.

Op basis van de aangeleverde Jupyter Notebook en voorbeeldbestanden is ons als Data Engineers gevraagd om een Machine Learning-model te operationaliseren.

We doen dit in een aantal stappen:

1. Het Jupyter-notebook met alle dependencies vertalen we naar een Docker-image die alles aan boord heeft
1. Het Jupyter-notebook vertalen we naar een normaal Python-script
1. Het Python-script splitsen we op in twee delen:
   * **Training** (trainen van het model)
   * **Inference** (het teruggeven van resultaten)
1. We registereren deze Docker-image naar de Azure Container Registry
1. We doen een deployment naar ACI om de image te testen
1. We doen een deployment naar AKS om de image in productie te nemen

Verdieping / verbreding:

* Het traject in Azure ML Studio laten uitvoeren (meer uitzoekwerk; meer Python-kennis nodig!)
* AKS-pipelines zelf vormgeven aan de hand van een tweede model (nabouwen in eigen DevOps-omgeving)
* De training plaats laten vinden in een ACR Task
