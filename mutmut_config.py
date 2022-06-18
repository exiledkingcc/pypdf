def pre_mutation(context):
    if context.filename in ["_adobe_glyphs.py"]:
        context.skip = True

    line = context.current_source_line.strip()
    if "# pragma: no cover" in line:
        context.skip = True
