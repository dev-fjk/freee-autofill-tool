import type { AxiosResponse } from "axios";
import { useState } from "react";

import type { LoginRequest, LoginResponse } from "../api/api";
import { AuthApi } from "../api/api";
import { Configuration } from "../api/configuration";

const config = new Configuration({
    basePath: "/api",
});

const api = new AuthApi(config);

export const useLogin = () => {
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);
    const [data, setData] = useState<LoginResponse | null>(null);

    const login = async (employee_id: string, password: string) => {
        setLoading(true);
        setError(null);

        const req: LoginRequest = {
            employee_id,
            password,
        };

        try {
            const response: AxiosResponse<LoginResponse> = await api.login(req);
            setData(response.data);
            return response.data;
        } catch (e: any) {
            setError(e.response?.data?.detail || e.message || "ログインに失敗しました");
            throw e;
        } finally {
            setLoading(false);
        }
    };

    return {
        loading,
        error,
        data,
        login,
    };
};
