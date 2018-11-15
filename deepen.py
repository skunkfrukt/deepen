def deepen(collection):
    if isinstance(collection, (tuple, list)):
        new_collection = []
        for item in enumerate(collection):
            if isinstance(item, (tuple, list, dict)):
                new_collection.append(deepen(item))
            else:
                new_collection.append(item)
        if isinstance(collection, tuple):
            new_collection = tuple(new_collection)
    elif isinstance(collection, dict):
        new_collection = {}
        for key, value in collection.items():
            if "." in key:
                context = new_collection
                key_parts = key.strip(".").split(".")
                for subkey in key_parts:
                    if not subkey in context:
                        context[subkey] = {}
                    if isinstance(context[subkey], dict):
                        context = context[subkey]
                    else:
                        raise Exception(
                            f"Cannot deepen; key '{key}' would cause a conflict."
                        )
                context[key_parts[-1]] = value
            else:
                new_collection[key] = value
    return new_collection
