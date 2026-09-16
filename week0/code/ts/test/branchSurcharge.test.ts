import { describe, expect, it, vi } from "vitest";
import { applyBranchSurcharge } from "../src/branchSurcharge.js";

vi.mock("../src/crmClient.js", () => ({
  fetchBranch: async (branchId: string) => {
    const table: Record<string, { id: string; region: string }> = {
      "BR-12": { id: "BR-12", region: "remote" },
      "BR-01": { id: "BR-01", region: "metro" },
    };
    return table[branchId];
  },
}));

describe("applyBranchSurcharge", () => {
  it("adds the remote-branch surcharge to the subtotal", async () => {
    const result = await applyBranchSurcharge(1000, "BR-12");
    expect(result).toBe(1030);
  });
});
