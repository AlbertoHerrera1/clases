Para subirlo a GCP
Pruebas: 
gcloud builds submit --tag northamerica-northeast1-docker.pkg.dev/pruebasdegcp-314904/test/t1:latest

Producción
En artifact registry
gcloud builds submit --tag us-east1-docker.pkg.dev/cursos-mios-01/tareas1/t1:latest

En cloud rund, pasando por artifact registry, no es necesario usar el de arriba
gcloud run deploy tareas --port=8888 --source .

Tareas
34.66.61.88/hub/user-redirect/git-pull?repo=https://github.com/AlbertoHerrera1/clases&branch=main&subPath=<subPath>&app=notebook

Tarea 1
34.66.61.88/hub/user-redirect/git-pull?repo=https://github.com/AlbertoHerrera1/clases&branch=main&subPath=tarea1.ipynb&app=notebook

http://<my-jhub-address>/hub/user-redirect/git-pull?repo=<your-repo-url>&branch=<your-branch-name>&subPath=<subPath>&app=<notebook | lab>