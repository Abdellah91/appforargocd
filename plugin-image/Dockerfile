FROM line/kubectl-kustomize:1.28.3-5.2.1

RUN wget -O /tmp/genvsub_1.2.3_Linux_x86_64.tar.gz \
    https://github.com/icy/genvsub/releases/download/v1.2.3/genvsub_1.2.3_Linux_x86_64.tar.gz && \
    tar -xvzf /tmp/genvsub_1.2.3_Linux_x86_64.tar.gz -C /usr/local/bin/
CMD ["/bin/sh"]