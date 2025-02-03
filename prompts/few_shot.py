FEW_SHOT_PROMPT = '''
Create a quiz about the topic {input} using the following JSON format. The output must adhere to the provided schema, with all content on a single line and no extra spaces or newlines. Do not include any Python code, dataclass, or class definitions.
Example:
  "questions": [
    {"question": "What is Photosynthesis?", "choices": ["a) A process of plant respiration", "b) A process where plants make their food", "c) A method of plant reproduction", "d) A type of chemical reaction"], "answer": "b"},
    {"question": "Where does photosynthesis occur?", "choices": ["a) Roots", "b) Flowers", "c) Leaves", "d) Stem"], "answer": "c"},
    {"question": "What is produced as a result of photosynthesis?", "choices": ["a) Oxygen", "b) Glucose", "c) Carbon dioxide", "d) Nitrogen"], "answer": "b"}
  ]
{format_instructions}
'''