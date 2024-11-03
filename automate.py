import json
import os

# Path to your exercises JSON file
json_file_path = './dist/exercises.json'  # Update this path to your JSON file

# Mapping of specific muscle groups to generalized muscle groups and their secondary muscles
muscle_mapping = {
    'lower back': ('Back', 'Lower Back'),
    'middle back': ('Back', 'Middle Back'),
    'lats': ('Back', 'Lats'),
    'traps': ('Back', 'Traps'),
    'quadriceps': ('Legs', 'Hamstrings'),
    'hamstrings': ('Legs', 'Hamstrings'),
    'calves': ('Legs', 'Calves'),
    'glutes': ('Legs', 'Glutes'),
    'adductors': ('Legs', 'Adductors'),
    'abductors': ('Legs', 'Abductors'),
    'chest': ('Chest', 'Shoulders'),
    'shoulders': ('Chest', 'Shoulders'),
    'biceps': ('Arms', 'Triceps'),
    'triceps': ('Arms', 'Triceps'),
    'forearms': ('Arms', 'Forearms'),
    'abdominals': ('Core', 'Obliques'),  # Optional secondary muscle
    'obliques': ('Core', 'Obliques'),     # Optional secondary muscle
    'neck': ('Neck', None)                 # No secondary muscle
}

# Read the JSON file
with open(json_file_path, 'r') as file:
    exercises = json.load(file)

# Update primaryMuscles and secondaryMuscles
for exercise in exercises:
    original_primary_muscles = exercise.get('primaryMuscles', [])
    
    # Create a new list for primary muscles and secondary muscles
    new_primary_muscles = []
    new_secondary_muscles = []

    for muscle in original_primary_muscles:
        if muscle in muscle_mapping:
            # Get the generalized primary and secondary muscles
            generalized_primary, secondary = muscle_mapping[muscle]
            new_primary_muscles.append(generalized_primary)
            if secondary and secondary not in new_secondary_muscles:
                new_secondary_muscles.append(secondary)
        else:
            # If no mapping is found, keep the original muscle
            new_primary_muscles.append(muscle)

    # Update the exercise with new values
    exercise['primaryMuscles'] = list(set(new_primary_muscles))  # Remove duplicates
    exercise['secondaryMuscles'] = list(set(new_secondary_muscles))  # Remove duplicates

# Write the updated data back to the JSON file
with open(json_file_path, 'w') as file:
    json.dump(exercises, file, indent=4)

print("Muscle groups updated successfully.")