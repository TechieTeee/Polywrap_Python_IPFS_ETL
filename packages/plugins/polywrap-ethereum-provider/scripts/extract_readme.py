import os
import subprocess
import polywrap_ethereum_provider


def extract_readme():
    headline = polywrap_ethereum_provider.__name__.replace("_", " ").title()
    header = headline + "\n" + "=" * len(headline)
    docstring = polywrap_ethereum_provider.__doc__
    return header + "\n" + docstring


def run_tests():
    run_doctest = os.path.join(os.path.dirname(__file__), "run_doctest.py")
    subprocess.check_call(["python", run_doctest])


if __name__ == "__main__":
    # Make sure that the doctests are passing before we extract the README.
    run_tests()

    # Extract the README.
    readme = extract_readme()

    # Write the README to the file.
    with open("README.rst", "w") as f:
        f.write(readme)
