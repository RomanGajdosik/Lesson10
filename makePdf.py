from reportlab.lib.pagesizes import LEGAL
from reportlab.pdfgen import canvas

# Define your content
content_en = """
Docker and Flask – Tutorial

=========================================

Docker:
---------
Docker is a containerization tool that allows running applications in an isolated environment.

Advantages of Docker for Python development:
- Consistent environment
- Easy dependency management
- Fast deployment
- Security and isolation
- Reproducibility

Installing Docker Compose:
--------------------------
If you have Docker Desktop, Compose is already included.
Verify installation:
    docker compose version

Using Docker Compose with Flask and PostgreSQL:
----------------------------------------------
Project structure:
    my_project/
    │── app/
    │   ├── app.py
    │   ├── requirements.txt
    │   ├── Dockerfile
    │── docker-compose.yml

Content of `docker-compose.yml`:
----------------------------
version: '3.8'
services:
  web:
    build: ./app
    ports:
      - "5000:5000"
    depends_on:
      - db
  db:
    image: postgres:15
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: mydatabase

Running:
    docker compose up

=========================================

Flask:
------
Flask is a minimalist web framework for Python.

Basic Flask application example:
----------------------------------
    from flask import Flask
    app = Flask(__name__)

    @app.route('/')
    def home():
        return "Hello, Flask!"

    if __name__ == '__main__':
        app.run(debug=True)

Running:
    python app.py

=========================================

REST API with Flask:
-------------------
Installation:
    pip install flask flask-restful

Example REST API:
-----------------
    from flask import Flask, request
    from flask_restful import Resource, Api

    app = Flask(__name__)
    api = Api(app)
    tasks = []

    class Task(Resource):
        def get(self, task_id):
            for task in tasks:
                if task["id"] == task_id:
                    return task, 200
            return {"message": "Task not found"}, 404

        def delete(self, task_id):
            global tasks
            tasks = [task for task in tasks if task["id"] != task_id]
            return {"message": "Task deleted"}, 200

    class TaskList(Resource):
        def get(self):
            return {"tasks": tasks}, 200

        def post(self):
            data = request.get_json()
            task_id = len(tasks) + 1
            new_task = {"id": task_id, "name": data["name"]}
            tasks.append(new_task)
            return new_task, 201

    api.add_resource(TaskList, "/tasks")
    api.add_resource(Task, "/tasks/<int:task_id>")

    if __name__ == "__main__":
        app.run(debug=True)

=========================================

Using cURL to test the API:
---------------------------------
GET list of tasks:
    curl -X GET http://127.0.0.1:5000/tasks

POST - Add a new task:
    curl -X POST http://127.0.0.1:5000/tasks -H "Content-Type: application/json" -d '{"name": "Complete project"}'

GET - Retrieve a specific task:
    curl -X GET http://127.0.0.1:5000/tasks/1

DELETE - Remove a task:
    curl -X DELETE http://127.0.0.1:5000/tasks/1

Tips for cURL:
- Format JSON output: `curl -X GET http://127.0.0.1:5000/tasks | jq`
- Authorization: `curl -X GET http://127.0.0.1:5000/tasks -H "Authorization: Bearer YOUR_TOKEN"`
- Save response to a file: `curl -X GET http://127.0.0.1:5000/tasks -o response.json`

=========================================
"""

# Create PDF
pdf_filename = "docker_flask_tutorial_en_v2.pdf"
c = canvas.Canvas(pdf_filename, pagesize=LEGAL)
c.setFont("Helvetica", 10)

# Add text to the PDF
y_position = 1000  # Start position
for line in content_en.split("\n"):
    c.drawString(50, y_position, line)
    y_position -= 12  # Move to the next line

    # Check if the page is full
    if y_position < 100:
        c.showPage()  # Create a new page
        c.setFont("Helvetica", 10)
        y_position = 1000

c.save()

print(f"PDF saved as {pdf_filename}")