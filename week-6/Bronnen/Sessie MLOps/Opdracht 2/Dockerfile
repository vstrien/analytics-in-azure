FROM python:3.7

# We installeren hier een "virtual environment". 
# Dit is een manier binnen Python om specifieke versies van een module (zoals een ML-module of een webserver) eenvoudig te groeperen.
RUN pip install virtualenv
ENV VIRTUAL_ENV=/venv
RUN virtualenv venv -p python3
ENV PATH="VIRTUAL_ENV/bin:$PATH"

# WORKDIR zorgt ervoor dat de directory 'app' aanwezig is in de container 
WORKDIR /app

# Kopieer de bestanden in de huidige map (.) naar de container. Zet ze in de container in de map '/app'
ADD . /app

# Installeer de libraries zoals deze beschreven staan in `requirements.txt` 
RUN pip install -r requirements.txt

# Om een website aan te kunnen bieden, moet er een poort openstaan. We openen voor nu poort 5000 (dit getal ga je later terugzien)
EXPOSE 5000

# Wanneer je de container start, moet dit commando uitgevoerd worden: "python app.py"
CMD ["python", "app.py"]