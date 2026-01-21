# التعديل المطلوب لربط OpenRouter
# بدلاً من مكتبة google-generativeai، سنستخدم طلباً مباشراً للمحرك
import requests

def analyze_with_openrouter(text, api_key):
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={"Authorization": f"Bearer {api_key}"},
        json={
            "model": "google/gemini-flash-1.5", # المحرك الذي تفضلينه
            "messages": [{"role": "user", "content": f"حلل هذا البحث: {text}"}]
        }
    )
    return response.json()['choices'][0]['message']['content']
