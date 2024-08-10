import sys
import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

API = os.environ.get("API")

genai.configure(api_key=API)

# Set up the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

model = genai.GenerativeModel(model_name="gemini-1.5-flash-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

def parse_response_to_json(response_text):
    """
    Parses the response text and converts it to a JSON structure.
    @param:
        response_text (str): The response text to be parsed.
    Returns:
        list: A list representing the parsed JSON structure.
    Example:
        response_text = "### Section 1\n- Item 1\n- Item 2\n### Section 2\n- Item 3"
        parse_response_to_json(response_text)
        # Output: [{'title': 'Section 1', 'items': [{'title': 'Item 1', 'subitems': []}, {'title': 'Item 2', 'subitems': []}]}, {'title': 'Section 2', 'items': [{'title': 'Item 3', 'subitems': []}]}]
    """
    lines = response_text.split('\n')
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



# Strutured prompt parts for generating a roadmap
def generate_roadmap(topic, save_directory):
    """
    Generates a roadmap for a given topic and saves it as a markdown file and a JSON file.
    @param:
        topic (str): The topic for which the roadmap is generated.
        save_directory (str): The directory where the generated files will be saved.
    Returns:
        None
    """

    prompt_parts = [
  "input: photography",
  "output: ### Photography\n\n1. **Photography Basics**\n   - Understanding Exposure (Aperture, Shutter Speed, ISO)\n   - Camera Types (DSLR, Mirrorless, Point-and-Shoot)\n   - Lens Types and Uses\n\n2. **Camera Settings and Controls**\n   - Manual Mode\n   - Aperture Priority Mode\n   - Shutter Priority Mode\n   - ISO Settings\n\n3. **Composition Techniques**\n   - Rule of Thirds\n   - Leading Lines\n   - Framing\n   - Symmetry and Patterns\n\n4. **Lighting Fundamentals**\n   - Natural Light\n   - Artificial Light\n   - Using Flash\n   - Reflectors and Diffusers\n\n5. **Focus and Depth of Field**\n   - Autofocus vs. Manual Focus\n   - Depth of Field Control\n   - Bokeh Effect\n\n6. **Shooting in Different Conditions**\n   - Low Light Photography\n   - Action and Sports Photography\n   - Landscape Photography\n   - Portrait Photography\n\n7. **Post-Processing Basics**\n   - Photo Editing Software (Adobe Lightroom, Photoshop)\n   - Basic Editing Techniques (Cropping, Exposure Adjustments)\n   - Color Correction and Grading\n\n8. **Advanced Editing Techniques**\n   - Retouching and Cloning\n   - HDR Photography\n   - Panorama Stitching\n   - Composite Imaging\n\n9. **Specialized Photography**\n   - Macro Photography\n   - Astrophotography\n   - Street Photography\n   - Wildlife Photography\n\n10. **Photography Equipment**\n    - Tripods and Stabilizers\n    - Filters (ND, Polarizers)\n    - External Flashes and Lighting Kits\n    - Camera Bags and Straps\n\n11. **Portfolio Development**\n    - Selecting Best Shots\n    - Creating a Cohesive Theme\n    - Building an Online Portfolio\n    - Printing and Framing Photographs\n\n12. **Professional Practices**\n    - Working with Clients\n    - Pricing and Contracts\n    - Marketing and Social Media\n    - Continuous Learning and Improvement",
  "input: Artificial intelligence",
  "output: ### Artificial Intelligence\n\n1. **Mathematics Fundamentals**\n   - Linear Algebra\n   - Calculus\n   - Probability\n   - Statistics\n\n2. **Programming Skills**\n   - Python\n   - R\n   - Java\n   - C++\n\n3. **Data Structures and Algorithms**\n   - Arrays\n   - Linked Lists\n   - Trees\n   - Graphs\n   - Sorting and Searching Algorithms\n\n4. **Probability and Statistics**\n   - Descriptive Statistics\n   - Inferential Statistics\n   - Probability Distributions\n   - Hypothesis Testing\n\n5. **Machine Learning Basics**\n   - Supervised Learning\n   - Unsupervised Learning\n   - Regression\n   - Classification\n   - Clustering\n\n6. **Deep Learning**\n   - Neural Networks\n   - Convolutional Neural Networks (CNNs)\n   - Recurrent Neural Networks (RNNs)\n   - Generative Adversarial Networks (GANs)\n\n7. **Natural Language Processing**\n   - Text Preprocessing\n   - Sentiment Analysis\n   - Language Models\n   - Named Entity Recognition (NER)\n\n8. **Computer Vision**\n   - Image Preprocessing\n   - Object Detection\n   - Image Classification\n   - Image Segmentation\n\n9. **Reinforcement Learning**\n   - Markov Decision Processes\n   - Q-Learning\n   - Policy Gradient Methods\n   - Deep Q-Networks (DQN)\n\n10. **AI Ethics**\n    - Fairness\n    - Accountability\n    - Transparency\n    - Privacy\n\n11. **AI Tools and Frameworks**\n    - TensorFlow\n    - Keras\n    - PyTorch\n    - Scikit-learn\n\n12. **Practical Projects and Applications**\n    - Building AI Models\n    - Real-world Case Studies\n    - Deploying AI Systems\n    - Continuous Learning and Improvement",
  "input: cooking",
  "output: ### Cooking\n\n1. **Kitchen Safety and Hygiene**\n   - Proper Hand Washing\n   - Food Storage\n   - Cross-contamination Prevention\n   - Safe Cooking Temperatures\n\n2. **Basic Knife Skills**\n   - Knife Types and Uses\n   - Chopping, Slicing, and Dicing\n   - Knife Sharpening and Maintenance\n   - Safe Knife Handling\n\n3. **Understanding Ingredients**\n   - Vegetables and Fruits\n   - Meats and Seafood\n   - Herbs and Spices\n   - Grains and Legumes\n\n4. **Cooking Techniques**\n   - Boiling\n   - Frying\n   - Baking\n   - Grilling\n   - Roasting\n\n5. **Flavor Pairings and Seasoning**\n   - Basic Seasoning Techniques\n   - Herb and Spice Combinations\n   - Balancing Flavors (Sweet, Sour, Salty, Bitter, Umami)\n   - Using Marinades and Rubs\n\n6. **Sauces and Condiments**\n   - Basic Sauces (Tomato, Bechamel, Velouté, etc.)\n   - Salad Dressings\n   - Dips and Spreads\n   - Homemade Condiments\n\n7. **Basic Recipes**\n   - Soups and Stews\n   - Salads\n   - Pasta Dishes\n   - Simple Desserts\n\n8. **Baking and Pastry Basics**\n   - Bread Baking\n   - Cake Baking\n   - Pastry Doughs\n   - Cookie and Biscuit Making\n\n9. **Meal Planning and Preparation**\n   - Creating a Meal Plan\n   - Grocery Shopping Tips\n   - Batch Cooking\n   - Storing Prepared Meals\n\n10. **Special Diets and Nutrition**\n    - Vegetarian and Vegan Cooking\n    - Gluten-Free Cooking\n    - Low-carb and Keto Cooking\n    - Balanced Meal Preparation\n\n11. **Plating and Presentation**\n    - Plate Composition\n    - Garnishing Techniques\n    - Color and Texture Balance\n    - Serving Techniques\n\n12. **Advanced Cooking Techniques**\n    - Sous Vide\n    - Fermentation\n    - Molecular Gastronomy\n    - Smoking and Curing",
  f"input: {topic}",
  "output: ",
]
    response = model.generate_content(prompt_parts)

    md_file_path = os.path.join(save_directory, f"{topic}.md")
    with open(md_file_path, "w") as f:
        f.write(response.text)
    
    roadmap_json = parse_response_to_json(response.text)
    json_file_path = os.path.join(save_directory, f"{topic}.json")
    with open(json_file_path, "w") as f:
        json.dump(roadmap_json, f, indent=4)

if __name__ == '__main__':
    if len(sys.argv) > 2:
        topic = sys.argv[1]
        save_directory = sys.argv[2]
        generate_roadmap(topic, save_directory)
    else:
        print("Please provide a topic and a save directory")
