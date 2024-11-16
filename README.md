# WatsonX AI Project Assistant

## Overview

The WatsonX AI Project Assistant is a Streamlit-based application that leverages IBM's WatsonX AI capabilities to provide intelligent project management assistance. This tool is designed to help project managers and teams streamline their workflow, generate documentation, analyze project impacts, and make data-driven decisions.

## Features

1. **Natural Language Query**: Ask project-related questions in natural language and receive detailed responses.
2. **Document Generation**: Automatically generate project documents such as PRD, BRD, Scope, and Plans based on project details.
3. **Impact Analysis**: Analyze the impact of proposed changes on project timeline, budget, and resources.
4. **Work Breakdown Structure (WBS) Generator**: Create a detailed WBS based on project information.
5. **Stakeholder Meeting Simulation**: Simulate stakeholder meetings and generate summaries with action items.
6. **Project Scope Validation**: Validate project scope and identify potential risks or inconsistencies.

## Setup

### Prerequisites

- Python 3.7+
- IBM Cloud account with WatsonX access

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/watsonx-ai-project-assistant.git
   cd watsonx-ai-project-assistant
   ```

2. Install required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your WatsonX credentials:
   - Create a file named `.streamlit/secrets.toml` in the project root
   - Add your WatsonX credentials:
     ```toml
     WATSONX_API_KEY = "your_api_key_here"
     WATSONX_URL = "your_watsonx_url_here"
     WATSONX_PROJECT_ID = "your_project_id_here"
     ```

## Usage

To run the Streamlit app:

```
streamlit run main.py
```

Navigate through the different tabs to access various features of the AI Project Assistant.

## File Structure

- `main.py`: The entry point of the Streamlit application
- `assistant.py`: Contains the WatsonXAssistant class that encapsulates AI functionalities
- `llm_setup.py`: Sets up the LangChain LLM connection to WatsonX
- `prompts.py`: Stores prompt templates for different AI tasks
- `ui_components.py`: Contains functions for rendering Streamlit UI components
- `config.yaml`: Configuration file for the application

## Contributing

Contributions to improve the WatsonX AI Project Assistant are welcome. Please follow these steps to contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgements

- [IBM WatsonX](https://www.ibm.com/products/watsonx-ai)
- [Streamlit](https://streamlit.io/)
- [LangChain](https://github.com/hwchase17/langchain)

## Contact

Your Name - [@your_twitter](https://twitter.com/your_twitter) - email@example.com

Project Link: [https://github.com/your-username/watsonx-ai-project-assistant](https://github.com/your-username/watsonx-ai-project-assistant)
