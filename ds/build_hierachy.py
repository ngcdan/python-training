import json

def build_hierarchy(elements, parent_id=None):
    hierarchy = []
    for element in elements:
        if element.get('parent_id') == parent_id:
            children = build_hierarchy(elements, element['id'])
            if children:
                element['children'] = children
            hierarchy.append(element)
    return hierarchy

# Example list of elements with parent_id
elements = [
    {'id': 1, 'name': 'Element 1', 'parent_id': None},
    {'id': 2, 'name': 'Element 2', 'parent_id': 1},
    {'id': 3, 'name': 'Element 3', 'parent_id': 1},
    {'id': 4, 'name': 'Element 4', 'parent_id': 2},
    {'id': 5, 'name': 'Element 5', 'parent_id': None},
    {'id': 6, 'name': 'Element 6', 'parent_id': 5},
]

hierarchy_tree = build_hierarchy(elements)
print(json.dumps(hierarchy_tree, indent=4))
