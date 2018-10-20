from enum import Enum


class StoryboardStatus(Enum):
    NONE = "None"
    WRITING = "Writing"
    PEER_REVIEW = "Peer Review"
    LMS_INSERT = "LMS Insertion"
    ASSIGN = "Assigning"
    MEETINGS = "Meetings"
    CREATING = "Creating"
    SME_SB_REVIEW = "SME Storyboard Review"
    SME_SB_REVISIONS = "SME Storyboard Revision"
    MANAGER_REVISIONS = "Manager Revisions"
    SME_COURSE_REVIEW = "SME Course Review"
    FINAL_REVISIONS = "Final Review"
    COMPLETE = "Completed"


class NarrationStatus(Enum):
    NONE = "None"
    ORDERED = "Ordered"
    RECEIVED = "Received"
    CHECKING = "Checking"
    REVISIONS = "Revisions"
    COMPLETE = "Complete"


class GraphicStatus(Enum):
    NONE = "None"
    PRE_GRAPHICS = "Pre Graphics"
    CREATING = "Creating"
    PEER_REVIEW = "Peer Review"
    PEER_REVISIONS = "Peer Revisions"
    WRITER_CHECK = "Writer Check"
    WRITER_REVISIONS = "Writer Revisions"
    COMPLETE = "Complete"


class RevisionCategory(Enum):
    STORYBOARD = "Storyboard"
    NARRATION = "Narration"
    GRAPHICS = "Graphics"


class RevisionType(Enum):
    PEER = "Peer"
    WRITER = "Writer"
    MANAGER = "Manager"
    SME = "SME"
    FINAL = "Final"


class UploadType(Enum):
    FILE = "File"
    DIRECTORY = "Directory"


class ScreenType(Enum):
    CONTENT = "Content"
    QUESTION = "Question"
