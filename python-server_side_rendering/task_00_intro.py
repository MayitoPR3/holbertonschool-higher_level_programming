import os

def generate_invitations(template, attendees):
    # Check if template is a string and attendees is a list of dictionaries
    if not isinstance(template, str):
        print("Error: Template should be a string.")
        return
    
    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print("Error: Attendees should be a list of dictionaries.")
        return
    
    # Check for empty template
    if not template.strip():
        print("Error: Template is empty, no output files generated.")
        return
    
    # Check for empty attendees list
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        output_filename = f"output_{index}.txt"
        
        # Replace placeholders with values from attendee's dictionary
        invitation_text = template.format(
            name=attendee.get('name', 'N/A'),
            event_title=attendee.get('event_title', 'N/A'),
            event_date=attendee.get('event_date', 'N/A'),
            event_location=attendee.get('event_location', 'N/A')
        )
        
        # Write to file
        try:
            with open(output_filename, 'w') as file:
                file.write(invitation_text)
            print(f"File '{output_filename}' generated successfully.")
        except IOError as e:
            print(f"Error writing to file '{output_filename}': {e}")