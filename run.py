import vertexai
from vertexai.generative_models import GenerativeModel, Part
 
 
def generate_text(project_id: str, location: str) -> str:
    # Initialize Vertex AI
    vertexai.init(project=project_id, location=location)
    # Load the model
    multimodal_model = GenerativeModel("gemini-1.0-pro-vision")
    # Query the model
    response = multimodal_model.generate_content(
        [
            # Add an example image
            Part.from_uri(
                "gs://generativeai-downloads/images/scones.jpg", mime_type="image/jpeg"
            ),
            # Add an example query
            "what is shown in this image?",
        ]
    )
    print(response)
    return response.text
 
# 開発用生成AI専用PJ
project_id="tabelog-genai-gemini-dev"
location="asia-northeast1"
generate_text(project_id, location)
