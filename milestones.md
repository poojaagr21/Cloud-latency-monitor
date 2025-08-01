The full “Cloud Latency Monitor”  is divided into 8 practical milestones.
Each one builds directly on the previous.

Milestone overview

Basic Flask Latency API
• Pure Python service with /ping route (✓ you just finished this).

Prometheus Metrics
• Add /metrics endpoint with Counter & Histogram.
• Verify text output.

Docker Container
• Write Dockerfile, build image, run with
docker run
.
• Commit image-build instructions.
Local Kubernetes (kind)
• Create one-node kind cluster inside Codespace.
• Write Deployment + Service YAML; access via
kubectl port-forward
.
Local Observability Stack
• Install Prometheus + Grafana with Helm into kind.
• View ping_latency_seconds, build a quick dashboard.

CI Pipeline (GitHub Actions)
• Lint + unit tests → build Docker image → (optional) push to GitHub Container Registry.
• Run on every push / PR.

Cloud Cluster with Terraform Cloud
• Use Terraform to provision a small EKS (or GKE/AKS) cluster.
• Store state and run plans in Terraform Cloud (no tools on your laptop).
• Deploy the app to the managed cluster via Helm in the CI job.

Full Observability, Autoscaling & Alerts
• Add HPA based on request rate or CPU.
• Install Loki for logs, maybe Tempo for traces.
• Create Grafana dashboard + Alertmanager rule (“p95 latency > 300 ms for 5 min”).
• Demo alert firing (Slack/email).

After Milestone 8 :

• IaC → cluster → CI/CD → metrics/logs/alerts
• Showcases Python, Docker, Kubernetes, Terraform, GitHub Actions, Prometheus stack.