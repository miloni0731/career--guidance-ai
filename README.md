# AI-Powered Career Guidance Assistant

> Built for real-world use in education, counseling, and talent development applications.

## Overview

An intelligent career guidance system that uses advanced language models to understand user interests and provide personalized career recommendations. The system features a user-friendly Streamlit interface and can handle natural language input to extract preferences, map them to career paths, and generate personalized explanations.

### Key Features

1.  **Intelligent Preference Extraction**
  - Natural language understanding
  - Implicit preference detection
  - Skill and interest identification

2.  **Smart Career Mapping**
  - Semantic similarity matching
  - Confidence scoring
  - Multiple career path suggestions

3.  **Personalized Explanations**
  - Clear, concise reasoning
  - Follow-up questions
  - Career path exploration

## System Architecture

### Core Components

1. **Preference Extractor**
   - Natural language processing
   - Interest and skill identification
   - Preference classification

2. **Career Path Mapper**
   - Semantic embedding matching
   - Domain classification
   - Confidence scoring

3. **Explanation Generator**
   - Personalized reasoning
   - Career path justification
   - Follow-up suggestions

4. **Fallback Handler**
   - Ambiguity detection
   - Clarifying questions
   - Input refinement

## Project Structure

```
career_guidance_ai/
├── streamlit_app.py # Streamlit UI + backend logic
├── README.md # Project overview, setup, usage
│
├── configs/
│   ├── prompt_templates.json     # Prompt formats
│   └── career_paths.json         # Career domains
├── data/
│   └── test_inputs.json          # Test cases
├── models/
│   ├── embedding_model.py        # Sentence-transformer
│   └── generation_model.py       # HF pipeline
├── pipeline/
│ ├── preference_extractor.py # Rule-based or HF model-based extractor
│ ├── path_mapper.py # Embedding matcher
│ ├── explanation_generator.py # Generates reasoning using HF LLMs
│ └── fallback_handler.py # Fallback question logic
│
├── utils/
│ ├── similarity_utils.py # Cosine similarity
│ └── io_helpers.py # Load/save utils
│
├── requirements.txt # Streamlit + Transformers dependencies
└── .streamlit/
   └── secrets.toml # Hugging Face API credentials

```

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Hugging Face API token
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/miloni0731/career-guidance-ai.git
   cd career-guidance-ai
   ```

2. **Set up virtual environment**
   ```bash
   # Linux/macOS
   python3 -m venv venv
   source venv/bin/activate

   # Windows
   python -m venv .venv
   .\.venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Hugging Face API**
   Create `.streamlit/secrets.toml`:
   ```toml
    [api]
    hf_token = "hf_xxxxxxxxxxxxxxxxxxx"
    provider = "Featherless AI"
    model_name = "mistralai/Mistral-7B-Instruct-v0.2"
   ```

### Running the Application

```bash
streamlit run streamlit_app.py
```

## Usage Example

```python
# Example input
"I love designing and solving puzzles, but I don't like reading too much theory."

# System response
Extracted Profile:
Interests: designing, solving puzzles
Skills: problem-solving, creativity
Traits: analytical, creative

Recommended Career Path: STEM
Confidence: 0.85

 Explanation: Your interest in design and puzzle-solving aligns well with STEM fields, particularly in areas like software engineering and data science where creative problem-solving is essential.

 Follow-up Questions:
- Have you considered exploring software development or data science?
- Would you enjoy working on complex technical problems?
- Are you interested in learning programming languages?
```

## Technical Stack

- **Frameworks & Libraries**
  - Streamlit
  - Hugging Face Transformers
  - Sentence Transformers
  - NumPy

##  Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Author

**Miloni Panchal**
- For: Brainwonders AI Engineering Internship
- June 2025

## Acknowledgments

- Hugging Face for providing the language models
- Streamlit for the web interface framework
- The open-source community for various tools and libraries
