def marshall_json_dict(dict_data):
    return {k: v.marshall_json() for k, v in dict_data.items() if v is not None}
