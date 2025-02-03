def get_user_history(user_id: int) -> dict:
    """
    Retorna o histórico de compras do usuário.
    """
    # Dados simulados de histórico de compras
    user_histories = {
        1: {'name': 'João', 'fiction': 2, 'documentario': 2, 'science': 0, 'horror': 8, 'romantic': 0},
        2: {'name': 'Marta', 'fiction': 1, 'documentario': 4, 'science': 1, 'horror': 5, 'romantic': 7},
        3: {'name': 'José', 'fiction': 0, 'documentario': 5, 'science': 5, 'horror': 1, 'romantic': 2},
        4: {'name': 'Maria', 'fiction': 3, 'documentario': 3, 'science': 5, 'horror': 1, 'romantic': 2},
    }
    return user_histories.get(user_id)