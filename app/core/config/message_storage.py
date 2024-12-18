import os
from dotenv import load_dotenv
from langchain_community.chat_message_histories import UpstashRedisChatMessageHistory


load_dotenv()
UPSTASH_REDIS_URL = os.getenv("UPSTASH_REDIS_URL")
UPSTASH_REDIS_TOKEN = os.getenv("UPSTASH_REDIS_TOKEN")
UPSTASH_REDIS_TTL = os.getenv("UPSTASH_REDIS_TTL")


def get_message_storage(session_id: str):
    message_storage = UpstashRedisChatMessageHistory(
        session_id=session_id,
        url=UPSTASH_REDIS_URL,
        token=UPSTASH_REDIS_TOKEN,
        ttl=UPSTASH_REDIS_TTL,
    )

    return message_storage
