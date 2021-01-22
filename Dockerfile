
FROM python:3.8
COPY requirements.txt /tmp/pip-tmp/
ADD vaultunseal /usr/src/app/vaultunseal/
ADD requirements.txt /tmp/pip-tmp/requirements.txt
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
   && rm -rf /tmp/pip-tmp
WORKDIR /usr/src/app

