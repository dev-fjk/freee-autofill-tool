import type { AxiosResponse } from "axios";
import { useEffect, useState } from "react";

import type { PaginatedResponseProjectRead, Pagination, ProjectRead } from "../api/api";
import { ProjectApi } from "../api/api";
import { Configuration } from "../api/configuration";
import { getUserInfo } from "../utils/auth";

type UseProjectsParams = {
    projectId?: number;
    projectName?: string;
    pageNumber?: number;
    pageSize?: number;
};

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

        const { employeeId, role } = getUserInfo();
        const config = new Configuration({
            basePath: "/api",
            baseOptions: {
                headers: {
                    "x-employee-id": employeeId ?? "",
                    "x-role": role ?? "",
                },
            },
        });
        const api = new ProjectApi(config);

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
