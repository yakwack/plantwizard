import json
import os

def split_json_file(input_filename='plants.json', output_dir='plants'):
    """
    Reads a single JSON file containing an array of plant objects and
    writes each object to a separate JSON file.

    Args:
        input_filename (str): The path to the input JSON file.
        output_dir (str): The directory where the new JSON files will be created.
    """
    try:
        # Open and read the JSON file
        with open(input_filename, 'r') as f:
            plants_data = json.load(f)

        # Ensure the output directory exists
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Check if the loaded data is a list of plants. If not, wrap it in a list.
        if not isinstance(plants_data, list):
            plants_data = [plants_data]

        # Iterate through each plant object in the list
        for plant in plants_data:
            # Get the plant's ID to use as the filename
            plant_id = plant.get('id')
            if not plant_id:
                print("Warning: Found a plant without an 'id' field. Skipping this entry.")
                continue

            # Create the output filename
            output_filename = os.path.join(output_dir, f"{plant_id}.json")

            # Check if an 'image' field exists and create its directory
            image_path = plant.get('image')
            if image_path:
                image_dir = os.path.dirname(image_path)
                if image_dir and not os.path.exists(image_dir):
                    print(f"Creating directory for image: '{image_dir}'")
                    os.makedirs(image_dir)

            # Write the individual plant object to a new file
            with open(output_filename, 'w') as out_f:
                json.dump(plant, out_f, indent=2)
                print(f"Successfully created '{output_filename}'")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except json.JSONDecodeError:
        print(f"Error: The file '{input_filename}' is not a valid JSON file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage: Run the function
if __name__ == "__main__":
    # Assuming your master file is called 'plants.json'
    split_json_file(input_filename='plants.json')
