from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
class Item(Base):
    __tablename__ = 'ODC$Item'

    sku = Column(name='No_', primary_key=True)
    description = Column(name='Description')
    buom = Column(name='Base Unit of Measure')
    suom = Column(name='Sales Unit of Measure')
    item_category = Column(name='Item Category Code')
    item_group = Column(name='Item Group')
    qty_per_case = Column(name='Aantal per karton')
    qty_per_layer = Column(name='Verpakkingen per layer')
    qty_per_pallet = Column(name='Verpakkingen per pallet')
    tariff_no_national = Column(name='National Tariff No_')
    tariff_no = Column(name='Tariff No_')
    volume = Column(name='Liter per eenheid')
    abv = Column(name='Alcoholgehalte')


class Vendor(Base):
    __tablename__ = 'ODC$Vendor'

    code = Column(String, name='No_', primary_key=True)
    name = Column(String, name='Name')

class Sku(Base):
    __tablename__ = 'ODC$Stockkeeping Unit'

    sku = Column(name='Item No_', primary_key=True)
    variant_code = Column(name='Variant Code', primary_key=True)
    vendor_code = Column(String, ForeignKey('ODC$Vendor.No_'),name='Vendor No_')
    vendor = relationship('Vendor')
