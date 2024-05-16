import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class PromptExpense():

    description = None
    expenses_categories = None
    current_datetime = None
    output_schema = None

    def __init__ (self, description, expenses_categories, current_datetime, output_schema):
        self.description = description
        self.expenses_categories = expenses_categories
        self.current_datetime = current_datetime
        self.output_schema = output_schema
    
    def get_ai_response(self):
        example_expenses_categories = [{'id':1,'name':'lazer'},{'id':2,'name':'mercado'},{'id':3,'name':'transporte'}]
        example_expenses_description = 'fui ao cinema e gastei 20 reais no ingresso e 50 com pipoca , na volta do caminho passei no mercado e comprei 400 reais em comida e 20 com gasolina'                               
        example_expenses_output = [
            {
                'id': 1,
                'date': '2024-05-01 20:53:23',
                'fk_category': 1,
                'description': 'ingresso do cinema',
                'value': 20
            },
            {
                'id': 2,
                'date': '2024-05-01 20:53:23',
                'fk_category': 1,
                'description': 'pipoca no cinema',
                'value': 50
            },
            {
                'id':3,
                'date': '2024-05-01 20:53:23',
                'fk_category': 2,
                'description': 'compras no mercado voltando do cinema',
                'value': 400
            },
            {
                'id':4,
                'date': '2024-05-01 20:53:23',
                'fk_category': 3,
                'description': 'gasolina voltando do cinema e compras',
                'value': 20
            }
        ]

        prompt = f"""
            Im going to send to you a list of some expenses_categories,  a user description and a json format that i need that you return to me only the json with the attributes filled

            EXAMPLE INPUT:
            based on the expenses_categories: {example_expenses_categories}
            and the description "{example_expenses_description}"

            EXAMPLE OUTPUT: {example_expenses_output}

            now the real data:
            based on these 'expenses_categories': {self.expenses_categories}
            return to me a json with the following format, but only with the attributes filleds based on the user description 
            {self.output_schema}
            the date must be {self.current_datetime}, fk_category must be the id of the expenses_categories that i showed previously.
            based on the following user expense description in portuguese: {self.description}

            return to me ONLY the json filled with the description details i dont need schema properties details. The id should be sequencial, begging in 1.
        """

        client = OpenAI(
            api_key=os.environ.get("OPENAI_API_KEY")
        )

        chat_completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )

        return chat_completion