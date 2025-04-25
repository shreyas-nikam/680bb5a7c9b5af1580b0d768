
import streamlit as st

st.set_page_config(page_title="Agentic AI Memory Poisoning Simulator", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("Agentic AI Memory Poisoning Simulator")
st.divider()

st.markdown("""
In this lab, we simulate a memory poisoning attack on an agentic AI system.
The application allows you to inject a 'poisoned' memory string and observe how the agent's behavior changes in response to subsequent inputs.
It simulates the "Case study: Memory poisoning attack on an agentic AI email assistant" section, particularly the memory manipulation.
The goal is to provide an interactive way to understand how such attacks work and how system prompts can be designed to mitigate them.

**Key Concepts:**

*   **Agentic AI System:** An AI system that can autonomously make decisions and take actions to achieve a goal.
*   **Memory Poisoning Attack:** A type of attack where malicious data is injected into an AI system's memory, causing it to behave in unintended or harmful ways.
*   **System Prompt:** The initial instructions or context provided to a large language model (LLM) that shapes its behavior and responses.

**How to Use the Application:**

1.  Enter a 'Poisoned Memory String' that you want to inject into the agent's memory.
2.  Provide a 'System Prompt' that defines the agent's role and behavior.
3.  Input an 'Email' that the agent will process.
4.  Enter the 'Expected Outcome' after the attack
5.  Click the 'Simulate Attack' button to see the simulated outcome.

**Note:** This is a simplified simulation and does not involve an actual LLM.
""")

# Your code starts here
page = st.sidebar.selectbox(label="Navigation", options=["Attack Simulation", "Mitigation Strategies"])

if page == "Attack Simulation":
    from application_pages.attack_simulation import run_attack_simulation
    run_attack_simulation()
elif page == "Mitigation Strategies":
    from application_pages.mitigation_strategies import run_mitigation_strategies
    run_mitigation_strategies()
# Your code ends

st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity.")
