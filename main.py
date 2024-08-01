from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from models import Message
import pymongo
import redis

REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_DB = 0
redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)

MONGO_URI = "mongodb://localhost:27017/bot"

app = FastAPI()

client = pymongo.MongoClient(MONGO_URI)
db = client.get_database("my_bot")
messages_collection = db.get_collection("messages")

@app.get("/api/v1/messages/")
async def get_messages(page: int = 1, page_size: int = 10):
    if page <= 0 or page_size <= 0:
        raise HTTPException(status_code=400, detail="Неверные значения страницы или размера страницы")
    messages = messages_collection.find({}).skip((page - 1) * page_size).limit(page_size)
    message_list = []
    for message in messages:
        message_list.append(Message(text=message["text"], author=message.get("author")))
    total_messages = messages_collection.count_documents({})
    total_pages = (total_messages + page_size - 1) // page_size
    return {"messages": message_list, "current_page": page, "total_pages": total_pages}


@app.post("/api/v1/message/")
async def add_message(message: Message):
    messages_collection.insert_one(message.dict())
    return JSONResponse(content={"message": "Сообщение успешно добавлено!"}, status_code=201)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)
