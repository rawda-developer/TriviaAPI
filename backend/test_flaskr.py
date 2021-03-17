import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category

"""This class represents the trivia test case"""

class TriviaTestCase(unittest.TestCase):
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        # self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        self.database_path = "postgres://postgres:password@localhost:5432/{}".format(
            self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    Test cases
    2 test cases for each end point
    One test case for success, and other for failure
    """

    '''
    This will test /questions endpoint success
    '''
    def test_get_questions(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['total_questions'])
        self.assertTrue(data['success'])

    '''
    This will test /questions endpoint failure
    '''
    def test_404_questions(self):
        res = self.client().get('/questions?page=1000')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)

    '''
    This will test /categories endpoint success
    get all categories
    '''
    def test_get_all_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(data['categories']))

    '''
    This will test /categories endpoint failure
    get all categories
    '''
    def test_get_all_categories_404(self):
        res = self.client().get('/categories/')
        self.assertEqual(res.status_code, 404)
        data = json.loads(res.data)
        self.assertFalse(data['success'])

    '''
    This will test /questions/<id> delete endpoint success
    get all questions
    '''
    def test_delete_question_by_id(self):
        res = self.client().delete('/questions/12')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    '''
    This will test /questions/<id> delete endpoint failure
    delete a questions
    '''
    def test_delete_question_by_id_404(self):
        res = self.client().delete('/questions/100')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])

    '''
    This will test /questions/<id> create endpoint success
    create a new question
    '''
    def test_create_question(self):
        res = self.client().post('/questions', json={'question': 'Question 1',
                                                     'answer': 'A',
                                                     'category': '2',
                                                     'difficulty': 4
                                                     })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    '''
    This will test /questions/<id> create endpoint failure
    create a new question
    '''
    def test_create_question_422(self):
        res = self.client().post('/questions/1', json={
            'question': 'Question 1',
            'answer': 'A',
            'category': '1',
            'difficulty': 4
        })
        self.assertEqual(res.status_code, 405)

    '''
    This will test /questions/search?search_term create endpoint success
    search questions based on a keyword
    '''
    def test_search_question(self):
        res = self.client().post('/questions/search?search_term=lake')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['success'])

    '''
    This will test /questions/search?search_term create endpoint failure
    search questions based on a keyword
    '''
    def test_search_question_404(self):
        res = self.client().post('/questions/search?no_question')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])

    '''
    This will test /categories/<id>/questions endpoint success
    get all questions based on a category id
    '''
    def test_get_question_by_category_id(self):
        res = self.client().get('/categories/1/questions')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue('total_questions')
        self.assertTrue(len('questions'))

    '''
    This will test /categories/<id>/questions endpoint failure
    get all questions based on a category id
    '''
    def test_get_question_by_category_id_404(self):
        res = self.client().get('/categories/100/questions')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])

    '''
    This will test /quizzes endpoint success
    get a random question based on quiz_category and previous_questions
    '''
    def test_get_random_question(self):
        res = self.client().post('/quizzes', json={
            "quiz_category": {
                "id": 6,
                "type": "Sports"
            },
            "previous_questions": [
                {
                    "answer": "Apollo 13",
                    "category": 5,
                    "difficulty": 4,
                    "id": 2,
                    "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
                }

            ]
        })
        data = json.loads(res.data)
        self.assertTrue(data['success'])
        self.assertEqual(res.status_code, 200)

    '''
    This will test /quizzes endpoint failure
    get a random question based on quiz_category and previous_questions
    '''
    def test_get_random_question_400(self):
        res = self.client().post('/quizzes', json={'wrong_attr': -1})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertFalse(data['success'])


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
