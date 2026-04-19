from groq import Groq
from config import GROQ_API_KEY, MODEL, MAX_TOKENS, TEMPERATURE
from prompts import (
    SYSTEM_PROMPT, TECHNICAL_SUPPORT_PROMPT, PLACEMENT_ASSISTANT_PROMPT,
    FAQ_PROMPT, CAREER_ADVISOR_PROMPT
)

client = Groq(api_key=GROQ_API_KEY)

def detect_prompt_type(user_message: str) -> str:
    user_lower = user_message.lower()
    
    technical_keywords = [
        'video', 'login', 'access', 'error', 'bug', 'crash', 'broken', 'not working',
        'can\'t', 'cannot', 'issue', 'problem', 'technical', 'server', 'payment failed',
        'download', 'certificate', 'platform', 'dashboard'
    ]
    
    placement_keywords = [
        'job', 'placement', 'interview', 'resume', 'career', 'interview prep',
        'mock interview', 'salary', 'hiring', 'recruiter', 'linkedin'
    ]
    
    career_keywords = [
        'career path', 'which course', 'should i take', 'learning path', 'track',
        'data analyst', 'ml engineer', 'python developer', 'ai specialist',
        'best course', 'suitable', 'recommend', 'prerequisites', 'experience needed'
    ]
    
    faq_keywords = [
        'refund', 'self-paced', 'instructor-led', 'time commitment', 'when',
        'batch', 'payment method', 'access after', 'live class', 'certificate value',
        'multiple courses', 'duration', 'how long', 'hours per week'
    ]
    
    for keyword in technical_keywords:
        if keyword in user_lower:
            return TECHNICAL_SUPPORT_PROMPT
    
    for keyword in placement_keywords:
        if keyword in user_lower:
            return PLACEMENT_ASSISTANT_PROMPT
    
    for keyword in career_keywords:
        if keyword in user_lower:
            return CAREER_ADVISOR_PROMPT
    
    for keyword in faq_keywords:
        if keyword in user_lower:
            return FAQ_PROMPT
    
    return SYSTEM_PROMPT

def chat(history, user_message):
    history.append({"role": "user", "content": user_message})
    selected_prompt = detect_prompt_type(user_message)
    messages = [{"role": "system", "content": selected_prompt}] + history
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        max_tokens=MAX_TOKENS,
        temperature=TEMPERATURE
    )
    reply = response.choices[0].message.content
    history.append({"role": "assistant", "content": reply})
    return reply

def stream_chat(history, user_message):
    history.append({"role": "user", "content": user_message})
    selected_prompt = detect_prompt_type(user_message)
    messages = [{"role": "system", "content": selected_prompt}] + history
    stream = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        max_tokens=MAX_TOKENS,
        temperature=TEMPERATURE,
        stream=True
    )
    for chunk in stream:
        if chunk.choices[0].delta.content:
            yield chunk.choices[0].delta.content

def new_conversation():
    return []

