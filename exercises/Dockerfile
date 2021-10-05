FROM cmscloud/standalone:cmssw_10_6_25-slc7_amd64_gcc700

# Install basic packages
RUN yum update -y && yum install -y curl xrootd-client

# Install conda
RUN curl -O -L https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
RUN bash Miniconda3-latest-Linux-x86_64.sh -b && rm Miniconda3-latest-Linux-x86_64.sh
# Set temporary env variable to make our lives easier
ENV CONDA=/root/miniconda3/bin/conda
# conda will be on $PATH when you log in
RUN $CONDA init
# Configure conda
RUN $CONDA config --set auto_activate_base false && $CONDA config --add channels conda-forge
# Set up conda environment
RUN $CONDA create --name exercise-env -y && \
    $CONDA install -n exercise-env -y uproot xrootd awkward numba pandas

WORKDIR /home
