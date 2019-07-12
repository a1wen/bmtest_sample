from enum import Enum


class ResponseCode(Enum):
    SUCCESS = 0  # 0 – Успешно
    ERROR = 1  # 1 – Ошибка разбора запроса
    INTERNAL_ERROR = 5  # 5 – Внутренняя ошибка
    VALIDATION_ERROR = 9  # 9 – Ошибка валидации
    IN_TERRORIST_LIST = 11  # 11 – Совпадение по спискам террористов
    IN_EXPIRED_PASSPORT_LIST = 12  # 12 – Совпадение по спискам истекших паспортов / отрицательный результат в СМЭВ
    IN_ALARM_LIST = 13  # 13 – Совпадение по "желтым"(alarm) спискам
    IN_STOP_LIST = 14  # 14 – Совпадение по стоп - спискам
    IN_MVD_LIST = 15  # 15 - Совпадение по ФРОМУ
