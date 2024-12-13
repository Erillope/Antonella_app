from src.common import ID, StringValue
from .form_question import FormQuestion
from typing import List
from datetime import date

class Form:
    def __init__(self, id: str, service_id: str, title: str,
                 questions: List[FormQuestion], created_date: date) -> None:
        self.__id = ID(id)
        self.__service_id = ID(service_id)
        self.__title = StringValue(title)
        self.__questions = questions
        self.__created_date = created_date
    
    
    def change_title(self, title: str) -> None:
         self.__title = StringValue(title)
    
    def change_questions(self, questions: List[FormQuestion]) -> None:
        self.__questions = questions
    
    def add_question(self, question: FormQuestion) -> None:
        self.__questions.append(question)
    
    def remove_question(self, question: FormQuestion) -> None:
        if question in self.__questions:
            self.__questions.remove(question)
    