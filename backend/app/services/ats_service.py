REQUIRED_WEIGHT=80
PREFERRED_WEIGHT=20


from app.schemas.candidate_schema import CandidateSchema
from app.schemas.job_scehma import JobSchema

def flatten_candidate_skills(
        candidate:CandidateSchema
)->set[str]:
    all_skills=set()
    all_skills.update(
        skill.lower
        for skill in candidate.skills.languages #normalise once,lookup forever
    )
    all_skills.update(
        skill.lower()
        for skill in candidate.skills.frameworks
    )
    all_skills.update(
        skill.lower()
        for skill in candidate.skills.databases
    )
    all_skills.update(
        skill.lower()
        for skill in candidate.skills.cloud
    )
    all_skills.update(
        skill.lower()
        for skill in candidate.skills.devops
    )
    all_skills.update(
        skill.lower()
        for skill in candidate.skills.ai_ml
    )
    all_skills.update(
        skill.lower()
        for skill in candidate.skills.tools
    )
    all_skills.update(
        skill.lower()
        for skill in candidate.skills.other
    )
    return all_skills
    

def calculate_skill_score(
        candidate_skills:set[str],
        required_skills:list[str],
        allow_empty: bool=False
):
    normalized_required={
        skill.lower() for skill in required_skills
    }
    if len(normalized_required)==0:
        raise ValueError(
            "No Required Skills Found" #optimistic machine and depression machine
        )
    matched_skills=candidate_skills.intersection(

        normalized_required
    )
    missing_skills=normalized_required-candidate_skills
    score=(len(matched_skills)/len(normalized_required))*100
    return{
        "score":round(score,2),
        "matched_skills":list(matched_skills),
        "missing_skills":list(missing_skills)
    }
def calculate_ats_score(
        candidate:CandidateSchema,
        job:JobSchema
):
    candidate_skills=flatten_candidate_skills(
        candidate
    )
    required_result=calculate_skill_score(
        candidate_skills,
        job.required_skills
    )
    preferred_result=calculate_skill_score(
        candidate_skills,
        job.preferred_skills,
        allow_empty=True
    )
    if len(job.preferred_skills)>0:
        base_score=(
            required_result["score"]*[REQUIRED_WEIGHT/100]
        )
        bonus_score=(
            preferred_result["score"]*[PREFERRED_WEIGHT/100]
        )
        final_score=min(100,base_score+bonus_score)
    else:
        final_score=required_result["score"]

