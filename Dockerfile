FROM python:3.11

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --disable-pip-version-check --no-cache-dir -r requirements.txt

# Manually download and place the frpc file
RUN mkdir -p /usr/local/lib/python3.11/site-packages/gradio/
RUN wget -O /usr/local/lib/python3.11/site-packages/gradio/frpc_linux_aarch64_v0.2 https://github.com/fatedier/frp/releases/download/v0.51.2/frp_0.51.2_linux_arm64.tar.gz


COPY . .

CMD ["python", "./app.py"]