FROM python:3.8
LABEL maintainer="HaLD"

COPY . /app
WORKDIR /app
COPY ./techtrends/requirements.txt ./
RUN pip install -r requirements.txt
COPY ./techtrends ./
RUN python init_db.py

EXPOSE 3111

# command to run on container start
CMD [ "python", "app.py" ]
