CHAIN_OF_THOUGHT_PROMPT = """
Let's explore different possibilities:

1. Consider the topic {input} for the quiz.
2. Generate between two to five questions related to this topic.
3. One of the questions must always be a math question.
4. For each question, provide at least four answer options.
5. Ensure the questions are diverse and do not repeat any.
6. The math question should be relevant to the topic if possible, otherwise, provide a general math question.

Be creative, but structured, in how the questions are formed.


{format_instructions}
"""