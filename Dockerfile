# This is dockerfile for xmind2testlink with python
FROM python:3.5-alpine

# maintainer
LABEL maintainer="Ricky <Ricky2971@hotmail.com>"

# add xmind2testlink
ADD xmind2testlink-S /opt/

# expose port
EXPOSE 5001/tcp

# set WORKDIR
WORKDIR /opt/web

# install dependences
RUN pip install -r requirements.txt -U

# mountpoint
VOLUME /opt/web/uploads/

CMD ["python","application.py"]