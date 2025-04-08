def modify_file():
  """Reads a file, modifies its contents, and writes the modified version to a new file."""

  filename = input("readMod.txt")

  try:
    with open(filename, "r") as file:
      content = file.read()

    # Modify the content (replace 'hello' with 'goodbye')
    modified_content = content.replace("hello", "goodbye")

    # Create a new file with a modified name (appending '_modified' to the original name)
    new_filename = filename + "_modified"
    with open(new_filename, "w") as new_file:
      new_file.write(modified_content)

    print(f"File '{filename}' modified and saved as '{new_filename}'.")

  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
  except PermissionError:
    print(f"Error: Permission denied to read or write file '{filename}'.")
  except Exception as e:
    print(f"An error occurred: {e}")

# Call the function to start the process
modify_file()
