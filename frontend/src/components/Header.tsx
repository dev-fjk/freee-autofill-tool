import { Box, Flex, Heading, Link, Text } from "@chakra-ui/react";
import { Link as RouterLink } from "react-router-dom";

const Header = () => {
    return (
        <Box bg="gray.800" color="white" px={8} py={4} boxShadow="md" width="100vw">
            <Flex align="center" maxW="1200px" mx={0} gap={4}>
                <Heading size="md" textAlign="left">
                    Freee Autofill Tool
                </Heading>
                <Link
                    as={RouterLink}
                    to="/projects"
                    _hover={{ textDecoration: "none", color: "cyan.400" }}
                    fontSize="md"
                >
                    勤怠登録
                </Link>
            </Flex>
        </Box>
    );
};

export default Header;
