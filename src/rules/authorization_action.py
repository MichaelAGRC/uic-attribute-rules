#!/usr/bin/env python
# * coding: utf8 *
'''
authorization_action.py
A module that has the UICAuthorizationAction rules
'''

from . import common
from config import config
from models.ruletypes import Constant, Constraint

constrain_to_parent_start_date = '''if (!haskey($feature, 'AuthorizationActionDate') || isempty($feature.AuthorizationActionDate)) {
    return true;
}

var field = 'StartDate';
var set = FeatureSetByName($datastore, 'UICAuthorization', [field], false);

var fk = $feature.authorization_fk;

// TODO: One day there will be a relationship traversal operation
var authorizations = filter(set, 'GUID=@fk');

if (isempty(authorizations)) {
    return true;
}

var authorization = first(authorizations);

return iif ($feature.AuthorizationActionDate < authorization.startdate, {
    'errorMessage': 'AuthorizationActionDate must be no earlier than the StartDate of the associated Authorization record'
}, true);'''

TABLE = 'UICAuthorizationAction'

GUID = Constant('Authorization Action Guid', 'GUID', 'AuthorizationAction.Guid', 'GUID()')

TYPE = Constraint('Authorization Action Type', 'AuthorizationAction.AuthorizationActionType', common.constrain_to_domain('AuthorizationActionType'))
TYPE.triggers = [config.triggers.insert, config.triggers.update]

ACTION_DATE = Constraint('Authorization Action Date', 'AuthorizationAction.AuthorizationActionDate', constrain_to_parent_start_date)
ACTION_DATE.triggers = [config.triggers.insert, config.triggers.update]
