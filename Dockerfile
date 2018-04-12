FROM jupyter/all-spark-notebook

# Install JDK
USER root
RUN apt-get -y update && \
    apt-get install -y --no-install-recommends \
    openjdk-8-jdk scala && apt-get clean

# Import the data
USER $NB_USER
ADD --chown=jovyan:users . /home/$NB_USER/work

# Build the software
WORKDIR /home/$NB_USER/work/machine-learning
RUN ./install.sh && \
    find magpie -name "build" -type d | xargs rm -r

# Fix the permissions
RUN fix-permissions /home/$NB_USER 
