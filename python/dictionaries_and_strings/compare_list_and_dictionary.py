
code_snippets = {
    "dictionary_value": {

        "code": " numbers = {}\n numbers[0] = -5\n numbers[1] = 10.5", 

        "explanation": "This code works because numbers is first assigned as a dictionary, so you can input keys without having to append or redefine anything."
    },
    "list_value": {
        "code": " other_numbers = []\n other_numbers[0] = -5\n other_numbers[1] = 10.5",

        "explanation": "This code does not work because other_numbers is assigned as a string, and you cannot input values into lists using keys.",

        "fixed": " other_numbers =  []\n other_numbers.append(-5)\n other_numbers.append(10.5)"
    }

    }

if __name__ == "__main__":

    for key, info in code_snippets.items():

        print(f'\nCode Snippet:')
    
        print(info["code"])

        print("\nExplanation:")

        print(info["explanation"])

        if "fixed" in info:
            print("\nFixed code:")
            
            print(info["fixed"])