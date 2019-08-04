FROM python:rc-buster
RUN apt-get install git
RUN git clone https://github.com/mandrewcito/signalrcore.git
WORKDIR /signalrcore
RUN python setup.py install
COPY SignalrClient.py .
CMD python SignalrClient.py
