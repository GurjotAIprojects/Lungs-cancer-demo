
import os
import gradio as gr

def analyze(age, smoking, symptoms):
    factors = []

    if age >= 50:
        factors.append("Age 50 or above selected")

    if smoking == "Yes":
        factors.append("Smoking history selected")

    if symptoms:
        factors.extend(symptoms)

    if factors:
        result = "## Educational Summary\n\n"
        result += "Selected factors:\n"
        result += "\n".join("- " + x for x in factors)
        result += "\n\nThese factors do not diagnose cancer. Please consult a healthcare professional for medical concerns."
    else:
        result = "No listed factors selected. This does not rule out any illness."

    return result

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("""
    # 🫁 Lung Cancer Awareness Project
    ### Educational Risk-Factor Demonstration
    Enter information to view an educational summary.
    """)

    age = gr.Slider(1, 100, value=25, label="Age")
    smoking = gr.Radio(["Yes", "No"], label="Smoking history")
    symptoms = gr.CheckboxGroup(
        ["Persistent cough", "Chest discomfort",
         "Breathlessness", "Blood in cough",
         "Persistent fatigue"],
        label="Symptoms (if applicable)"
    )

    button = gr.Button("Analyse Information", variant="primary")
    output = gr.Markdown()
    button.click(analyze, [age, smoking, symptoms], output)

    gr.Markdown("""
    ---
    **Disclaimer:** This is not an AI diagnostic system.
    It cannot detect or rule out lung cancer.
    """)

demo.launch(
    server_name="0.0.0.0",
    server_port=int(os.environ.get("PORT", 10000))
)
