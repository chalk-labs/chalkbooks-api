import os
from openai import OpenAI
import json
from fastapi import HTTPException

client = OpenAI(
    api_key=os.environ['OPENAI_API_KEY']
)


def process_transcript(transcript: str):
    prompt = f"""
    You are an AI assistant. Process the following diary entry and provide a summary, title, one mood analysis , one emoji, activities, and reflections in JSON format as follow: "summary",
        "title",
        "mood_analysis",
        "emoji",
        "activities",
        "reflections"

     for the given diary entry:
    {transcript}
    """

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt},
            ]
        )
        # data = response['choices'][0]['message']['content']
        data = response.choices[0].message.content
        print(data)
        return parse_response(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def parse_response(data: str):
    try:
        response_data = json.loads(data)  # Parse the JSON response
        summary = response_data.get("summary", "No summary provided")
        title_with_emoji = response_data.get("title", "No title provided")
        mood_analysis = response_data.get("mood_analysis", "No mood analysis provided")
        emoji = response_data.get("emoji", "No summary provided")
        activities = response_data.get("activities", [])
        reflections = response_data.get("reflections", [])

        return {
            "summary": summary,
            "title_with_emoji": title_with_emoji,
            "mood_analysis": mood_analysis,
            "activities": activities,
            "reflections": reflections,
            "emoji": emoji  
        }
    except json.JSONDecodeError as e:
        raise HTTPException(status_code=500, detail=f"Error parsing JSON response: {str(e)}")

def llm_json_maker(transcript: str):
    result = process_transcript(transcript)
    return result

# Example usage
# if '_name_' == "_main_":
def runner():
    print("1")
    transcript = "Today was a great day. I went to the park and played with my friends. I also had a picnic with my family. I felt happy and relaxed. I am grateful for the time spent with my loved ones."
    result = llm_json_maker(transcript)
    print("2")

    print(json.dumps(result, indent=2))

# runner()