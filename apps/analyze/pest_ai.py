# apps/visual/ai_suggestions.py

import openai
from apps.visual.data_fetcher import get_latest_pest_analysis

openai.api_key = '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'

def generate_pest_suggestions(user_name):
    pest_analysis = get_latest_pest_analysis(user_name)
    if pest_analysis:
        # Construct the prompt for the AI
        prompt = (
            "Given the following pest counts in a paddy field, provide suggestions for pest management:\n"
            f"Leaf Folders: {pest_analysis['leaf_folders_count']}\n"
            f"Whorl Maggots: {pest_analysis['whorl_maggots_count']}\n"
            f"Rice Bugs: {pest_analysis['rice_bugs_count']}\n"
            f"Stem Borer: {pest_analysis['stem_borer_count']}\n"
            f"Green Leafhoppers: {pest_analysis['green_leafhoppers_count']}\n"
        )

        # Call the OpenAI API
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=150,
            temperature=0.7
        )
        suggestions = response.choices[0].text.strip()
        return suggestions
    else:
        return "No recent pest analysis data available to make suggestions."
