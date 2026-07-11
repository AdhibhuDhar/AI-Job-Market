from app.schemas.candidate_schema import CandidateSchema

def flatten_candidate_skills(
        candidate:CandidateSchema
)->set[str]:
    all_skills=set()
    all_skills.update(
        skill.lower
        for skill in candidate.skills.languages #normalise once,lookup forever
    )
    all_skills.update(
        skill.lower
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
        candidate_skills:list[str],
        required_skills:list[str]
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

