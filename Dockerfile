FROM debian
RUN apt update
RUN apt upgrade -y
RUN apt dist-upgrade -y
RUN apt install python3-pip -y
RUN apt clean
RUN pip3 install pip --upgrade
RUN pip3 install numpy
RUN pip3 install tensorflow
RUN pip3 install cycler
RUN pip3 install matplotlib
RUN pip3 install pyparsing
RUN pip3 install python-dateutil
RUN pip3 install pytz
RUN pip3 install scipy
RUN pip3 install six
RUN pip3 install wheel
RUN pip3 install keras
RUN mkdir /src
WORKDIR /src
VOLUME /src
ENTRYPOINT ["python3"]
CMD []
