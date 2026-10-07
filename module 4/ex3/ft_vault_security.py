def secure_archive(file_name, action = None, data = None):
    try:
        if action == "r":
            with open(file_name, "r") as f:
                content = f.read()
            return True, content
        elif action == "w":
            with open(file_name, "w") as f:
                f.write(data)
            return True, "Content successfully written to file"

        return False, "invalid action"
    except OSError as e:
        return False, f"{e}"


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")
    print("Using 'secure archive' to read from a nonexistent file:")
    answer = secure_archive("nonexistent_file.txt", "r")
    print(answer)
    print("\nUsing 'secure archive' to read from an inaccessible file:")
    answer = secure_archive(".", "r")
    print(answer)
    print("\nUsing 'secure archive' to read from a regular file:")
    answer = secure_archive("xx", "r")
    print(answer)
    print("\nUsing 'secure archive' to write previous content to a new file:")
    answer = secure_archive("new_file.txt", "w", answer[1])
    print(answer)