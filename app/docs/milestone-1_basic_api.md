# Milestone 1 – Basic Flask Latency API

Date completed: YYYY-MM-DD  
Codespace size: 2 cores / 8 GB RAM (or whatever you picked)

---

## What we built

A tiny Python 3 Flask web service that:

* exposes a **/ping** endpoint
* measures raw TCP handshake latency to any host you pass with `target=`
* returns JSON with the measured value

Example:
GET /ping?target=github.com → 200 OK { "target": "github.com", "latency": 0.0556 }

---

## Why this matters

1. **Linux networking**
2. **Flask** for quick HTTP APIs.  
3. foundation for later milestones (metrics, Docker, Kubernetes, CI/CD).

---

## File layout introduced in this milestone

. ├── app/ │ └── app.py # Flask code └── requirements.txt # Python deps (flask)



## Step-by-step (exact commands)

```bash
# 1. Create folders & files
mkdir -p app
touch app/app.py
echo "flask" > requirements.txt

# 2. Write the code  (see app/app.py in repo)

# 3. Install dependency
pip install -r requirements.txt

# 4. Run locally inside Codespace
python app/app.py          # service on port 8080
# open browser:
# https://8080-<hash>.<region>.codespaces.azure.com/ping?target=github.com

# 5. JSON output confirms success
# Press Ctrl+C to stop server

# 6. Commit
git add app requirements.txt
git commit -m "milestone1: basic Flask latency API"
git push


Troubleshooting notes
Symptom	Fix
Browser shows “404 Not Found”	Make sure to adde  /ping?target=github.com
to the URL
Port 8080 not listed in Ports tab	Restart Flask, Codespaces auto-detects active ports
ModuleNotFoundError: flask
pip install -r requirements.txt
inside the Codespace