
Listed Runtime Requirements
• Noted that only the Flask package is needed for now.
• Wrote its name in a requirements file so dependency installation can be scripted later.

Containerised the Service with Docker
• Created a Dockerfile (the build recipe).
– Declared a small Linux image that already contains Python.
– Copied our application code and requirements list into that image.
– Instructed the image to install Flask and, when it boots, to start our Python process.
• Ran

docker build

; Docker followed the recipe, layer-by-layer, and produced an immutable image that now contains OS, Python, Flask, and our code.
Launched the Service as a Container
• Started the image with


docker run
in detached mode.
• Published an external port on the host (8000) and connected it to the port the application listens on inside the container (8080).
• The container now runs isolated from the host but is reachable at

localhost:8000
.
Debugged Typical First-Time Issues
• Build Context Error: initial build failed because the requirements file was outside the build context; fixed by running the build command from the correct directory.
• Port Mismatch: first run produced “connection reset” because the host port was forwarded to 8000 while the app listened on 8080; corrected by updating the port mapping.
• Route Mismatch: received HTTP 404 because we were calling /latency but the application originally exposed /ping; added /latency route and kept /ping as an alias.

Validated End-to-End
• Rebuilt the image with the corrected route.
• Relaunched the container with the corrected port mapping.
• Successfully called the endpoint: a JSON payload returned the measured latency, confirming the containerised service works as intended.

Key Takeaways
• Docker images capture the entire runtime environment so the service runs the same on any machine.
• Binding the application to 0.0.0.0 inside the container is essential so docker’s port-forwarding can reach it.

-p host:container
maps network traffic; the number on the right must match the port the service actually listens on.
• Common debugging path: check container status (
docker ps
), view logs (

docker logs
), and verify route paths when you get a 404.