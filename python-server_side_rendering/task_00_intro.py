import os

def generate_invitations(template, attendees):
    # Check input types
    if not isinstance(template, str):
        print("Error: Template is not a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print("Error: Attendees should be a list of dictionaries.")
        return
    
    # Check for empty inputs
    if not template:
        print("Error: Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    # Process each attendee
    for i, attendee in enumerate(attendees, start=1):
        output = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key, "N/A")
            output = output.replace(f"{{{{ {key} }}}}", value if value else "N/A")
        
        # Write to file
        output_filename = f"output_{i}.txt"
        with open(output_filename, 'w') as f:
            f.write(output)
        print(f"Generated {output_filename}")
