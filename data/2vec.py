DIM = 100
if __name__ == "__main__":
    import sys
    filename = sys.argv[1]
    with open(filename) as f:
        lines = f.readlines()
    lines = [" ".join(l.split()[-100:]) for l in lines]
    with open(filename+".vec", "w") as f:
        for l in lines:
            f.write(l)
            f.write("\n")
