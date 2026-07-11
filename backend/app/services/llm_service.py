from groq import Groq
import os
import json
from dotenv import load_dotenv
from app.schemas.candidate_schema import CandidateSchema

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError(
        "GROQ_API_KEY not found in environment variables"
    )

client = Groq(
    api_key=api_key
)

MODEL_NAME = "llama-3.3-70b-versatile"


def generate_candidate_profile(
    resume_text: str
):

    prompt = f"""
You are an expert ATS and recruiter assistant.

Analyze the following resume.

Return ONLY valid JSON.

Do not include markdown.
Do not include explanations.
Do not include code fences.
Do not infer information not explicitly mentioned.
If a field is missing, return null.

Use EXACTLY this schema:

{{
    "candidate_name": "",
    "experience_years": null,

    "skills": {{
        "languages": [],
        "frameworks": [],
        "databases": [],
        "cloud": [],
        "devops": [],
        "ai_ml": [],
        "tools": [],
        "other": []
    }},

    "projects": [
        {{
            "name": "",
            "technologies": [],
            "description": "",
            "domain": ""
        }}
    ],

    "strengths": [],
    "weaknesses": [],
    "roles_suitable_for": [],
    "industry_domains": [],
    "certifications": null,
    "seniority_level": null
}}

Resume:

{resume_text}
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    response_text = response.choices[0].message.content

    response_text = response_text.replace(
        "```json",
        ""
    )

    response_text = response_text.replace(
        "```",
        ""
    )

    candidate_data = json.loads(
    response_text
)

    validated_candidate = CandidateSchema(
        **candidate_data #** dictionary unpacking
)

    return validated_candidate


if __name__ == "__main__":

    test_text = """
    John Doe

    Skills:
    Python
    FastAPI
    React

    Projects:
    AI Resume Matcher
    """

    response = generate_candidate_profile(
        test_text
    )

    print(
        response.model_dump_json(
            #response,
            indent=4
        )
    )