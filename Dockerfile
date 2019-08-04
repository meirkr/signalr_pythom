FROM python:rc-buster
RUN apt-get install git
RUN git clone https://github.com/mandrewcito/signalrcore.git
RUN python signalrcore/setup.py
COPY SignalrClient.py .
CMD pyrhon SignalrClient.py
