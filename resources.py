import google.generativeai as genai
import sys
import os
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


def generate_resources(topic, save_directory):
  prompt_parts = [
  "You are a expert in any topic asked to you. When asked, you will tell about the important terms, techniques and methods needed to learn that and other things needed to learn that topic. You try to not give out any links to external resources and try to handle things and explain them as much a possible on your own",
  "input: Artificial Intelligence",
  "output: ## Artificial Intelligence: A Deep Dive\n\n\n**Core Concepts:**\n\n* **Machine Learning (ML):** The ability of a system to learn from data without explicit programming. This is achieved through algorithms that identify patterns and relationships in data, allowing the system to make predictions or decisions.\n* **Deep Learning (DL):** A subset of ML that uses artificial neural networks with multiple layers. These networks are inspired by the structure of the human brain and excel at processing complex, unstructured data like images, sound, and text.\n* **Natural Language Processing (NLP):** Enables computers to understand, interpret, and generate human language. This involves tasks like text classification, sentiment analysis, machine translation, and chatbots.\n* **Computer Vision:** Allows computers to \"see\" and interpret images and videos. This includes tasks like object recognition, image segmentation, and facial recognition.\n* **Robotics:** Focuses on designing, constructing, operating, and applying robots. This involves integrating AI for navigation, manipulation, and decision-making in various environments.\n\n**Key Techniques & Methods:**\n\n* **Supervised Learning:**  Algorithms learn from labeled data, where each input is associated with a known output. This allows the model to learn the relationship between inputs and outputs, enabling predictions for new data.\n* **Unsupervised Learning:**  Algorithms learn from unlabeled data, uncovering hidden patterns and structures. This is useful for tasks like clustering, anomaly detection, and dimensionality reduction.\n* **Reinforcement Learning:**  Algorithms learn through trial and error, receiving rewards or penalties for their actions. This allows them to optimize their behavior over time, achieving desired goals in complex environments.\n* **Neural Networks:**  Inspired by the human brain, these networks consist of interconnected nodes (neurons) that process information in layers. They learn by adjusting the weights of connections between neurons, allowing them to extract features and make predictions.\n* **Genetic Algorithms:** Inspired by biological evolution, these algorithms use a population of solutions and apply genetic operators (like mutation and crossover) to find optimal solutions for a given problem.\n\n**Important Terms:**\n\n* **Agent:** A system that can perceive its environment and take actions to achieve its goals.\n* **Algorithm:** A set of rules or steps that a computer follows to solve a specific problem.\n* **Data:** The raw material that AI systems learn from.\n* **Features:** Characteristics or properties extracted from data, used to train and evaluate AI models.\n* **Model:** A representation of the relationship between input and output, learned from data.\n* **Training:** The process of feeding data to a model to improve its performance.\n* **Evaluation:** Assessing the performance of a trained model on unseen data.\n* **Bias:** Systemic errors or prejudices introduced into AI models during training, leading to unfair or inaccurate results.\n\n**Beyond the Basics:**\n\n* **Ethics & Safety:**  AI raises important ethical considerations regarding bias, privacy, security, and the potential impact on society.\n* **Explainability & Transparency:**  Understanding how AI models make decisions is crucial for building trust and ensuring fairness.\n* **Applications:** AI is transforming numerous industries, including healthcare, finance, transportation, and entertainment.\n\n**Learning AI:**\n\n* **Online Courses & Resources:**  Numerous platforms like Coursera, edX, and Udacity offer comprehensive AI courses.\n* **Books:**  There are excellent textbooks and introductory guides on AI, machine learning, and deep learning.\n* **Practice:**  Hands-on experience is crucial. Experiment with AI tools and libraries, build projects, and participate in online competitions.",
  "input: Machine Learning",
  "output: ## Machine Learning: Demystifying the Magic of Data\n\n\n**Key Concepts:**\n\n* **Data:** The lifeblood of ML. Algorithms learn from patterns and relationships within data to make predictions or decisions. \n* **Algorithms:** The mathematical recipes that define how ML systems learn and operate. Each algorithm has its strengths and weaknesses, suitable for different types of data and tasks.\n* **Model:** The outcome of the learning process, representing the relationships discovered in the data. This model is then used to make predictions or decisions on new, unseen data.\n* **Training:** The process of feeding data to an algorithm to refine its parameters and optimize its performance.\n* **Evaluation:** Assessing the model's accuracy and performance on unseen data, ensuring it generalizes well to real-world scenarios.\n* **Features:** The specific characteristics or attributes extracted from data used to train and evaluate models.\n\n**Types of Machine Learning:**\n\n1. **Supervised Learning:** The algorithm is trained on labeled data, where each input is associated with a known output. This allows the model to learn the relationship between inputs and outputs, enabling predictions for new data.\n    * **Regression:** Predicting continuous values (e.g., house prices, stock prices).\n    * **Classification:** Categorizing data into predefined classes (e.g., spam detection, image recognition).\n2. **Unsupervised Learning:**  The algorithm learns from unlabeled data, uncovering hidden patterns and structures. This is useful for tasks like:\n    * **Clustering:** Grouping similar data points together (e.g., customer segmentation, anomaly detection).\n    * **Dimensionality Reduction:** Simplifying complex data by reducing the number of features while preserving important information.\n3. **Reinforcement Learning:**  The algorithm learns through trial and error, receiving rewards or penalties for its actions. This allows it to optimize its behavior over time, achieving desired goals in complex environments (e.g., game playing, robotics).\n\n**Essential Techniques & Methods:**\n\n* **Linear Regression:**  Predicting a continuous output based on a linear relationship between input features.\n* **Logistic Regression:**  Classifying data into categories based on a logistic function.\n* **Decision Trees:**  Building tree-like structures to represent decision rules, enabling predictions based on feature values.\n* **Support Vector Machines (SVMs):**  Finding optimal hyperplanes to separate data into distinct classes.\n* **Neural Networks:**  Inspired by the human brain, these networks consist of interconnected nodes (neurons) that process information in layers. They learn by adjusting the weights of connections between neurons, allowing them to extract features and make predictions.\n* **K-Means Clustering:**  Grouping data points into clusters based on their distance to cluster centers.\n* **Principal Component Analysis (PCA):**  Reducing data dimensionality by finding principal components (directions of greatest variance).\n\n**Important Considerations:**\n\n* **Data Quality:**  Garbage in, garbage out. ML models are highly sensitive to the quality and quantity of data used for training.\n* **Bias and Fairness:**  ML models can inherit biases from the data they are trained on, leading to unfair or discriminatory outcomes. \n* **Explainability and Interpretability:**  Understanding how models make decisions is crucial for building trust and ensuring ethical use.\n\n**Learning Machine Learning:**\n\n* **Online Courses & Resources:**  Platforms like Coursera, edX, and Udacity offer comprehensive ML courses.\n* **Books:**  There are excellent textbooks and introductory guides on ML, covering various concepts and algorithms.\n* **Libraries & Tools:**  Familiarize yourself with popular ML libraries like TensorFlow, PyTorch, scikit-learn, and others.\n* **Projects & Experiments:**  Hands-on experience is essential. Apply your knowledge to build projects, participate in online competitions, and explore real-world datasets.",
  "input: Linear Regression",
  "output: ## Linear Regression: Unveiling the Straight Line Secrets\n\n\n**Core Concepts:**\n\n* **Dependent Variable (Y):** The variable you are trying to predict (e.g., house price, temperature).\n* **Independent Variable(s) (X):** The variables you use to predict the dependent variable (e.g., square footage of the house, time of day).\n* **Linear Relationship:** The assumption that there is a straight-line relationship between the independent and dependent variables.\n* **Regression Line:** The best-fit straight line that minimizes the distance between the data points and the line itself.\n* **Slope (m):** The steepness of the regression line, indicating the change in the dependent variable for a unit change in the independent variable.\n* **Intercept (b):** The point where the regression line crosses the y-axis, indicating the value of the dependent variable when the independent variable is zero.\n* **Residuals:** The difference between the actual values of the dependent variable and the values predicted by the regression line.\n\n**Key Techniques & Methods:**\n\n* **Ordinary Least Squares (OLS):**  The most common method used to find the best-fit line. It minimizes the sum of squared residuals, finding the line that best fits the data points.\n* **Multiple Linear Regression:**  Extends the single-variable case to include multiple independent variables, allowing for more complex relationships between variables.\n* **Regularization:**  Techniques like Lasso and Ridge regression are used to prevent overfitting, where the model becomes too specific to the training data and performs poorly on new data.\n* **Feature Selection:**  Identifying the most relevant independent variables for the model, improving its accuracy and interpretability.\n\n**Interpreting Linear Regression:**\n\n* **R-squared (R²):** A measure of how well the regression line fits the data, ranging from 0 to 1. A higher R-squared indicates a better fit.\n* **p-value:**  A statistical test to determine whether the slope of the regression line is statistically significant. A low p-value suggests a strong relationship between the independent and dependent variables.\n* **Confidence Intervals:**  Represent the range of likely values for the slope and intercept, giving a sense of uncertainty in the model's predictions.\n\n**Applications of Linear Regression:**\n\n* **Predicting Housing Prices:**  Using features like square footage, number of bedrooms, and location to predict house prices.\n* **Estimating Sales:**  Predicting future sales based on factors like advertising spend, seasonality, and economic indicators.\n* **Analyzing Stock Market Trends:**  Using historical data to predict future stock prices.\n* **Forecasting Weather Patterns:**  Predicting temperature, rainfall, and other weather variables based on historical data.\n\n**Learning Linear Regression:**\n\n* **Online Courses & Resources:**  Platforms like Coursera, edX, and Khan Academy offer courses and tutorials on linear regression.\n* **Books:**  Numerous textbooks and introductory guides cover linear regression and related statistical concepts.\n* **Software & Libraries:**  Use statistical software like R, Python, or MATLAB with libraries like scikit-learn to implement and analyze linear regression models.\n* **Hands-on Practice:**  Work with datasets, build models, interpret results, and experiment with different techniques.",
  "input: Generative AI",
  "output: ## Generative AI: Crafting New Realities from Data\n\n**Core Concepts:**\n\n* **Generative Models:**  AI systems that learn patterns from existing data and use that knowledge to create new, original content. They don't simply copy or modify existing data; they generate something entirely new.\n* **Data:**  The foundation for generative AI. Models learn from massive datasets to understand the nuances of language, images, sounds, and other data formats.\n* **Latent Space:**  A hidden space where the model represents data in a compressed form, capturing the underlying structure and relationships. \n* **Sampling:**  The process of drawing new data points from the learned latent space, resulting in the generation of novel content.\n* **Creativity and Innovation:**  Generative AI unlocks new possibilities for creating unique and diverse content, ranging from realistic images and videos to compelling text and music.\n\n**Key Techniques & Methods:**\n\n* **Generative Adversarial Networks (GANs):**  A powerful framework where two neural networks compete against each other: a generator that creates fake data and a discriminator that tries to distinguish it from real data. This adversarial process leads to increasingly realistic and diverse outputs.\n* **Variational Autoencoders (VAEs):**  Another type of generative model that learns a compressed representation of the data and allows for sampling new data points from this compressed representation. VAEs are known for their ability to generate smooth and coherent outputs.\n* **Diffusion Models:**  Based on the concept of gradually adding noise to data and then reversing the process to generate new data. These models are known for their high-quality outputs and ability to capture fine-grained details.\n* **Transformer Models (e.g., GPT-3, DALL-E):**  Powerful language and image models that leverage the transformer architecture, enabling them to process data in a more efficient and context-aware manner. These models have achieved impressive results in text generation, image creation, and other tasks.\n\n**Applications of Generative AI:**\n\n* **Content Creation:**  Generate realistic images, videos, text, music, and other types of content for various applications, including art, advertising, entertainment, and education.\n* **Design and Innovation:**  Create novel designs for products, buildings, and other objects, exploring new possibilities and pushing creative boundaries.\n* **Drug Discovery and Material Science:**  Generate new drug candidates, design novel materials, and accelerate scientific research.\n* **Personalized Experiences:**  Create personalized content, recommendations, and interactions, tailoring experiences to individual preferences.\n\n**Important Considerations:**\n\n* **Ethical Implications:**  The potential for misuse of generative AI, such as creating deepfakes or spreading misinformation, raises concerns about its ethical use.\n* **Bias and Fairness:**  Generative models can inherit biases from the data they are trained on, leading to biased outputs and perpetuating existing inequalities.\n* **Intellectual Property:**  The ownership and rights to generated content are still evolving, raising questions about copyright and fair use.\n\n**Learning Generative AI:**\n\n* **Online Courses & Resources:**  Platforms like Coursera, edX, and Udacity offer courses and tutorials on generative AI techniques.\n* **Books and Research Papers:**  Stay updated on the latest advancements and explore research papers from leading institutions.\n* **Code Libraries and Frameworks:**  Experiment with tools like TensorFlow, PyTorch, and others to implement generative models.\n* **Participate in Communities:**  Engage with online communities and forums to learn from others, share knowledge, and contribute to the field.",
  "input: cooking",
  "output: ## Cooking: A Culinary Adventure\n\n**Core Concepts:**\n\n* **Ingredients:** The building blocks of any dish, each with unique properties, flavors, and textures.\n* **Techniques:** The methods and skills used to transform ingredients into delicious meals.\n* **Recipes:**  Detailed instructions for preparing specific dishes, outlining ingredients, quantities, and step-by-step procedures.\n* **Flavor Profiles:**  The combination of tastes that define a dish, considering sweet, sour, salty, bitter, umami, and spice.\n* **Culinary Traditions:**  The unique cuisines, ingredients, and techniques of different cultures and regions.\n* **Sensory Experience:**  The interplay of taste, smell, sight, touch, and sound that contribute to the enjoyment of a meal.\n\n**Essential Techniques & Methods:**\n\n* **Chopping & Slicing:**  Precisely cutting ingredients into various shapes and sizes for optimal cooking and presentation.\n* **Sautéing:**  Cooking ingredients quickly over medium-high heat in a small amount of oil, developing flavors and textures.\n* **Roasting:**  Cooking ingredients in an oven, using dry heat to create crispy exteriors and tender interiors.\n* **Boiling:**  Cooking ingredients in simmering water, transferring heat and creating tender textures.\n* **Baking:**  Cooking ingredients in an oven, using dry heat to produce pastries, breads, and desserts.\n* **Grilling:**  Cooking ingredients over direct heat, creating charred surfaces and smoky flavors.\n* **Braising:**  Cooking ingredients slowly in liquid, resulting in tender and flavorful results.\n* **Stir-frying:**  Cooking ingredients quickly in a wok, tossing constantly to ensure even cooking and create crispy textures.\n\n**Important Ingredients & Their Roles:**\n\n* **Proteins:**  The primary building blocks of a meal, providing essential nutrients and flavor. Examples: chicken, beef, fish, tofu, beans.\n* **Vegetables:**  Add color, vitamins, minerals, and flavor. Examples: onions, garlic, carrots, broccoli, spinach.\n* **Starch:**  Provides bulk, texture, and can be used to create sauces and gravies. Examples: potatoes, rice, pasta.\n* **Fats:**  Add richness, flavor, and moisture to dishes. Examples: butter, oil, olive oil.\n* **Herbs & Spices:**  Enhance flavors and aromas, adding complexity and depth to dishes. Examples: basil, oregano, cumin, cinnamon.\n\n**Beyond the Basics:**\n\n* **Understanding Seasonality:**  Knowing when certain ingredients are in season helps you access the freshest and most flavorful produce.\n* **Experimentation:**  Don't be afraid to experiment with flavors and techniques, substituting ingredients or adapting recipes to your preferences.\n* **Food Safety:**  Proper food handling, cooking temperatures, and hygiene practices are crucial for ensuring food safety.\n* **Presentation:**  Arrange dishes attractively, considering color, texture, and height to create an appealing visual experience.\n\n**Learning to Cook:**\n\n* **Cookbooks:**  A wealth of recipes, techniques, and culinary inspiration from all over the world.\n* **Online Resources:**  Websites, blogs, and videos offer recipes, cooking tips, and educational resources.\n* **Cooking Classes:**  Hands-on learning experiences led by experienced chefs, allowing you to gain practical skills.\n* **Practice:**  The more you cook, the more confident and skilled you will become. Start with simple recipes and gradually work your way up to more complex dishes.\n* **Food Communities:**  Connect with other cooking enthusiasts, share tips, recipes, and experiences.",
  "input: UPSC Exam",
  "output: ## UPSC Exam: The Gateway to India's Civil Services\n\n**Understanding the UPSC Exam:**\n\n* **Union Public Service Commission (UPSC):**  The central recruiting agency of the Indian government, responsible for selecting candidates for various civil services positions.\n* **Civil Services:**  The backbone of the Indian administration, encompassing roles in various departments like the Indian Administrative Service (IAS), Indian Foreign Service (IFS), Indian Police Service (IPS), and others.\n* **Highly Competitive:**  The UPSC exam is known for its rigorous nature and high competition, with lakhs of candidates vying for limited seats.\n* **Multi-Tiered Structure:**  The exam is conducted in three tiers, each testing different aspects of a candidate's knowledge and abilities.\n\n**Exam Structure:**\n\n**Tier 1: Preliminary Examination (Objective Type)**\n\n* **General Studies (GS):**  Covers topics like history, geography, polity, economics, and current affairs.\n* **Civil Services Aptitude Test (CSAT):**  Evaluates comprehension, reasoning, analytical ability, and basic numerical skills.\n\n**Tier 2: Main Examination (Descriptive Type)**\n\n* **General Studies (GS):**  Covers four papers in greater depth than Tier 1, including ethics, integrity, and aptitude.\n* **Optional Subject:**  Candidates choose one subject from a list of options, showcasing specialized knowledge.\n* **Language Papers:**  Assesses proficiency in English and a qualifying language (for those whose native language is not English).\n\n**Tier 3: Personality Test (Interview)**\n\n* **Interview Board:**  Candidates are assessed by a panel of experts on their personality, leadership qualities, communication skills, and general awareness.\n\n**Key Subjects and Areas of Focus:**\n\n* **History:**  India's ancient, medieval, and modern history, including art, culture, and social movements.\n* **Geography:**  India's physical, economic, and human geography, along with global issues like climate change and disaster management.\n* **Polity:**  Indian Constitution, political institutions, governance, and public policy.\n* **Economics:**  Indian economy, economic planning, development, and global economic trends.\n* **Current Affairs:**  National and international events, social issues, and government initiatives.\n* **Ethics, Integrity, and Aptitude:**  Ethical principles, values, leadership, and public service ethics.\n\n**Preparation Strategies:**\n\n* **Thorough Study:**  Invest significant time and effort in understanding the syllabus and mastering the core concepts.\n* **Regular Practice:**  Solve previous years' question papers and mock tests to get familiar with the exam pattern and improve time management.\n* **Coaching and Guidance:**  Consider enrolling in coaching classes or seeking guidance from mentors to enhance understanding and preparation.\n* **Reading and Current Affairs:**  Stay updated with current events through newspapers, magazines, and online resources.\n* **Self-Discipline and Motivation:**  Maintain consistency, focus, and a positive attitude throughout the preparation journey.\n\n**Important Points:**\n\n* **Age Limit:**  Candidates must meet the eligibility criteria, including age limits, educational qualifications, and other requirements.\n* **Reservation:**  The exam provides reservation for candidates belonging to Scheduled Castes (SC), Scheduled Tribes (ST), Other Backward Classes (OBC), and other categories.\n* **Preparation Resources:**  Numerous books, websites, and online resources are available for UPSC preparation. \n* **Success Requires Dedication:**  The UPSC exam demands unwavering dedication, hard work, and perseverance.",
  "input: Current Affairs",
  "output: ## Current Affairs: Staying Informed in a Dynamic World\n\n**What are Current Affairs?**\n\n* **News and Events:**  Current affairs encompass the latest happenings, trends, and developments in the world, including political, economic, social, cultural, and technological aspects.\n* **Global and National Significance:**  Events with significant impact on national and international affairs, influencing policies, economies, and societies.\n* **Dynamic and Ever-Changing:**  Current affairs are constantly evolving, requiring continuous monitoring and analysis to stay informed.\n\n**Why are Current Affairs Important?**\n\n* **Informed Citizenry:**  Staying informed about current affairs empowers individuals to make informed decisions and engage in constructive discussions.\n* **Exam Preparation:**  Current affairs are essential for various competitive exams, including UPSC, state civil services, and other entrance tests.\n* **Career Advancement:**  Knowledge of current affairs is crucial for professionals in fields like journalism, public relations, diplomacy, and law.\n* **Global Awareness:**  Understanding current affairs fosters a broader perspective on global issues, promoting empathy and understanding across cultures.\n\n**Key Areas to Focus on:**\n\n* **Politics and Governance:**  National and international political developments, elections, government policies, and diplomatic relations.\n* **Economics:**  Global and national economic trends, financial markets, business news, and industry updates.\n* **Social Issues:**  Current social challenges, including poverty, inequality, gender issues, environmental concerns, and healthcare.\n* **Science and Technology:**  Advancements in technology, scientific discoveries, innovations, and their impact on society.\n* **Environment and Climate Change:**  Environmental issues, climate change impacts, international agreements, and sustainability efforts.\n* **Arts and Culture:**  Latest trends in art, music, literature, cinema, and cultural events.\n\n**How to Stay Updated:**\n\n* **Newspapers and Magazines:**  Reputable news sources like The Hindu, The Indian Express, and The Times of India provide comprehensive coverage.\n* **News Websites and Apps:**  Online news platforms like BBC News, Al Jazeera, and Reuters offer real-time updates and in-depth analysis.\n* **Current Affairs Magazines:**  Publications like Yojana, Kurukshetra, and Pratiyogita Darpan offer concise summaries and analysis of key issues.\n* **Online Resources:**  Websites like PIB (Press Information Bureau), PRS Legislative Research, and Indian Institute of Public Administration provide government publications and policy analysis.\n* **Social Media:**  Follow official accounts of government bodies, news organizations, and experts to get quick updates and insights.\n\n**Important Considerations:**\n\n* **Fact-Checking:**  Be critical of information and verify it from multiple sources to avoid misinformation.\n* **Analytical Thinking:**  Develop the ability to analyze current events, understand their underlying causes, and predict potential outcomes.\n* **Note-Taking and Summarizing:**  Regularly take notes and summarize key events and developments to retain information.\n* **Discussion and Debate:**  Engage in discussions and debates with others to gain different perspectives and deepen your understanding.",
  "input: Transformer based AI",
  "output: ## Transformer-Based AI: A Revolution in Language and Beyond\n\n**Core Concepts:**\n\n* **Transformers:** A type of neural network architecture that revolutionized natural language processing (NLP) and has since expanded to other domains like computer vision. \n* **Attention Mechanism:**  The key innovation of transformers. It allows the model to focus on specific parts of the input sequence (e.g., words in a sentence) and weigh them differently based on their relevance to the task at hand. This helps capture long-range dependencies and relationships within data.\n* **Self-Attention:**  A special case of attention where the model attends to different parts of the same input sequence. This allows it to understand the context of words and their relationships within the sequence.\n* **Encoder-Decoder Architecture:**  The typical structure of transformer models, where an encoder processes the input sequence and a decoder generates the output based on the encoded information.\n\n**Key Features and Advantages:**\n\n* **Parallel Processing:**  Transformers can process sequences in parallel, making them significantly faster than traditional recurrent neural networks (RNNs) that processed data sequentially.\n* **Long-Range Dependencies:**  The attention mechanism allows transformers to capture relationships between words or elements far apart in a sequence, overcoming the limitations of RNNs that struggled with long sequences.\n* **Contextual Embeddings:**  Transformers learn contextual word embeddings, meaning that the representation of a word changes based on its context within a sentence or document.\n* **Versatility:**  Transformers have proven highly versatile, excelling in various NLP tasks like machine translation, text summarization, question answering, and text generation.\n\n**Notable Transformer-Based Models:**\n\n* **GPT-3 (Generative Pre-trained Transformer 3):**  A powerful language model known for its ability to generate realistic and coherent text, translate languages, write different kinds of creative content, and answer your questions in an informative way.\n* **BERT (Bidirectional Encoder Representations from Transformers):**  A model that excels at understanding the context of words within a sentence, achieving state-of-the-art results on tasks like sentiment analysis, question answering, and text classification.\n* **DALL-E:**  A transformer model that can generate images from text descriptions, showcasing its ability to bridge the gap between language and vision.\n* **ViT (Vision Transformer):**  An adaptation of the transformer architecture to image processing, demonstrating its potential for tasks like image classification and object detection.\n\n**Implications and Future Directions:**\n\n* **Advancements in NLP:**  Transformers have significantly improved the performance of NLP systems, leading to more accurate and sophisticated language models.\n* **Multimodality:**  Research is expanding into multi-modal applications, where transformers can process and generate different forms of data like text, images, and audio.\n* **Ethical Considerations:**  As transformer models become more powerful, ethical considerations like bias, misinformation, and the responsible use of these technologies become increasingly important.\n\n**Learning about Transformer-Based AI:**\n\n* **Online Courses and Resources:**  Platforms like Coursera, edX, and DeepLearning.AI offer courses and tutorials on transformers and NLP.\n* **Research Papers:**  Keep up with the latest research on transformers by exploring publications from leading universities and research labs.\n* **Open-Source Libraries:**  Experiment with open-source libraries like Hugging Face Transformers and TensorFlow to implement and use transformer models.\n* **Community Engagement:**  Join online communities and forums to learn from experts, discuss advancements, and collaborate on projects.",
  "input: Python Programming",
  "output: ## Python Programming: A Gateway to the World of Code\n\n**Core Concepts:**\n\n* **Variables:**  Containers that store data. Think of them as labeled boxes holding different types of information.\n* **Data Types:**  Different categories of data, including numbers (integers, floats), text (strings), and logical values (booleans).\n* **Operators:** Symbols that perform operations on data, such as addition, subtraction, comparison, and logical operations.\n* **Control Flow:**  Structures that determine the order in which code is executed, allowing for branching (if-else statements), loops (for, while), and functions.\n* **Functions:**  Reusable blocks of code that perform specific tasks, making your programs modular and efficient.\n* **Data Structures:**  Ways to organize and store collections of data, including lists, tuples, dictionaries, and sets.\n* **Modules and Libraries:**  Pre-written code that extends Python's capabilities, providing tools for various tasks like web development, data analysis, and machine learning.\n\n**Key Techniques & Methods:**\n\n* **Object-Oriented Programming (OOP):**  A paradigm that models real-world entities as objects with attributes (data) and methods (functions). This promotes code reusability and maintainability.\n* **Debugging:**  The process of identifying and fixing errors in your code, often involving techniques like print statements, code inspection, and using a debugger tool.\n* **Testing:**  Writing code to ensure your program behaves as expected under different scenarios, ensuring code quality and reliability.\n* **Documentation:**  Creating clear and concise documentation to explain your code's functionality, making it easier for others (and your future self) to understand.\n\n**Important Libraries:**\n\n* **NumPy:**  A powerful library for numerical computing, providing tools for arrays, matrices, and mathematical operations.\n* **Pandas:**  A data manipulation and analysis library, excellent for working with spreadsheets, tables, and time series data.\n* **Matplotlib:**  A plotting library for creating visualizations of data, generating charts, graphs, and figures.\n* **Scikit-learn:**  A machine learning library, offering algorithms for classification, regression, clustering, and more.\n* **Requests:**  A library for making HTTP requests, enabling you to interact with web services and APIs.\n* **Django/Flask:**  Popular web frameworks for building web applications, providing tools for routing, templating, and database interaction.\n\n**Beyond the Basics:**\n\n* **Data Structures and Algorithms:**  A deeper dive into advanced data structures and algorithms, optimizing your code's efficiency and performance.\n* **Database Interaction:**  Learning to connect Python with databases like MySQL or PostgreSQL, managing and manipulating data.\n* **Web Development:**  Building interactive web applications using frameworks like Django or Flask, combining front-end and back-end development.\n* **Machine Learning:**  Applying your Python skills to train and deploy machine learning models, automating tasks and making predictions.\n\n**Learning Python:**\n\n* **Online Courses:**  Platforms like Coursera, edX, and Codecademy offer comprehensive Python courses for beginners and experienced learners.\n* **Books:**  Numerous textbooks and online resources provide excellent introductions to Python programming.\n* **Coding Platforms:**  Websites like HackerRank, LeetCode, and Project Euler offer coding challenges to practice your skills and learn new concepts.\n* **Open-Source Projects:**  Contribute to open-source projects to gain real-world experience and collaborate with other developers.\n* **Community Support:**  Join online forums and communities like Stack Overflow to ask questions, share knowledge, and learn from others.\n* **Practice:**  The key to mastering Python is through consistent practice. Build projects, solve problems, and experiment with different concepts.",
  f"input: {topic}",
  "output: ",
]
  response = model.generate_content(prompt_parts)

  md_file_path = os.path.join(save_directory, f"{topic}_resource.md")
  with open(md_file_path, "w") as f:
     f.write(response.text)


if __name__ == '__main__':
    if len(sys.argv) > 2:
        topic = sys.argv[1]
        save_directory = sys.argv[2]
        generate_resources(topic, save_directory)
    else:
        print("Please provide a topic and a save directory")