import { useEffect, useState } from "react";

import type { PaginatedResponseProjectRead, ProjectRead } from "../api/api";
import { ProjectApi } from "../api/api";

type UseProjectsParams = {
    projectId?: number;
    projectName?: string;
    pageNumber?: number;
    pageSize?: number;
};

export const useProjects = ({ projectId, projectName, pageNumber = 1, pageSize = 30 }: UseProjectsParams = {}) => {
    const [projects, setProjects] = useState<ProjectRead[]>([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);
    const [totalCount, setTotalCount] = useState<number>(0);

    useEffect(() => {
        setLoading(true);
        setError(null);

        getProjects({
            projectId,
            projectName,
            pageNumber,
            pageSize,
        })
            .then((response: PaginatedResponse<ProjectRead>) => {
                setProjects(response.items || []);
                setTotalCount(response.total || 0);
            })
            .catch((e) => {
                setError(e.message || "プロジェクトの取得に失敗しました");
            })
            .finally(() => {
                setLoading(false);
            });
    }, [projectId, projectName, pageNumber, pageSize]);

    return { projects, loading, error, totalCount };
};
