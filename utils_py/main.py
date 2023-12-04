def read_file(path):
    with open(f"../{path}", "r") as f:
        return f.read().split("\n")
