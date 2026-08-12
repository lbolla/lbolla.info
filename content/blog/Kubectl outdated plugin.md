---
title: Kubectl outdated plugin
date: 2018-01-04
tags:
- programming
---
We use [Kubernetes](https://kubernetes.io/) at [work](https://yougov.co.uk/) and I am mostly responsible for making it run smoothly. This means staying on top of new releases, libraries and tools that come out at a pace I\'ve never experienced before, in any project.

To help with that, I wrote a [kubectl plugin](https://kubernetes.io/docs/tasks/extend-kubectl/kubectl-plugins/) that finds outdated components in a Kubernetes cluster. The **[code can be found here](https://github.com/lbolla/kubectl-plugin-outdated)**.

It works like this.

-   First it goes through all `deployments` and `daemonsets`, collecting the `images` referenced in their `containers`.
-   For each container, search for a newer image *tag* in its repository. I currently support querying Docker Hub and Google Container Repository (you need [gcloud](https://cloud.google.com/sdk/gcloud/) for that).
-   Outputs which deployment or daemonset needs upgrading.

E.g. running it on a testing cluster I setup gives this output:

``` shell
$> kubectl plugin outdated
Deployment:gitlab-ci/gitlab-runner                                                     gitlab/gitlab-runner:alpine-v9.5.0 -> v10.3.0             
Deployment:gitlab/gitlab-ce                                                                   gitlab/gitlab-ce:9.5.9-ce.0 -> 10.3.3-ce.0         
Deployment:gitlab/redis                                                                            bitnami/redis:3.2.8-r2 -> 4.0.6-r1            
Deployment:kube-system/dashboard                               gcr.io/google_containers/kubernetes-dashboard-amd64:v1.6.3 -> v1.8.1              
Deployment:kube-system/heapster                                            gcr.io/google_containers/heapster-amd64:v1.4.0 -> v1.5.0              
Deployment:kube-system/kube-dns                                    gcr.io/google_containers/k8s-dns-kube-dns-amd64:1.14.5 -> 1.14.7              
Deployment:kube-system/kube-dns                               gcr.io/google_containers/k8s-dns-dnsmasq-nanny-amd64:1.14.5 -> 1.14.7              
Deployment:kube-system/kube-dns                                     gcr.io/google_containers/k8s-dns-sidecar-amd64:1.14.5 -> 1.14.7              
Deployment:kube-system/monitoring-grafana                          gcr.io/google_containers/heapster-grafana-amd64:v4.4.1 -> v4.4.3              
Deployment:kube-system/monitoring-influxdb                        gcr.io/google_containers/heapster-influxdb-amd64:v1.1.1 -> v1.3.3              
DaemonSet:kube-system/calico-etcd                                                     gcr.io/google_containers/etcd:2.2.1 -> 3.1.11              
DaemonSet:kube-system/kube-proxy                                         gcr.io/google_containers/kube-proxy-amd64:v1.8.5 -> v1.10.0-alpha.1 
```
