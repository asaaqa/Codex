# Using python slim-buster
FROM asaaqa/codex:buster

# Install pytgcalls
RUN pip3 install --no-cache-dir pytgcalls[telethon]

# Git clone repository + root 
RUN git clone https://github.com/asaaqa/Codex.git /root/usercodex
#working directory 
WORKDIR /root/usercodex

# Install requirements
RUN pip3 install --no-cache-dir -r requirements.txt

ENV PATH="/home/usercodex/bin:$PATH"

CMD ["python3","-m","usercodex"]
