import type { AxiosResponse } from "axios";
import { useEffect, useState } from "react";

import type { PaginatedResponseProjectRead, ProjectRead } from "../api/api";
import { ProjectApi } from "../api/api";

type UseProjectsParams = {
    projectId?: number;
    projectName?: string;
    pageNumber?: number;
    pageSize?: number;
};

const api = new ProjectApi();

/**
 * プロジェクト一覧を取得し、状態管理する
 *
 * @param {UseProjectsParams} params - 検索条件とページング設定
 * @param {number} [params.projectId] - プロジェクトIDで絞り込み（任意）
 * @param {string} [params.projectName] - プロジェクト名で絞り込み（任意）
 * @param {number} [params.pageNumber=1] - ページ番号（デフォルト1）
 * @param {number} [params.pageSize=30] - 1ページあたりの件数（デフォルト30）
 *
 * @returns {{
 *   projects: ProjectRead[],
 *   loading: boolean,
 *   error: string | null,
 *   totalCount: number
 * }}
 */
export const useProjects = ({ projectId, projectName, pageNumber = 1, pageSize = 30 }: UseProjectsParams = {}) => {
    const [projects, setProjects] = useState<ProjectRead[]>([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);
    const [totalCount, setTotalCount] = useState<number>(0);

    useEffect(() => {
        setLoading(true);
        setError(null);

        api.getProjects(projectId, projectName, pageNumber, pageSize)
            .then((response: AxiosResponse<PaginatedResponseProjectRead>) => {
                const data = response.data;
                setProjects(data.items || []);
                setTotalCount(data.pagination?.total || 0);
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
