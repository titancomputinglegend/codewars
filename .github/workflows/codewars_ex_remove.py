def parse_float(string):
    out=0

    try:
        out=float(string)

    except:
        ValueError
        out=string
    return(out)
parse_float("a")