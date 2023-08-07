from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os
from hangman_pictures import lives_visual_dict

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Message(db.Model):
    # DB lentelei priskiria pavadinimą, jei nenurodysite, priskirs automatiškai pagal klasės pavadinimą.
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)  # stulpelis, kurio reikšmės integer. Taip pat jis bus primary_key.
    name = db.Column(db.String(80), nullable=False)
    lives = db.Column(db.Text, nullable=False)

    def __init__(self, name, lives):
        self.name = name
        self.lives = lives
    
    def __repr__(self):
        return f'{self.name} - {self.lives}'
    
with app.app_context():
    db.create_all()


# @app.route('/', methods=['GET'])
# def my_function():
#     print('Getting infos')
#     return render_template('index.html', data = {'lives': 7, 'message': '', 'picture': ''})
    
# my_dictionary = {"name": "Tomas","lives": 7}
# @app.route('/', methods=['POST'])
# def post_function():
#     user_guess = request.form['name']
#     db.session.add(user_guess)
#     db.session.commit()
#     return render_template('index.html')
    # print(f'{my_dictionary["lives"]}')
    # if my_dictionary.get("lives") >0:
    #     
    #     print('Letter was already used!!!')
    #     print(user_guess)
        
    #     current_live = my_dictionary.get("lives")
    #     current_live -= 1
    #     my_dictionary.get("lives") ==current_live
    #     print(current_live)
    #     return render_template('index.html')
                
            
    # else:
    #     print('While cicle is over')
    #     return render_template('index.html')
# data = {'lives': 7, 'message': '', 'picture': ''}
# @app.route('/', methods=['POST'])
# def test_while_cycle():
#     if data['lives'] > 0:
#         current_lives = data.get('lives')
#         current_lives -= 1
#         data['picture'] = lives_visual_dict.get(current_lives)
#         data['lives'] = current_lives
#         data['message'] = f'You have {current_lives} lives'
#         print(data)
#         return render_template('index.html', data=data)
#     else:
#         data['message'] = 'GameOver'
#         return render_template('index.html', data=data)
    


# new_data = {'lives': 7, 'message': '', 'picture': ''}
# # data = {'lives': 7, 'message': '', 'picture': ''}
# @app.route('/', methods=['GET', 'POST'])
# def my_function():
#     if request.method == 'GET':
#         data = new_data
#         print(data)
#         return render_template('index.html', data = data)

#     data = new_data
#     if request.method == 'POST':
#         print(data)
#         if data['lives'] > 0:
#             current_lives = data.get('lives')
#             current_lives -= 1
#             data['picture'] = lives_visual_dict.get(current_lives)
#             data['lives'] = current_lives
#             data['message'] = f'You have {current_lives} lives'
#             return render_template('index.html', data=data)
#         else:
#             data['message'] = 'GameOver'
#             return render_template('index.html', data=data)
data = {'lives': 7, 'message': '', 'picture': ''}


@app.route('/', methods=['GET'])
def my_function():
    if request.method == 'GET':
        # data = {'lives': 7, 'message': '', 'picture': ''}
        return render_template('index.html', data = data)

# data = {'lives': 7, 'message': '', 'picture': ''}
@app.route('/', methods=['POST'])
def my_function2():
    # data = new_data
    if request.method == 'POST':
        print(data)
        
        if data['lives'] > 0:
            current_lives = data.get('lives')
            current_lives -= 1
            data['picture'] = lives_visual_dict.get(current_lives)
            data['lives'] = current_lives
            data['message'] = f'You have {current_lives} lives'
            return render_template('index.html', data=data)
        else:
            data['message'] = 'GameOver'
            return render_template('index.html', data=data)
        


if __name__ == "__main__":
    app.run(debug=True)