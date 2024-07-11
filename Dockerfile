FROM python:3.8
LABEL maintainer="HaLD"

WORKDIR /usr/src/app

COPY ./techtrends/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

# RUN docker builder prune --all --force

COPY ./techtrends/init_db.py ./

RUN python init_db.py

EXPOSE 3111

CMD [ "python", "app.py" ]