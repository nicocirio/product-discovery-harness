"""Record source labels and lifecycle transition rules."""
from __future__ import annotations

SOURCES = {"observed", "user_reported", "inferred", "proposed", "decided"}
STATES = {"raw", "exploring", "candidate", "accepted", "rejected", "deferred", "superseded"}
TRANSITIONS = {"raw": {"exploring"}, "exploring": {"candidate"}, "candidate": {"accepted", "rejected", "deferred"}, "accepted": {"superseded"}, "deferred": {"exploring"}, "rejected": {"exploring"}, "superseded": set()}

def validate_record(record: dict) -> list[str]:
    errors=[]
    if record.get("source") not in SOURCES: errors.append("source must be an allowed evidence label")
    if record.get("status") not in STATES: errors.append("status must be an allowed lifecycle state")
    if record.get("status") == "accepted" and not record.get("accepted_by"): errors.append("accepted record requires accepted_by metadata")
    return errors

def transition(record: dict, status: str, accepted_by: str | None = None) -> dict:
    current = record.get("status", "raw")
    if status not in TRANSITIONS.get(current, set()): raise ValueError(f"invalid lifecycle transition: {current} -> {status}")
    if status == "accepted" and not accepted_by: raise ValueError("acceptance requires explicit accepted_by")
    updated = dict(record, status=status)
    if accepted_by: updated["accepted_by"] = accepted_by
    return updated
