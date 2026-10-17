import os
import dotenv


if __name__ == "__main__":
    print("ORACLE STATUS: Consulting the configuration...")
    dotenv.load_dotenv()
    mode = os.getenv("MATRIX_MODE", "production")
    database = os.getenv("DATABASE_URL")
    api = os.getenv("API_KEY")
    log = os.getenv("LOG_LEVEL")
    zion = os.getenv("ZION_ENDPOINT")
    print(f"\nMode: {mode}")
    print(f"\nDatabase: {database}")
    print(f"\nApiAccess: {'Configured' if api else 'Missing'}")
    print(f"\nLog Level: {log}")
    print(f"\nRemote Network: {zion}")