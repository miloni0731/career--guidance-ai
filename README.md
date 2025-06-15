# AI-Powered Career Guidance Assistant

> An intelligent career counseling system built with Streamlit and Hugging Face LLMs for personalized career recommendations.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.32.0-red.svg)](https://streamlit.io)
[![Hugging Face](https://img.shields.io/badge/🤗-Hugging%20Face-yellow.svg)](https://huggingface.co)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

## Overview

The AI Career Guidance Assistant is an intelligent system that leverages advanced language models to understand user interests, skills, and preferences through natural language input. It provides personalized career path recommendations with detailed explanations and follow-up questions to guide users in their career exploration journey.

Built for real-world applications in education, counseling, and talent development environments.

## Key Features

- **Natural Language Understanding**: Process user input in conversational format
- **Intelligent Preference Extraction**: Automatically identify interests, skills, and traits
- **Smart Career Mapping**: Match user profiles to relevant career domains using semantic similarity
- **Personalized Explanations**: Generate detailed reasoning for recommendations
- **Interactive Follow-ups**: Provide thoughtful questions for deeper exploration
- **Confidence Scoring**: Quantify recommendation reliability with numerical confidence values
- **Conversation History**: Track and review previous recommendations for continuity

## System Architecture

### Core Components

**Preference Extractor** (`preference_extractor.py`)
- Analyzes natural language input using LLM-based processing
- Extracts structured data: interests, skills, and personality traits
- Handles ambiguous or unclear inputs with fallback mechanisms

**Domain Classifier** (`domain_classifier.py`)
- Maps extracted preferences to predefined career domains
- Implements confidence scoring algorithms for recommendation reliability
- Supports multi-class career path classification

**Explanation Generator** (`explanation_generator.py`)
- Creates personalized career recommendations with detailed justifications
- Connects user preferences to specific career requirements and opportunities
- Generates human-readable explanations for AI decision-making

**Fallback Handler** (`fallback_handler.py`)
- Generates clarifying questions for unclear or insufficient inputs
- Provides domain-specific follow-up questions for career exploration
- Implements error handling and edge case management

## Project Structure

```
CAREERGUIDER/
├── streamlit_app.py              # Main Streamlit application interface
├── main.py                       # CLI interface (optional)
├── README.md                     # Project documentation
├── requirements.txt              # Python dependencies
│
├── .streamlit/
│   └── secrets.toml             # API credentials (not tracked in git)
│
├── configs/
│   ├── career_paths.json        # Career domain definitions and mappings
│   └── prompt_templates.json    # LLM prompt templates and configurations
│
├── data/
│   └── test_inputs.json         # Test cases and validation examples
│
├── models/
│   └── generation_model.py      # LLM API integration and model management
│
├── pipeline/
│   ├── preference_extractor.py  # User preference extraction pipeline
│   ├── domain_classifier.py     # Career domain classification logic
│   ├── explanation_generator.py # Recommendation explanation generation
│   ├── fallback_handler.py      # Error handling and fallback mechanisms
│   └── __init__.py              # Pipeline module initialization
│
└── utils/
    ├── io_helpers.py            # File I/O and data loading utilities
    ├── similarity_utils.py      # Semantic similarity calculations
    └── __init__.py              # Utilities module initialization
```

## Installation and Setup

### Prerequisites

- Python 3.8 or higher
- Hugging Face API token with appropriate model access
- Git version control system

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/miloni0731/career-guidance-ai.git
   cd career-guidance-ai
   ```

2. **Create and activate virtual environment**
   ```bash
   # Linux/macOS
   python3 -m venv venv
   source venv/bin/activate

   # Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API credentials**
   
   Create `.streamlit/secrets.toml` in the project root:
   ```toml
   [api]
   hf_token = "hf_your_hugging_face_token_here"
   provider = "Featherless"
   model_name = "sarvamai/sarvam-m"
   ```

### Running the Application

**Streamlit Web Interface**
```bash
streamlit run streamlit_app.py
```
Application will be available at `http://localhost:8501`

**Command Line Interface** (Optional)
```bash
python main.py
```

## Usage Example

### Input
```
"I love designing and solving puzzles, but I don't like reading too much theory."
```

### System Output
```
Extracted Profile:
├── Interests: designing, solving puzzles
├── Skills: problem-solving, creativity
└── Traits: analytical, creative

Recommended Career Path: STEM
Confidence Score: 0.85

Explanation: 
Your combination of design interests and puzzle-solving abilities aligns strongly 
with STEM career paths, particularly in software engineering and data science 
where creative problem-solving is highly valued. These fields emphasize 
hands-on application over theoretical study.

Follow-up Questions:
• Have you considered exploring software development or data science roles?
• Would you be interested in working on complex technical problems?
• Are you open to learning programming languages and development tools?
```

## Technical Stack

| Component | Technology | Version | Purpose |
|-----------|------------|---------|---------|
| **Web Framework** | Streamlit | 1.32.0 | User interface and web application |
| **ML Models** | Hugging Face Hub | 0.21.4 | Large language model integration |
| **Data Processing** | Pandas | 2.2.1 | Data manipulation and analysis |
| **ML Utilities** | Scikit-learn | 1.3.2 | Machine learning utilities |
| **HTTP Client** | Requests | 2.31.0 | API communication |
| **Configuration** | Python-dotenv | 1.0.1 | Environment variable management |
| **Numerical Computing** | NumPy | 1.26.4 | Mathematical operations |

## Configuration

### Supported LLM Providers

The system supports multiple language model providers through configurable endpoints:

- **Featherless AI**: High-performance inference with `sarvamai/sarvam-m`
- **Novita AI**: Alternative provider with `teknium/OpenHermes-2.5-Mistral-7B`
- **Hugging Face**: Direct API access to any compatible text generation model

### Career Domain Classifications

The system categorizes careers into six primary domains:

- **STEM**: Science, Technology, Engineering, Mathematics
- **Creative Arts**: Design, Arts, Media, Entertainment
- **Business**: Management, Finance, Marketing, Sales
- **Healthcare**: Medical, Nursing, Therapy, Wellness
- **Education**: Teaching, Training, Academic Research
- **Social Services**: Counseling, Social Work, Non-profit

## API Integration

### Model Configuration

```python
# Example configuration in secrets.toml
[api]
hf_token = "your_token_here"
provider = "Featherless"
model_name = "sarvamai/sarvam-m"
base_url = "https://api.featherless.ai/v1"
```

### Request/Response Format

The system processes requests through a structured pipeline:

1. **Input Validation**: Sanitize and validate user input
2. **Preference Extraction**: Parse natural language into structured preferences
3. **Domain Classification**: Map preferences to career domains with confidence scores
4. **Response Generation**: Create explanations and follow-up questions

## Performance Considerations

- **Caching**: Streamlit resource caching for component initialization
- **Error Handling**: Comprehensive error handling for API failures
- **Rate Limiting**: Built-in request throttling for API compliance
- **Memory Management**: Efficient handling of conversation history

## Development and Contributing

### Development Setup

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-feature`
3. Make changes and add tests
4. Commit changes: `git commit -m 'Add new feature'`
5. Push to branch: `git push origin feature/new-feature`
6. Submit a Pull Request

### Code Standards

- Follow PEP 8 Python style guidelines
- Include comprehensive docstrings for all functions
- Add unit tests for new functionality
- Update documentation for significant changes
- Use type hints where applicable

### Testing

```bash
# Run tests (when test suite is implemented)
python -m pytest tests/

# Run linting
flake8 .

# Run type checking
mypy .
```

## Deployment

### Local Deployment
```bash
streamlit run streamlit_app.py --server.port 8501
```

### Production Deployment
- Configure environment variables for production API keys
- Use appropriate process managers (gunicorn, uvicorn, etc.)
- Implement proper logging and monitoring
- Set up SSL certificates for HTTPS

## Author

**Miloni Panchal**
- Project: Brainwonders AI Engineering Internship
- Date: June 2025
- Focus: AI-powered career guidance and counseling systems

## Acknowledgments

- Hugging Face for providing language model infrastructure
- Streamlit for the web application framework
- The open-source community for foundational tools and libraries

## Support and Documentation

For technical support, bug reports, or feature requests:

1. Check existing [Issues](https://github.com/miloni0731/career-guidance-ai/issues)
2. Create a new issue with detailed description and error logs
3. Provide system information and reproduction steps

---
