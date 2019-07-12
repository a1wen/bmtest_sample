from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Response(BaseModel):
    code: int
    description: Optional[str]


class MsisdnResponse(Response):
    is_person_in_white_list: bool
    is_person_in_stop_list: bool
    is_person_in_alarm_list: bool
    is_person_in_mdw_list: bool
    is_person_in_terror_list: Optional[bool]


class PassportResponse(Response):
    is_person_in_terror_list: Optional[bool]
    is_passport_expired: Optional[bool]
    smev_check_date: Optional[str] = datetime.now().strftime('%Y-%m-%d')
    smev_code: Optional[int]
    smev_subcode: Optional[int]
    smev_invalidity_date: Optional[str]


class SimpleCheckResponse(Response):
    is_person_in_white_list: bool
    is_person_in_stop_list: bool
    is_person_in_alarm_list: bool
    is_person_in_mdw_list: bool
    is_passport_expired: Optional[bool]
    is_person_in_terror_list: Optional[bool]
    smev_check_date: Optional[str]
    smev_code: Optional[int]
    smev_subcode: Optional[int]
    smev_invalidity_date: Optional[str]


class SimpleCheckLazyResponse(Response):
    accepted: bool
    version: Optional[str]
    status: Optional[str]


class FullCheckResponse(SimpleCheckResponse):
    task_id: Optional[str]


class FullCheckLazyResponse(SimpleCheckLazyResponse):
    task_id: Optional[str]
