""""
Name:  Xavier Colon

Description: Trivia Quiz game using Tkinter and requests.

Resources:
- Images:
    - Correct Image: https://www.pngwing.com/en/free-png-zaomi
    - Wrong Image: https://emojipedia.org/cross-mark/
"""


from data import q_data
from question import Question
from trivia_engine import TriviaEngine
from ui import TriviaUI

# Create the questions list
question_list = [Question(q["question"], q["correct_answer"]) for q in q_data]
# Instantiate the TriviaEngine
game = TriviaEngine(question_list)
# Run the game UI
game_ui = TriviaUI(game)