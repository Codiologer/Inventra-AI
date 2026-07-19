interface StockBadgeProps {
  stock: number;
  minimum: number;
}

export default function StockBadge({
  stock,
  minimum,
}: StockBadgeProps) {
  if (stock <= minimum) {
    return (
      <span className="rounded-full bg-red-100 px-3 py-1 text-xs font-semibold text-red-700">
        Critical
      </span>
    );
  }

  if (stock <= minimum + 10) {
    return (
      <span className="rounded-full bg-yellow-100 px-3 py-1 text-xs font-semibold text-yellow-700">
        Low
      </span>
    );
  }

  return (
    <span className="rounded-full bg-green-100 px-3 py-1 text-xs font-semibold text-green-700">
      Healthy
    </span>
  );
}