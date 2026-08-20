def is_json_content_type(content_type: str | None) -> bool:
    if not content_type:
        return False

    essence = content_type.split(";", 1)[0].strip().lower()
    return essence == "application/json" or essence.endswith("+json")
