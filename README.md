
# Lab for Taxonomy of Failure Mode in Agentic AI Systems

This Streamlit application simulates a memory poisoning attack on an agentic AI system, as described in the document. The application allows users to inject a 'poisoned' memory string and observe how the agent's behavior changes in response to subsequent inputs. It simulates the "Case study: Memory poisoning attack on an agentic AI email assistant" section, particularly the memory manipulation. The goal is to provide an interactive way to understand how such attacks work and how system prompts can be designed to mitigate them.

## Usage

1.  Clone the repository.
2.  Create a virtual environment (optional): `python -m venv venv`
3.  Activate the virtual environment: `source venv/bin/activate` (Linux/macOS) or `venv\Scripts\activate` (Windows)
4.  Install the requirements: `pip install -r requirements.txt`
5.  Run the Streamlit application: `streamlit run app.py`

## Docker

Alternatively, you can run the application using Docker:

1.  Build the Docker image: `docker build -t agentic-ai-memory-poisoning .`
2.  Run the Docker container: `docker run -p 8501:8501 agentic-ai-memory-poisoning`

## Pages

*   **Attack Simulation:** This page allows you to inject a poisoned memory string, system prompt, and input email to simulate an attack.
*   **Mitigation Strategies:** This page explores potential mitigation strategies to defend against memory poisoning attacks.

## Contributing

[Add your contributions here]

## License

[Add your license information here]
