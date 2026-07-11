from fastapi import APIRouter,UploadFile,File #uploadfile acts as a temporary file,exposes metadeta,efficient data streaming
from app.services.pdf_service import extract_text_from_pdf
from app.services.llm_service import generate_candidate_profile
router=APIRouter()

@router.post("/upload")
async def upload_resume(
    file:UploadFile=File(...)
):
    contents=await file.read() #bad for large files,as it reads entire file into mem
    file_path=f"uploads/{file.filename}"
    with open(
        file_path,
        "wb" #wb means write binary,as pdf is binary file
    ) as f:
        f.write(contents)
    text = extract_text_from_pdf(file_path)

    candidate_profile=generate_candidate_profile(
        text
    )
    return candidate_profile