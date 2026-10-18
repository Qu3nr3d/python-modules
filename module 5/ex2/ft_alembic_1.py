import alchemy

print("== Alembic 1 ==")
print("Accessing the alchemy module using import alchemy")
print(f"Testing create_air: {alchemy.create_air()}")
print("Now show that earth is not accessible...")
print("This will raise an exception:")
print(alchemy.create_earth())