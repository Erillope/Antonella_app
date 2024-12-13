from src.common import ID
from .values import ServiceStatus, ServiceType
from .service import Service
from .form import Form
from typing import List
from datetime import date

class ServiceBuilder:
    def __init__(self, title: str, detail: str, min_price: int, max_price: int, 
                 form: Form, type: ServiceType) -> None:
        self.__id = ID.generate()
        self.__status = ServiceStatus.ENABLE
        self.__images : List[str] = []
        self.__created_date = date.today()
        self.__title = title
        self.__detail = detail
        self.__min_price = min_price
        self.__max_price = max_price
        self.__form = form
        self.__type = type
    
    def id(self, id: str) -> "ServiceBuilder":
        self.__id = id
        return self
    
    def status(self, status: ServiceStatus) -> "ServiceBuilder":
        self.__status = status
        return self
    
    def images(self, images: List[str]) -> "ServiceBuilder":
        self.__images = images
        return self
    
    def created_date(self, created_date: date) -> "ServiceBuilder":
        self.__created_date = created_date
        return self
    
    def build(self) -> Service:
        return Service(
            id = self.__id,
            title = self.__title,
            images = self.__images,
            detail = self.__detail,
            min_price = self.__min_price,
            max_price = self.__max_price,
            form = self.__form,
            status = self.__status,
            type = self.__type,
            created_date = self.__created_date
        )