
import sys
import os
import site


def is_virtualenv():
    return sys.prefix != sys.base_prefix


def main():
    if is_virtualenv():
        print("Laboratory Status: The laboratory is sealed\n")
        print(f"Current Python: {sys.executable}")

        env_name = os.path.basename(sys.prefix)
        print(f"Virtual Environment: {env_name}")
        print(f"Environment Path: {sys.prefix}")

        print("\nSUCCESS: You are working in an isolated environment!")
        print("Safe to install reagents without affecting")
        print("the global system.")

        print("\nReagent installation path:")
        for path in site.getsitepackages():
            print(path)

        print(f"\nGlobal Python location: {sys.base_prefix}")

    else:
        print("Laboratory Status: You are working in the open")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected\n")

        print("WARNING: You are in the global environment!")
        print("Every reagent you install here leaks into the whole system.")

        print("\nGlobal package installation path:")
        for path in site.getsitepackages():
            print(path)

        print("\nTo seal the laboratory, run:")
        print("python3 -m venv lab_env")
        print("source lab_env/bin/activate # On Unix")
        print(r".\lab_env\Scripts\Activate.ps1 # On Windows PowerShell")

        print("\nThen run this program again.")


if __name__ == '__main__':
    main()
