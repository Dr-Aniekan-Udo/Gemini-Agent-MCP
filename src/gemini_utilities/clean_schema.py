
def clean_schema(schema):
    """recursively remove title fields from the JSON schema

    Args:
        schema (dict): The schema dictonary
    Returns:
        dict: cleaned schema without  "title" fields
    """

    if isinstance(schema, dict):
        # remove title if present
        schema.pop("title", None)
        # recursively clean nested properties
        if "properties" in schema and isinstance(schema["properties"], dict):
            for key in schema["properties"]:
                schema["properties"][key] = clean_schema(schema["properties"][key])
    return schema


example_schema = {
    "title": "Example Schema",
    "properties": {
        "field1": {
            "title": "Field 1 Title",
            "type": "string"
        },
        "field2": {
            "properties": {
                "nested_field": {
                    "title": "Nested Field Title",
                    "type": "integer"
                }
            }
        }
    }
}


if __name__ == "__main__":
    print(clean_schema(example_schema))
