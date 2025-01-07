import os
from openai import OpenAI
import json
from fastapi import HTTPException

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)


def process_transcript(transcript: str):
    prompt = f"""
    You are an AI assistant. Process the following diary entry and provide a summary, title with emoji, mood analysis, activities, and reflections in JSON format:
    {transcript}
    """

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": query},
            ]
        )
        data = response['choices'][0]['message']['content']
        # data = response.choices[0].message.content
        return parse_response(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def parse_response(data: str):
    try:
        response_data = json.loads(data)  # Parse the JSON response
        summary = response_data.get("diary", "No summary provided")
        title_with_emoji = response_data.get("title", "No title provided")
        mood_analysis = response_data.get("mood", "No mood analysis provided")
        activities = response_data.get("activities", [])
        reflections = response_data.get("reflections", [])

        return {
            "summary": summary,
            "title_with_emoji": title_with_emoji,
            "mood_analysis": mood_analysis,
            "activities": activities,
            "reflections": reflections
        }
    except json.JSONDecodeError as e:
        raise HTTPException(status_code=500, detail=f"Error parsing JSON response: {str(e)}")

def main(transcript: str):
    result = process_transcript(transcript)
    return result

# Example usage
if __name__ == "__main__":
    transcript = "Your transcript for diary here"
    result = main(transcript)
    print(json.dumps(result, indent=2))