#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import relationship, backref
from sqlalchemy import ForeignKey
from models.city import City
from sqlalchemy import Table


place_amenity = Table('place_amenity', Base.metadata,
        Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
        Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
)

class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    reviews = relationship('Review',
            cascade='all, delete',
            backref='place')
    amenities = relationship("Amenity", seconday=place_amenity, viewonly=False)

    @property
    def amenities(self):
        """returns amenities"""
        return self.amenities

    @amenities.setter
    def amenities(self, amenity):
        """sets the conditions for amenities"""
        if isinstance(amenity, Amenity):
            self.amenities.append(amenity.id)

    @property
    def reviews(self):
        """Getter attribute that returns the list of Review instance"""
        reviews_list = []
        for review in models.storage.all(Review).values():
            if review.place_id == self.id:
                reviews_list.append(review)
        return reviews_list
