from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .taskrouter_v1_workspace_task_queue_task_queues_statistics import (
    TaskrouterV1WorkspaceTaskQueueTaskQueuesStatistics,
    TaskrouterV1WorkspaceTaskQueueTaskQueuesStatisticsDict,
)


class ListTaskQueuesStatisticsResponse(SdkBaseModel):
    task_queues_statistics: Optional[list[TaskrouterV1WorkspaceTaskQueueTaskQueuesStatistics]] = UNSET
    meta: Optional[Meta] = UNSET


class ListTaskQueuesStatisticsResponseDict(TypedDict):
    task_queues_statistics: NotRequired[
        list[
            TaskrouterV1WorkspaceTaskQueueTaskQueuesStatistics | TaskrouterV1WorkspaceTaskQueueTaskQueuesStatisticsDict
        ]
    ]
    meta: NotRequired[Meta | MetaDict]
