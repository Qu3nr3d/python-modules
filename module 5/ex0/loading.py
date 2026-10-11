import importlib

def check_package(name):
    try:
        package = importlib.import_module(name)
        version = package.__version__
        print(f"[OK] {name} ({version})")
        return True
    except ImportError:
        print(f"[MISSING] {name} is not installed")
        return False

def main():
    print("REAGENT STATUS: Loading reagents...")
    print("\nChecking dependencies:\n")
    pandas_ok = check_package("pandas")
    numpy_ok = check_package("numpy")
    if not pandas_ok or not numpy_ok:
        print("\nSome reagents are missing!")
        print("\nInstall using pip:")
        print("\npython -m pip install -r requirements.txt")
        print("\nor install using poetry:")
        print("\npoetry install")
        print("\npoetry run python loading.py")
    else:
        print("\nAll reagents present and accounted for.")
    print("\npip vs poetry:")
    print("\nrequirements.txt declares what to instal; pip resolves it at install time.")
    print("pyproject.toml declares the same intent; Poetry pins the resolved")
    print("\nversions in poetry.lock so every install is identical.")

if __name__ == "__main__":
    main()