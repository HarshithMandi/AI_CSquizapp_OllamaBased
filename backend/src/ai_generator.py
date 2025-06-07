import os
import json
from typing import Dict, Any
import requests

def generate_challenge_with_ai(difficulty: str) -> Dict[str, Any]:
    """
    Generate a coding challenge using an AI service.
    
    Args:
        difficulty (str): The difficulty level of the challenge ('easy', 'medium', 'hard').
    
    Returns:
        Dict[str, Any]: A dictionary containing the challenge details.
    """
    ollama_url = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")
    model = os.getenv("OLLAMA_MODEL", "mistral")

    prompt = f"""You are an expert coding challenge creator. Generate a {difficulty} level coding question with multiple choice answers.

For easy questions: Focus on basic syntax, simple operations, or common programming concepts.
For medium questions: Cover intermediate concepts like data structures, algorithms, or language features.  
For hard questions: Include advanced topics, design patterns, optimization techniques, or complex algorithms.

IMPORTANT: If your question references a code snippet, include the complete code snippet in the title itself. Do not reference external code.

Examples of good titles:
- "What does this Python code print: x = [1, 2, 3]; print(len(x))"
- "Which method correctly adds an element to a Python list?"
- "What is the time complexity of binary search?"

You must respond with ONLY valid JSON in this exact format:
{{
    "title": "Complete question including any code if needed",
    "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
    "correct_answer_id": 0,
    "explanation": "Detailed explanation of why the correct answer is right"
}}

Make sure the options are plausible but with only one clearly correct answer."""

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        
    }

    try:
        print(f"Calling Ollama API at {ollama_url} with model {model}")
        # Increased timeout but still reasonable
        response = requests.post(ollama_url, json=payload, timeout=120)
        response.raise_for_status()
        
        data = response.json()
        challenge_text = data.get("response", "").strip()
        
        print(f"Raw Ollama response: {challenge_text[:200]}...")
        
        # Try to extract JSON from the response
        # Sometimes Ollama includes extra text, so we need to find the JSON part
        start_idx = challenge_text.find('{')
        end_idx = challenge_text.rfind('}') + 1
        
        if start_idx == -1 or end_idx == 0:
            raise Exception("No JSON found in response")
            
        json_str = challenge_text[start_idx:end_idx]
        challenge = json.loads(json_str)
        
        # Validate required fields
        required_fields = ["title", "options", "correct_answer_id", "explanation"]
        for field in required_fields:
            if field not in challenge:
                raise Exception(f"Missing required field: {field}")
        
        # Validate data types
        if not isinstance(challenge["options"], list) or len(challenge["options"]) != 4:
            raise Exception("Options must be a list of 4 items")
            
        if not isinstance(challenge["correct_answer_id"], int) or challenge["correct_answer_id"] not in [0, 1, 2, 3]:
            raise Exception("correct_answer_id must be an integer between 0 and 3")
        
        # Additional validation: check if title references code but doesn't include it
        if ("code snippet" in challenge["title"].lower() or 
            "code below" in challenge["title"].lower()) and \
           ("print(" not in challenge["title"] and 
            "def " not in challenge["title"] and
            "=" not in challenge["title"]):
            print("Warning: Question references code but doesn't include it, using fallback")
            return get_fallback_challenge(difficulty)
        
        print(f"Successfully generated challenge: {challenge['title']}")
        return challenge
        
    except requests.exceptions.ConnectionError:
        print("Error: Cannot connect to Ollama. Make sure Ollama is running on http://localhost:11434")
        return get_fallback_challenge(difficulty)
    except requests.exceptions.Timeout:
        print("Error: Ollama request timed out")
        return get_fallback_challenge(difficulty)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON from Ollama: {e}")
        return get_fallback_challenge(difficulty)
    except Exception as e:
        print(f"Error generating challenge with AI: {e}")
        return get_fallback_challenge(difficulty)

def get_fallback_challenge(difficulty: str) -> Dict[str, Any]:
    """Return a fallback challenge based on difficulty level"""
    
    fallback_challenges = {
        "easy": {
            "title": "What does this Python code print: x = [1, 2, 3]; print(len(x))",
            "options": [
                "3",
                "[1, 2, 3]", 
                "1",
                "Error"
            ],
            "correct_answer_id": 0,
            "explanation": "The len() function returns the number of items in a list. Since x contains 3 elements [1, 2, 3], len(x) returns 3."
        },
        "medium": {
            "title": "What is the time complexity of accessing an element in a Python dictionary?",
            "options": [
                "O(1) average case",
                "O(n)",
                "O(log n)", 
                "O(n²)"
            ],
            "correct_answer_id": 0,
            "explanation": "Python dictionaries use hash tables internally, providing O(1) average case time complexity for access operations. In the worst case (with many hash collisions), it could degrade to O(n), but this is rare with Python's hash implementation."
        },
        "hard": {
            "title": "What does this code output: def f(x=[]):x.append(1);return x; print(f(),f())",
            "options": [
                "[1] [1, 1]",
                "[1] [1]",
                "Error",
                "[] []"
            ],
            "correct_answer_id": 0,
            "explanation": "This demonstrates the mutable default argument gotcha in Python. The default list [] is created once when the function is defined, not each time it's called. So the first call appends 1 to [], returning [1]. The second call appends 1 to the same list that already contains [1], returning [1, 1]."
        }
    }
    
    return fallback_challenges.get(difficulty, fallback_challenges["easy"])