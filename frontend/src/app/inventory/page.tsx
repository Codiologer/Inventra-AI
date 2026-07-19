"use client";

import AppLayout from "@/components/layout/AppLayout";

import InventoryToolbar from "@/components/inventory/InventoryToolbar";
import InventoryTable from "@/components/inventory/InventoryTable";

import { useInventory } from "@/hooks/useInventory";

export default function InventoryPage() {
  const { products, loading, error } = useInventory();

  return (
    <AppLayout>
      <div className="space-y-6">
        <div>
          <h1 className="text-3xl font-bold">
            Inventory Management
          </h1>

          <p className="text-gray-500">
            Manage products, stock and suppliers
          </p>
        </div>

        <InventoryToolbar />

        {loading && <p>Loading...</p>}

        {error && (
          <p className="text-red-600">{error}</p>
        )}

        {!loading && !error && (
          <InventoryTable products={products} />
        )}
      </div>
    </AppLayout>
  );
}