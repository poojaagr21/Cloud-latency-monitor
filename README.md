# Cloud-latency-monitor
It measures how long it takes to open a TCP connection to any website you ask for, stores that time as a metric, and lets you see the numbers—plus the service’s own health—in Grafana dashboards.


A tiny Python web API
• Route /ping?target=example.com
• When called, it opens a TCP connection (a SYN / SYN-ACK / ACK) to example.com:443, times the handshake, then closes it.
• It returns the measured latency in JSON: { "target": "example.com", "latency": 0.074 }.

Metrics inside the service
• Every call increases ping_requests_total (a Prometheus counter).
• The handshake time is recorded in ping_latency_seconds (a Prometheus histogram).
• Errors are tracked in ping_errors_total.

Logs
• Each request is logged: target=example.com latency=74 ms status=200.
• Logs are collected by Loki so you can search them later.

Where it runs
• The Python container runs on a Kubernetes cluster that Terraform builds for you in AWS (or GCP/Azure).
• A Kubernetes Service of type LoadBalancer gives the API a public URL so anyone can test latency from your cluster to any host.

How you observe it
• Prometheus automatically scrapes the /metrics endpoint and stores the counters and histograms.
• Grafana dashboards show: requests-per-second, 95th-percentile latency, error rate, node CPU/RAM, etc.
• Alertmanager can page you if p95 latency goes above a threshold or error rate spikes.

Automation around it
• GitHub Actions pipeline lints and tests the Python code, builds the Docker image, pushes it to a registry, and upgrades the Kubernetes deployment—so every commit gives you a fresh version in the cloud with zero manual steps.
• Terraform keeps the cluster, network, and IAM roles under version control, so you can recreate or destroy the whole environment with one command.

Why it’s useful 
• Shows real Linux/TCP behaviour (handshake timing) in a cloud network.
•  end-to-end SRE tooling: IaC → cluster → CI/CD → metrics → logs → alerts.
