from enum import Enum

# Prefixes for routes i.e /users, /budgets, etc.
class RoutePrefixes(Enum):
    dummy = '/dummy'
    users = '/users'
    budgets = '/budgets'
    transactions = '/transactions'
    categories = '/categories'
    accounts = '/accounts'
    tags = '/tags'
    goals = '/goals'
    reports = '/reports'
    settings = '/settings'
    auth = '/auth'