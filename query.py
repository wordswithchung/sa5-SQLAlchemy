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

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.

Brand.query.filter_by(id=8).first()

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.

Model.query.filter(Model.name=="Corvette", Model.brand_name=="Chevrolet").all()

# Get all models that are older than 1960.

Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.

Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".

Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.

Brand.query.filter(Brand.founded == 1903, Brand.discontinued == None).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.

Brand.query.filter(Brand.discontinued != None, Brand.founded < 1950).all()

# Get all models whose brand_name is not Chevrolet.

Model.query.filter(Model.brand_name != "Chervolet").all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    """Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query."""

    model_info = Model.query.filter(Model.year==year).all()

    for model in model_info:
        print "MODEL NAME: ", model.name
        print "BRAND NAME: ", model.brand_name
        if model.brand != None: 
        # Fillmore is a Model, but not a Brand; need this clause to
        # bypass NoneType error
            print "BRAND HEADQUARTERS: ", model.brand.headquarters
        print

def get_brands_summary(brand):
    """Prints out each brand name, and each model name for that brand
     using only ONE database query."""

    model_info = Model.query.filter(Model.brand_name==brand).all()

    for model in model_info:
        print model.brand_name, model.name

# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of
# ``Brand.query.filter_by(name='Ford')``?

"""
The returned value of the query VERBATIM(!) is "<flask_sqlalchemy.BaseQuery 
at 0x7f27b807e910>" and its datatype is a query from the Flask-SQLAlchemy
library. 

If we were to add a ".first()" or ".all()" to the end of that query, we would 
get a brand object for Ford, from which you can pull out info such as:
- brand id
- brand name
- when the brand was founded (year)
- brand's headquarters location
- and the year it was discontinued (if applicable)
"""

# 2. In your own words, what is an association table, and what *type* of
# relationship does an association table manage?

"""
An association table is one that holds the ID (usually primary key) of table X 
and an ID of table Y as foreign keys, but does not contain any important 
information within the table (outside of its own association table ID). 

It simply connects tables X and Y together, and makes many-to-many table 
relationship types possible.
"""

# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    """Design a function in python that takes in any string as parameter, and 
    returns a list of objects that are brands whose name contains or is equal 
    to the input string.
    """

    mystr = "".join('%' + mystr + '%')

    return Brand.query.filter( (Brand.name.like(mystr)) |
                               (Brand.name==mystr) ).all()


def get_models_between(start_year, end_year):
    """Design a function that takes in a start year and end year (two integers),
     and returns a list of objects that are models with years that fall between 
     the start year (inclusive) and end year (exclusive).
    """

    return Model.query.filter(Model.year >= start_year, 
                              Model.year < end_year).all()