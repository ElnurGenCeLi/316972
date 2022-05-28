FROM python:latest

RUN apt update && apt upgrade -y

#Yükleme Gereksinimleri
RUN apt install git curl python3-pip ffmpeg -y

#Pip'i Güncelleme
RUN pip3 install -U pip

#Kopyalama Gereksinimleri
COPY requirements.txt /requirements.txt
RUN cd /
RUN pip3 install -U -r requirements.txt
RUN mkdir /Se
WORKDIR /Se
COPY /app
CMD ["python3", "kelime_bot/__init__.py"]
