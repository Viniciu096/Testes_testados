FROM python:3

WORKDIR /user/src/app

COPY requirements.txt  ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 80
CMD [ "fastapi","run", "./Main.py", "--port", "80" ]