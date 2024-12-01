def charlson_comorbidity_idx(age, comorbidities):
    points = 0

    if age >= 50 and age < 60:
        points += 1
    elif age >= 60 and age < 70:
        points += 2
    elif age >= 70 and age < 80:
        points += 3
    elif age >= 80:
        points += 4

    if comorbidities['myocardial_infarction']:
        points += 1
    
    if comorbidities['congestive_heart_failure']:
        points += 1
    
    if comorbidities['peripheral_vascular_disease']:
        points += 1
    
    if comorbidities['cerebrovascular_disease']:
        points += 1

    if comorbidities['dementia']:
        points += 1

    if comorbidities['copd']:
        points += 1

    if comorbidities['connective_tissue_disease']:
        points += 1

    if comorbidities['peptic_ulcer_disease']:
        points += 1
    
    if comorbidities['uncomplicated_diabetes_mellitus']:
        points += 1
    
    if comorbidities['diabetes_mellitus_with_end_organ_damage']:
        points += 2
    
    if comorbidities['chronic_kidney_disease']:
        points += 2
    
    if comorbidities['hemiplegia_from_stroke']:
        points += 2

    if comorbidities['leukemia']:
        points += 2
    
    if comorbidities['malignant_lymphoma']:
        points += 2

    if comorbidities['localized_solid_tumor']:
        points += 2
    
    if comorbidities['metastatic_solid_tumor']:
        points += 6
    
    if comorbidities['mild_liver_disease']:
        points += 1

    if comorbidities['moderate_to_severe_liver_disease']:
        points += 3
    
    if comorbidities['aids']:
        points += 6
    
    return points