# Linked Services

## Doel

Azure Data Factory heeft in de basis twee belangrijke taken in het data-landschap:

* Orchestratie (het aansturen van services)
* Data Movement (het kopiëren van data tussen je services)

Een *service* zoals hierboven twee keer benoemd, is in feite elke dienst die ADF kan aansturen of waar ADF data tussen kan kopiëren. Met andere woorden:

* SQL Databases
  * Als bron waar je data leest
  * Als doel waar je data wegschrijft
  * Als *compute engine* die je *stored procedures* laat uitvoeren
* Storage Accounts
  * Als bron waar je data leest
  * Als doel waar je data wegschrijft
* Key Vault
  * Als nette integratie om je wachtwoorden centraal in te beheren
* Etc.

De registratie van hoe er verbinding gemaakt kan worden met één van deze services heet een *Linked Service* - en die gaan we hier aanmaken.

## Opdracht

Open Azure Data Factory. Om Linked Services eenvoudig aan te maken gaan we naar het tabblad **Manage**, waar de Linked Services te vinden zijn.

1. Maak hier een Linked Service aan naar je storage account
   * Naam van de Linked Service: `ls_adls`

Voordat je nu verder gaat, is er één zaak die geregeld moet zijn:

* De Azure SQL Server in jouw resource group moet toestaan dat andere Azure Resources de server kunnen benaderen. Dit kun je instellen in de Azure Portal:
  * Open de databaseserver
  * Selecteer aan de linkerzijde van het scherm **Firewalls and virtual networks**
  * Zet het schuifje bij **Allow Azure services and resources to access this server** op **Yes**

Nu kun je binnen ADF een nieuwe Linked Service toevoegen naar je database. Test de connectie voordat je deze aanmaakt.

2. Maak een Linked service aan naar de SQL-database; noem deze `ls_sql_awlt`
