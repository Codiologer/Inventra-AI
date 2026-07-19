import { Search } from "lucide-react";

export default function InventoryToolbar() {
  return (
    <div className="mb-6 flex flex-wrap items-center justify-between gap-4">
      <div className="relative w-full max-w-md">
        <Search
          size={18}
          className="absolute left-3 top-3 text-gray-400"
        />

        <input
          type="text"
          placeholder="Search products..."
          className="w-full rounded-lg border py-2 pl-10 pr-4 outline-none focus:ring-2 focus:ring-blue-500"
        />
      </div>

      <button className="rounded-lg bg-blue-600 px-5 py-2 font-medium text-white hover:bg-blue-700">
        + Add Product
      </button>
    </div>
  );
}