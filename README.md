# PathFinder

PathFinder is an innovative tool designed to streamline the learning process for individuals eager to explore new topics. It generates customized roadmaps tailored to any subject of interest and aggregates learning resources, providing learners with easy access to essential materials.

## Table of Contents

- [Problem Statement](#problem-statement)
- [Objectives](#objectives)
- [Technology Stack](#technology-stack)
- [Key Features](#key-features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Implementation Details](#implementation-details)
    - [APIs Used](#apis-used)
    - [Application Structure](#application-structure)
- [Challenges](#challenges)
- [Future Scope](#future-scope)
- [Contributions](#contributions)
- [License](#license)
- [References](#references)


## Problem Statement

In today's information-rich world, finding a structured and efficient learning path for a new topic can be overwhelming. Learners often face the challenge of sifting through vast amounts of unorganized information, leading to confusion and frustration. There is a need for a tool that can provide a clear and interactive roadmap for learning any new subject, along with relevant resources to facilitate the learning process.

## Objectives

  - Provide a structured learning path to offer learners a well-organized roadmap for any topic they wish to explore.
  - Enhancing learning experience by creating an interactive and user-friendly platform where learners can easily navigate through the roadmaps.
  - Intergrating relevant resources directly into the roadmap for easy access.

## Technology Stack

### Frontend
- **HTML**: Used for structuring the content of the PathFinder website.
- **CSS**: Applied for styling the website and ensuring a visually appealing and responsive design.
- **JavaScript (JS)**: Utilized for creating interactive elements and handling client-side logic.

### APIs and Libraries
- **Gemini API**: Employed for generating the customized roadmaps tailored to the user's subject of interest.
- **YouTube API**: Used to fetch related YouTube tutorials, providing users with valuable learning resources.
- **D3.js**: A JavaScript library for producing dynamic and interactive data visualizations, specifically used to render the roadmap tree.
- **Markdown.js**: Used to render and display the generated markdown resources in a user-friendly format.

### Backend
- **Flask**: A lightweight WSGI web application framework for Python. Flask is used to connect and route through all components, handling the submission of information and button clicks. It manages the rendering of HTML files and executes Python scripts to make the necessary API calls.

### Workflow
1. **User Interface**: The website, built with HTML, CSS, and JavaScript, provides an intuitive interface for users to input topics and interact with the generated roadmaps.
2. **API Integration**: Flask handles the routing and connects to the Gemini API for roadmap generation and the YouTube API for fetching tutorial videos.
3. **Visualization and Rendering**: D3.js is used to create an interactive roadmap tree, while Markdown.js displays the generated markdown resources.
4. **Dynamic Interaction**: Flask manages the interactions based on user input, rendering HTML files or running Python scripts to call the relevant APIs and update the content dynamically.

## Key Features

- **Interactive Roadmap**: Users can zoom in and out of the roadmap, making it easy to focus on specific sections or get an overview of the entire learning path. Nodes on the roadmap can be interacted with, allowing users to copy text for their notes.
- **Resource Listing**: With a single click, users can access a list of YouTube tutorials related to the topic, ensuring they have the necessary resources to support their learning journey.
- **Customizable Paths**: Users can enter any topic of their choice, and PathFinder will generate a customized roadmap tailored to their learning needs.
- **User-Friendly Interface**: The platform is designed to be intuitive, making it accessible for learners of all levels.
- **AI powered chatbot**: Provides users with a chatbot to get further resources or clear doubts regarding any topic.

## Getting Started

To get started with PathFinder, follow these steps:

1. Clone the repository using the following command:
```bash
git clone https://github.com/Shubhranil-Basak/PathFinder.git
```
2. Install the dependencies using the following command:
```bash
cd PathFinder
```
```bash
pip install -r requirements.txt
```
3. Set up environment variables by making a `.env` file and filling the following information:
Get your Gemini API Key here: https://aistudio.google.com/app/apikey
You need to enable your youtube API key in the google developer console and copy it from there.
```plaintext
API = YOUR_GEMINI_API
YTAPI = YOUR_YOUTUBE_API
```
4. Run the application by running the following command:
```bash
python app.py
```
and access it through your web browser

5. To use the chatbot, run the following command:
```bash
streamlit run gemini.py
```

## Usage
1. Input the topic you want to learn about aor upload a pre-generated roadmap file.
2. Click on the `submit` button to create a interactive learning path.
3. Click on the `Get Resources` button to generate resources on a desired topic.
4. Input the topic name you want the resources for or upload a pre-generated resource file.
5. Click on the `submit` button to get a resource markdown file.
6. Click on the `load news` and `load tutorial` button to get youtube based video news and tutorials on the specified topic.
7. In the chatbot, just type what you want to know about and click the `Send` button and to clear the chat history, click the `Clear Chat` button.

## Implementation Details

### APIs Used

1. **Gemini API**: The main API which generates the roadmap and the resource mardown file.
2. **Youtube API**: This API is used to gather the Youtube video for news and tutorials regarding the topics.

### Application Structure
1. `generated_resources` folder stores all the resources gathered using the youtube API.
2. `generated_roadmap` folder stores all the geerated roadmap made using the Gemini API and stores both the markdown and json format of the roadmap.
3. `templates` folder stores the HTML file for the necessary webpages.
4. `static` folder holds the CSS and JS files for the necessary webpages.
5. `app.py` is file which is responsible for linking and exeecuting all the necessary files and gathering resources for rendering when necessary.
6. `roadmap.py` is responsible for making the API call for generating the roadmap and storing it.
7. `resources.py` is responsible for making the API call for genrating a basic markdown regarding a specific topic.
8. `YT.py` is responsible for making the API call for gathering the youtube video links to be displayed in the resources webpage.
9. `.env` stores the environment variables (API Keys).
10. `gemini.py` is used for using Gemini as a chatbot for questions ad answers reagrdning any topic.

## Challenges

1. **Structured Prompt in Gemini**: Crafting a structured prompt in Gemini to ensure it produces data compatible with D3.js for generating the roadmap tree.
2. **File Integration with Flask**: Linking together various files using Flask to ensure they work cohesively and function as intended.
3. **Frontend and Backend Implementation**: Coordinating the implementation of webpages using HTML, CSS, and JS alongside Python for seamless user interaction.
4. **UI/UX Design**: Designing an intuitive and focused user interface to facilitate learning while minimizing distractions.

## Future Scope

1. **Expanding Resource Variety**: Currently limited to YouTube tutorials, future updates will aim to include related articles and other free/open source educational resources.
2. **Enhancing UI/UX**: Continuously improving the user interface and experience for a more intuitive and engaging platform.
3. **Improving Chat Interface**: Enhancing the chatbot functionality and integrating Retrieval-Augmented Generation (RAG) options for better assistance.
4. **Diversifying Roadmap Options**: Offering more diverse and comprehensive roadmap options to cover a wider range of topics and learning paths.

## Contributions

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

## References

1. Build a basic LLM chat app: https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps
2. Tidy tree: https://observablehq.com/@d3/tree/2?intent=fork
3. Youtube API documentation: https://developers.google.com/youtube/v3/docs/guideCategories/list
