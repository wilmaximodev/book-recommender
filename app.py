import google.generativeai as genai
import os
from flask import Flask, render_template
from Utils.user_data import get_user_history

from Functions.book_recommendations import (
    recommend_fiction,
    recommend_doc,
    recommend_science,
    recommend_horror,
    recommend_romantic
)

app = Flask(__name__)

GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]
genai.configure(api_key=GEMINI_API_KEY)

magical_if = genai.GenerativeModel(
    "gemini-1.5-flash",
    tools=[
        recommend_fiction,
        recommend_doc,
        recommend_science,
        recommend_horror,
        recommend_romantic
    ]
)

def ia_decision(user_id, history):
    business_rules = """
Analise o histórico de compras do usuário e decida qual categoria de livros recomendar.
    Regras:
    1. Se o usuário comprou mais livros de ficção, recomende um livro de ficção.
    2. Se o usuário comprou mais livros de não ficção, recomende um livro de não ficção.
    3. Se o usuário demonstrou interesse em ciência, recomende um livro de ciência.
    4. Se o usuáio comprou mais, recomende um livro de de ficção.
    5. Chame sempre o usuário pelo nome, não por número.
    6. Se o usuário comprou mais livros de terror, recomende terror.
    7. Se o usuário comprou mais livros de romance, recomende romance.
"""
    # Inicia o chat com a IA
    user_decision = magical_if.start_chat(enable_automatic_function_calling=True)
    # Envia os dados e as regras de negócio para a IA
    response = user_decision.send_message(
        f"Histórico do usuário {user_id}: {history}; Regras de negócio: {business_rules}"
    )
    # Retorna a resposta da IA
    return response.text

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/recommend/<int:user_id>')
def recommend(user_id):
    history = get_user_history(user_id)
    if not history:
        return "Usuário não encontrado", 404
    ia_response = ia_decision(user_id, history)
    return render_template('recommendation.html', user_id=user_id, message=ia_response)

if __name__ == '__main__':
    app.run(debug=True)
