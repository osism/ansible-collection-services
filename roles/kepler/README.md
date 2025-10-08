Kepler

Kepler (Kubernetes-based Efficient Power Level Exporter) is a Prometheus exporter that measures energy consumption at the container, pod, VM, and process level by reading hardware sensors and attributing power based on resource utilization.

Kepler uses Intel RAPL (Running Average Power Limit) sensors to collect energy data from CPU packages, cores, and memory subsystems, then distributes this energy proportionally to workloads based on their CPU time consumption.

  * GIT: https://github.com/sustainable-computing-io/kepler
  * IMAGES: https://quay.io/repository/sustainable_computing_io/kepler
  * WWW: https://sustainable-computing.io/
