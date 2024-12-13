from src.common import ID, StringValue
from .values import ServiceStatus, ServiceType, PriceRange
from .form import Form
from typing import List
from datetime import date

class Service:
    def __init__(self, id: str, title: str, images: List[str], detail: str, min_price: int, max_price: int,
                 form: Form, status: ServiceStatus, type: ServiceType, created_date: date) -> None:
        self.__id = ID(id)
        self.__title = StringValue(title)
        self.__images = images
        self.__detail = StringValue(detail, lower=False)
        self.__price_range = PriceRange(min_price, max_price)
        self.__form = form
        self.__status = status
        self.__type = type
        self.__created_date = created_date
        
    def change_title(self, title: str) -> None:
        self.__title = StringValue(title)
    
    def change_images(self, images: List[str]) -> None:
        self.__images = images
    
    def change_detail(self, detail: str) -> None:
        self.__detail = StringValue(detail)
    
    def change_price_range(self, min: int, max: int) -> None:
        self.__price_range = PriceRange(min, max)
    
    def change_form(self, form: Form) -> None:
        self.__form = form
    
    def enable(self) -> None:
        self.__status = ServiceStatus.ENABLE
    
    def disable(self) -> None:
        self.__status = ServiceStatus.DISABLE
    
    def is_enable(self) -> bool:
        return self.__status == ServiceStatus.ENABLE

    def get_id(self) -> str:
        return self.__id.get_value()
    
    def get_title(self) -> str:
        return self.__title.get_value()
    
    def get_images(self) -> List[str]:
        return self.__images
    
    def get_detail(self) -> str:
        return self.__detail.get_value()
    
    def get_min_price(self) -> int:
        return self.__price_range.get_min()
    
    def get_max_price(self) -> int:
        return self.__price_range.get_max()

    def get_status(self) -> ServiceStatus:
        return self.__status
    
    def get_form(self) -> Form:
        return self.__form
    
    def get_type(self) -> ServiceType:
        return self.__type
    
    def get_created_date(self) -> date:
        return self.__created_date
    
    def __str__(self) -> str:
        return f"Service(id={self.get_id()},title={self.get_title()},images={self.get_images()},"\
            f"detail={self.get_detail()},min_price={self.get_min_price()},"\
            f"max_price={self.get_max_price()},form={self.get_form()},status={self.get_status()},"\
            f"type={self.get_type()},created_date={self.get_created_date()})"