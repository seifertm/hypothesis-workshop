# You've built an HTTP API that allows managing a shopping list. A shopping list consists of shopping items and each item stores an ID, the name and the amount to be bought. The web application stores the current shopping list as an in-memory list. The whole application is built using FastAPI [0]. ShoppingItem is a pydantic model [1].
# You don't need to dive into the documentation of these packages right now. Check the example below and see how far you get.
#
# [0] https://fastapi.tiangolo.com/
# [1] https://pydantic-docs.helpmanual.io/
from typing import Dict, List
import pytest
from hypothesis import given, strategies as st
from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import BaseModel, parse_obj_as

class ShoppingItem(BaseModel):
    id: int = 0
    name: str
    amount: int


app = FastAPI()
_shopping_items_by_id: Dict[int, ShoppingItem]  = {}


@app.get("/")
def get_shopping_list() -> List[ShoppingItem]:
    """Returns the current shopping list."""
    return list(_shopping_items_by_id.values())


@app.post("/")
def add_item(item: ShoppingItem) -> ShoppingItem:
    """Adds the specified item to the shopping list and returns the added item."""
    next_item_id = max(_shopping_items_by_id.keys()) + 1 if _shopping_items_by_id else 1
    item.id = next_item_id
    _shopping_items_by_id[item.id] = item
    return item


@app.delete("/{id_}")
def delete_item(id_: int) -> ShoppingItem:
    """Removes the item with the specified ID from the shopping list and returns the new list."""
    item = _shopping_items_by_id[id_]
    del _shopping_items_by_id[id_]
    return item


# See the following example on how you can use the FastAPI test client to issue requests and how you
# can use pydantic to serialize and deserialize ShoppingItems to and from JSON
@pytest.fixture(scope="session")
def api() -> TestClient:
    return TestClient(app)


def test_api_example(api):
    # Add a new shopping item
    new_item = ShoppingItem(name="milk", amount=2)
    add_item_response = api.post("/", json=new_item.dict())
    # calling "response.raise_for_status()" is helpful to get errors for HTTP response codes >= 400
    add_item_response.raise_for_status()
    added_item = ShoppingItem.parse_obj(add_item_response.json())

    # Retrieve shopping items
    get_list_response = api.get("/")
    get_list_response.raise_for_status()
    shopping_list = parse_obj_as(List[ShoppingItem], get_list_response.json())
    assert len(shopping_list) == 1
    assert added_item in shopping_list

    # Delete shopping items
    delete_item_response = api.delete(f"/{added_item.id}")
    delete_item_response.raise_for_status()
    deleted_item = ShoppingItem.parse_obj(delete_item_response.json())

    # Retrieve shopping list again
    get_list_response = api.get("/")
    get_list_response.raise_for_status()
    shopping_list = parse_obj_as(List[ShoppingItem], get_list_response.json())
    get_list_response.raise_for_status()
    assert deleted_item not in shopping_list


# You want to assert that the operations on the API are working as expected. Come up with tests using Hypothesis based on the test approaches presented in the slides of this session.
# Have fun testing the API!
