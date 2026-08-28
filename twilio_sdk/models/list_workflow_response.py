from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .taskrouter_v1_workspace_workflow import TaskrouterV1WorkspaceWorkflow, TaskrouterV1WorkspaceWorkflowDict


class ListWorkflowResponse(SdkBaseModel):
    workflows: Optional[list[TaskrouterV1WorkspaceWorkflow]] = UNSET
    meta: Optional[Meta] = UNSET


class ListWorkflowResponseDict(TypedDict):
    workflows: NotRequired[list[TaskrouterV1WorkspaceWorkflow | TaskrouterV1WorkspaceWorkflowDict]]
    meta: NotRequired[Meta | MetaDict]
