"""news-image-20261123 entry program.

Copies the finished front-page image (entry.png, authored in this
repository) to the grader's output directory. Standard library only,
no network, deterministic: both runs write the same bytes.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
IMAGE = "entry.png"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, IMAGE)
    dst = os.path.join(out_dir, IMAGE)
    shutil.copyfile(src, dst)


if __name__ == "__main__":
    main()
