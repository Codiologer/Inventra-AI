export default function EmptyState() {
  return (
    <div className="rounded-xl border border-dashed p-12 text-center">
      <h3 className="text-lg font-semibold">
        No Products Found
      </h3>

      <p className="mt-2 text-gray-500">
        Add your first product to start managing inventory.
      </p>
    </div>
  );
}