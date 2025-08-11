import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { Box, Button, FormControl, FormLabel, Input, Heading, Text, VStack } from "@chakra-ui/react";
import { useLogin } from "../hooks/useLogin";
import { isLoggedIn } from "../utils/auth";
import { STORAGE_KEYS } from "../constants/storageKeys";

function LoginPage({ onLogin }: { onLogin: () => void }) {
    const [employeeId, setEmployeeId] = useState("");
    const [password, setPassword] = useState("");
    const { loading, login } = useLogin();
    const [error, setError] = useState<string | null>(null);
    const navigate = useNavigate();

    // ログイン済みならプロジェクト一覧ページへリダイレクト
    useEffect(() => {
        if (isLoggedIn()) {
            navigate("/projects");
        }
    }, [navigate]);

    // 社員IDバリデーション関数
    const validateEmployeeId = (id: string): boolean => {
        return /^e\d{0,6}$/.test(id); // 入力途中も許容（数字0桁もOKにしてる）
    };

    // 社員ID変更時にリアルタイムチェック＆エラー表示
    const handleEmployeeIdChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const val = e.target.value;
        if (validateEmployeeId(val)) {
            setError(null); // 問題なければエラー消す
        } else {
            setError("社員IDは「e」から始まり、その後に最大6桁の数字で入力してください。");
        }
        setEmployeeId(val);
    };

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();

        // 最終チェック（数字1～6桁必須にする）
        if (!/^e\d{1,6}$/.test(employeeId)) {
            setError("社員IDは「e」から始まり、その後に最大6桁の数字で入力してください。");
            return;
        }

        if (!password) {
            setError("パスワードを入力してください。");
            return;
        }

        try {
            setError(null);
            const data = await login(employeeId, password);
            localStorage.setItem(STORAGE_KEYS.EMPLOYEE_ID, data.employee_id);
            localStorage.setItem(STORAGE_KEYS.ROLE, data.role);
            onLogin();
            navigate("/projects");
        } catch (err) {
            console.error(err);
            setError("ログインに失敗しました");
        }
    };

    return (
        <Box maxW="md" mx="auto" mt={10} p={6} borderWidth={1} borderRadius="md" boxShadow="md">
            <Heading mb={6} textAlign="center">
                ログイン
            </Heading>
            <form onSubmit={handleSubmit}>
                <VStack spacing={4} align="stretch">
                    <FormControl id="employeeId" isRequired isInvalid={!!error && error.includes("社員ID")}>
                        <FormLabel>社員ID</FormLabel>
                        <Input type="text" placeholder="e001" value={employeeId} onChange={handleEmployeeIdChange} />
                    </FormControl>

                    <FormControl id="password" isRequired isInvalid={!!error && error.includes("パスワード")}>
                        <FormLabel>パスワード</FormLabel>
                        <Input
                            type="password"
                            placeholder="password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                        />
                    </FormControl>

                    <Button type="submit" colorScheme="blue" isLoading={loading}>
                        ログイン
                    </Button>

                    {error && (
                        <Text color="red.500" textAlign="center" fontWeight="bold" mt={2}>
                            {error}
                        </Text>
                    )}
                </VStack>
            </form>
        </Box>
    );
}

export default LoginPage;
