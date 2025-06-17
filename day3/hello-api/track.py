from fastapi import APIRouter, Header

router = APIRouter()

@router.post("/api/track")
def tracking_by_barcode(authorization: str | None = Header(None)):
    # TODO
    return {"message": f"Tracking item authorization: {authorization}"}