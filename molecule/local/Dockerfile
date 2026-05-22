FROM debian:bookworm
ENV container docker
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        systemd systemd-sysv \
        python3 python3-pip \
        sudo \
        kmod iptables \
        fuse-overlayfs fuse3 \
        iproute2 rsync && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -f /lib/systemd/system/multi-user.target.wants/* \
          /etc/systemd/system/*.wants/* \
          /lib/systemd/system/local-fs.target.wants/* \
          /lib/systemd/system/sockets.target.wants/*udev* \
          /lib/systemd/system/sockets.target.wants/*initctl* \
          /lib/systemd/system/basic.target.wants/*
VOLUME /sys/fs/cgroup
CMD ["/lib/systemd/systemd"]
