FROM python:3.9-buster
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD python src/_03_app.py
