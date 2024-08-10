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
    """
    Parses markdown content and converts it into a JSON representation of a roadmap.
    Args:
        md_content (str): The markdown content to be parsed.
    Returns:
        list: A list of dictionaries representing the roadmap. Each dictionary contains the title of a section and its corresponding items and subitems.
    Example:
        md_content = "# Roadmap\n\n### Section 1\n\n- Item 1\n- Item 2\n\n### Section 2\n\n- Item 3\n- Item 4\n\n#### Subitem 1\n\n- Subitem 2\n\n"
        parse_md_to_json(md_content)
        # Output:
        # [
        #     {
        #         "title": "Section 1",
        #         "items": [
        #             {
        #                 "title": "Item 1",
        #                 "subitems": []
        #             },
        #             {
        #                 "title": "Item 2",
        #                 "subitems": []
        #             }
        #         ]
        #     },
        #     {
        #         "title": "Section 2",
        #         "items": [
        #             {
        #                 "title": "Item 3",
        #                 "subitems": []
        #             },
        #             {
        #                 "title": "Item 4",
        #                 "subitems": [
        #                     "Subitem 1",
        #                     "Subitem 2"
        #                 ]
        #             }
        #         ]
        #     }
        # ]
    """
    
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
    """
    This function handles the index page of the application.
    If the request method is POST, it checks if a file with a .md extension is uploaded. 
    If a file is uploaded, it saves the file, reads its content, parses it to JSON, and saves the JSON file.
    If no file is uploaded, it calls a Python script with the provided topic and saves the result.
    Parameters:
        None
    Returns:
        If a file is uploaded, it redirects to the 'view_roadmap' page with the topic as a parameter.
        If no file is uploaded, it redirects to the 'view_roadmap' page with the topic as a parameter.
        If neither a file nor a topic is provided, it returns a 400 error with the message "Please provide either a topic or a .md file."
    """

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

@app.route('/resource', methods=['GET', 'POST'])
def resource():
    """
    Handle the resource endpoint.
    This function handles the HTTP POST request to the resource endpoint. It expects a form data with a 'topic' field and an optional 'resource_file' field. 
    If a valid Markdown file is uploaded, it saves the file to the specified directory and redirects to the 'view_md' endpoint with the extracted topic from the filename. 
    If no file is uploaded but a topic is provided, it calls a Python script with the topic and the save directory as arguments and redirects to the 'view_md' endpoint. 
    If neither a file nor a topic is provided, it returns a 400 Bad Request response with a message.
    Returns:
        If successful, it redirects to the 'view_md' endpoint.
        If unsuccessful, it returns a 400 Bad Request response with a message.
    """

    if request.method == 'POST':
        topic = request.form.get('topic', '').strip()
        file = request.files.get('resource_file')

        if file and file.filename.endswith('.md'):
            file_path = os.path.join(SAVE_RESOURCES, file.filename)
            file.save(file_path)
            topic = (os.path.splitext(file.filename)[0])
            topic = topic.replace('_resource', "")
            return redirect(url_for('view_md', topic=topic))
        elif topic:
            # Call the Python script with the topic if no file is uploaded
            subprocess.run(['python', 'resources.py', topic, SAVE_RESOURCES])
            return redirect(url_for('view_md', topic=topic))
        else:
            return "Please provide either a topic or a .md file.", 400
        
    return render_template('html/resources.html')

@app.route('/download/<topic>')
def download(topic):
    """
    Downloads a file based on the given topic.
    Args:
        topic (str): The topic of the file to be downloaded.
    Returns:
        If the file exists, the file will be sent as an attachment.
        If the file does not exist, a "File not found" message with a 404 status code will be returned.
    """

    file_path = os.path.join(SAVE_DIRECTORY, f"{topic}.md")
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return "File not found", 404

@app.route('/roadmap/<topic>.json')
def get_roadmap_json(topic):
    """
    Retrieves the roadmap data in JSON format for the specified topic.
    Parameters:
    - topic (str): The topic for which the roadmap data is requested.
    Returns:
    - If the file exists, the roadmap data in JSON format.
    - If the file does not exist, a tuple containing the string "File not found" and the HTTP status code 404.
    """

    file_path = os.path.join(SAVE_DIRECTORY, f"{topic}.json")
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            roadmap_data = json.load(f)
        return jsonify(roadmap_data)
    else:
        return "File not found", 404

@app.route('/resources/<topic>_resource.md')
def get_resource_md(topic):
    """
    Retrieves the content of a resource file based on the given topic.
    Parameters:
    - topic (str): The topic of the resource file to retrieve.
    Returns:
    - str: The content of the resource file if it exists.
    - tuple: A tuple containing the error message "File not found" and the status code 404 if the resource file does not exist.
    """


    file_path = os.path.join(SAVE_RESOURCES, f"{topic}_resource.md")
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            resource_data = f.read()
        return resource_data
    else:
        return "File not found", 404

@app.route('/resources/<topic> Latest News.json')
def get_resource_News_json(topic):
    """
    Retrieves the latest news resource data for a given topic.
    Args:
        topic (str): The topic for which to retrieve the news resource data.
    Returns:
        If the resource data file exists:
            jsonify(resource_data) (json): The latest news resource data in JSON format.
        If the resource data file does not exist:
            "File not found", 404 (str, int): A message indicating that the file was not found and the HTTP status code 404.
    """

    if not os.path.exists(os.path.join(SAVE_RESOURCES, f"{topic} Latest News.json")):
        subprocess.run(['python', 'YT.py', topic, SAVE_RESOURCES])
        file_path = os.path.join(SAVE_RESOURCES, f"{topic} Latest News.json")
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                resource_data = json.load(f)
            return jsonify(resource_data)
        else:
            return "File not found", 404
    else:
        file_path = os.path.join(SAVE_RESOURCES, f"{topic} Latest News.json")
        with open(file_path, 'r') as f:
            resource_data = json.load(f)
        return jsonify(resource_data)

@app.route('/resources/<topic> Tutorial.json')
def get_resource_Tutorial_json(topic):
    """
    Retrieves the resource data for a given topic from a JSON file.
    Args:
        topic (str): The topic for which to retrieve the resource data.
    Returns:
        If the JSON file exists:
            jsonify: The resource data in JSON format.
        If the JSON file does not exist:
            str: "File not found"
            int: 404
    """

    if not os.path.exists(os.path.join(SAVE_RESOURCES, f"{topic} Tutorial.json")):
        subprocess.run(['python', 'YT.py', topic, SAVE_RESOURCES])
        file_path = os.path.join(SAVE_RESOURCES, f"{topic} Tutorial.json")
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                resource_data = json.load(f)
            return jsonify(resource_data)
        else:
            return "File not found", 404
    else:
        file_path = os.path.join(SAVE_RESOURCES, f"{topic} Tutorial.json")
        with open(file_path, 'r') as f:
            resource_data = json.load(f)
        return jsonify(resource_data)

@app.route('/view/<topic>')
def view_roadmap(topic):
    """
    Renders the view_roadmap.html template with the specified topic.
    Parameters:
    - topic (str): The topic to be displayed in the roadmap.
    Returns:
    - str: The rendered HTML template.
    """

    return render_template('html/view_roadmap.html', topic=topic)

@app.route('/view_md/<topic>')
def view_md(topic):
    """
    Renders and returns the HTML template 'md_render.html' with the specified topic.
    Parameters:
    - topic (str): The topic to be rendered in the HTML template.
    Returns:
    - str: The rendered HTML template.
    """
    
    return render_template('html/md_render.html', topic=topic)


@app.route('/resources.html')
def resources():
    """
    Returns the rendered template for the 'resources.html' page.
    """

    return render_template('html/resources.html')


if __name__ == '__main__':
    app.run(debug=True)
