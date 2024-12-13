from src.common import ID, StringValue
from .values import InputType
from datetime import date

class FormQuestion:
    def __init__(self, id: str, question: str, required: bool,
                 created_date: date, input_type: InputType) -> None:
        self.__id = ID(id)
        self.__question = StringValue(question)
        self.__required = required
        self.__created_date = created_date
        self.__input_type = input_type
    
    def get_id(self) -> str:
        return self.__id.get_value()
    
    def get_question(self) -> str:
        return self.__question.get_value()
    
    def is_required(self) -> bool:
        return self.__required
    
    def get_created_date(self) -> date:
        return self.__created_date
    
    def get_input_type(self) -> InputType:
        return self.__input_type
    
    def __str__(self) -> str:
        return f"FormQuestion(id={self.get_id()},question={self.get_question()},"\
            f"required={self.is_required()},created_date={self.get_created_date()},"\
                f"input_type={self.get_input_type()})"
    
    def __eq__(self, value: object) -> bool:
        if isinstance(value, FormQuestion):
            return value.get_id() == self.get_id()
        return False