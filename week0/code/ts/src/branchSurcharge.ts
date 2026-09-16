import { fetchBranch } from "./crmClient.js";

// Meridian charges a delivery surcharge by branch region: remote branches
// cost more to service than metro ones.
const SURCHARGE_BY_REGION: Record<string, number> = {
  remote: 0.03,
  suburban: 0.01,
  metro: 0,
};

export async function getBranchSurchargeMultiplier(branchId: string): Promise<number> {
  const branch = await fetchBranch(branchId);
  const rate = SURCHARGE_BY_REGION[branch.region] ?? 0;
  return 1 + rate;
}

export async function applyBranchSurcharge(subtotal: number, branchId: string): Promise<number> {
  const multiplier = await getBranchSurchargeMultiplier(branchId);
  return subtotal * multiplier;
}
