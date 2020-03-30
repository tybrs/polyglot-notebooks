FROM continuumio/miniconda3

RUN conda install --quiet -y -c conda-forge root

ARG username=polyglot
RUN useradd --create-home --home-dir /home/${username} ${username}

ENV HOME /home/${username}
ENV NOTEBOOK_DIR ${HOME}/notebooks
ENV NOTEBOOK_PW password
ENV NOTEBOOK_LOCATION cpp
ENV PORT 8888

USER ${username}

WORKDIR ${HOME}/app
COPY root/entrypoint.sh .
COPY jupyter_write_passwd.py .
RUN ["python", "jupyter_write_passwd.py"]

RUN mkdir ${NOTEBOOK_DIR}
ENV NOTEBOOKARGS "--notebook-dir=${NOTEBOOK_DIR} --ip='*' \
				  --port=${PORT} --no-browser \
				  --config=${HOME}/.jupyter/jupyter_notebook_config.json"

# Allow incoming connections on port
EXPOSE ${PORT}

# Start ROOT with the --notebook flag to fire up the container
ENTRYPOINT /bin/bash -c ${HOME}/app/entrypoint.sh
