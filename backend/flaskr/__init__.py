import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

# number of books shown per page
QUESTIONS_PER_PAGE = 10

'''
    A helper function that returns a
    list of qustions from selction list in a page
'''


def paginate_questions(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    questions = [question.format() for question in selection]
    current_questions = questions[start:end]

    return current_questions


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    '''
     Set up CORS. Allow '*' for origins.
     Delete the sample route after completing the TODOs
    '''
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    '''
     after_request decorator to set Access-Control-Allow
    '''
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PUT,POST,DELETE,OPTIONS')
        return response

    '''
    Create an endpoint to handle GET requests
    for all available categories.
    '''
    @app.route('/categories', methods=['GET'])
    def get_all_categories():
        try:
            categories = Category.query.all()
            categories_dictionary = {}
            for category in categories:
                categories_dictionary[category.id] = category.type
            return jsonify({
                'success': True,
                'categories': categories_dictionary
            }), 200
        except:
            return jsonify({
                'success': False
            }), 404

    '''
    An endpoint to handle GET requests for questions,
    including pagination (every 10 questions).
    This endpoint returns a list of questions,
    number of total questions, current category, categories.
    '''
    @app.route('/questions', methods=['GET'])
    def get_questions():
        try:
            questions = Question.query.all()
            categories = Category.query.all()
            category_dictionary = {}
            # create a dictionary of id and type
            for category in categories:
                category_dictionary[category.id] = category.type
            current_questions = paginate_questions(request, questions)
            if len(current_questions) == 0:
                abort(404)
            return jsonify({
                'success': True,
                'questions': current_questions,
                'total_questions': len(questions),
                'categories': category_dictionary
            })
        except:
            return jsonify({
                'success': False
            }), 404
    '''
    An endpoint to DELETE question using a question ID.
    '''
    @app.route("/questions/<int:id>", methods=["DELETE"])
    def delete_question(id):
        question = Question.query.filter(Question.id == id).one_or_none()
        if question is None:
            return jsonify({
                'success': False
            }), 404
        question.delete()
        return jsonify({
            'success': True,
            'id': id
        }), 200

    '''
    An endpoint to POST a new question,
    which will require the question and answer text,
    category, and difficulty score.
    or
    get questions based on a search term.
    It should return any questions for whom the search term
    is a substring of the question.
    '''
    @app.route('/questions', methods=['POST'])
    def post_question():
        body = request.get_json()
        if body.get('searchTerm'):
            search_term = body.get('searchTerm')
            try:
                questions = Question.query.filter(
                    Question.question.ilike(f'%{search_term}%')).all()
                questions_list = paginate_questions(request, questions)
                if len(questions_list) == 0:
                    return jsonify({
                        'success': False
                    }), 404
                return jsonify({
                    'total_questions': len(questions_list),
                    'success': True,
                    'questions': questions_list
                })
            except:
                return jsonify({
                    'success': False
                }), 404
        else:
            question_text = body.get("question", None)
            answer_text = body.get("answer", None)
            category_text = body.get("category", None)
            difficult_score = body.get("difficulty", None)
            try:
                question = Question(question=question_text,
                                    answer=answer_text,
                                    category=category_text,
                                    difficulty=difficult_score)
                question.insert()
                questions = Question.query.order_by(Question.id).all()
                current_questions = paginate_questions(request, questions)
                return jsonify({
                    'success': True,
                    'questions': current_questions,
                    'total_questions': len(Question.query.all())
                })
            except:
                return jsonify({
                    'success': False
                }), 422

    '''
    A GET endpoint to get questions based on category.
    '''
    @app.route('/categories/<int:id>/questions')
    def get_questions_by_id(id):
        try:
            category = Category.query.filter(Category.id == id).one_or_none()
            if category is None:
                abort(400)
            questions = Question.query.filter(
                Question.category == category.id).all()
            if questions is None:
                abort(404)
            return jsonify({
                'success': True,
                'questions': paginate_questions(request, questions),
                'total_questions': len(Question.query.all()),
                'current_category': category.type
            }), 200
        except:
            return jsonify({
                'success': False
            }), 404
    '''
    A POST endpoint to get questions to play the quiz.
    This endpoint should take category and previous question parameters
    and return a random questions within the given category,
    if provided, and that is not one of the previous questions.
    '''
    @app.route('/quizzes', methods=['POST'])
    def get_random_question():
        body = request.get_json()
        quiz_category = body.get('quiz_category')
        previous_questions = body.get('previous_questions')
        if (quiz_category is None) or (previous_questions is None):
            return jsonify({
                'success': False
                }), 400
        if quiz_category['id'] == 0:
            questions = Question.query.all()
        else:
            questions = Question.query.filter(
                Question.category == quiz_category["id"]).all()
        if questions is None:
            abort(404)
        total = len(questions)

        def get_random_question():
            return questions[random.randrange(0, len(questions), 1)]

        def check_used(question):
            used = False
            for q in previous_questions:
                if q == question.id:
                    used = True
            return used

        random_question = get_random_question()
        while check_used(random_question):
            random_question = get_random_question()
            if (len(previous_questions) == total):
                return jsonify({
                    'success': True
                })

        return jsonify({
            'success': True,
            'total': total,
            'question': random_question.format()
        })

    '''
    Error handlers for all expected errors
    '''
    @app.errorhandler(404)
    def error_404(err):
        return jsonify({
            'success': False,
            'page': 'Error 404 -> Not found'
        }, 404)

    @app.errorhandler(400)
    def error_400(err):
        return jsonify({
            'success': False,
            'data': 'error 400 -> Bad Request'
        })

    @app.errorhandler(422)
    def error_422(err):
        return jsonify({
            'success': False,
            'data': 'Error 422 -> Unprocessable Entity'
        })

    @app.errorhandler(500)
    def error_500(err):
        return jsonify({
            'success': False,
            'data': 'Error 500 -> Internal Server Error'
        })
    return app
