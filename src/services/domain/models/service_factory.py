from .values import ServiceType, ServiceStatus
from .form import Form
from .service import Service
from .service_builder import ServiceBuilder
from datetime import date
from typing import List

class ServiceFactory:
    def create(self, title: str, detail: str, min_price: int, max_price: int, 
                 form: Form, type: ServiceType) -> Service:
        return ServiceBuilder(
            title = title,
            detail = detail,
            min_price = min_price,
            max_price = max_price,
            form = form,
            type = type
        ).build()
    
    def load(self, id: str, title: str, images: List[str], detail: str, min_price: int, max_price: int,
                 form: Form, status: ServiceStatus, type: ServiceType, created_date: date) -> Service:
        return ServiceBuilder(
            title = title,
            detail = detail,
            min_price = min_price,
            max_price = max_price,
            form = form,
            type = type
        ).id(id).images(images).created_date(created_date).status(status).build()