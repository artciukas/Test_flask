from fastapi import FastAPI, Depends, Request, Form, status
 
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates
 
from sqlalchemy.orm import Session
 
import models
from database import SessionLocal, engine
from app2 import get_random_word, word_database, display_word, guessed_letters, get_random_word_length, lives, print_hangman_picture, display_all_letters, unused_letters_list

models.Base.metadata.create_all(bind=engine)
 
templates = Jinja2Templates(directory="templates")
 
app = FastAPI()


 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def cycle():
    lives = 7
    guessed_letters = []
    while lives > 0:
        guessed_letters.append(lives)
        lives -= 1
    return guessed_letters
 
@app.get("/")
def home(request: Request, db: Session = Depends(get_db)):
    lives = 7
    word_database = ['apple', 'watermelone', 'lemon']
    unused_letters_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    current_lives = []
    todos = db.query(models.Todo).all()
    random_word = get_random_word(word_database)
    joined_list = display_all_letters(unused_letters_list)
    while lives > 0:
            print(f'Word are: {display_word(random_word, guessed_letters)}')
            print(get_random_word_length(random_word))
            print(f'{print_hangman_picture(lives)}')
            print("******************************************")
            print('Available letters:')
            print(display_all_letters(unused_letters_list))
            print("******************************************")
            user_guess = input('Please enter a letter: ').upper()
            if user_guess in guessed_letters:
                print('Letter was already used!!!')
                print("############################")
            elif user_guess.isalpha() and len(user_guess) == 1:
                guessed_letters.append(user_guess)

                if user_guess in random_word:
                    print('Correct. This letter is in the word')
                    unused_letters_list.remove(user_guess)
                    print("############################")
                else:
                    lives -= 1
                    print('This letter does not exist in the word')
                    print("############################")
                
            else:
                print('Please enter single letter!')
                print("############################")

            if "_" not in display_word(random_word, guessed_letters):
                print("\nCongratulations! You guessed the word:", random_word)
                break
    else:
        print(f'{print_hangman_picture(lives)}')
        print(f'GAME OVER. The word was {random_word}')
    return templates.TemplateResponse("index.html",
                                      {"request": request, "todo_list": todos, "random_word": random_word, "joined_list": joined_list, 'current_lives': current_lives})



# @app.post("/add")
# def add(request: Request, title: str = Form(...), db: Session = Depends(get_db)):
#     new_todo = models.Todo(title=title)
#     db.add(new_todo)
#     db.commit()
#     aaaa = title
#     url = app.url_path_for("home")
#     return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER), aaaa
 
 
# @app.get("/update/{todo_id}")
# def update(request: Request, todo_id: int, db: Session = Depends(get_db)):
#     todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
#     todo.complete = not todo.complete
#     db.commit()
 
#     url = app.url_path_for("home")
#     return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)
 
 
# @app.get("/delete/{todo_id}")
# def delete(request: Request, todo_id: int, db: Session = Depends(get_db)):
#     todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
#     db.delete(todo)
#     db.commit()
 
#     url = app.url_path_for("home")
#     return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)