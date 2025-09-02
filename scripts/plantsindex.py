import json
import os

# Creates a plants-index.json file from individual plant files in the plants/ directory
def create_plant_index(input_dir='../plants', output_filename='../plants-index.json'):
    """
    Reads individual plant JSON files from a directory and compiles them
    into a single, structured index file.

    Args:
        input_dir (str): The directory containing the individual plant JSON files.
        output_filename (str): The name of the output index file.
    """
    plant_index = []

    try:
        # Check if the input directory exists
        if not os.path.exists(input_dir):
            print(f"Error: The directory '{input_dir}' was not found.")
            return

        # Iterate over each file in the specified directory
        for filename in os.listdir(input_dir):
            if filename.endswith('.json'):
                filepath = os.path.join(input_dir, filename)
                with open(filepath, 'r') as f:
                    plant_data = json.load(f)

                # Extract required information and create a thumbnail path
                plant_id = plant_data.get('id')
                scientific_name = plant_data.get('scientificName')
                common_names = plant_data.get('commonNames')

                # Use the first image from the gallery as the thumbnail
                thumbnail = plant_data.get('gallery', ["images/placeholder.jpg"])[0]

                # Get the tags directly from the plant data
                tags = plant_data.get('tags', [])

                # Create the index entry
                index_entry = {
                    "id": plant_id,
                    "scientificName": scientific_name,
                    "commonNames": common_names,
                    "thumbnail": thumbnail,
                    "tags": tags
                }
                plant_index.append(index_entry)

        # Write the final index to the output file
        with open(output_filename, 'w') as out_f:
            json.dump(plant_index, out_f, indent=2)
            print(f"Successfully created '{output_filename}' with {len(plant_index)} plants.")

    except json.JSONDecodeError:
        print(f"Error: A file in '{input_dir}' is not a valid JSON file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function to create the index
if __name__ == "__main__":
    create_plant_index()
