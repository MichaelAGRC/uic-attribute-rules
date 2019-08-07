#!/usr/bin/env python
# * coding: utf8 *
'''
art_pen.py
A module that has the UICArtPen rules
'''

from config import config
from models.ruletypes import Constant, Constraint
from services.loader import load_rule_for

from . import common

TABLE = 'UICArtPen'
FOLDER = 'artPen'

guid_constraint = Constant('Art Pen Guid', 'GUID', 'ArtPen.Guid', 'GUID()')

name_constraint = Constraint('Art Pen Well Name', 'ArtPen.ArtPen_WellName', load_rule_for(FOLDER, 'wellNameConstraint'))
name_constraint.triggers = [config.triggers.insert, config.triggers.update]

well_type_constraint = Constraint(
    'Art Pen Well Type', 'ArtPen.ArtPen_WellType', common.constrain_to_domain('ArtPen_WellType', allow_null=False, domain='UICArtPenWellType')
)
well_type_constraint.triggers = [config.triggers.insert, config.triggers.update]

review_date_constraint = Constraint('Art Pen Review Date', 'ArtPen.Artpen_ReviewDate', load_rule_for(FOLDER, 'reviewDateConstraint'))
review_date_constraint.triggers = [config.triggers.insert, config.triggers.update]

catype_constraint = Constraint('Art Pen Review Date', 'ArtPen.ArtPen_CAType', load_rule_for(FOLDER, 'caTypeConstraint'))
catype_constraint.triggers = [config.triggers.insert, config.triggers.update]

cadate_constraint = Constraint('CA Date', 'ArtPen.ArtPen_CADate', load_rule_for(FOLDER, 'caDateConstraint'))
cadate_constraint.triggers = [config.triggers.insert, config.triggers.update]

RULES = [
    guid_constraint,
    name_constraint,
    well_type_constraint,
    review_date_constraint,
    catype_constraint,
    cadate_constraint,
]
