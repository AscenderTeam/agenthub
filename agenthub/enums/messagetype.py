from enum import Enum


class MessageTypeEnum(Enum):
    SYSTEM_EVENT = 'system_event' # user is created, or added to chat or smth
    USER_MESSAGE = 'user_message'
    OPERATOR_MESSAGE = 'operator_message'
    CUSTOMER_MESSAGE = 'customer_message'
    AI_MESSAGE = 'ai_message'
    SYSTEM_MESSAGE = 'system_message'