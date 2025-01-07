from fastapi import HTTPException
import openai
import json

async def process_transcript(transcript: str):
    try:
        response = await openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"Process the following diary entry and provide a summary, title with emoji, mood analysis, activities, and reflections in JSON format: {transcript}"}
            ]
        )
        data = response['choices'][0]['message']['content']
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