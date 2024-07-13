from flask import Flask, request, render_template, redirect, url_for, send_file, jsonify
import subprocess
import json
import os

app = Flask(__name__)
SAVE_DIRECTORY = "generated_roadmaps"
SAVE_RESOURCES = "generated_resources"

if not os.path.exists(SAVE_DIRECTORY):
    os.makedirs(SAVE_DIRECTORY)

if not os.path.exists(SAVE_RESOURCES):
    os.makedirs(SAVE_RESOURCES)

def parse_md_to_json(md_content):
    lines = md_content.split('\n')
    roadmap = []
    current_section = None

    for line in lines:
        line = line.strip()
        if line.startswith('###'):
            if current_section:
                roadmap.append(current_section)
            current_section = {
                "title": line[3:].strip(),
                "items": []
            }
        elif line.endswith('**'):
            if current_section:
                current_section['items'].append({
                    "title": (line[5:-2].replace("*", "")).strip(),
                    "subitems": []
                })
        elif line.startswith('- '):
            if current_section and current_section['items']:
                current_section['items'][-1]['subitems'].append((line[2:].replace("*", "")).strip())

    if current_section:
        roadmap.append(current_section)

    return roadmap

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        topic = request.form.get('topic', '').strip()
        file = request.files.get('roadmap_file')

        if file and file.filename.endswith('.md'):
            file_path = os.path.join(SAVE_DIRECTORY, file.filename)
            file.save(file_path)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            roadmap_json = parse_md_to_json(content)
            json_path = os.path.join(SAVE_DIRECTORY, f"{os.path.splitext(file.filename)[0]}.json")
            with open(json_path, 'w', encoding='utf-8') as json_file:
                json.dump(roadmap_json, json_file)
            topic = os.path.splitext(file.filename)[0] # Use the filename (without extension) as the topic
            # result = subprocess.run(['python', 'YT_tutorial.py', topic])
            # print("result", result)
            return redirect(url_for('view_roadmap', topic=topic))
        elif topic:
            # Call the Python script with the topic if no file is uploaded
            subprocess.run(['python', 'roadmap.py', topic, SAVE_DIRECTORY])
            return redirect(url_for('view_roadmap', topic=topic))
        else:
            return "Please provide either a topic or a .md file.", 400

    return render_template('html/index.html')

@app.route('/roadmap/<topic>.json')
def get_roadmap_json(topic):
    file_path = os.path.join(SAVE_DIRECTORY, f"{topic}.json")
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            roadmap_data = json.load(f)
        return jsonify(roadmap_data)
    else:
        return "File not found", 404

@app.route('/download/<topic>')
def download(topic):
    file_path = os.path.join(SAVE_DIRECTORY, f"{topic}.md")
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return "File not found", 404



@app.route('/view/<topic>')
def view_roadmap(topic):
    return render_template('html/view_roadmap.html', topic=topic)

@app.route('/view_md/<topic>')
def view_md(topic):
    return render_template('html/md_render.html', topic=topic)


@app.route('/resources.html')
def resources():
    return render_template('html/resources.html')

if __name__ == '__main__':
    app.run(debug=True)
