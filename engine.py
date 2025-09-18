'''
engine.py
---------
This module executes query plans expressed as dictionaries.
Each query plan dictionary must contain:
    - "operation": type of operation ("select", "project", etc.)
    - "relation": either a Relation, a relation name (string), or another query plan (nested dict)
    - Extra keys depending on operation:
        * "condition" (for select)
        * "columns" (for project)

Example:
query_plan = {
    "operation": "project",
    "columns": ["Name"],
    "relation": {
        "operation": "select",
        "condition": lambda r: r["Age"] > 30,
        "relation": "Employees"
    }
}
'''

from operations import select, project
from data_structures import Relation

def execute_query(query_plan, relations_dict):
    # Base case: if already a Relation, return it
    if isinstance(query_plan, Relation):
        return query_plan
    
    # Base case: if it's a string, look up relation by name
    if isinstance(query_plan, str):
        return relations_dict[query_plan]
    
    # Otherwise, it must be a dictionary representing an operation
    operation = query_plan['operation']
    
    if operation == 'select':
        relation = execute_query(query_plan['relation'], relations_dict)
        condition = query_plan['condition']
        return select(relation, condition)
    
    elif operation == 'project':
        relation = execute_query(query_plan['relation'], relations_dict)
        columns = query_plan['columns']
        return project(relation, columns)
    
    else:
        raise ValueError(f"Unknown operation: {operation}")
