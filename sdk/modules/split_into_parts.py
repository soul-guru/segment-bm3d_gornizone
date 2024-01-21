from sdk.modules.rephrase import rephrase


def split_into_parts(text: str, force: bool = False, skip_summary: bool = False) -> list[str]:
    if (len(text) > 12 or force) and not skip_summary:
        text = rephrase(text)
    
    if isinstance(text, list):
        splited_text = str(" ".join(text))
    else:
        splited_text = str(text)
    
    return splited_text.split(". ")
