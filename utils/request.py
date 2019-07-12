from typing import Optional
from pydantic import BaseModel


class Request(BaseModel):
    msg_id: str
    first_name: str
    surname: str
    patronymic: Optional[str]
    birth_date: str


class ByMsisdnRequest(Request):
    msisdn: str


class ByPassportRequest(Request):
    series: Optional[str]
    number: str
    document_type: int
    issue_date: Optional[str]
    issue_authority: Optional[str]


class SimpleCheckRequest(Request):
    msisdn: Optional[str]
    series: Optional[str]
    number: str
    document_type: int
    issue_date: Optional[str]
    issue_authority: Optional[str]


class FullCheckRequest(SimpleCheckRequest):
    callback_url: Optional[str]
    smev_ttl: Optional[int]
    smev_ignore_cache: Optional[bool] = False
    smev_priority: Optional[str] = 'medium'
