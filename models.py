"""
models.py — GroceryList

SQLAlchemy models for all database entities.
"""

import uuid
from datetime import datetime, timezone
from extensions import db


def generate_uuid():
    return str(uuid.uuid4())


class User(db.Model):
    """A GroceryList member."""

    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    lists = db.relationship("GroceryList", backref="owner", lazy=True,
                            foreign_keys="GroceryList.created_by")
    added_items = db.relationship("Item", backref="adder", lazy=True,
                                  foreign_keys="Item.added_by")

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
        }


class GroceryList(db.Model):
    """A named grocery list belonging to one user."""

    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    name = db.Column(db.String(200), nullable=False)
    created_by = db.Column(db.String(36), db.ForeignKey("user.id"), nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    is_shared = db.Column(db.Boolean, default=False, nullable=False)

    items = db.relationship("Item", backref="grocery_list", lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "created_by": self.created_by,
            "created_at": self.created_at.isoformat(),
            "is_shared": self.is_shared,
        }


class Item(db.Model):
    """
    A single item on a grocery list.

    is_purchased tracks whether the item has been picked up during shopping.
    purchased_by and purchased_at are set when the item is marked done.

    """

    """
    Question 1: What fields does Item have? Which ones are always set when an item is added, and which ones start as null?
    
    Always set:
    id, list_id, name, added_by, is_purchased

    starts as null:
    quantity, unit, category, added_at, purchased_by, purchased_at

    Question 2: Which two fields together record who purchased an item and when?
    purchased_by, purchased_at

    Question 3: The Item model has an added_by field and a purchased_by field. What does the distinction between these two fields represent in terms of real user behavior?
    added_by represent who added the item into the list, whereas purchased_by shows who actually bought the item. Two separate distinctions in regards to the list and the cart.
    """

    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    list_id = db.Column(db.String(36), db.ForeignKey("grocery_list.id"), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    quantity = db.Column(db.Float, nullable=True)
    unit = db.Column(db.String(50), nullable=True)
    category = db.Column(db.String(100), nullable=True)
    added_by = db.Column(db.String(36), db.ForeignKey("user.id"), nullable=False)
    added_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    is_purchased = db.Column(db.Boolean, default=False, nullable=False)
    purchased_by = db.Column(db.String(36), db.ForeignKey("user.id"), nullable=True)
    purchased_at = db.Column(db.DateTime, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "list_id": self.list_id,
            "name": self.name,
            "quantity": self.quantity,
            "unit": self.unit,
            "category": self.category,
            "added_by": self.added_by,
            "added_at": self.added_at.isoformat(),
            "is_purchased": self.is_purchased,
            "purchased_by": self.purchased_by,
            "purchased_at": self.purchased_at.isoformat() if self.purchased_at else None,
        }
