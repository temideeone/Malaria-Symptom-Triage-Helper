def get_recommendation(severity):

    if severity == "Severe":
        return "Immediate hospital admission required."

    elif severity == "Moderate":
        return "Seek medical attention within 24 hours."

    else:
        return "Outpatient treatment and monitoring recommended."