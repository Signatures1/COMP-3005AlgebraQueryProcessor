'''
'''

from data_structures import Relation

def select(relation, condition):
    new_rows = []
    for row in relation.rows:
        if condition(row):
            new_rows.append(row.copy())

    return Relation(
        name = relation.name + "_select",
        attributes = relation.attributes,
        rows = new_rows
    )

def project(relation, columns):
    new_rows = []
    for row in relation.rows:
        new_row = {col: row[col] for col in columns if col in row}
        new_rows.append(new_row)

    return Relation(
        name = relation.name + "_project",
        attributes = columns,
        rows = new_rows
    )