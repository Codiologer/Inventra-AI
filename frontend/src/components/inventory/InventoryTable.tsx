"use client";

import { Pencil, Trash2 } from "lucide-react";

import { Product } from "@/types/inventory";

import StockBadge from "./StockBadge";
import EmptyState from "./EmptyState";

interface Props {
  products: Product[];
}

export default function InventoryTable({
  products,
}: Props) {
  if (!products.length) {
    return <EmptyState />;
  }

  return (
    <div className="overflow-hidden rounded-xl border bg-white shadow-sm">
      <table className="w-full">
        <thead className="bg-gray-100">
          <tr>
            <th className="px-5 py-3 text-left">SKU</th>
            <th className="px-5 py-3 text-left">Product</th>
            <th className="px-5 py-3 text-left">Category</th>
            <th className="px-5 py-3 text-left">Stock</th>
            <th className="px-5 py-3 text-left">Status</th>
            <th className="px-5 py-3 text-left">Supplier</th>
            <th className="px-5 py-3 text-left">Price</th>
            <th className="px-5 py-3 text-center">Actions</th>
          </tr>
        </thead>

        <tbody>
          {products.map((product) => (
            <tr
              key={product.id}
              className="border-t hover:bg-gray-50"
            >
              <td className="px-5 py-4">{product.sku}</td>

              <td className="px-5 py-4 font-medium">
                {product.name}
              </td>

              <td className="px-5 py-4">
                {product.category}
              </td>

              <td className="px-5 py-4">
                {product.stock_quantity}
              </td>

              <td className="px-5 py-4">
                <StockBadge
                  stock={product.stock_quantity}
                  minimum={product.minimum_stock}
                />
              </td>

              <td className="px-5 py-4">
                {product.supplier}
              </td>

              <td className="px-5 py-4">
                ₹{product.unit_price}
              </td>

              <td className="px-5 py-4">
                <div className="flex justify-center gap-3">
                  <button className="rounded p-2 hover:bg-blue-100">
                    <Pencil
                      size={18}
                      className="text-blue-600"
                    />
                  </button>

                  <button className="rounded p-2 hover:bg-red-100">
                    <Trash2
                      size={18}
                      className="text-red-600"
                    />
                  </button>
                </div>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}