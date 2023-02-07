def get_labels(filepath: str):
    with open(filepath, 'r') as file:
        labels = file.readlines()
    labels_dict = {i: label.strip() for (i, label) in enumerate(labels)}

    return labels_dict
