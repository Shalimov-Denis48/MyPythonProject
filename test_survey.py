import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Тесты для класса AnonymousSurvey"""
    def setUp(self):
        """Создание опроса и набораответов для всех методов"""
        question = "Какой язык программирования для вас наиболее интерсен"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['Java', 'Python', 'C+', 'Go', 'JavaScript']

    def test_store_single_response(self):
        """Проверяется, что один ответ сохарнен в списке"""
        self.my_survey.store_response(self.responses[1])
        self.assertIn(self.responses[1], self.my_survey.responses)

    # def test_five_responses(self):
    #     """"Проверяет что пять ответов были сохранены"""
    #
    #
    #
    #     question = "Какой язык программирования для вас наиболее интерсен"
    #     my_survey = AnonymousSurvey(question)
    #     responses = ['Java', 'Python', 'C+', 'Go', 'JavaScript']
    #     for response in responses:
    #         my_survey.store_response(response)
    #
    #     for response in responses:
    #         self.assertIn(response, my_survey.responses)


if __name__ == '__name__':
    unittest.main()