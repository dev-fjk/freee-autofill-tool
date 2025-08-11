import { Box, Heading } from "@chakra-ui/react";

import Header from "../components/Header";

const ProjectsPage = () => {
    return (
        <>
            <Header />
            <Box maxW="1200px" mx="auto" px={8} py={6}>
                <Heading mb={4}>プロジェクト一覧</Heading>
                {/* プロジェクト一覧のコンポーネントや表示処理 */}
            </Box>
        </>
    );
};

export default ProjectsPage;
