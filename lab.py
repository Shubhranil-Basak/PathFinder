from dotenv import load_dotenv
import os
import google.generativeai as genai


load_dotenv()

API = os.environ.get("API")
print(API)


genai.configure(api_key=API)

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
]

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro-latest",
  safety_settings=safety_settings,
  generation_config=generation_config,
  system_instruction="You are now an expert roadmap maker. When given a topic, you make a short but a comprehensive roadmap. Starting with the basics and under each topic list resources as the content with title corresponding to the type of the resource. Resources can be books, articles, research papers, websites, communities and forums, videos, news and make sure to provide valid links and references to those resources. Make sure the resources are open sources and even if paid, they should be cheap.",
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "Artificial Intelligence\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "### Artificial Intelligence\n\n# 1. Foundations\n\n* **Course:** Elements of AI - [https://www.elementsofai.com/](https://www.elementsofai.com/) (Free online course covering basic AI concepts)\n* **Book:** Artificial Intelligence: A Modern Approach - Stuart Russell and Peter Norvig (Comprehensive textbook on AI)\n* **Article:** Computing machinery and intelligence - Alan Turing (Seminal paper introducing the Turing Test) - [https://www.csee.umbc.edu/~chang/141/papers/turing.pdf](https://www.csee.umbc.edu/~chang/141/papers/turing.pdf)\n\n# 2. Mathematics for AI\n\n* **Course:** Mathematics for Machine Learning - Coursera - [https://www.coursera.org/courses?query=mathematics%20for%20machine%20learning](https://www.coursera.org/courses?query=mathematics%20for%20machine%20learning) (Series of courses covering essential mathematical concepts)\n* **Book:** Linear Algebra and Its Applications - Gilbert Strang (Textbook focusing on linear algebra, crucial for understanding AI algorithms)\n* **Video Series:** 3Blue1Brown - Essence of linear algebra - [https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_Qr](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_Qr) (Visual explanations of key linear algebra concepts)\n\n# 3. Programming for AI\n\n* **Course:** Python for Everybody - Coursera - [https://www.coursera.org/specializations/python](https://www.coursera.org/specializations/python) (Specialization covering Python basics, data structures, and programming for data analysis)\n* **Book:** Python for Data Analysis -  Wes McKinney (Focuses on using Python libraries like pandas and NumPy for data manipulation and analysis)\n* **Website:** Real Python - [https://realpython.com/](https://realpython.com/) (Extensive resource with tutorials, articles, and courses on various Python topics, including data science and AI)\n\n# 4. Core AI Concepts\n\n* **Course:** Machine Learning - Andrew Ng - Coursera - [https://www.coursera.org/learn/machine-learning](https://www.coursera.org/learn/machine-learning) (Widely acclaimed introductory course to machine learning)\n* **Book:** Deep Learning - Ian Goodfellow, Yoshua Bengio, and Aaron Courville (Comprehensive book on deep learning)\n* **Research Paper:** Playing Atari with Deep Reinforcement Learning - DeepMind ([https://www.nature.com/articles/nature14236](https://www.nature.com/articles/nature14236)) (Groundbreaking work on using deep learning for game playing) \n\n# 5. Specialized AI Areas\n\n* **Natural Language Processing (NLP):**\n    - **Book:** Speech and Language Processing - Jurafsky & Martin (Comprehensive textbook on NLP)\n    - **Course:** Natural Language Processing - Stanford University - [https://nlp.stanford.edu/courses/](https://nlp.stanford.edu/courses/) (Graduate-level courses covering various NLP topics) \n\n* **Computer Vision (CV):**\n    - **Book:** Computer Vision: Algorithms and Applications - Richard Szeliski (Textbook covering computer vision techniques)\n    - **Website:** OpenCV - [https://opencv.org/](https://opencv.org/) (Open-source computer vision library with documentation, tutorials, and a community forum) \n\n* **Robotics:**\n    - **Book:** Probabilistic Robotics - Sebastian Thrun, Wolfram Burgard, Dieter Fox (Focuses on probabilistic algorithms for robotic applications)\n    - **Community:** ROS Discourse - [https://discourse.ros.org/](https://discourse.ros.org/) (Forum for the Robot Operating System (ROS)) \n\n# 6. Keeping Up with AI\n\n* **News:** MIT Technology Review AI section - [https://www.technologyreview.com/topic/artificial-intelligence/](https://www.technologyreview.com/topic/artificial-intelligence/) (Provides news and analysis on AI advancements)\n* **Forum:** Reddit r/MachineLearning - [https://www.reddit.com/r/MachineLearning/](https://www.reddit.com/r/MachineLearning/) (Active community for discussing machine learning research, applications, and news)\n* **Conferences:** NeurIPS, ICML, AAAI (Top academic conferences in AI, often featuring new research and breakthroughs)\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "Photography",
      ],
    },
    {
      "role": "model",
      "parts": [
        "### Roadmap for Photography\n\n\n\n# 1. Foundations of Photography\n\n* **Course:** Alison Diploma in Digital Photography - [https://alison.com/course/diploma-in-digital-photography](https://alison.com/course/diploma-in-digital-photography) (Free online course covering the basics of digital photography)\n* **Book:** Understanding Exposure - Bryan Peterson (Explains the fundamental elements of exposure: aperture, shutter speed, and ISO)\n* **Website:** Photography Life - [https://photographylife.com/](https://photographylife.com/) (Extensive resource with tutorials, tips, and reviews on various photography aspects)\n\n# 2. Camera Operations and Settings\n\n* **Video Series:** Peter McKinnon's YouTube Channel - [https://www.youtube.com/user/petermckinnon24](https://www.youtube.com/user/petermckinnon24) (Entertaining tutorials and insights on camera techniques and creative filmmaking)\n* **Book:** The Photographer's Eye - Michael Freeman (Focuses on composition, visual storytelling, and developing your photographic style)\n* **Community:** Reddit r/photography - [https://www.reddit.com/r/photography/](https://www.reddit.com/r/photography/) (Active community for sharing photos, asking questions, and discussing various photographic topics)\n\n# 3. Lighting and Composition\n\n* **Book:** Light: Science & Magic - Fil Hunter, Steven Biver, Paul Fuqua (Explores the science of light and its application in photography)\n* **Article:** Rule of Thirds - [https://photographylife.com/landscapes/rule-of-thirds-photography](https://photographylife.com/landscapes/rule-of-thirds-photography) ( Explains the classic compositional guideline for creating balanced and engaging photos)\n* **Video Tutorial:** Using Natural Light for Portraits - Jessica Kobeissi - [https://www.youtube.com/watch?v=mJ2h5NF_tHs](https://www.youtube.com/watch?v=mJ2h5NF_tHs) (Demonstrates how to effectively use natural light for portrait photography)\n\n# 4. Post-Processing and Editing\n\n* **Software:** GIMP - [https://www.gimp.org/](https://www.gimp.org/) (Free and open-source image editing software with powerful features)\n* **Course:** Adobe Photoshop Tutorials - [https://helpx.adobe.com/photoshop/tutorials.html](https://helpx.adobe.com/photoshop/tutorials.html) (Official tutorials for learning various Photoshop techniques)\n* **Video Series:** Phlearn YouTube Channel - [https://www.youtube.com/user/PhlearnLLC](https://www.youtube.com/user/PhlearnLLC) (Offers comprehensive tutorials on Photoshop and Lightroom, covering both basic and advanced edits)\n\n# 5. Exploring Different Genres\n\n* **Book:** Landscape Photography: From Vision to Image - Guy Tal (Focuses on landscape photography techniques, composition, and capturing nature's beauty)\n* **Article:** Street Photography Tips - [https://digital-photography-school.com/10-street-photography-tips/](https://digital-photography-school.com/10-street-photography-tips/) (Offers advice on approaching street photography and capturing candid moments)\n* **Forum:** DPReview - [https://www.dpreview.com/forums/](https://www.dpreview.com/forums/) (Active community for discussing different photography genres, gear, and techniques)\n\n# 6. Developing Your Style and Vision\n\n* **Book:**  The Art of Photography: An Approach to Personal Expression - Bruce Barnbaum (Encourages photographers to develop their unique vision and artistic style)\n* **Website:** Magnum Photos - [https://www.magnumphotos.com/](https://www.magnumphotos.com/) (Browse through work of renowned photographers for inspiration and understanding different perspectives)\n* **Exhibitions:** Local photography exhibitions and galleries (Experience various photographic styles and approaches firsthand)\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "Generative AI",
      ],
    },
    {
      "role": "model",
      "parts": [
        "### Generative AI\n\n# 1. Foundations\n\n* **Article:** Generative AI: A Creative New World - Sequoia Capital - [https://www.sequoia.com/generative-ai-a-creative-new-world/](https://www.sequoia.com/generative-ai-a-creative-new-world/) (Overview of generative AI and its potential impact)\n* **Course:** Introduction to Generative Adversarial Networks (GANs) - Coursera - [https://www.coursera.org/lecture/build-basic-generative-adversarial-networks-gans/introduction-to-gans-fN6No](https://www.coursera.org/lecture/build-basic-generative-adversarial-networks-gans/introduction-to-gans-fN6No) (Explores the foundational architecture of GANs)\n* **Book:** Deep Learning with Python - François Chollet (Covers deep learning fundamentals and includes chapters on generative models) \n\n# 2. Key Generative Models\n\n* **GANs:**\n    - **Research Paper:** Generative Adversarial Networks - Ian Goodfellow et al. - [https://arxiv.org/abs/1406.2661](https://arxiv.org/abs/1406.2661) (The seminal paper introducing GANs)\n    - **Website:**  This Person Does Not Exist - [https://thispersondoesnotexist.com/](https://thispersondoesnotexist.com/) (Showcases the power of GANs in generating realistic human faces)\n\n* **Variational Autoencoders (VAEs):**\n    - **Blog Post:** Understanding Variational Autoencoders (VAEs) - Towards Data Science - [https://towardsdatascience.com/understanding-variational-autoencoders-vaes-f705c71b714](https://towardsdatascience.com/understanding-variational-autoencoders-vaes-f705c71b714) (Explanation of VAEs and how they work)\n    - **Code Example:** Keras VAE Example - [https://keras.io/examples/generative/vae/](https://keras.io/examples/generative/vae/) (Practical implementation of a VAE using the Keras library)\n\n* **Diffusion Models:**\n    - **Research Paper:** Denoising Diffusion Probabilistic Models - Jonathan Ho et al. - [https://arxiv.org/abs/2006.11239](https://arxiv.org/abs/2006.11239) (Introduces diffusion models as a powerful generative approach)\n    - **Tool:**  DALL-E 2 - [https://openai.com/dall-e-2/](https://openai.com/dall-e-2/) (Advanced text-to-image generation system based on diffusion models)\n\n# 3.  Applications of Generative AI\n\n* **Image Generation:**\n    - **Tool:** Artbreeder - [https://www.artbreeder.com/](https://www.artbreeder.com/) (Web-based platform for creating and modifying images using generative algorithms) \n* **Text Generation:**\n    - **Tool:**  GPT-3 Playground - [https://beta.openai.com/](https://beta.openai.com/) (Experiment with text generation capabilities of GPT-3, a powerful language model)\n* **Music Generation:**\n    - **Article:** AI Music Generation: The Current State of the Art - [https://magenta.tensorflow.org/2020/04/01/ai-music-generation/](https://magenta.tensorflow.org/2020/04/01/ai-music-generation/) (Overview of AI techniques for composing music)\n\n# 4. Ethical and Societal Implications\n\n* **Article:** The Malicious Use of Artificial Intelligence: Forecasting, Prevention, and Mitigation - [https://arxiv.org/abs/1802.07228](https://arxiv.org/abs/1802.07228) (Explores potential risks and misuse of AI, including generative models)\n* **Book:**  Weapons of Math Destruction - Cathy O'Neil (Discusses the societal impact of algorithms and potential biases in data-driven systems)\n\n# 5. Keeping Up with Generative AI\n\n* **News:** MIT Technology Review AI section - [https://www.technologyreview.com/topic/artificial-intelligence/](https://www.technologyreview.com/topic/artificial-intelligence/) (Covers advances and news in the field of AI, including generative AI)\n* **Community:** Reddit r/MachineLearning - [https://www.reddit.com/r/MachineLearning/](https://www.reddit.com/r/MachineLearning/) (Discussions on new research, tools, and applications of generative models)\n* **Conferences:** NeurIPS, ICML, ICLR (Major AI research conferences where groundbreaking work on generative AI is often presented) \n",
      ],
    },
  ]
)

topic = input("Enter a topic: ")

response = chat_session.send_message(f"{topic}")

with open("test.md", 'w') as f:
    f.write(response.text)

# print(response.text)
# print(chat_session.history)