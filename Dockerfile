FROM asaaqa/codex:slim-buster

RUN git clone https://github.com/asaaqa/codex.git /root/usercodex

WORKDIR /root/usercodex

RUN pip3 install --no-cache-dir -r requirements.txt

ENV PATH="/home/usercodex/bin:$PATH"

CMD ["python3","-m","usercodex"]
