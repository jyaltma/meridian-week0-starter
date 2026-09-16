export interface Branch {
  id: string;
  region: "metro" | "suburban" | "remote";
}

const CRM_BASE_URL = process.env.MERIDIAN_CRM_URL ?? "http://localhost:8082";

export async function fetchBranch(branchId: string): Promise<Branch> {
  const res = await fetch(`${CRM_BASE_URL}/api/v1/branches/${branchId}`, {
    headers: { Authorization: `Bearer ${process.env.MERIDIAN_API_KEY ?? ""}` },
  });
  if (!res.ok) {
    throw new Error(`CRM returned ${res.status} for branch ${branchId}`);
  }
  return (await res.json()) as Branch;
}
