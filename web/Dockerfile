FROM python:3.11.2
ADD server.py server.py
ADD flats.py flats.py
ADD requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 80
ENTRYPOINT ["python3", "server.py"]
