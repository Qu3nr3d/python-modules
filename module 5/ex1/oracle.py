import os
from dotenv import load_dotenv


def get_config(name, default):
    value = os.getenv(name)

    if not value:
        print(f"[WARNING] Missing configuration: {name}")
        return default

    return value


if __name__ == "__main__":
    print("ORACLE STATUS: Consulting the configuration...")

    load_dotenv()

    mode = get_config("MATRIX_MODE", "development")

    if mode not in ("development", "production"):
        print("[WARNING] Invalid MATRIX_MODE")
        mode = "development"

    database = get_config("DATABASE_URL", "Not configured")
    api = get_config("API_KEY", "")
    log = get_config("LOG_LEVEL", "INFO")
    zion = get_config("ZION_ENDPOINT", "Not configured")

    print("\nConfiguration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: {database}")
    print(f"API Access: {'Configured' if api else 'Missing'}")
    print(f"Log Level: {log}")
    print(f"Remote Network: {zion}")

    if mode == "development":
        print("\nDevelopment: Detailed diagnostics enabled")
    else:
        print("\nProduction: Minimal diagnostics enabled")

    print("\nConfiguration security check:")
    print("[OK] API key is not exposed in output")
