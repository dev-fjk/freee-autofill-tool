import react from "@vitejs/plugin-react";
import { defineConfig } from "vite";

export default defineConfig({
    base: "/freee-autofill-tool/", // ルートパスを指定
    plugins: [react()],
    server: {
        port: 3000, // 開発サーバーのポート指定（任意）
    },
    resolve: {
        alias: {
            "@": "/src", // パスエイリアス（任意）
        },
    },
});
