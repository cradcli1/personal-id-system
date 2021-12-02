FROM registry.access.redhat.com/ubi8/python-38:1-7

USER root

Copy BaseCodes/* ./BaseCodes/
Copy SlackBot ./SlackBot/
Copy startup.sh ./

run pip3 install --upgrade pip && pip3 install zmq
run chmod +x ./dockerStartup.sh

CMD [ "./startup.sh"]