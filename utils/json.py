def marshal_json_dict(dict_data):
    return {k: v.marshal_json() for k, v in dict_data.items() if v is not None}


def unmarshal_json_dict(dict_data, unmarshaler):
    return {k: unmarshaler(v) for k, v in dict_data.items()}
