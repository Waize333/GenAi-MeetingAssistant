import torch
import os
import gradio as gr
from transformers import pipeline
from langchain_core.prompts import PromptTemplate
from langchain_ibm import WatsonxLLM
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams

#######------------- LLM-------------####
from dotenv import load_dotenv
load_dotenv()

# IBM watsonx.ai credentials and model setup
my_credentials = {
    "url": "https://eu-de.ml.cloud.ibm.com",
    "apikey": os.getenv("IBM_CLOUD_API_KEY")
}

# Check if environment variables are set
if not my_credentials["apikey"]:
    print("ERROR: IBM_CLOUD_API_KEY environment variable not set!")
    exit(1)

project_id = os.getenv("WATSONX_PROJECT_ID")
if not project_id:
    print("ERROR: WATSONX_PROJECT_ID environment variable not set!")
    exit(1)

# Fixed parameters
params = {
    GenParams.MAX_NEW_TOKENS: 700,
    GenParams.TEMPERATURE: 0.1,
    GenParams.DECODING_METHOD: "greedy"
}

# WatsonxLLM initialization
try:
    llm = WatsonxLLM(
        model_id='ibm/granite-13b-instruct-v2',
        url=my_credentials["url"],
        apikey=my_credentials["apikey"],
        project_id=project_id,
        params=params
    )
    print("✅ IBM watsonx connection successful!")
except Exception as e:
    print(f"❌ Error connecting to IBM watsonx: {e}")
    exit(1)

#######------------- Prompt Template-------------####
temp = """
Analyze the following audio transcript and provide:
1. A concise summary
2. Key discussion points
3. Important insights or action items

Text: {context}

Analysis:
"""

pt = PromptTemplate(input_variables=["context"], template=temp)
prompt_to_LLM = pt | llm  # Updated: Modern LangChain syntax

#######------------- Speech Processing-------------####
def transcript_audio(audio_file, analysis_type):
    try:
        if audio_file is None:
            return "❌ Please upload an audio file first."
        
        # Initialize speech recognition
        pipe = pipeline(
            "automatic-speech-recognition",
            model="openai/whisper-tiny.en",
            chunk_length_s=30,
            ignore_warning=True
        )
        
        # Transcribe audio
        transcript_txt = pipe(audio_file, batch_size=8)["text"]
        
        if not transcript_txt.strip():
            return "❌ No speech detected in the audio file."
        
        # Customize prompt based on analysis type
        if analysis_type == "Summary":
            custom_prompt = f"Provide a concise summary of this text: {transcript_txt}"
            result = llm.invoke(custom_prompt)
        elif analysis_type == "Key Points":
            custom_prompt = f"Extract the main key points from this text: {transcript_txt}"
            result = llm.invoke(custom_prompt)
        else:  # Detailed Analysis
            result = prompt_to_LLM.invoke({"context": transcript_txt})
        
        # Format output
        formatted_result = f"""
## 📝 Transcript
{transcript_txt}

---

## 🎯 Analysis ({analysis_type})
{result if isinstance(result, str) else result}

---
*Powered by OpenAI Whisper + IBM Granite*
        """
        
        return formatted_result
        
    except Exception as e:
        return f"❌ Error processing audio: {str(e)}"

#######------------- Enhanced Gradio Interface-------------####

# Custom CSS for better styling
custom_css = """
.gradio-container {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
.title {
    text-align: center;
    color: #2E86AB;
    font-size: 2.5em;
    margin-bottom: 0.5em;
}
.subtitle {
    text-align: center;
    color: #666;
    font-size: 1.2em;
    margin-bottom: 1em;
}
"""

# Create the interface
with gr.Blocks(css=custom_css, theme=gr.themes.Soft()) as iface:
    
    # Header
    gr.HTML("""
    <div class="title">🎤 AI-Powered Meeting Assistant</div>
    <div class="subtitle">Transform your audio into actionable insights with IBM Granite AI</div>
    """)
    
    with gr.Row():
        with gr.Column(scale=1):
            # Input section
            gr.Markdown("### 📤 Upload Audio")
            audio_input = gr.Audio(
                sources=["upload", "microphone"],
                type="filepath",
                label="Select Audio File or Record",
                show_label=False
            )
            
            analysis_type = gr.Radio(
                choices=["Summary", "Key Points", "Detailed Analysis"],
                value="Detailed Analysis",
                label="Analysis Type",
                info="Choose what type of analysis you want"
            )
            
            process_btn = gr.Button(
                "🚀 Process Audio", 
                variant="primary",
                size="lg"
            )
            
            # Examples section
            gr.Markdown("### 📋 Supported Formats")
            gr.Markdown("""
            - **Audio formats**: MP3, WAV, M4A, FLAC
            - **Languages**: English (optimized)
            - **Duration**: Up to 30 minutes recommended
            - **Quality**: Clear speech works best
            """)
        
        with gr.Column(scale=2):
            # Output section
            gr.Markdown("### 📊 Results")
            output_text = gr.Textbox(
                lines=20,
                max_lines=30,
                label="Analysis Results",
                show_label=False,
                placeholder="Your analysis will appear here...",
                container=True
            )
    
    # Footer
    gr.HTML("""
    <div style="text-align: center; margin-top: 2em; padding: 1em; background-color: #f8f9fa; border-radius: 10px;">
        <p style="color: #666;">
            🔒 <strong>Privacy</strong>: Audio is processed securely and not stored permanently<br>
            ⚡ <strong>Technology</strong>: OpenAI Whisper + IBM watsonx Granite AI<br>
            🌟 <strong>Use Cases</strong>: Meetings, Interviews, Lectures, Podcasts
        </p>
    </div>
    """)
    
    # Event handlers
    process_btn.click(
        fn=transcript_audio,
        inputs=[audio_input, analysis_type],
        outputs=output_text,
        show_progress=True
    )

if __name__ == "__main__":
    iface.launch(
        server_name="0.0.0.0", 
        server_port=7860,
        share=False,
        show_error=True
    )