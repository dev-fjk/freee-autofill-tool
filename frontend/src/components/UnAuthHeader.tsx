import { Box, Flex, Heading, Link } from "@chakra-ui/react";
import { Link as RouterLink } from "react-router-dom";

const Header = () => {
    return (
        <Box bg="#00b0ff" color="white" px={8} py={4} boxShadow="md" width="100vw">
            <Flex align="center" maxW="1200px" mx={0} gap={4}>
                <Link as={RouterLink} to="/" _hover={{ textDecoration: "none", color: "blue.800" }}>
                    <Heading size="md" textAlign="left" color="white" cursor="pointer">
                        Freee Autofill Tool
                    </Heading>
                </Link>
            </Flex>
        </Box>
    );
};

export default Header;
