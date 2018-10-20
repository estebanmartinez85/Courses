from enum import Enum


class CourseStatus(Enum):
    ASSIGN_WRITER = "Assign Writer"
    SCHEDULE_MEETING = "Schedule Meeting"
    STORYBOARD = "Storyboard"
    MANAGER_QUALITY_CHECK = "Manager Quality Check"
    MANAGER_QUALITY_REVISIONS = "Manager Quality Revisions"
    SME_REVIEW = "SME Review"
    SME_REVISIONS = "SME Revisions"
    FINAL_REVIEW = "Final Review"
    COMPLETE = "Complete"
