import { Button, Flex, Text } from "@chakra-ui/react";

type PaginationProps = {
    pageNumber: number;
    totalPages: number;
    onPageChange: (page: number) => void;
};

const Pagination = ({ pageNumber, totalPages, onPageChange }: PaginationProps) => {
    return (
        <Flex mt={4} justifyContent="center" alignItems="center" gap={4}>
            <Button onClick={() => onPageChange(pageNumber - 1)} isDisabled={pageNumber === 1}>
                前へ
            </Button>

            <Text>
                {pageNumber} / {totalPages}
            </Text>

            <Button onClick={() => onPageChange(pageNumber + 1)} isDisabled={pageNumber === totalPages}>
                次へ
            </Button>
        </Flex>
    );
};

export default Pagination;
