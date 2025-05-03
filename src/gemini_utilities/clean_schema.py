
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


def tool_schema_handler(schema):
    """Recursively clean the schema by removing 'title' fields
    and sanitizing file-like parameters to avoid Gemini file inference.

    Args:
        schema (dict): The schema dictionary.

    Returns:
        dict: Cleaned schema without 'title' fields and unnecessary 'format' keys.
    """

    if isinstance(schema, dict):
        # Remove 'title' if present
        schema.pop("title", None)

        # Remove or sanitize suspicious 'format' fields
        if schema.get("type") == "string" and schema.get("format") in ["uri", "binary"]:
            schema.pop("format")

        # Rename keys like 'file', 'document', etc., if needed
        # (optional: rename keys in 'properties' dict if desired)

        # Recursively clean nested 'properties'
        if "properties" in schema and isinstance(schema["properties"], dict):
            cleaned_properties = {}
            for key, value in schema["properties"].items():
                cleaned_properties[key] = clean_schema(value)
            schema["properties"] = cleaned_properties

        # Also clean items in case of array-type schemas
        if "items" in schema:
            schema["items"] = clean_schema(schema["items"])

    elif isinstance(schema, list):
        return [clean_schema(item) for item in schema]

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
