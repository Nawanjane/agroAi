# apps/analyze/models.py

from apps import db

class TeaAnalysisResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    user_name = db.Column(db.String(100), nullable=False)
    healthy_count = db.Column(db.Integer, nullable=False)
    unhealthy_count = db.Column(db.Integer, nullable=False)

class paddydenalysisResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    user_name = db.Column(db.String(100), nullable=False)
    healthy_count = db.Column(db.Integer, nullable=False)
    unhealthy_count = db.Column(db.Integer, nullable=False)
    
    
class paddyPestAnalysisResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    user_name = db.Column(db.String(100), nullable=False)
    with_pest_count = db.Column(db.Integer, nullable=False)
    without_pest_count = db.Column(db.Integer, nullable=False)

class ADpaddydenalysisResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    user_name = db.Column(db.String(100), nullable=True)
    bacterial_panicle_blight_count = db.Column(db.Integer, nullable=False, default=0)
    dead_heart_count = db.Column(db.Integer, nullable=False, default=0)
    brown_spot_count = db.Column(db.Integer, nullable=False, default=0)
    bacterial_leaf_streak_count = db.Column(db.Integer, nullable=False, default=0)
    blast_count = db.Column(db.Integer, nullable=False, default=0)
    tungro_count = db.Column(db.Integer, nullable=False, default=0)
    nispa_count = db.Column(db.Integer, nullable=False, default=0)
    bacterial_leaf_high_count = db.Column(db.Integer, nullable=False, default=0)
    downy_mildew_count = db.Column(db.Integer, nullable=False, default=0)
    leaf_smut_count = db.Column(db.Integer, nullable=False, default=0)

class ADpaddyPestAnalysisResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    user_name = db.Column(db.String(100), nullable=False)
    leaf_folders_count = db.Column(db.Integer, nullable=False, default=0)
    whorl_maggots_count = db.Column(db.Integer, nullable=False, default=0)
    rice_bugs_count = db.Column(db.Integer, nullable=False, default=0)
    stem_borer_count = db.Column(db.Integer, nullable=False, default=0)
    green_leafhoppers_count = db.Column(db.Integer, nullable=False, default=0)
    
class ADvTeaAnalysisResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    user_name = db.Column(db.String(100), nullable=False)
    bird_eye_spot_count = db.Column(db.Integer, nullable=False, default=0)
    white_spot_count = db.Column(db.Integer, nullable=False, default=0)
    Anthracnose_count = db.Column(db.Integer, nullable=False, default=0)
    algal_leaf_count = db.Column(db.Integer, nullable=False, default=0)
    gray_light_count = db.Column(db.Integer, nullable=False, default=0)
    brown_blight_count = db.Column(db.Integer, nullable=False, default=0)
    red_leaf_spot_count = db.Column(db.Integer, nullable=False, default=0)
