"use client";

import { useQuery } from "@tanstack/react-query";
import { InventoryAPI } from "@/services/inventory";

export function useInventory() {
  const {
    data: products = [],
    isLoading: loading,
    error,
    refetch,
  } = useQuery({
    queryKey: ["products"],
    queryFn: InventoryAPI.getProducts,
  });

  return {
    products,
    loading,
    error: error ? "Unable to load products." : "",
    refresh: refetch,
  };
}