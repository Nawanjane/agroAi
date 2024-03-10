from apps.analyze.models import db, paddydenalysisResult  # Adjust the import path as needed

def get_healthy_paddy_percentage():
    # Fetch the latest PaddyAnalysisResult entry or use aggregate functions as needed
    latest_result = paddydenalysisResult.query.order_by(paddydenalysisResult.date.desc()).first()

    if latest_result:
        # Calculate the percentage (healthy / (healthy + unhealthy) * 100)
        total = latest_result.healthy_count + latest_result.unhealthy_count
        healthy_paddy_pre = (latest_result.healthy_count / total) * 100 if total > 0 else 0
    else:
        healthy_paddy_pre = 0

    # Return the percentage for the card
    return healthy_paddy_pre