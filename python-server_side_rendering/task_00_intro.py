#!/usr/bin/python3

import os

def generate_invitations(template, attendees):
    # Step 1: Input Type Validation
    if not isinstance(template, str):
        print("Error: Template should be a string.")
        return
    
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees should be a list of dictionaries.")
        return
    
    # Step 2: Empty Inputs Check
    if not template.strip():
        print("Error: Template is empty, no output files generated.")
        return
    
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    # Step 3: Process Each Attendee
    for index, attendee in enumerate(attendees, start=1):
        output_content = template
        
        for key, value in attendee.items():
            placeholder = f'{{{{ {key} }}}}'
            output_content = output_content.replace(placeholder, str(value))
        
        # Replace any remaining placeholders that were not found in the attendee's data
        output_content = output_content.replace("N/A")
        
        # Step 4: Generate Output Files
        output_filename = f'output_{index}.txt'
        
        try:
            # Check if file already exists
            if os.path.exists(output_filename):
                print(f"Warning: File {output_filename} already exists. Skipping.")
                continue
            
            # Write to file
            with open(output_filename, 'w') as f:
                f.write(output_content)
            print(f'Generated: {output_filename}')
        
        except Exception as e:
            print(f"Error occurred while writing {output_filename}: {str(e)}")
