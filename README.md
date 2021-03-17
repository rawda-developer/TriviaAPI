# Udacitrivia

## Introduction
This project is a RESTful API written in python 3 and is based on Flask Framework and Postgresql. The project has a front end written in REACT js

## Getting Started
- Base URL:
  - Currently we do not have a web hosting, so you can only run on `http://localhost:3000/`
- API keys/Authorization
  - The API does not require authentication at this moment
## Instructions 
### install the project 
#### Front End
- Run REACT js
```
npm install
npm start
```

#### Back end
- Install Required dependencies
```
pip install -r requirements.txt
```
- Setup Psql Database
```
psql trivia < trivia.psql
```
- Run the server
```
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```
- Testing
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
dependencies and start the project server.

## Errors
- 404 status code
  - It means that the required resource or page is not found
- 400 status code
  - Bad Request response status code indicates that the server cannot or will not process the request due to a client error
- 422 status code
  - Unprocessable Entity response status code indicates that the server understands the content type of the request entity, and the syntax of the request entity is correct, but it was unable to process the contained instructions.Feb 19, 2021
  
## Resource Endpoint Library
- GET/categories
  - General
  - Returns a list of category objects, success value, and total number of categories
- Sample: curl `http://127.0.0.1:5000/categories`
- Response 
```
{
    "categories": {
        "1": "Science",
        "2": "Art",
        "3": "Geography",
        "4": "History",
        "5": "Entertainment",
        "6": "Sports"
    },
    "success": true
}
```

- GET/questions
  - General
    - Returns a list of categories, a list of question objects, success value, and total number of questions
- Sample: curl ` http://127.0.0.1:5000/questions `
- Response
```
{
    "categories": {
        "1": "Science",
        "2": "Art",
        "3": "Geography",
        "4": "History",
        "5": "Entertainment",
        "6": "Sports"
    },
    "questions": [
        {
            "answer": "Apollo 13",
            "category": 5,
            "difficulty": 4,
            "id": 2,
            "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
        },
        {
            "answer": "Tom Cruise",
            "category": 5,
            "difficulty": 4,
            "id": 4,
            "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
        },
        {
            "answer": "Edward Scissorhands",
            "category": 5,
            "difficulty": 3,
            "id": 6,
            "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
        },
        {
            "answer": "Brazil",
            "category": 6,
            "difficulty": 3,
            "id": 10,
            "question": "Which is the only team to play in every soccer World Cup tournament?"
        },
        {
            "answer": "George Washington Carver",
            "category": 4,
            "difficulty": 2,
            "id": 12,
            "question": "Who invented Peanut Butter?"
        },
        {
            "answer": "Lake Victoria",
            "category": 3,
            "difficulty": 2,
            "id": 13,
            "question": "What is the largest lake in Africa?"
        },
        {
            "answer": "The Palace of Versailles",
            "category": 3,
            "difficulty": 3,
            "id": 14,
            "question": "In which royal palace would you find the Hall of Mirrors?"
        },
        {
            "answer": "Agra",
            "category": 3,
            "difficulty": 2,
            "id": 15,
            "question": "The Taj Mahal is located in which Indian city?"
        },
        {
            "answer": "Escher",
            "category": 2,
            "difficulty": 1,
            "id": 16,
            "question": "Which Dutch graphic artist–initials M C was a creator of optical illusions?"
        },
        {
            "answer": "Mona Lisa",
            "category": 2,
            "difficulty": 3,
            "id": 17,
            "question": "La Giaconda is better known as what?"
        }
    ],
    "success": true,
    "total_questions": 45
}
```
- DELETE/questions
  - General
    - Returns a success value of the request
- Sample: `curl -X "DELETE" http://localhost:5000/questions/1`

 - Response
 
```
    {
        "success": true
    }
```

- POST/questions
  - General
    - Returns a success value of the request

- Sample:

```
curl -d '{
    "question": "What is your favorite fruit ?",
    "answer": "Apple",
    "category": "3",
    "difficulty": 1
}' -H "Content-Type: application/json" -X POST http://localhost:5000/questions
```

 - Response

```
{
    "questions": [
        {
            "answer": "Apollo 13",
            "category": 5,
            "difficulty": 4,
            "id": 2,
            "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
        },
        {
            "answer": "Tom Cruise",
            "category": 5,
            "difficulty": 4,
            "id": 4,
            "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
        },
        {
            "answer": "Maya Angelou",
            "category": 4,
            "difficulty": 2,
            "id": 5,
            "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
        },
        {
            "answer": "Edward Scissorhands",
            "category": 5,
            "difficulty": 3,
            "id": 6,
            "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
        },
        {
            "answer": "Muhammad Ali",
            "category": 4,
            "difficulty": 1,
            "id": 9,
            "question": "What boxer's original name is Cassius Clay?"
        },
        {
            "answer": "Brazil",
            "category": 6,
            "difficulty": 3,
            "id": 10,
            "question": "Which is the only team to play in every soccer World Cup tournament?"
        },
        {
            "answer": "Uruguay",
            "category": 6,
            "difficulty": 4,
            "id": 11,
            "question": "Which country won the first ever soccer World Cup in 1930?"
        },
        {
            "answer": "George Washington Carver",
            "category": 4,
            "difficulty": 2,
            "id": 12,
            "question": "Who invented Peanut Butter?"
        },
        {
            "answer": "Lake Victoria",
            "category": 3,
            "difficulty": 2,
            "id": 13,
            "question": "What is the largest lake in Africa?"
        },
        {
            "answer": "The Palace of Versailles",
            "category": 3,
            "difficulty": 3,
            "id": 14,
            "question": "In which royal palace would you find the Hall of Mirrors?"
        }
    ],
    "success": true,
    "total_questions": 22
}
```

- POST/questions/search
 - General
    - Returns a success value of the request
    -      question_text = body.get('question', None)
        answer_text = body.get('answer', None)
        category = body.get('category', None)
        difficult_score = body.get('difficulty', None)
- Sample:

```
curl -d "http://127.0.0.1:5000/questions/search?search_term=movie" -H "Content-Type: application/x-www-form-urlencoded" -X POST http://localhost:5000/questions/search 
```

 - Response
```
{
    "questions": [
        {
            "answer": "Apollo 13",
            "category": 5,
            "difficulty": 4,
            "id": 2,
            "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
        }
    ],
    "success": true,
    "total_questions": 1
}
```

- POST/categories/1/questions
 - General
    * Returns a success value of the request, a list of question objects
- Sample:
  
  ```
    curl localhost:5000/categories/1/questions
  ```
  
  - Response
  
  ```
      {
        "current_category": "Science",
        "questions": [
            {
                "answer": "The Liver",
                "category": 1,
                "difficulty": 4,
                "id": 20,
                "question": "What is the heaviest organ in the human body?"
            },
            {
                "answer": "Alexander Fleming",
                "category": 1,
                "difficulty": 3,
                "id": 21,
                "question": "Who discovered penicillin?"
            },
            {
                "answer": "Blood",
                "category": 1,
                "difficulty": 4,
                "id": 22,
                "question": "Hematology is a branch of medicine involving the study of what?"
            }
        ],
        "success": true,
        "total_questions": 22
    } 
```

- POST/quizzes
- General
    * Returns a success value of the request, a random question
- Sample:

```
    curl -X POST -H "Content-Type: application/json" \
        -d '{
            "quiz_category": {
                "id": "1",
                "type": "Science"
            },
            "previous_questions": [{
                "answer": "Maya Angelou",
                "category": 4,
                "difficulty": 2,
                "id": 5,
                "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
            },
            {
                "answer": "Muhammad Ali",
                "category": 4,
                "difficulty": 1,
                "id": 9,
                "question": "What boxer's original name is Cassius Clay?"
            },
            {
                "answer": "Apollo 13",
                "category": 5,
                "difficulty": 4,
                "id": 2,
                "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
            }]
        }' https://localhost:5000/quizzes 
```

Response
```
    {
        "question": {
            "answer": "The Liver",
            "category": 1,
            "difficulty": 4,
            "id": 20,
            "question": "What is the heaviest organ in the human body?"
        },
        "success": true,
        "total": 3
    } 
```