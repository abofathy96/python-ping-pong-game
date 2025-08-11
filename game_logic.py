# game_logic.py
"""
منطق ذكاء اصطناعي بسيط للمضرب المقابل.
- يتحرك المضرب باتجاه مركز الكرة (ball_y) لكن بسرعة مقيدة (AI_SPEED_LIMIT).
- الهدف: جعل المضرب يحاكي حركة الكرة دون أن يكون غاية في السهولة أو الصعوبة.
"""

def ai_move(ai_paddle_y, ball_y, height, paddle_height, ai_speed_limit=20):
    """
    يحسب موضع المضرب المقابل بناءً على موقع الكرة.

    Parameters:
    - ai_paddle_y: موضع المسبك المقابل (Top y) للمضرب
    - ball_y: موضع الكرة على المحور y
    - height: ارتفاع نافذة اللعب
    - paddle_height: ارتفاع المضرب
    - ai_speed_limit: الحد الأعلى لسرعة حركة المضرب في كل إطار

    Returns:
    - فاصل (int): التغير في y للمضرب المقابل هذا الإطار
    """
    center_of_paddle = ai_paddle_y + paddle_height / 2
    error = ball_y - center_of_paddle

    # تقنين السرعة: حركة مضبوطة وليست سريعة
    if error > 0:
        dy = min(ai_speed_limit, error)
    else:
        dy = max(-ai_speed_limit, error)

    # التأكد من حدود النافذة
    new_y = ai_paddle_y + dy
    if new_y < 0:
        dy = -ai_paddle_y  # اضمن أن يعود للمكان 0
    elif new_y > height - paddle_height:
        dy = height - paddle_height - ai_paddle_y

    return int(dy)