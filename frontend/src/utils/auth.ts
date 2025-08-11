import { STORAGE_KEYS } from "../constants/storageKeys";

export const isLoggedIn = (): boolean => {
    const employeeId = localStorage.getItem(STORAGE_KEYS.EMPLOYEE_ID);
    const role = localStorage.getItem(STORAGE_KEYS.ROLE);
    return employeeId !== null && role !== null;
};

export const getUserInfo = (): { employeeId: string | null; role: string | null } => {
    const employeeId = localStorage.getItem(STORAGE_KEYS.EMPLOYEE_ID);
    const role = localStorage.getItem(STORAGE_KEYS.ROLE);
    return { employeeId, role };
};
