### Building and running your application

When you're ready, start your application by running:
`docker compose up --build`.

Your application will be available at http://localhost:8000.

### Deploying your application to the cloud

First, build your image, e.g.: `docker build -t myapp .`.
If your cloud uses a different CPU architecture than your development
machine (e.g., you are on a Mac M1 and your cloud provider is amd64),
you'll want to build the image for that platform, e.g.:
`docker build --platform=linux/amd64 -t myapp .`.

Then, push it to your registry, e.g. `docker push myregistry.com/myapp`.

Consult Docker's [getting started](https://docs.docker.com/go/get-started-sharing/)
docs for more detail on building and pushing.

### References
* [Docker's Python guide](https://docs.docker.com/language/python/)

## Notities
Mbv Dockerfile bouw je een docker image. 

docker build -t docker_dagster .
- -t betekent "tag" en geeft de naam van de image op.
- De . aan het einde betekent dat Docker zoekt naar de Dockerfile in de huidige map (pwd).

docker build -t docker_dagster /folder waarin de commando's uitgevoerd moet worden/
- In plaats van een punt geef je een relatief pad op naar de map waar de Dockerfile staat die gebruikt moet worden.

docker build --progress=plain --no-cache -t docker_dagster .
- --progress=plain zorgt ervoor dat de voortgang van de build in platte tekst wordt weergegeven (handig voor debugging).
- --no-cache zorgt ervoor dat Docker geen cache gebruikt en alles opnieuw bouwt.
- -t docker_dagster geeft de naam van de image op.
- De . betekent dat de Dockerfile in de huidige map gezocht wordt.

docker run -p 8080:8080 docker_dagster
- run start een nieuwe container op basis van de image docker_dagster.
- -p 8080:8080 koppelt poort 8080 van de container aan poort 8080 van de host, zodat je bijvoorbeeld een webapplicatie in de browser kunt openen.

docker run -p 8080:8080 docker_dagster dagster dev -h 0.0.0.0 -p 8080
- Start een container van de image docker_dagster.
- -p 8080:8080 koppelt poort 8080 van de container aan poort 8080 van de host.
- dagster dev -h 0.0.0.0 -p 8080 voert in de container het commando uit om de Dagster development server te starten, luisterend op alle netwerkinterfaces (-h 0.0.0.0) en poort 8080 (-p 8080), zodat deze bereikbaar is vanaf de host.
- Belangrijk om te onthouden hierbij is dat je niet naar http://0.0.0.0:8080 moet gaan zoals in de logging.info berichten staan wanneer je de dagster webserver start. Je moet in plaats daarvan naar localhost:8080 gaan. 

Je kunt deze commando's ook toevoegen aan je Dockerfile door het volgende naar behoefte uit te breiden: CMD ["dagster", "dev", "-p", "8080"]