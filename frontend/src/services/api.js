const API_BASE_URL = "http://127.0.0.1:8000";

export async function getDashboardSummary() {
    const response = await fetch(
        `${API_BASE_URL}/dashboard/summary`
    );

    if (!response.ok) {
        throw new Error("Failed to fetch dashboard summary");
    }

    return response.json();
}


export async function getDepartments() {
    const response = await fetch(
        `${API_BASE_URL}/dashboard/departments`
    );

    if (!response.ok) {
        throw new Error("Failed to fetch department data");
    }

    return response.json();
}


export async function getPerformance() {
    const response = await fetch(
        `${API_BASE_URL}/dashboard/performance`
    );

    if (!response.ok) {
        throw new Error("Failed to fetch performance data");
    }

    return response.json();
}


export async function getTraining() {
    const response = await fetch(
        `${API_BASE_URL}/dashboard/training`
    );

    if (!response.ok) {
        throw new Error("Failed to fetch training data");
    }

    return response.json();
}