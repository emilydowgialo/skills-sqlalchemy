"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *
from sqlalchemy import or_, and_

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.
query = Brand.query.get(8)
query.name

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
Model.query.filter_by(name="Corvette", brand_name="Chevrolet").all()

# Get all models that are older than 1960.
db.session.query(Model).filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.
db.session.query(Brand).filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".
Model.query.filter(Model.name.contains('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
Brand.query.filter(Brand.discontinued==None, Brand.founded==1903).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded 
# before 1950.
Brand.query.filter(or_(Brand.discontinued!=None, Brand.founded < 1950)).all()

# Get any model whose brand_name is not Chevrolet.
Model.query.filter(Model.brand_name != 'Chevrolet').all()

# Fill in the following functions. (See directions for more info.)


def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    # This query retrieves the headquarters, brand_name, and name attributes
    query = db.session.query(Brand.headquarters, Model.brand_name, Model.name).join(Model).filter(Model.year == year).all()

    # Prints out the name, brand_name, and headquarter attributes
    for headquarters, brand_name, name in query:
        print name, brand_name, headquarters


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    # This queries for information in the Model table
    query = Model.query.all()

    # Iterates over each object in the query list and prints brand_name and name
    for i in range(len(query)):
        print query[i].brand_name, query[i].name


# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
# The returned value is a sequence (a list), and the datatype is an object.

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
# An association table shows the relationship between two tables, but contains no 
# useful data - just ids. They are present in many-to-many data models. They
# are not referenced directly, but provide a bridge between two tables with
# a M2M relationship.

# -------------------------------------------------------------------
# Part 3

# Design a function in python that takes in any string as parameter, and returns 
# a list of objects that are brands whose name contains or is equal to the input 
# string.
def search_brands_by_name(thing):

    # This will take in any string and return a list of objects containing that string
    query = Brand.query.filter(Brand.name.contains(thing)).all()

    return query

# Design a function that takes in a start year and end year (two integers), and 
# returns a list of objects that are models with years that fall between the
# start year (inclusive) and end year (exclusive).


def get_models_between(start_year, end_year):

    # This takes in a start and end year and returns a list of objects that are
    # models with years that fall between the start and end years
    query = Model.query.filter(Model.year.between(start_year, end_year)).all()

    return query
