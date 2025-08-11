// ProjectsPage.tsx
import { Box, Flex, Input, Spinner, Table, Tbody, Td, Text, Th, Thead, Tr } from "@chakra-ui/react";
import { useEffect, useState } from "react";
import { useSearchParams } from "react-router-dom";

import Pagination from "../components/Pagination";
import { useProjects } from "../hooks/useProjects";

const ProjectsPage = () => {
    const [searchParams, setSearchParams] = useSearchParams();
    const pageSize = 30;

    const pageParam = searchParams.get("page");
    const projectNameParam = searchParams.get("projectName") || "";

    const pageNumber = pageParam ? Number(pageParam) : 1;
    const [searchKeyword, setSearchKeyword] = useState(projectNameParam);

    useEffect(() => {
        // URLのprojectNameと違うときだけ更新（無限ループ防止）
        if (searchKeyword !== projectNameParam) {
            setSearchParams({ page: "1", projectName: searchKeyword });
        }
    }, [searchKeyword, projectNameParam, setSearchParams]);

    const { projects, loading, error, pagination } = useProjects({
        pageNumber,
        pageSize,
        projectName: projectNameParam,
    });

    const totalPages = pagination?.total_pages ?? 1;
    const totalCount = pagination?.total ?? 0;

    const onPageChange = (newPage: number) => {
        setSearchParams({ page: newPage.toString(), projectName: projectNameParam });
    };

    return (
        <>
            <Box maxW={{ base: "100%", md: "1400px", xl: "1800px" }} mx="auto" px={{ base: 4, md: 6 }} py={6}>
                <Flex mb={4} alignItems="center">
                    <Input
                        placeholder="プロジェクト名で検索"
                        value={searchKeyword}
                        onChange={(e) => setSearchKeyword(e.target.value)}
                        maxW="350px"
                    />
                    <Text ml={4} whiteSpace="nowrap">
                        全 {totalCount} 件
                    </Text>
                </Flex>

                {loading && <Spinner />}

                {error && <Text color="red.500">{error}</Text>}

                {!loading && !error && (
                    <>
                        <Table variant="simple" size="md">
                            <Thead>
                                <Tr>
                                    <Th>ID</Th>
                                    <Th>プロジェクト名</Th>
                                    <Th>開始時間</Th>
                                    <Th>終了時間</Th>
                                    <Th>更新者</Th>
                                    <Th>更新キー</Th>
                                </Tr>
                            </Thead>
                            <Tbody>
                                {projects.map((project) => (
                                    <Tr key={project.project_id}>
                                        <Td>{project.project_id}</Td>
                                        <Td>{project.project_name}</Td>
                                        <Td>{project.start_time}</Td>
                                        <Td>{project.end_time}</Td>
                                        <Td>{project.updated_by}</Td>
                                        <Td>{project.update_key}</Td>
                                    </Tr>
                                ))}
                            </Tbody>
                        </Table>

                        <Pagination pageNumber={pageNumber} totalPages={totalPages} onPageChange={onPageChange} />
                    </>
                )}
            </Box>
        </>
    );
};

export default ProjectsPage;
