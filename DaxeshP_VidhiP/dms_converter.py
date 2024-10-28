def dms2dd(dms_record):
    try:
        # Split the DMS into its components
        parts = dms_record.split()
        degrees = float(parts[0])
        minutes = float(parts[1])
        seconds = float(parts[2])
        direction = parts[3]

        # Validate the ranges
        if direction in ['N', 'S']:
            if not (0 <= degrees <= 90):
                return None, None
        elif direction in ['E', 'W']:
            if not (0 <= degrees <= 180):
                return None, None
        else:
            return None, None  # Invalid direction

        if not (0 <= minutes < 60) or not (0 <= seconds < 60):
            return None, None

        # Convert DMS to decimal degrees
        decimal_degrees = degrees + (minutes / 60) + (seconds / 3600)

        # Apply the direction
        if direction in ['W', 'S']:
            decimal_degrees = -decimal_degrees

        # Return the results
        if direction in ['N', 'S']:
            return None, decimal_degrees  # Latitude
        elif direction in ['E', 'W']:
            return decimal_degrees, None  # Longitude
    except (ValueError, IndexError):
        return None, None  # Invalid input format

