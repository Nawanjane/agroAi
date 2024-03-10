from apps.analyze.models import db, paddyPestAnalysisResult  # Adjust the import path as needed

# Function to get the pest percentage
def get_pest_percentage():
    # Fetch the latest PaddyPestAnalysisResult entry
    latest_pest_result = paddyPestAnalysisResult.query.order_by(paddyPestAnalysisResult.date.desc()).first()

    if latest_pest_result:
        # Calculate the total and percentage of pest presence
        total_pest = latest_pest_result.without_pest_count + latest_pest_result.with_pest_count
        pest_percentage = (latest_pest_result.with_pest_count / total_pest) * 100 if total_pest > 0 else 0
    else:
        pest_percentage = 0

    # Return the pest percentage
    return pest_percentage