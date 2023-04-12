import os

from decouple import Csv, config
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from kafka import KafkaAdminClient
from kafka.admin import NewTopic
from kafka.errors import TopicAlreadyExistsError

from .api import main as api

app = FastAPI()

ORIGINS = config("ORIGINS", default="*", cast=Csv())

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(api.router)


@app.on_event("startup")
async def startup_event():
    # Kafka Admin Client
    client = KafkaAdminClient(bootstrap_servers=os.environ.get("BOOTSTRAP-SERVERS"))
    # Creating topic
    topic = NewTopic(
        name=os.environ.get("TOPIC_PEOPLE_BASIC_NAME"),
        num_partitions=int(os.environ.get("TOPIC_PEOPLE_BASIC_PARTITIONS", "1")),
        replication_factor=int(
            os.environ.get("TOPIC_PEOPLE_BASIC_REPLICATION_FACTOR", "1")
        ),
    )
    # If topic already exists, it will throw an error
    try:
        # Creating topic
        client.create_topics(new_topics=[topic], validate_only=False)
    except TopicAlreadyExistsError:
        pass
    finally:
        # Close the client
        client.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}
