TREE_OF_THOUGHT_PROMPT = """
Let's break this down step by step to generate a quiz on the topic {input}:

1. First, I will consider the topic {input} and think about the key concepts or areas related to it.
2. I will then decide how many questions should be included in the quiz, which should be between 1 and 5 questions.
3. I will make sure that one of the questions is a math-related question, ensuring that it is relevant to the topic if possible.
4. Next, I will create each question. For every question, I will:
   - Ensure that the question is clear and properly phrased.
   - Generate at least four answer options for each question, making sure that one of them is correct and the rest are plausible distractors.
5. I will ensure that the questions cover a variety of aspects of the topic and that they do not repeat any content.
6. Once the questions are ready, I will review them to ensure they are relevant to the topic and follow the guidelines above.

Now, I will begin generating the quiz for the topic {input}.

{format_instructions}
"""