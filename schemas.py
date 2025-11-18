"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogpost" collection
"""

from pydantic import BaseModel, Field, HttpUrl
from typing import Optional, List

class User(BaseModel):
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Tourism app schemas
class Destination(BaseModel):
    name: str = Field(..., description="Nom de la destination")
    region: str = Field(..., description="Région au Maroc")
    description: str = Field(..., description="Description courte")
    hero_image: Optional[HttpUrl] = Field(None, description="Image principale")
    gallery: Optional[List[HttpUrl]] = Field(default=None, description="Images de la galerie")
    highlights: Optional[List[str]] = Field(default=None, description="Points forts")

class Tour(BaseModel):
    title: str = Field(..., description="Titre du circuit")
    duration_days: int = Field(..., ge=1, description="Durée en jours")
    price_eur: float = Field(..., ge=0, description="Prix en EUR")
    difficulty: Optional[str] = Field(None, description="Niveau (facile, moyen, avancé)")
    summary: str = Field(..., description="Résumé du circuit")
    thumbnail: Optional[HttpUrl] = Field(None, description="Image de couverture")
    destinations: Optional[List[str]] = Field(default=None, description="Destinations incluses")
    includes: Optional[List[str]] = Field(default=None, description="Ce qui est inclus")
    not_included: Optional[List[str]] = Field(default=None, description="Non inclus")
