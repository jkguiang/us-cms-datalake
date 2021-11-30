FROM opensciencegrid/software-base:fresh

RUN yum -y install vim && \
    yum -y install osg-xrootd-standalone --enablerepo=osg-upcoming && \
    yum -y install xrootd-scitokens && \
    yum -y install voms-clients && \
    yum -y install vo-client-lcmaps-voms

ADD image-config.d/* /etc/osg/image-config.d/
