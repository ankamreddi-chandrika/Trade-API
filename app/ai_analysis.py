import google.generativeai as genai

genai.configure(api_key="YOUR_GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-pro")

def analyze_sector(sector, news):

    prompt = f"""
    Analyze trade opportunities in India's {sector} sector.

    Market News:
    {news}

    Provide insights including:
    - Market trend
    - Investment opportunities
    - Risks
    """

    response = model.generate_content(prompt)

    return response.text