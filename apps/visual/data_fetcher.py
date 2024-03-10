# apps/visual/data_fetcher.py

from apps.analyze.models import db, paddydenalysisResult
from apps.analyze.models import db, paddyPestAnalysisResult
from apps.analyze.models import db, TeaAnalysisResult
from apps.analyze.models import db, ADpaddydenalysisResult
from apps.analyze.models import db, ADvTeaAnalysisResult
from apps.analyze.models import db, ADpaddyPestAnalysisResult
def fetch_paddy_analysis_data():
    # Query the PaddyAnalysisResult entries
    results = paddydenalysisResult.query.order_by(paddydenalysisResult.date.desc()).limit(4).all()
    
    # Reverse the results to get them in ascending order by date
    results = list(reversed(results))    
    # Prepare the data for the chart # 
    # dates = [result.date.strftime("%Y-%m-%d") for result in results]
    dates = [f"Analyze {result.id}" for result in results]
    healthy_counts = [result.healthy_count for result in results]
    unhealthy_counts = [result.unhealthy_count for result in results]
    
    return dates, healthy_counts, unhealthy_counts

def fetch_paddy_pest_analysis_data():
    # Query the PaddyAnalysisResult entries
    results = paddyPestAnalysisResult.query.order_by(paddyPestAnalysisResult.date.desc()).limit(4).all()
    
    # Reverse the results to get them in ascending order by date
    results = list(reversed(results))    
    # Prepare the data for the chart # 
    # dates = [result.date.strftime("%Y-%m-%d") for result in results]
    dates = [f"Analyze {result.id}" for result in results]
    without_pest_count = [result.without_pest_count for result in results]
    with_pest_count = [result.with_pest_count for result in results]
    
    return dates, without_pest_count, with_pest_count

def fetch_tea_analysis_data():
    # Query the PaddyAnalysisResult entries
    results = TeaAnalysisResult.query.order_by(TeaAnalysisResult.date.desc()).limit(4).all()
    
    # Reverse the results to get them in ascending order by date
    results = list(reversed(results))    
    # Prepare the data for the chart # 
    # dates = [result.date.strftime("%Y-%m-%d") for result in results]
    dates = [f"Analyze {result.id}" for result in results]
    healthy_counts = [result.healthy_count for result in results]
    unhealthy_counts = [result.unhealthy_count for result in results]
    
    return dates, healthy_counts, unhealthy_counts

def paddy_advanve_pi_disease_data():
    # Fetch the last PaddyAnalysisResult entry
    last_result = ADpaddydenalysisResult.query.order_by(ADpaddydenalysisResult.date.desc()).first()

    # Prepare the data for the chart
    series_data = [last_result.bacterial_panicle_blight_count,last_result.dead_heart_count,last_result.brown_spot_count,last_result.bacterial_leaf_streak_count,last_result.blast_count,last_result.tungro_count,last_result.nispa_count,last_result.bacterial_leaf_high_count,last_result.downy_mildew_count,last_result.leaf_smut_count]
    labels = ['Bacterial Panicle Blight','Dead Heart','Brown Spot','Bacterial Leaf Streak','Blast','Tungro','Hispa','Bacterial leaf blight','Downy mildew','Leaf Smut']
     # Send the data as JSON
    return series_data, labels
def tea_advanve_pi_disease_data():
    # Fetch the last PaddyAnalysisResult entry
    last_result = ADvTeaAnalysisResult.query.order_by(ADvTeaAnalysisResult.date.desc()).first()

    # Prepare the data for the chart
    series_data = [last_result.bird_eye_spot_count,last_result.white_spot_count,last_result.Anthracnose_count,last_result.algal_leaf_count,last_result.gray_light_count,last_result.brown_blight_count,last_result.red_leaf_spot_count]
    labels = ['Bird eye spot_count','White spot','Anthracnose','Algal leaf','Gray light','Brown blight','Red leaf spot']
     # Send the data as JSON
    return series_data, labels
def paddy_pest_advanve_pi_disease_data():
    # Fetch the last ADpaddyPestAnalysisResult entry
    last_result = ADpaddyPestAnalysisResult.query.order_by(ADpaddyPestAnalysisResult.date.desc()).first()

    # Prepare the data for the chart
    series_data = [last_result.leaf_folders_count,last_result.whorl_maggots_count,last_result.rice_bugs_count,last_result.stem_borer_count,last_result.green_leafhoppers_count]
    labels = ['Leaf folders','Whorl maggots','Rice bugs','Stem borer','Green leafhoppers']
     # Send the data as JSON
    return series_data, labels

# apps/visual/data_fetcher.py

from apps.analyze.models import db, ADpaddyPestAnalysisResult
from datetime import datetime

def get_latest_pest_analysis():
    last_result = ADpaddyPestAnalysisResult.query.order_by(ADpaddyPestAnalysisResult.date.desc()).first()
    if last_result:
        return {
            'leaf_folders_count': last_result.leaf_folders_count,
            'whorl_maggots_count': last_result.whorl_maggots_count,
            'rice_bugs_count': last_result.rice_bugs_count,
            'stem_borer_count': last_result.stem_borer_count,
            'green_leafhoppers_count': last_result.green_leafhoppers_count,
            # Add other fields as necessary
        }
    return None

