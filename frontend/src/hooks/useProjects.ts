import type { AxiosResponse } from "axios";
import { useEffect, useState } from "react";

import type { PaginatedResponseProjectRead, Pagination, ProjectRead } from "../api/api";
import { ProjectApi } from "../api/api";
import { Configuration } from "../api/configuration";

type UseProjectsParams = {
    projectId?: number;
    projectName?: string;
    pageNumber?: number;
    pageSize?: number;
};

const config = new Configuration({
    basePath: "/api",
});

const api = new ProjectApi(config);

/**
 * プロジェクト一覧を取得し、状態管理する
 */
export const useProjects = ({ projectId, projectName, pageNumber = 1, pageSize = 30 }: UseProjectsParams = {}) => {
    const [projects, setProjects] = useState<ProjectRead[]>([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);
    const [pagination, setPagination] = useState<Pagination | null>(null);

    useEffect(() => {
        setLoading(true);
        setError(null);

        api.getProjects(projectId, projectName, pageNumber, pageSize)
            .then((response: AxiosResponse<PaginatedResponseProjectRead>) => {
                const data = response.data;
                setProjects(data.items || []);
                setPagination(data.pagination || null);
            })
            .catch((e) => {
                setError(e.message || "プロジェクトの取得に失敗しました");
            })
            .finally(() => {
                setLoading(false);
            });
    }, [projectId, projectName, pageNumber, pageSize]);

    return {
        projects,
        loading,
        error,
        pagination,
    };
};
