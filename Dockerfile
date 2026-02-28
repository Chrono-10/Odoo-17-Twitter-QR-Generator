FROM odoo:17.0

USER root
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt && rm /tmp/requirements.txt
COPY ./addons /mnt/extra-addons
EXPOSE 8069
USER odoo