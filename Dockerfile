FROM python:rc-alpine
WORKDIR /app
RUN pip install signalrcore
COPY SignalrClient.py .
CMD python SignalrClient.py
