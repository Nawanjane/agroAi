from apps.analyze.models import db, TeaAnalysisResult  # Adjust the import path as needed

def get_card_data():
    # Fetch the required data from the database
    # Here we are fetching the latest analysis result
    latest_result = TeaAnalysisResult.query.order_by(TeaAnalysisResult.date.desc()).first()

    if latest_result:
        # Calculate the percentage (healthy / (healthy + unhealthy) * 100)
        total = latest_result.healthy_count + latest_result.unhealthy_count
        percentage = (latest_result.healthy_count / total) * 100 if total > 0 else 0
    else:
        percentage = 0

    # Return the data for the card
    return percentage