def flatten_dict(d):
    def flatten_inner(subdict, prefix=''):
        items = []
        for key, value in subdict.items():
            new_key = f"{prefix}.{key}" if prefix else key
            if isinstance(value, dict):
                items.extend(flatten_inner(value, new_key))
            else:
                items.append((new_key, value))
        return items
    
    return dict(flatten_inner(d))
print(flatten_dict({'a': 1, 'b': {'i': 2, 'j': 3}, 'c': 4}))
# Output: {'a': 1, 'b.i': 2, 'b.j': 3, 'c': 4}