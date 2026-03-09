from datetime import datetime

def generate_report(sector, analysis):

    report = f"""
# Trade Opportunity Report

## Sector
{sector}

## Generated On
{datetime.now()}

## Market Analysis
{analysis}

## Conclusion
This report highlights current trade opportunities and market insights
for the {sector} sector in India.
"""

    return report