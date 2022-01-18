Para subirlo a GCP
Pruebas: 
gcloud builds submit --tag northamerica-northeast1-docker.pkg.dev/pruebasdegcp-314904/test/t1:latest

Producción
En artifact registry
gcloud builds submit --tag northamerica-northeast1-docker.pkg.dev/cursos-mios-01/tareas/t1:latest

En cloud rund, pasando por artifact registry, no es necesario usar el de arriba
gcloud run deploy tareas --port=8888 --source .
