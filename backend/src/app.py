import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from strawberry.schema.config import StrawberryConfig

from schemas.query import Query

schema = strawberry.Schema(query=Query, config=StrawberryConfig(auto_camel_case=False))


app = FastAPI()
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")

