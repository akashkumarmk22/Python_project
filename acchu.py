def capitalize_lines():
    try:
        line = input("Enter the text: ")  # Prompt user for input
        capitalized_line = line.upper()  # Convert input to uppercase
        print(capitalized_line)  # Print the capitalized input
    except EOFError:
        print("Error: No input provided.")  # Handle EOFError
    except Exception as e:
        print(f"Error: {e}")  # Handle other exceptions

capitalize_lines()  # Call the function
