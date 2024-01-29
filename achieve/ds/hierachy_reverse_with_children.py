import json

def build_hierarchy_reverse_with_children(elements, start_element):
    hierarchy = []

    # Find the start_element in the elements list
    current_element = None
    for element in elements:
        if element['id'] == start_element['id']:
            current_element = element
            break

    # Traverse from the current element to the root
    while current_element:
        hierarchy.insert(0, current_element)
        parent_id = current_element.get('parent_id')
        if parent_id is None:
            break
        current_element = next((element for element in elements if element['id'] == parent_id), None)

    # Build children for each parent
    for idx, parent in enumerate(hierarchy):
        children = []
        parent_id = parent['id']
        for element in elements:
            if element.get('parent_id') == parent_id:
                children.append(element)
        hierarchy[idx]['children'] = children

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

start_element = {'id': 4, 'name': 'Element 4', 'parent_id': 2}

hierarchy_tree = build_hierarchy_reverse_with_children(elements, start_element)
print(json.dumps(hierarchy_tree, indent=2))
