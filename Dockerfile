FROM python:3.9-slim
ENV PYTHONUNBUFFERED True

WORKDIR /src
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["jupyter", "notebook", "tarea1.ipynb", "--ip=0.0.0.0", "--allow-root", "--no-browser", "--NotebookApp.token=''", "--NotebookApp.password=''"]
